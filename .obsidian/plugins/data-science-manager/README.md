# 数据科学知识库管理器

本知识库独立的 Obsidian 桌面插件，用户说明见库内 [[00 - 首页/知识库管理器使用指南|知识库管理器使用指南]]。

## 文件与运行

- Obsidian 直接加载 `manifest.json`、已生成的单文件 `main.js` 与 `styles.css`；普通使用无需构建。`main.js` 已内含目录模块，不依赖 Obsidian 不支持的插件目录相对 `require`。
- `main.source.js`、`catalog.js` 为开发源文件。修改后运行 `node .obsidian/plugins/data-science-manager/build.cjs` 重新生成入口；构建仅使用 Node 内置模块，无需安装构建依赖。
- `scripts/vault_index.py` 通过逐行 JSON 提供 `status`、`sync`、`search`、`related`。插件启动隐藏的 Python 子进程，串行处理请求，超时、错误与卸载时清理；不开 HTTP 端口。
- 前端关键词即时读取笔记，语义与关联查询使用本库真实 LanceDB；后端也提供中英文关键词查询供测试。
- 学习状态使用 Obsidian `processFrontMatter`，仅在用户选择后更新该笔记的 `status`。后端只读 Markdown。

默认 Python 为 `C:/Users/Administrator/.conda/envs/localllm/python.exe`；模型为 `E:/OneDrive/Documents/project/lm_weight/bge_m3`，均可在设置中修改。已验证 Python 3.12、LanceDB 0.37.1、PyArrow 25.0.1、PyYAML 6.0.3、sentence-transformers 5.7.0、torch 2.5.1+cu121；本轮未安装依赖或下载模型。

## 开发检查

从知识库根目录运行：

```powershell
node --check .obsidian/plugins/data-science-manager/main.js
node .obsidian/plugins/data-science-manager/build.cjs --check
node --test .obsidian/plugins/data-science-manager/tests/catalog.test.cjs .obsidian/plugins/data-science-manager/tests/frontend.test.cjs .obsidian/plugins/data-science-manager/tests/loading.test.cjs
& 'C:\Users\Administrator\.conda\envs\localllm\python.exe' -B -X utf8 .obsidian/plugins/data-science-manager/tests/test_vault_index.py -v
```

LanceDB 后台事件循环需要本机回环通信；受限执行器可能在导入阶段阻塞。本次已在正常本地执行环境实际验证索引和检索，不以包已安装替代可运行检查。

语义索引只保存真实 1024 维 bge-m3 向量；关键词模式未嵌入的记录为 `null`，不填假向量。关联查询依据链接、共同链接、来源和主题，分别解释理由。语义取标题及正文前 2048 个模型词元；关键词可查全文。未纳入 PDF 正文。

## 许可

MIT 许可见 `LICENSE`。参考本机原代数库 `.obsidian/plugins/exercise_manager`，保留其 `Copyright (c) 2026 local`；未复制数据库、`data.json`、每日抽样或系统推进状态。
