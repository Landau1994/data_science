"use strict";

// 即时目录只读 Obsidian 已解析的元数据，不依赖索引或模型。
const KINDS = Object.freeze([
  Object.freeze({ value: "source", label: "教材" }),
  Object.freeze({ value: "concept", label: "概念" }),
  Object.freeze({ value: "exercise", label: "习题" }),
  Object.freeze({ value: "project", label: "项目" }),
  Object.freeze({ value: "experiment", label: "实验" }),
]);

const TOPICS = Object.freeze([
  Object.freeze({ value: "probability-theory", label: "概率论" }),
  Object.freeze({ value: "mathematical-statistics", label: "数理统计" }),
  Object.freeze({ value: "linear-algebra-optimization", label: "线性代数与优化" }),
  Object.freeze({ value: "statistical-learning", label: "统计学习" }),
  Object.freeze({ value: "probabilistic-models", label: "概率模型与推断" }),
  Object.freeze({ value: "deep-learning", label: "深度学习" }),
  Object.freeze({ value: "causal-inference", label: "因果推断与实验" }),
  Object.freeze({ value: "stochastic-processes", label: "随机过程与时间序列" }),
  Object.freeze({ value: "data-computing", label: "数据计算与可复现性" }),
]);

const STATES = Object.freeze([
  Object.freeze({ value: "not-started", label: "尚未开始" }),
  Object.freeze({ value: "in-progress", label: "正在学习" }),
  Object.freeze({ value: "completed", label: "已完成" }),
]);

const KIND_PRIORITY = ["experiment", "project", "exercise", "concept", "source"];
const TOPIC_LABELS = new Map(TOPICS.map((item) => [item.value, item.label]));

function scalar(value) {
  return typeof value === "string" || typeof value === "number" || typeof value === "boolean"
    ? String(value).trim()
    : "";
}

function normalize(value) {
  return scalar(value).normalize("NFKC").toLowerCase();
}

function tagsFrom(value) {
  const values = Array.isArray(value) ? value : [value];
  const tags = [];
  for (const entry of values) {
    if (typeof entry !== "string") continue;
    let expanded = entry.trim();
    if (!expanded) continue;
    if (expanded.startsWith("[") && expanded.endsWith("]")) {
      try {
        const parsed = JSON.parse(expanded);
        if (Array.isArray(parsed)) {
          tags.push(...tagsFrom(parsed));
          continue;
        }
      } catch (_) {
        // 已解析的 YAML 通常提供数组；也兼容手工传入的裸行内标签。
      }
      expanded = expanded.slice(1, -1);
    }
    for (const token of expanded.split(/[\s,，]+/)) {
      const tag = token.replace(/^['"]|['"]$/g, "").replace(/^#+/, "").trim();
      if (tag) tags.push(tag);
    }
  }
  return [...new Set(tags)];
}

function aliasesFrom(value) {
  const values = Array.isArray(value) ? value : [value];
  return [...new Set(values.map(scalar).filter(Boolean))];
}

function recordFromFile(file, cache) {
  if (!file || typeof file.path !== "string" || !/\.md$/i.test(file.path)) return null;
  const path = file.path.replace(/\\/g, "/");
  if (path.startsWith("模板/") || path.split("/").some((part) => part.startsWith("."))) return null;
  const frontmatter = cache && typeof cache.frontmatter === "object" && cache.frontmatter
    ? cache.frontmatter
    : {};
  const inlineTags = Array.isArray(cache && cache.tags)
    ? cache.tags.map((entry) => entry && entry.tag)
    : [];
  const tags = [...new Set([...tagsFrom(frontmatter.tags), ...tagsFrom(inlineTags)])];
  const kind = KIND_PRIORITY.find((candidate) => tags.includes(candidate));
  if (!kind) return null;
  const topic = scalar(frontmatter.topic) || tags.find((tag) => TOPIC_LABELS.has(tag)) || "";
  const basename = scalar(file.basename) || path.split("/").pop().replace(/\.md$/i, "");
  return {
    path,
    title: scalar(frontmatter.title) || basename,
    kind,
    topic,
    topic_label: scalar(frontmatter.topic_label) || TOPIC_LABELS.get(topic) || "",
    status: scalar(frontmatter.status),
    difficulty: scalar(frontmatter.difficulty),
    source_id: scalar(frontmatter.source_id),
    source_exercise: scalar(frontmatter.source_exercise),
    archive_status: scalar(frontmatter.archive_status),
    tags,
    aliases: aliasesFrom(frontmatter.aliases),
  };
}

function keywordMatches(record, query, text = "") {
  const tokens = normalize(query).split(/\s+/).filter(Boolean);
  if (!tokens.length) return true;
  const haystack = normalize([
    record && record.title,
    record && record.path,
    record && record.source_id,
    record && record.source_exercise,
    ...(Array.isArray(record && record.aliases) ? record.aliases : []),
    scalar(text),
  ].filter((part) => part !== undefined && part !== null).join("\n"));
  return tokens.every((token) => haystack.includes(token));
}

function filterRecords(records, filters = {}) {
  return (Array.isArray(records) ? records : []).filter((record) => {
    if (!record || typeof record.path !== "string") return false;
    for (const key of ["kind", "topic", "status", "source_id"]) {
      const expected = scalar(filters[key]);
      if (expected && expected !== "all" && record[key] !== expected) return false;
    }
    return keywordMatches(record, filters.query, record.text || "");
  }).sort((left, right) => {
    const result = left.path.localeCompare(right.path, "zh-CN", { numeric: true });
    return result || (left.path < right.path ? -1 : left.path > right.path ? 1 : 0);
  });
}

function excerpt(text, max = 180) {
  let body = typeof text === "string" ? text : "";
  body = body.replace(/^\uFEFF?---\r?\n[\s\S]*?\r?\n---(?:\r?\n|$)/, "");
  body = body.replace(/<!--[\s\S]*?-->/g, " ");
  body = body.replace(/<\/?[a-z][^>]*>/gi, " ");
  body = body.replace(/^\s*>\s*\[![^\]]+\][+-]?[^\r\n]*/gm, " ");
  body = body.replace(/^\s*>\s?/gm, "");
  body = body.replace(/^\s*(?:#{1,6}\s+|[-*+]\s+(?:\[[ xX]\]\s*)?|\d+[.)]\s+)/gm, "");
  body = body.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (_, target, label) => label || target);
  body = body.replace(/!?\[([^\]]+)\]\([^)]*\)/g, "$1");
  body = body.replace(/```[^\r\n]*/g, " ").replace(/`|\*\*|__/g, "");
  body = body.replace(/\s+/g, " ").trim();
  const requested = Number(max);
  const limit = Number.isFinite(requested) ? Math.max(0, Math.floor(requested)) : 180;
  const chars = Array.from(body);
  if (chars.length <= limit) return body;
  return limit ? chars.slice(0, limit - 1).join("") + "…" : "";
}

function countKinds(records) {
  const counts = Object.fromEntries(KINDS.map(({ value }) => [value, 0]));
  for (const record of Array.isArray(records) ? records : []) {
    if (record && Object.prototype.hasOwnProperty.call(counts, record.kind)) counts[record.kind] += 1;
  }
  return counts;
}

module.exports = { KINDS, TOPICS, STATES, recordFromFile, filterRecords, keywordMatches, excerpt, countKinds };
