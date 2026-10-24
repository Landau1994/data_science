"use strict";

const { Plugin, ItemView, PluginSettingTab, Setting, Notice, TFile } = require("obsidian");
const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");
const catalog = require("./catalog");

const VIEW_TYPE = "data-science-manager-view";
const DEFAULT_SETTINGS = Object.freeze({
  pythonPath: "C:/Users/Administrator/.conda/envs/localllm/python.exe",
  modelDir: "E:/OneDrive/Documents/project/lm_weight/bge_m3",
  device: "auto",
  semanticEnabled: true,
  resultLimit: 50,
});
const DB_RELATIVE_PATH = ".data-science-index/lancedb";
const EXCLUDED_ROOTS = new Set(["模板", "附件", ".obsidian", ".data-science-index"]);
const STATE_LABELS = Object.fromEntries(catalog.STATES.map((entry) => [entry.value, entry.label]));
const KIND_LABELS = Object.fromEntries(catalog.KINDS.map((entry) => [entry.value, entry.label]));
const TOPIC_LABELS = Object.fromEntries(catalog.TOPICS.map((entry) => [entry.value, entry.label]));
const DIFFICULTIES = { beginner: "入门", intermediate: "中级", advanced: "进阶" };

function normalizeSettings(raw) {
  const value = Object.assign({}, DEFAULT_SETTINGS, raw || {});
  value.pythonPath = String(value.pythonPath || DEFAULT_SETTINGS.pythonPath).trim();
  value.modelDir = String(value.modelDir || DEFAULT_SETTINGS.modelDir).trim();
  value.device = ["auto", "cpu", "cuda"].includes(value.device) ? value.device : "auto";
  value.semanticEnabled = value.semanticEnabled !== false;
  const count = Number(value.resultLimit);
  value.resultLimit = Number.isInteger(count) && count > 0 && count <= 200 ? count : 50;
  return value;
}

function messageOf(error) {
  return error && error.message ? error.message : String(error);
}

function isManagedPath(relativePath) {
  const normalized = String(relativePath || "").replace(/\\/g, "/");
  return !path.posix.isAbsolute(normalized)
    && !/^[A-Za-z]:/.test(normalized)
    && !normalized.split("/").some((part) => part === ".." || part.startsWith("."))
    && !EXCLUDED_ROOTS.has(normalized.split("/")[0])
    && normalized.toLowerCase().endsWith(".md");
}

function insideVault(root, candidate) {
  const target = path.resolve(root, candidate);
  const relative = path.relative(path.resolve(root), target);
  if (relative === ".." || relative.startsWith(`..${path.sep}`) || path.isAbsolute(relative)) {
    throw new Error("索引与插件文件必须位于当前知识库内。");
  }
  return target;
}

/** One worker, one in-flight request. All callers share this queue. */
class PythonBridge {
  constructor({ getConfig, onLog = () => {}, spawnProcess = spawn }) {
    this.getConfig = getConfig;
    this.onLog = onLog;
    this.spawnProcess = spawnProcess;
    this.proc = null;
    this.pending = new Map();
    this.serial = Promise.resolve();
    this.sequence = 0;
    this.disposed = false;
    this.buffer = "";
    this.logText = "";
  }

  appendLog(value) {
    this.logText = (this.logText + String(value)).slice(-16000);
    this.onLog(this.logText);
  }

  request(op, payload = {}, timeoutMs) {
    const timeout = timeoutMs || (op === "sync" ? 15 * 60 * 1000 : op === "status" ? 30000 : 3 * 60 * 1000);
    const task = () => this.send(op, payload, timeout);
    const result = this.serial.then(task, task);
    this.serial = result.catch(() => {});
    return result;
  }

  ensureProcess() {
    if (this.disposed) throw new Error("管理器已关闭。");
    if (this.proc) return this.proc;
    const config = this.getConfig();
    const args = ["-B", "-u", "-X", "utf8", config.scriptPath,
      "--vault", config.vaultRoot, "--db-dir", config.dbDir,
      "--model", config.modelDir, "--device", config.device, "--serve"];
    const proc = this.spawnProcess(config.pythonPath, args, {
      cwd: config.vaultRoot,
      shell: false,
      windowsHide: true,
      stdio: ["pipe", "pipe", "pipe"],
      env: Object.assign({}, process.env, {
        PYTHONDONTWRITEBYTECODE: "1",
        PYTHONIOENCODING: "utf-8",
        HF_HUB_OFFLINE: "1",
        TRANSFORMERS_OFFLINE: "1",
        HF_DATASETS_OFFLINE: "1",
      }),
    });
    this.proc = proc;
    this.buffer = "";
    proc.stdout.setEncoding("utf8");
    proc.stderr.setEncoding("utf8");
    proc.stdout.on("data", (chunk) => {
      if (this.proc !== proc) return;
      this.buffer += chunk;
      if (this.buffer.length > 2 * 1024 * 1024) {
        this.reset("本地检索返回的数据过长，已停止本次请求。");
        return;
      }
      let newline;
      while ((newline = this.buffer.indexOf("\n")) >= 0) {
        const line = this.buffer.slice(0, newline).trim();
        this.buffer = this.buffer.slice(newline + 1);
        if (!line) continue;
        let response;
        try { response = JSON.parse(line); }
        catch (_) {
          this.appendLog("本地检索返回了无法解析的数据。\n");
          this.reset("本地检索返回格式有误，请检查运行环境。");
          return;
        }
        const waiting = this.pending.get(response.id);
        if (!waiting) continue;
        this.pending.delete(response.id);
        clearTimeout(waiting.timer);
        if (response.ok === true) waiting.resolve(response.result || {});
        else waiting.reject(new Error(typeof response.error === "string" ? response.error : "本地检索未能完成。"));
      }
    });
    proc.stderr.on("data", (chunk) => { if (this.proc === proc) this.appendLog(chunk); });
    proc.stdin.on("error", () => { if (this.proc === proc) this.reset("无法向本地检索进程发送请求。"); });
    proc.on("error", (error) => {
      if (this.proc !== proc) return;
      const detail = error.code === "ENOENT"
        ? "未找到本地运行环境，请在插件设置中检查 Python 路径。"
        : `本地检索进程启动失败：${messageOf(error)}`;
      this.reset(detail);
    });
    proc.on("close", (code, signal) => {
      if (this.proc !== proc) return;
      this.reset(`本地检索进程已退出（${signal || code}），可重新执行或检查设置。`);
    });
    return proc;
  }

  send(op, payload, timeout) {
    return new Promise((resolve, reject) => {
      let proc;
      try { proc = this.ensureProcess(); }
      catch (error) { reject(error); return; }
      const id = ++this.sequence;
      const timer = setTimeout(() => {
        if (this.pending.has(id)) this.reset("本地检索等待超时，已停止进程。请查看诊断信息或调整运行环境后重试。");
      }, timeout);
      this.pending.set(id, { resolve, reject, timer });
      try {
        proc.stdin.write(JSON.stringify(Object.assign({}, payload, { id, op })) + "\n", "utf8", (error) => {
          if (error && this.proc === proc) this.reset("无法向本地检索进程发送请求。");
        });
      } catch (_) { this.reset("无法向本地检索进程发送请求。"); }
    });
  }

  reset(reason = "本地检索设置已更新，请重新执行。") {
    const proc = this.proc;
    this.proc = null;
    this.buffer = "";
    for (const waiting of this.pending.values()) {
      clearTimeout(waiting.timer);
      waiting.reject(new Error(reason));
    }
    this.pending.clear();
    if (proc) {
      try { proc.stdin.end(); } catch (_) { /* already closed */ }
      try { proc.kill(); } catch (_) { /* already exited */ }
    }
  }

  dispose() {
    this.disposed = true;
    this.reset("管理器已关闭，本地请求已取消。");
  }
}

function addSelect(parent, label, entries, selected, onChange) {
  const wrapper = parent.createDiv({ cls: "dsm-field" });
  wrapper.createEl("label", { text: label });
  const element = wrapper.createEl("select", { attr: { "aria-label": label } });
  for (const entry of entries) element.createEl("option", { text: entry.label, value: entry.value });
  element.value = selected || "";
  element.addEventListener("change", () => onChange(element.value));
  return element;
}

class ManagerView extends ItemView {
  constructor(leaf, plugin) {
    super(leaf);
    this.plugin = plugin;
    this.filters = { kind: "", topic: "", status: "", source_id: "" };
    this.query = "";
    this.mode = "keyword";
    this.items = [];
    this.total = 0;
    this.busy = false;
    this.searchSequence = 0;
    this.closed = false;
    this.resultMode = "catalog";
    this.relatedReferencePath = "";
  }

  getViewType() { return VIEW_TYPE; }
  getDisplayText() { return "数据科学知识库管理器"; }
  getIcon() { return "database"; }

  async onOpen() {
    this.contentEl.empty();
    this.root = this.contentEl.createDiv({ cls: "dsm-manager" });
    const heading = this.root.createDiv({ cls: "dsm-heading" });
    heading.createEl("h2", { text: "知识库管理" });
    this.syncButton = heading.createEl("button", { text: "同步本地索引", cls: "mod-cta" });
    this.syncButton.addEventListener("click", () => { void this.sync(); });
    this.summaryEl = this.root.createDiv({ cls: "dsm-summary" });
    this.indexEl = this.root.createDiv({ cls: "dsm-index-state", attr: { role: "status", "aria-live": "polite" } });
    this.tabsEl = this.root.createDiv({ cls: "dsm-kind-tabs", attr: { "aria-label": "笔记类别" } });
    const searchRow = this.root.createDiv({ cls: "dsm-search-row" });
    this.searchInput = searchRow.createEl("input", { type: "search", placeholder: "搜索中文、英文或原书题号", attr: { "aria-label": "搜索笔记" } });
    this.searchInput.addEventListener("input", () => { this.query = this.searchInput.value; });
    this.searchInput.addEventListener("keydown", (event) => { if (event.key === "Enter") void this.search(); });
    this.modeSelect = addSelect(searchRow, "检索方式", [
      { value: "keyword", label: "关键词" }, { value: "semantic", label: "语义" },
    ], this.mode, (value) => { this.mode = value; });
    this.searchButton = searchRow.createEl("button", { text: "检索" });
    this.searchButton.addEventListener("click", () => { void this.search(); });
    const filterRow = this.root.createDiv({ cls: "dsm-filters" });
    addSelect(filterRow, "主题", [{ value: "", label: "全部主题" }, ...catalog.TOPICS], "", (value) => { this.filters.topic = value; void this.filterChanged(); });
    addSelect(filterRow, "学习状态", [{ value: "", label: "全部状态" }, ...catalog.STATES], "", (value) => { this.filters.status = value; void this.filterChanged(); });
    this.sourceSelect = addSelect(filterRow, "教材来源", [{ value: "", label: "全部来源" }], "", (value) => { this.filters.source_id = value; void this.filterChanged(); });
    const secondary = this.root.createDiv({ cls: "dsm-secondary-actions" });
    this.relatedButton = secondary.createEl("button", { text: "查找当前笔记的相关内容" });
    this.relatedButton.addEventListener("click", () => { void this.related(); });
    this.feedback = this.root.createDiv({ cls: "dsm-feedback", attr: { role: "status", "aria-live": "polite" } });
    this.resultsEl = this.root.createDiv({ cls: "dsm-results" });
    const diagnostics = this.root.createEl("details", { cls: "dsm-diagnostics" });
    diagnostics.createEl("summary", { text: "诊断信息" });
    this.logEl = diagnostics.createEl("pre");
    this.onCatalogChanged();
    void this.plugin.checkIndex().catch((error) => { this.showError("索引检查未完成；仍可浏览和使用关键词检索。", error); });
  }

  async onClose() { this.closed = true; this.searchSequence += 1; }

  onCatalogChanged() {
    if (!this.root || this.closed) return;
    this.summaryEl.textContent = `本库共 ${this.plugin.records.length} 篇教材、概念、习题、项目与实验记录`;
    this.renderKindTabs();
    this.sourceSelect.empty();
    this.sourceSelect.createEl("option", { text: "全部来源", value: "" });
    const sourceIds = [...new Set(this.plugin.records.map((record) => record.source_id).filter(Boolean))].sort();
    for (const id of sourceIds) this.sourceSelect.createEl("option", { text: id, value: id });
    if (!sourceIds.includes(this.filters.source_id)) this.filters.source_id = "";
    this.sourceSelect.value = this.filters.source_id;
    const semanticOption = this.modeSelect.querySelector('option[value="semantic"]');
    if (semanticOption) semanticOption.disabled = !this.plugin.settings.semanticEnabled;
    if (!this.plugin.settings.semanticEnabled && this.mode === "semantic") { this.mode = "keyword"; this.modeSelect.value = "keyword"; }
    this.updateIndexState();
    this.updateLog();
    if (this.resultMode !== "related" && (!this.query.trim() || this.mode === "keyword")) void this.search();
    else {
      const byPath = new Map(this.plugin.records.map((record) => [record.path, record]));
      this.items = this.items.filter((record) => byPath.has(record.path)).map((record) => Object.assign({}, record, byPath.get(record.path)));
      this.renderResults();
    }
  }

  updateLog() { if (this.logEl) this.logEl.textContent = this.plugin.bridge ? this.plugin.bridge.logText : ""; }

  renderKindTabs() {
    const counts = catalog.countKinds(this.plugin.records);
    this.tabsEl.empty();
    for (const kind of [{ value: "", label: "全部" }, ...catalog.KINDS]) {
      const count = kind.value ? counts[kind.value] : this.plugin.records.length;
      const button = this.tabsEl.createEl("button", {
        text: `${kind.label} ${count || 0}`,
        cls: this.filters.kind === kind.value ? "is-active" : "",
        attr: { "aria-pressed": String(this.filters.kind === kind.value) },
      });
      button.addEventListener("click", () => { this.filters.kind = kind.value; this.renderKindTabs(); void this.filterChanged(); });
    }
  }

  updateIndexState() {
    if (!this.indexEl) return;
    const status = this.plugin.indexStatus;
    const dirty = this.plugin.indexDirty;
    let text = "笔记目录可直接使用；本地索引尚未检查。";
    if (status && !status.exists) text = "尚未建立本地索引；关键词检索可直接使用，语义与关联查找请先同步。";
    else if (status) text = `索引已收录 ${status.total || 0} 篇；${status.semantic_ready ? "语义检索已就绪" : "语义索引尚未就绪"}。`;
    if (dirty) text += " 笔记有更新，索引待同步。";
    this.indexEl.textContent = text;
    this.indexEl.classList.toggle("is-dirty", dirty);
  }

  async filterChanged() {
    if (this.resultMode === "related" && this.relatedReferencePath) await this.related(this.relatedReferencePath);
    else await this.search();
  }

  setBusy(value, message = "") {
    if (this.closed || !this.root) return;
    this.busy = value || Boolean(this.plugin.syncPromise);
    for (const element of [this.syncButton, this.searchButton, this.relatedButton]) element.disabled = this.busy;
    if (message) this.feedback.textContent = message;
  }

  showError(summary, error) {
    if (this.closed) return;
    this.feedback.textContent = summary;
    this.feedback.classList.add("is-error");
    if (this.plugin.bridge && error) this.plugin.bridge.appendLog(`${messageOf(error)}\n`);
  }

  async search() {
    if (this.closed) return;
    const sequence = ++this.searchSequence;
    const query = this.query.trim();
    this.feedback.classList.remove("is-error");
    if (!query) {
      this.resultMode = "catalog";
      this.items = this.plugin.records.slice();
      this.total = this.items.length;
      this.feedback.textContent = "直接浏览本库笔记；可按类别、主题、学习状态或教材来源筛选。";
      this.renderResults();
      this.setBusy(false);
      return;
    }
    this.setBusy(true, this.mode === "semantic" ? "正在检索本地语义索引…" : "正在检索笔记正文…");
    try {
      let result;
      if (this.mode === "semantic") {
        if (!this.plugin.settings.semanticEnabled) throw new Error("请先在设置中启用本地语义索引。");
        result = await this.plugin.bridge.request("search", Object.assign({}, this.filters, { query, mode: "semantic", limit: this.plugin.settings.resultLimit }));
      } else result = await this.plugin.keywordSearch(query, this.filters);
      if (sequence !== this.searchSequence || this.closed) return;
      this.items = Array.isArray(result.items) ? result.items : [];
      this.resultMode = this.mode;
      this.total = Number(result.total) || this.items.length;
      this.feedback.textContent = `找到 ${this.total} 篇相关笔记。`;
      this.renderResults();
    } catch (error) {
      if (sequence === this.searchSequence) this.showError("检索未完成，请先同步索引或检查设置；关键词检索可直接使用。", error);
    } finally { if (sequence === this.searchSequence) this.setBusy(false); }
  }

  async sync() {
    this.setBusy(true, "正在同步本地索引。首次语义索引需要加载已有本地模型，请稍候…");
    this.feedback.classList.remove("is-error");
    try {
      const result = await this.plugin.syncIndex();
      if (this.closed) return;
      this.feedback.textContent = `同步完成：新增 ${result.added || 0}，更新 ${result.updated || 0}，删除 ${result.deleted || 0}，共 ${result.total || 0} 篇。`;
      this.updateIndexState();
    } catch (error) { this.showError("同步未完成，原笔记和学习状态不受影响。请查看诊断信息。", error); }
    finally { this.setBusy(false); }
  }

  async related(referenceFile) {
    const file = typeof referenceFile === "string"
      ? this.plugin.app.vault.getAbstractFileByPath(referenceFile)
      : referenceFile || this.plugin.referenceFile();
    if (!(file instanceof TFile) || !this.plugin.records.some((record) => record.path === file.path)) { new Notice("请先打开一篇教材、概念、习题、项目或实验笔记。"); return; }
    const sequence = ++this.searchSequence;
    this.relatedReferencePath = file.path;
    this.setBusy(true, "正在查找链接与主题相关的笔记…");
    this.feedback.classList.remove("is-error");
    try {
      const result = await this.plugin.bridge.request("related", Object.assign({}, this.filters, { path: file.path, limit: this.plugin.settings.resultLimit }));
      if (this.closed || sequence !== this.searchSequence) return;
      this.items = Array.isArray(result.items) ? result.items : [];
      this.resultMode = "related";
      this.total = Number(result.total) || this.items.length;
      this.feedback.textContent = `与“${file.basename}”相关的 ${this.total} 篇笔记；可继续按条件筛选。`;
      this.renderResults();
    } catch (error) { if (sequence === this.searchSequence) this.showError("关联查找未完成，请先同步本地索引。", error); }
    finally { if (sequence === this.searchSequence) this.setBusy(false); }
  }

  renderResults() {
    if (!this.resultsEl || this.closed) return;
    this.resultsEl.empty();
    const included = new Set(catalog.filterRecords(this.items, this.filters).map((record) => record.path));
    const items = this.items.filter((record) => included.has(record.path));
    const visible = items.slice(0, this.plugin.settings.resultLimit);
    this.resultsEl.createDiv({ text: `显示 ${visible.length} / ${items.length} 篇${this.total > items.length ? `（本次检索共 ${this.total} 篇）` : ""}`, cls: "dsm-result-count" });
    if (!visible.length) { this.resultsEl.createDiv({ text: "当前条件下没有笔记。可以调整筛选或检索词。", cls: "dsm-empty" }); return; }
    for (const item of visible) {
      const row = this.resultsEl.createDiv({ cls: "dsm-result" });
      const heading = row.createDiv({ cls: "dsm-result-heading" });
      heading.createSpan({ text: KIND_LABELS[item.kind] || item.kind || "笔记", cls: "dsm-kind-badge" });
      const title = heading.createEl("button", { text: item.title || path.basename(item.path || "", ".md"), cls: "dsm-note-link" });
      title.addEventListener("click", () => { void this.plugin.openNote(item.path); });
      const info = [item.topic_label || TOPIC_LABELS[item.topic] || "", STATE_LABELS[item.status] || "未设置学习状态", DIFFICULTIES[item.difficulty] || "", item.source_id || "", item.source_exercise ? `原题 ${item.source_exercise}` : ""].filter(Boolean);
      row.createDiv({ text: info.join(" · "), cls: "dsm-note-meta" });
      if (item.excerpt) row.createDiv({ text: String(item.excerpt), cls: "dsm-excerpt" });
      if (Array.isArray(item.reasons) && item.reasons.length) row.createDiv({ text: item.reasons.join("；"), cls: "dsm-reasons" });
      row.createDiv({ text: item.path || "", cls: "dsm-note-path" });
      const actions = row.createDiv({ cls: "dsm-note-actions" });
      const options = [{ value: "", label: "选择学习状态" }, ...catalog.STATES];
      const select = addSelect(actions, "学习状态", options, item.status, async (next) => {
        if (!next || next === item.status) return;
        const previous = item.status || "";
        select.disabled = true;
        try {
          await this.plugin.setStudyStatus(item.path, next);
          item.status = next;
          new Notice("学习状态已更新；本地索引待同步。");
        } catch (error) { select.value = previous; this.showError("学习状态未能更新。", error); }
        finally { select.disabled = false; }
      });
    }
  }
}

class ManagerSettings extends PluginSettingTab {
  constructor(app, plugin) { super(app, plugin); this.plugin = plugin; }

  display() {
    const { containerEl } = this;
    containerEl.empty();
    containerEl.createEl("h2", { text: "数据科学知识库管理器" });
    containerEl.createEl("p", { text: "目录浏览与关键词检索直接读取当前笔记。LanceDB 索引手动同步，语义功能只使用已有本地模型。" });
    new Setting(containerEl).setName("启用本地语义索引").setDesc("开启后，手动同步会建立真实语义向量；关闭时仍可管理笔记与使用关键词检索。不会自动下载模型。")
      .addToggle((toggle) => toggle.setValue(this.plugin.settings.semanticEnabled).onChange(async (value) => { await this.plugin.updateSettings({ semanticEnabled: value }); }));
    new Setting(containerEl).setName("Python 路径").setDesc("使用已安装 LanceDB 与 sentence-transformers 的本地环境。")
      .addText((text) => text.setValue(this.plugin.settings.pythonPath).setPlaceholder(DEFAULT_SETTINGS.pythonPath).onChange(async (value) => { if (value.trim()) await this.plugin.updateSettings({ pythonPath: value.trim() }); }));
    new Setting(containerEl).setName("本地模型目录").setDesc("选择已有的嵌入模型目录，可与其他知识库共用模型文件。")
      .addText((text) => text.setValue(this.plugin.settings.modelDir).setPlaceholder(DEFAULT_SETTINGS.modelDir).onChange(async (value) => { if (value.trim()) await this.plugin.updateSettings({ modelDir: value.trim() }); }));
    new Setting(containerEl).setName("计算设备").setDesc("自动模式由本地环境选择可用设备。")
      .addDropdown((dropdown) => dropdown.addOptions({ auto: "自动", cpu: "CPU", cuda: "CUDA GPU" }).setValue(this.plugin.settings.device).onChange(async (value) => { await this.plugin.updateSettings({ device: value }); }));
    new Setting(containerEl).setName("单次显示数量").setDesc("限制显示数量不等于总记录数，面板会同时显示实际结果数。")
      .addDropdown((dropdown) => dropdown.addOptions({ 20: "20", 50: "50", 100: "100", 200: "200" }).setValue(String(this.plugin.settings.resultLimit)).onChange(async (value) => { await this.plugin.updateSettings({ resultLimit: Number(value) }); }));
    containerEl.createEl("p", { text: "索引独立保存在当前库的 .data-science-index/lancedb。插件不会修改教材归档进度，不管理每日抽样或系统推进队列。", cls: "setting-item-description" });
  }
}

class DataScienceManagerPlugin extends Plugin {
  async onload() {
    this.settings = normalizeSettings(await this.loadData());
    this.records = [];
    this.catalogRevision = 0;
    this.indexDirty = false;
    this.indexStatus = null;
    this.disposed = false;
    this.refreshTimer = null;
    this.syncPromise = null;
    this.lastActiveNotePath = this.app.workspace.getActiveFile()?.path || "";
    this.bridge = new PythonBridge({ getConfig: () => this.workerConfig(), onLog: () => this.forEachView((view) => view.updateLog()) });
    this.registerView(VIEW_TYPE, (leaf) => new ManagerView(leaf, this));
    this.addRibbonIcon("database", "打开数据科学知识库管理器", () => { void this.activateView(); });
    this.addCommand({ id: "open-manager", name: "打开知识库管理面板", callback: () => { void this.activateView(); } });
    this.addCommand({ id: "sync-index", name: "同步本库 LanceDB 索引", callback: () => { void this.activateView().then((view) => view && view.sync()); } });
    this.addCommand({ id: "related-notes", name: "查找当前笔记的相关内容", checkCallback: (checking) => {
      const file = this.referenceFile();
      if (!(file instanceof TFile) || !this.records.some((record) => record.path === file.path)) return false;
      if (!checking) void this.activateView().then((view) => view && view.related(file));
      return true;
    } });
    this.addSettingTab(new ManagerSettings(this.app, this));
    this.registerEvent(this.app.workspace.on("file-open", (file) => { if (file instanceof TFile && isManagedPath(file.path)) this.lastActiveNotePath = file.path; }));
    this.registerEvent(this.app.metadataCache.on("changed", () => this.scheduleRefresh(true)));
    this.registerEvent(this.app.metadataCache.on("resolved", () => this.scheduleRefresh(false)));
    for (const event of ["create", "modify", "delete", "rename"]) {
      this.registerEvent(this.app.vault.on(event, (file) => { if (file && isManagedPath(file.path)) this.scheduleRefresh(true); }));
    }
    this.app.workspace.onLayoutReady(() => this.refreshCatalog());
    this.refreshCatalog();
  }

  workerConfig() {
    const adapter = this.app.vault.adapter;
    const root = adapter && typeof adapter.getBasePath === "function" ? adapter.getBasePath() : "";
    if (!root) throw new Error("此管理器需要在桌面版本地知识库中使用。");
    const directory = this.manifest.dir || ".obsidian/plugins/data-science-manager";
    const script = insideVault(root, path.join(directory, "scripts", "vault_index.py"));
    if (!fs.existsSync(script)) throw new Error("插件索引组件缺失，请检查安装文件。");
    return { pythonPath: this.settings.pythonPath, modelDir: this.settings.modelDir,
      device: this.settings.device, vaultRoot: root, scriptPath: script,
      dbDir: insideVault(root, DB_RELATIVE_PATH) };
  }

  forEachView(callback) {
    if (this.disposed) return;
    for (const leaf of this.app.workspace.getLeavesOfType(VIEW_TYPE)) {
      if (leaf.view instanceof ManagerView) callback(leaf.view);
    }
  }

  scheduleRefresh(dirty) {
    if (this.disposed) return;
    if (dirty) { this.indexDirty = true; this.catalogRevision += 1; }
    if (this.refreshTimer) clearTimeout(this.refreshTimer);
    this.refreshTimer = setTimeout(() => { this.refreshTimer = null; this.refreshCatalog(); }, 180);
  }

  refreshCatalog() {
    if (this.disposed) return;
    this.records = this.app.vault.getMarkdownFiles().filter((file) => isManagedPath(file.path))
      .map((file) => catalog.recordFromFile(file, this.app.metadataCache.getFileCache(file)))
      .filter(Boolean).sort((left, right) => left.path.localeCompare(right.path, "zh-CN"));
    this.forEachView((view) => view.onCatalogChanged());
  }

  async activateView() {
    let leaf = this.app.workspace.getLeavesOfType(VIEW_TYPE)[0];
    if (!leaf) {
      leaf = this.app.workspace.getRightLeaf(false);
      if (!leaf) { new Notice("无法打开知识库管理面板。"); return null; }
      await leaf.setViewState({ type: VIEW_TYPE, active: true });
    }
    this.app.workspace.revealLeaf(leaf);
    return leaf.view instanceof ManagerView ? leaf.view : null;
  }

  async checkIndex() {
    const status = await this.bridge.request("status");
    this.indexStatus = status;
    this.forEachView((view) => view.updateIndexState());
    return status;
  }

  async syncIndex() {
    if (this.syncPromise) return this.syncPromise;
    const revision = this.catalogRevision;
    this.syncPromise = this.bridge.request("sync", { semantic: this.settings.semanticEnabled });
    try {
      const result = await this.syncPromise;
      this.indexStatus = Object.assign({}, result, { exists: true });
      this.indexDirty = this.catalogRevision !== revision;
      this.forEachView((view) => view.updateIndexState());
      return result;
    } finally { this.syncPromise = null; }
  }

  referenceFile() {
    const active = this.app.workspace.getActiveFile();
    if (active instanceof TFile && isManagedPath(active.path)) return active;
    return this.lastActiveNotePath ? this.app.vault.getAbstractFileByPath(this.lastActiveNotePath) : null;
  }

  async keywordSearch(query, filters) {
    const eligible = catalog.filterRecords(this.records, filters);
    const results = [];
    for (const record of eligible) {
      const file = this.app.vault.getAbstractFileByPath(record.path);
      if (!(file instanceof TFile)) continue;
      let text;
      try { text = await this.app.vault.cachedRead(file); }
      catch (_) { continue; }
      if (catalog.keywordMatches(record, query, text)) results.push(Object.assign({}, record, { excerpt: catalog.excerpt(text) }));
    }
    return { items: results.slice(0, this.settings.resultLimit), total: results.length, mode: "keyword" };
  }

  async openNote(relativePath) {
    if (!isManagedPath(relativePath)) { new Notice("该笔记位置不在管理范围内。"); return; }
    const file = this.app.vault.getAbstractFileByPath(String(relativePath).replace(/\\/g, "/"));
    if (!(file instanceof TFile)) { new Notice("笔记已移动或不存在，请刷新目录后重试。"); return; }
    await this.app.workspace.getLeaf(false).openFile(file);
  }

  async setStudyStatus(relativePath, nextStatus) {
    if (!Object.hasOwn(STATE_LABELS, nextStatus)) throw new Error("请选择合法的学习状态。");
    if (!isManagedPath(relativePath)) throw new Error("该笔记不在当前库的管理范围内。");
    const file = this.app.vault.getAbstractFileByPath(relativePath);
    if (!(file instanceof TFile) || !this.records.some((record) => record.path === relativePath)) throw new Error("找不到该结构化笔记。");
    if (typeof this.app.fileManager.processFrontMatter !== "function") throw new Error("当前 Obsidian 版本不支持安全更新元数据，请升级后重试。");
    await this.app.fileManager.processFrontMatter(file, (frontmatter) => { frontmatter.status = nextStatus; });
    this.records = this.records.map((record) => record.path === relativePath ? Object.assign({}, record, { status: nextStatus }) : record);
    this.indexDirty = true;
    this.catalogRevision += 1;
    this.forEachView((view) => view.onCatalogChanged());
  }

  async updateSettings(values) {
    this.settings = normalizeSettings(Object.assign({}, this.settings, values));
    await this.saveData(this.settings);
    this.bridge.reset();
    if (Object.hasOwn(values, "modelDir") || Object.hasOwn(values, "semanticEnabled")) this.indexDirty = true;
    this.forEachView((view) => view.onCatalogChanged());
  }

  onunload() {
    this.disposed = true;
    if (this.refreshTimer) clearTimeout(this.refreshTimer);
    if (this.bridge) this.bridge.dispose();
    this.app.workspace.detachLeavesOfType(VIEW_TYPE);
  }
}

module.exports = DataScienceManagerPlugin;
module.exports._internals = { PythonBridge, normalizeSettings, isManagedPath, insideVault, ManagerView, DEFAULT_SETTINGS, VIEW_TYPE };
