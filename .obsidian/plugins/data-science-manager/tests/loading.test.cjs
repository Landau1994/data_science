"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const { renderBundle } = require("../build.cjs");

const directory = path.resolve(__dirname, "..");
const source = fs.readFileSync(path.join(directory, "main.source.js"), "utf8");
const built = fs.readFileSync(path.join(directory, "main.js"), "utf8").replace(/\r\n/g, "\n");
const catalog = fs.readFileSync(path.join(directory, "catalog.js"), "utf8");

class FakePlugin {
  constructor(app, manifest) {
    this.app = app;
    this.manifest = manifest;
    this.commands = [];
    this.ribbons = [];
    this.views = [];
    this.events = [];
    this.settingsTabs = [];
  }
  async loadData() { return {}; }
  registerView(...args) { this.views.push(args); }
  addRibbonIcon(...args) { this.ribbons.push(args); }
  addCommand(command) { this.commands.push(command); }
  addSettingTab(tab) { this.settingsTabs.push(tab); }
  registerEvent(event) { this.events.push(event); }
}

class FakeTFile {
  constructor(relative) {
    this.path = relative;
    this.basename = path.basename(relative, ".md");
    this.extension = "md";
  }
}

function obsidianLoader(code) {
  const requested = [];
  const api = {
    Plugin: FakePlugin,
    ItemView: class {},
    PluginSettingTab: class {},
    Setting: class {},
    Notice: class {},
    TFile: FakeTFile,
  };
  // 复制实际 Obsidian loadPlugin 的调用形态：eval 包裹入口，再传入 window.require。
  // window.require 不知道插件目录，本地相对 require 在这里必须失败。
  const loaderRequire = (name) => {
    requested.push(name);
    if (name === "obsidian") return api;
    if (name === "child_process") return {
      spawn() { throw new Error("加载插件不能启动模型或索引进程"); },
    };
    if (["path", "fs"].includes(name)) return require(name);
    const error = new Error(`Cannot find module '${name}' from the Obsidian application loader`);
    error.code = "MODULE_NOT_FOUND";
    throw error;
  };
  const entry = vm.runInNewContext(
    `(function anonymous(require,module,exports){${code}\n})`,
    { console, process: { env: {} }, setTimeout, clearTimeout },
    { filename: "plugin:data-science-manager" },
  );
  const module = { exports: {} };
  entry(loaderRequire, module, module.exports);
  return { Plugin: module.exports.default || module.exports, requested };
}

test("原来的未打包入口可复现 Obsidian 相对模块加载失败", () => {
  assert.throws(() => obsidianLoader(source), { code: "MODULE_NOT_FOUND" });
});

test("发布入口在 Obsidian 式加载器下只依赖 API 与 Node 内置模块", () => {
  const loaded = obsidianLoader(built);
  assert.equal(typeof loaded.Plugin, "function");
  assert.equal(typeof loaded.Plugin._internals.PythonBridge, "function");
  assert.deepEqual(loaded.requested, ["obsidian", "child_process", "path", "fs"]);
  assert.equal(loaded.Plugin.prototype instanceof FakePlugin, true);
});

test("打包入口能实例化并完成 onload，保留目录且不启动后台模型", async () => {
  const { Plugin } = obsidianLoader(built);
  const file = new FakeTFile("00 - 首页/教材归档/DS001 - Understanding Deep Learning.md");
  const app = {
    vault: { getMarkdownFiles: () => [file], on: () => ({}) },
    metadataCache: {
      on: () => ({}),
      getFileCache: () => ({ frontmatter: { title: "理解深度学习", tags: ["source", "reading-ledger"], source_id: "DS001", status: "not-started" } }),
    },
    workspace: {
      getActiveFile: () => file,
      getLeavesOfType: () => [],
      on: () => ({}),
      onLayoutReady: (callback) => callback(),
      detachLeavesOfType: () => {},
    },
  };
  const plugin = new Plugin(app, { id: "data-science-manager", dir: ".obsidian/plugins/data-science-manager" });
  await plugin.onload();
  assert.equal(plugin.commands.length, 3);
  assert.equal(plugin.ribbons.length, 1);
  assert.equal(plugin.views.length, 1);
  assert.equal(plugin.settingsTabs.length, 1);
  assert.equal(plugin.records.length, 1);
  assert.equal(plugin.records[0].source_id, "DS001");
  assert.equal(plugin.bridge.proc, null);
  assert.equal(plugin.indexStatus, null);
  plugin.onunload();
  assert.equal(plugin.bridge.disposed, true);
});

test("单文件构建可重复且发布入口与源码严格一致", () => {
  assert.equal(built, renderBundle(source, catalog));
  assert.equal(renderBundle(source, catalog), renderBundle(source, catalog));
  assert.doesNotMatch(built, /\brequire\s*\(\s*['"]\./);
});
