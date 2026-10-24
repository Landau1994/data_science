"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { KINDS, TOPICS, STATES, recordFromFile, filterRecords, keywordMatches, excerpt, countKinds } = require("../catalog.js");

const file = { path: "04 - 统计学习/习题/习题 ML003 - 生成式与判别式线性回归.md", basename: "习题 ML003 - 生成式与判别式线性回归" };
const base = {
  title: "习题 ML003：生成式与判别式线性回归",
  tags: ["exercise", "statistical-learning"],
  topic: "statistical-learning",
  status: "not-started",
  difficulty: "intermediate",
  source_id: "DS001",
  source_exercise: "2.3",
  aliases: ["Generative Linear Regression", "Inverse Regression"],
};

test("读取 YAML 列表与完整来源字段，并使用中文主题标签", () => {
  const record = recordFromFile(file, { frontmatter: base });
  assert.equal(record.kind, "exercise");
  assert.equal(record.path, file.path);
  assert.equal(record.title, base.title);
  assert.equal(record.topic_label, "统计学习");
  for (const field of ["status", "difficulty", "source_id", "source_exercise"]) assert.equal(record[field], base[field]);
  assert.deepEqual(record.aliases, base.aliases);
});

test("标签字符串、内联数组与 Obsidian 行内标签均不会按字符拆分", () => {
  for (const tags of ["#exercise statistical-learning", "exercise,statistical-learning", '["exercise", "statistical-learning"]', "[exercise, statistical-learning]"]) {
    const record = recordFromFile(file, { frontmatter: { ...base, tags } });
    assert.deepEqual(record.tags, ["exercise", "statistical-learning"]);
  }
  const inline = recordFromFile(file, { frontmatter: { title: "行内概念" }, tags: [{ tag: "#concept" }, { tag: "#deep-learning" }] });
  assert.equal(inline.kind, "concept");
  assert.equal(inline.topic, "deep-learning");
  assert.equal(inline.topic_label, "深度学习");
});

test("只发现真实的五类 Markdown 笔记，不索引导航或模板", () => {
  assert.equal(recordFromFile(file, { frontmatter: { tags: ["hub", "index"] } }), null);
  assert.equal(recordFromFile({ path: "模板/习题模板.md" }, { frontmatter: base }), null);
  assert.equal(recordFromFile({ path: ".obsidian/记录.md" }, { frontmatter: base }), null);
  assert.equal(recordFromFile({ path: "附件/书籍.pdf" }, { frontmatter: { tags: ["source"] } }), null);
  assert.equal(recordFromFile(null, null), null);
});

test("教材兼归档标签仍是教材，实验标签优先于项目", () => {
  const source = recordFromFile({ path: "00 - 首页/教材归档/DS001.md" }, { frontmatter: { tags: ["source", "exercise-archive"], archive_status: "in-progress" } });
  assert.equal(source.kind, "source");
  assert.equal(source.archive_status, "in-progress");
  const experiment = recordFromFile(file, { frontmatter: { tags: ["project", "experiment"] } });
  assert.equal(experiment.kind, "experiment");
});

test("空状态保持空，不根据习题标题猜测学习进度", () => {
  const record = recordFromFile(file, { frontmatter: { tags: ["exercise"], source_exercise: 2.3, aliases: "Simple Linear Regression" } });
  assert.equal(record.status, "");
  assert.equal(record.source_exercise, "2.3");
  assert.deepEqual(record.aliases, ["Simple Linear Regression"]);
  assert.equal(record.title, file.basename);
});

test("九个主题及三个稳定学习状态完整且没有重复", () => {
  assert.equal(TOPICS.length, 9);
  assert.equal(new Set(TOPICS.map(({ value }) => value)).size, 9);
  assert.deepEqual(STATES.map(({ value }) => value), ["not-started", "in-progress", "completed"]);
  assert.deepEqual(KINDS.map(({ value }) => value), ["source", "concept", "exercise", "project", "experiment"]);
});

test("组合筛选严格匹配类别、主题、来源和学习状态", () => {
  const record = recordFromFile(file, { frontmatter: base });
  const records = [record, { ...record, path: "03 - 线性代数与优化/概念/梯度.md", kind: "concept", topic: "linear-algebra-optimization", status: "completed", source_id: "DS017" }];
  assert.deepEqual(filterRecords(records, { kind: "exercise", topic: "statistical-learning", source_id: "DS001", status: "not-started" }), [record]);
  assert.deepEqual(filterRecords(records, { kind: "exercise", status: "completed" }), []);
  assert.equal(filterRecords(records, { kind: "all" }).length, 2);
});

test("中文、英文别名、正文与原题号查询支持大小写和全角输入", () => {
  const record = recordFromFile(file, { frontmatter: base });
  assert.equal(keywordMatches(record, "生成式 DS001"), true);
  assert.equal(keywordMatches(record, "GENERATIVE regression"), true);
  assert.equal(keywordMatches(record, "２．３"), true);
  assert.equal(keywordMatches(record, "backpropagation", "A Backpropagation example."), true);
  assert.equal(keywordMatches(record, "regression missing"), false);
  assert.equal(keywordMatches(record, "[.*]"), false);
  assert.equal(keywordMatches(record, "  "), true);
  assert.equal(filterRecords([{ ...record, text: "Loss function on training data" }], { query: "loss" }).length, 1);
});

test("筛选不会修改原记录，按库内路径稳定排序", () => {
  const records = [{ path: "习题 10.md", title: "十" }, { path: "习题 2.md", title: "二" }];
  const before = structuredClone(records);
  assert.deepEqual(filterRecords(records).map(({ path }) => path), ["习题 2.md", "习题 10.md"]);
  assert.deepEqual(records, before);
});

test("摘要去掉来源元数据、callout及HTML标记，保留正文纯文本", () => {
  const source = '\uFEFF---\r\ntitle: 不应进入摘要\r\nsource_id: DS999\r\n---\r\n## 定义\r\n> [!info] 提示\r\n> **监督学习** [[概念/梯度|梯度]]\r\n> <img src=x onerror=alert(1)> 用于优化。';
  const result = excerpt(source);
  assert.equal(result, "定义 监督学习 梯度 用于优化。");
  assert.equal(result.includes("DS999"), false);
  assert.equal(result.includes("onerror"), false);
  assert.equal(excerpt("😀😀😀😀", 3), "😀😀…");
  assert.equal(excerpt("abc", 0), "");
});

test("五类计数包含零，忽略未知类别", () => {
  assert.deepEqual(countKinds([null, { kind: "source" }, { kind: "source" }, { kind: "exercise" }, { kind: "hub" }]), { source: 2, concept: 0, exercise: 1, project: 0, experiment: 0 });
  assert.deepEqual(filterRecords([null, undefined]), []);
});
