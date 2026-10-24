"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { EventEmitter } = require("node:events");
const { PassThrough } = require("node:stream");
const Module = require("node:module");
const path = require("node:path");
const os = require("node:os");

class FakeTFile {
  constructor(relative) { this.path = relative; this.basename = path.basename(relative, ".md"); this.extension = "md"; }
}
class FakePlugin {}
class FakeItemView { constructor(leaf) { this.leaf = leaf; } }
const originalLoad = Module._load;
Module._load = function (request, parent, isMain) {
  if (request === "obsidian") return {
    Plugin: FakePlugin, ItemView: FakeItemView, PluginSettingTab: class {},
    Setting: class {}, Notice: class {}, TFile: FakeTFile,
  };
  return originalLoad.call(this, request, parent, isMain);
};
const Plugin = require("../main.js");
Module._load = originalLoad;
const { PythonBridge, normalizeSettings, isManagedPath, insideVault, ManagerView } = Plugin._internals;
const tick = () => new Promise((resolve) => setImmediate(resolve));

function child() {
  const proc = new EventEmitter();
  proc.stdout = new PassThrough();
  proc.stderr = new PassThrough();
  proc.stdin = new PassThrough();
  proc.messages = [];
  proc.stdin.on("data", (chunk) => { proc.messages.push(JSON.parse(chunk.toString("utf8"))); });
  proc.killed = false;
  proc.kill = () => { proc.killed = true; };
  return proc;
}

function harness() {
  const spawned = [];
  const calls = [];
  const bridge = new PythonBridge({
    getConfig: () => ({ pythonPath: "local-python", scriptPath: "local-script.py", vaultRoot: "local-vault", dbDir: "local-index", modelDir: "local-model", device: "auto" }),
    spawnProcess: (...args) => { const proc = child(); calls.push(args); spawned.push(proc); return proc; },
  });
  return { bridge, spawned, calls };
}

test("worker启动参数禁止shell、隐藏窗口并关闭在线模型下载", async () => {
  const { bridge, spawned, calls } = harness();
  const pending = bridge.request("status");
  await tick();
  assert.equal(calls[0][0], "local-python");
  assert.equal(calls[0][2].shell, false);
  assert.equal(calls[0][2].windowsHide, true);
  assert.equal(calls[0][2].env.HF_HUB_OFFLINE, "1");
  assert.equal(calls[0][2].env.TRANSFORMERS_OFFLINE, "1");
  assert.deepEqual(calls[0][1], ["-B", "-u", "-X", "utf8", "local-script.py", "--vault", "local-vault", "--db-dir", "local-index", "--model", "local-model", "--device", "auto", "--serve"]);
  const id = spawned[0].messages[0].id;
  spawned[0].stdout.write(JSON.stringify({ id, ok: true, result: { exists: false } }) + "\n");
  assert.deepEqual(await pending, { exists: false });
  bridge.dispose();
});

test("请求按序执行且共享worker；分块JSON响应可正确拼接", async () => {
  const { bridge, spawned } = harness();
  const first = bridge.request("status");
  const second = bridge.request("search", { query: "中文\n2.3", mode: "semantic" });
  await tick();
  const proc = spawned[0];
  assert.equal(proc.messages.length, 1);
  proc.stdout.write('{"id":1,"ok":true,"result":');
  await tick();
  assert.equal(proc.messages.length, 1);
  proc.stdout.write('{"total":3}}\n');
  assert.deepEqual(await first, { total: 3 });
  await tick();
  assert.equal(spawned.length, 1);
  assert.equal(proc.messages.length, 2);
  assert.equal(proc.messages[1].query, "中文\n2.3");
  proc.stdout.write('{"id":2,"ok":true,"result":{"items":[]}}\n');
  assert.deepEqual(await second, { items: [] });
  bridge.dispose();
});

test("后端错误只拒绝对应请求，stderr不混入JSON协议", async () => {
  const { bridge, spawned } = harness();
  const pending = bridge.request("search");
  const rejected = assert.rejects(pending, /请先同步索引/);
  await tick();
  const proc = spawned[0];
  proc.stderr.write("正在加载已有模型…\n");
  proc.stdout.write('{"id":1,"ok":false,"error":"请先同步索引"}\n');
  await rejected;
  assert.match(bridge.logText, /已有模型/);
  assert.equal(proc.killed, false);
  bridge.dispose();
});

test("无效协议响应停止worker并清理pending", async () => {
  const { bridge, spawned } = harness();
  const pending = bridge.request("status");
  const rejected = assert.rejects(pending, /返回格式有误/);
  await tick();
  spawned[0].stdout.write("not-json\n");
  await rejected;
  assert.equal(spawned[0].killed, true);
  assert.equal(bridge.pending.size, 0);
  bridge.dispose();
});

test("超时会终止worker并清理等待；日志大小有界", async () => {
  const { bridge, spawned } = harness();
  const pending = bridge.request("status", {}, 15);
  const rejected = assert.rejects(pending, /等待超时/);
  await tick();
  bridge.appendLog("日志".repeat(20000));
  assert.ok(bridge.logText.length <= 16000);
  await rejected;
  assert.equal(spawned[0].killed, true);
  assert.equal(bridge.pending.size, 0);
  bridge.dispose();
});

test("卸载拒绝活动及排队请求，之后不会再创建worker", async () => {
  const { bridge, spawned } = harness();
  const active = bridge.request("sync");
  const queued = bridge.request("status");
  const activeRejected = assert.rejects(active, /管理器已关闭/);
  const queuedRejected = assert.rejects(queued, /管理器已关闭/);
  await tick();
  bridge.dispose();
  await Promise.all([activeRejected, queuedRejected]);
  assert.equal(spawned.length, 1);
  assert.equal(spawned[0].killed, true);
  assert.equal(bridge.pending.size, 0);
  await assert.rejects(bridge.request("status"), /管理器已关闭/);
  assert.equal(spawned.length, 1);
});

test("stdin错误被处理而非成为未捕获异常", async () => {
  const { bridge, spawned } = harness();
  const pending = bridge.request("status");
  const rejected = assert.rejects(pending, /无法向本地检索进程发送请求/);
  await tick();
  spawned[0].stdin.emit("error", new Error("EPIPE"));
  await rejected;
  assert.equal(spawned[0].killed, true);
  bridge.dispose();
});

test("Python启动失败给出可理解错误并允许之后重启", async () => {
  const { bridge, spawned } = harness();
  const first = bridge.request("status");
  const rejected = assert.rejects(first, /检查 Python 路径/);
  await tick();
  const missing = new Error("missing"); missing.code = "ENOENT";
  spawned[0].emit("error", missing);
  await rejected;
  const second = bridge.request("status");
  await tick();
  assert.equal(spawned.length, 2);
  spawned[1].stdout.write('{"id":2,"ok":true,"result":{}}\n');
  await second;
  bridge.dispose();
});

test("拒绝库外、隐藏目录和模板路径，规范化无效设置", () => {
  assert.equal(isManagedPath("04 - 统计学习/习题/习题 ML001.md"), true);
  for (const value of ["../outside.md", "C:/outside.md", "/outside.md", "模板/概念模板.md", "附件/readme.md", ".obsidian/a.md", "abc/.hidden/a.md"]) assert.equal(isManagedPath(value), false);
  const root = path.resolve(os.tmpdir(), "dsm-vault");
  assert.equal(insideVault(root, ".data-science-index/lancedb"), path.join(root, ".data-science-index", "lancedb"));
  assert.throws(() => insideVault(root, "../outside"), /当前知识库内/);
  const settings = normalizeSettings({ resultLimit: 0, device: "invalid", semanticEnabled: false });
  assert.equal(settings.resultLimit, 50);
  assert.equal(settings.device, "auto");
  assert.equal(settings.semanticEnabled, false);
});

test("用户状态操作只写status，保留归档进度与其他字段", async () => {
  const plugin = new Plugin();
  const file = new FakeTFile("04 - 统计学习/习题/习题 ML001.md");
  const frontmatter = { status: "not-started", archive_status: "in-progress", source_id: "DS001", untouched: [1, 2] };
  let writes = 0;
  plugin.records = [{ path: file.path, kind: "exercise", status: "not-started" }];
  plugin.catalogRevision = 0;
  plugin.app = {
    vault: { getAbstractFileByPath: (value) => value === file.path ? file : null },
    fileManager: { processFrontMatter: async (_, callback) => { writes += 1; callback(frontmatter); } },
    workspace: { getLeavesOfType: () => [] },
  };
  await plugin.setStudyStatus(file.path, "in-progress");
  assert.deepEqual(frontmatter, { status: "in-progress", archive_status: "in-progress", source_id: "DS001", untouched: [1, 2] });
  assert.equal(writes, 1);
  assert.equal(plugin.records[0].status, "in-progress");
  assert.equal(plugin.indexDirty, true);
  await assert.rejects(plugin.setStudyStatus(file.path, "archived"), /合法的学习状态/);
  await assert.rejects(plugin.setStudyStatus("../outside.md", "completed"), /管理范围/);
  assert.equal(writes, 1);
});

test("插件加载只读取元数据，不同步索引或启动Python", async () => {
  const plugin = new Plugin();
  const file = new FakeTFile("04 - 统计学习/习题/习题 ML001.md");
  plugin.loadData = async () => ({});
  plugin.registerView = plugin.addRibbonIcon = plugin.addCommand = plugin.addSettingTab = plugin.registerEvent = () => {};
  plugin.app = {
    vault: { getMarkdownFiles: () => [file], on: () => ({}) },
    metadataCache: { on: () => ({}), getFileCache: () => ({ frontmatter: { tags: ["exercise"], status: "not-started" } }) },
    workspace: { getActiveFile: () => file, getLeavesOfType: () => [], on: () => ({}), onLayoutReady: (callback) => callback(), detachLeavesOfType: () => {} },
  };
  await plugin.onload();
  assert.equal(plugin.records.length, 1);
  assert.equal(plugin.bridge.proc, null);
  assert.equal(plugin.bridge.pending.size, 0);
  assert.equal(plugin.indexStatus, null);
  plugin.onunload();
});

class Element {
  constructor(tag = "div", options = {}) { this.tag = tag; this.text = options.text || ""; this.children = []; this.value = ""; }
  child(tag, options) { const value = new Element(tag, options); this.children.push(value); return value; }
  createDiv(options = {}) { return this.child("div", options); }
  createEl(tag, options = {}) { return this.child(tag, options); }
  createSpan(options = {}) { return this.child("span", options); }
  addEventListener() {}
  empty() { this.children = []; }
}

test("显示筛选不改变后端语义或关联结果的排序", () => {
  const plugin = { settings: { resultLimit: 50 }, openNote() {}, setStudyStatus() {} };
  const view = new ManagerView({}, plugin);
  view.resultsEl = new Element();
  view.items = [
    { path: "z.md", title: "最相关", kind: "concept", topic: "deep-learning", status: "not-started" },
    { path: "a.md", title: "次相关", kind: "concept", topic: "deep-learning", status: "not-started" },
  ];
  view.total = 2;
  view.renderResults();
  const flatten = (element) => [element, ...element.children.flatMap(flatten)];
  assert.deepEqual(flatten(view.resultsEl).filter((element) => element.tag === "button").map((element) => element.text), ["最相关", "次相关"]);
});

test("语义筛选改变会重新检索，而非只过滤已取出的前N项", async () => {
  const view = new ManagerView({}, {});
  view.mode = "semantic";
  view.query = "损失函数";
  view.resultMode = "semantic";
  let searches = 0;
  view.search = async () => { searches += 1; };
  view.renderResults = () => { throw new Error("不能仅在现有结果中筛选"); };
  await view.filterChanged();
  assert.equal(searches, 1);
});

test("相关内容筛选会以原参考笔记重查，并把筛选条件传给后端", async () => {
  const file = new FakeTFile("04 - 统计学习/概念/一元回归.md");
  const requests = [];
  const plugin = {
    app: { vault: { getAbstractFileByPath: () => file } },
    records: [{ path: file.path, kind: "concept" }],
    settings: { resultLimit: 20 },
    bridge: { request: async (op, payload) => { requests.push({ op, payload }); return { items: [], total: 0 }; } },
  };
  const view = new ManagerView({}, plugin);
  view.setBusy = view.renderResults = () => {};
  view.feedback = { classList: { remove() {} }, textContent: "" };
  view.resultMode = "related";
  view.relatedReferencePath = file.path;
  view.filters = { kind: "exercise", topic: "statistical-learning", status: "not-started", source_id: "DS001" };
  await view.filterChanged();
  assert.deepEqual(requests, [{ op: "related", payload: { ...view.filters, path: file.path, limit: 20 } }]);
  assert.equal(view.relatedReferencePath, file.path);
});
