"use strict";

// Obsidian 使用 window.require 加载插件，不提供按插件目录绑定的本地 require。
// 发布入口因此必须内含 catalog；只使用 Node 内置模块，无需安装构建依赖。
const fs = require("node:fs");
const path = require("node:path");

const directory = __dirname;
const anchor = 'const catalog = require("./catalog");';

function normalize(text) {
  return text.replace(/\r\n/g, "\n").trimEnd() + "\n";
}

function renderBundle(entry, catalog) {
  entry = normalize(entry);
  catalog = normalize(catalog);
  if (entry.split(anchor).length !== 2) {
    throw new Error("入口源码必须且只能包含一个 catalog 导入位置。");
  }
  const inline = [
    "const catalog = (() => {",
    "  const module = { exports: {} };",
    "  const exports = module.exports;",
    catalog.trimEnd(),
    "  return module.exports;",
    "})();",
  ].join("\n");
  const result = "// 由 build.cjs 从 main.source.js 与 catalog.js 生成；请修改源码后重新构建。\n"
    + entry.replace(anchor, inline);
  if (/\brequire\s*\(\s*['"]\./.test(result)) {
    throw new Error("发布入口仍包含本地相对 require，不能由 Obsidian 直接加载。");
  }
  return result;
}

function build(checkOnly = false) {
  const rendered = renderBundle(
    fs.readFileSync(path.join(directory, "main.source.js"), "utf8"),
    fs.readFileSync(path.join(directory, "catalog.js"), "utf8"),
  );
  const target = path.join(directory, "main.js");
  if (checkOnly) {
    // Git 的 Windows 换行转换不会改变入口含义，检查时只统一 CRLF。
    if (!fs.existsSync(target) || fs.readFileSync(target, "utf8").replace(/\r\n/g, "\n") !== rendered) {
      throw new Error("main.js 与源码不一致，请运行 node build.cjs。");
    }
  } else {
    fs.writeFileSync(target, rendered, "utf8");
  }
  return rendered;
}

if (require.main === module) {
  try {
    const checkOnly = process.argv.includes("--check");
    build(checkOnly);
    console.log(checkOnly ? "单文件入口与源码一致。" : "已生成自包含的 Obsidian 单文件入口。");
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}

module.exports = { renderBundle, build };
