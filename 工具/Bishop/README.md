# Bishop 教材习题来源对账

`source-manifest.json` 保存 DS003 原始 PDF 的 SHA-256、已核对章节的有序题号、星数、精确页码和一题一笔记映射。它是原题核对记录，正文、解答与学习状态以 Markdown 为准；统一教材台账位于 [[00 - 首页/教材归档/DS003 - Deep Learning Foundations and Concepts|DS003]]。

在知识库根目录运行只读检查（需要 Python 与 PyYAML）：

```powershell
python -X utf8 工具/Bishop/archive_audit.py
python -X utf8 工具/Bishop/archive_audit.py --chapter 2
```

已登记第1–20章全部352道编号习题，第1章经原页审计为零题。检查原书版本、缺失、重复、多余、无法解析的映射及必要元数据和结构，支持P、ST、LA、ML、PM、DL主题前缀。章节清单同时记录印刷页、PDF物理页、跨页和图件；各章页码偏移分别核对，不套用全书统一偏移。未登记章节会明确报错，不把空查询误当作无习题。

原题星数使用 `source_stars` 保留，笔记难度仍使用 `beginner`、`intermediate`、`advanced`。归档状态、来源核对范围与个人学习状态分别维护。本工具不改笔记、不生成题单、不维护抽样队列，也不执行 Obsidian 的实际渲染。
