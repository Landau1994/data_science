---
title: "微软智能体入门课程（AI Agents for Beginners）"
aliases: ["AI Agents for Beginners"]
tags: [source]
topic: ai-engineering
topic_label: AI工程
status: not-started
source_id: DS027
source_kind: course
source_status: partially-verified
archive_status: source-audit-pending
archived_chapters: []
archived_exercise_count: 0
author: Microsoft
edition: "GitHub 英文课程，2026-11-21 核对版本 3bee2ddf"
source_commit: "3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e"
location: "microsoft/ai-agents-for-beginners"
url: "https://github.com/microsoft/ai-agents-for-beginners"
checked: 2026-11-21
created: 2026-11-21
---

# 微软智能体入门课程（AI Agents for Beginners）

## 文献信息

微软维护的在线课程包括 18 节正课和 1 节环境配置。以下导读依据 2026-11-21 核对的英文版本，逐课链接固定到同一提交。[英文课程目录](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/README.md) · [简体中文入口](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/translations/zh-CN/README.md) · [官方学习指南](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/STUDY_GUIDE.md)

## 与 AI 工程学习路线的关系

本库把这门课接在 [[00 - 首页/教材归档/DS018 - Building Effective Agents|DS018《构建有效智能体》]] 之后。下列两个入口对应 [[10 - AI工程/AI工程导航|AI 工程导航]] 的第 2、3 步。按课号顺读可直接进入 [[#完整课程导读]]。

### 智能体实践

读过 [[10 - AI工程/概念/智能体|智能体（agent）]] 后，先看模型如何发出一次请求、工具如何返回结果，再看多个请求如何组成计划。[[#第 04 课 工具使用|04 工具使用]] · [[#第 07 课 任务规划|07 任务规划]]

### 运行支撑选读

学习 [[10 - AI工程/概念/智能体运行支撑|智能体运行支撑（agent harness）]] 时，可以把一次运行拆成三个问题：发生了哪些调用、模型当时看到了什么、哪些信息能留到下次会话。[[#第 10 课 运行追踪与评价|10 运行追踪与评价]] · [[#第 12 课 上下文工程|12 上下文工程]] · [[#第 13 课 智能体记忆|13 智能体记忆]]

## 完整课程导读

每课链接指向英文正文中实际核对的小节。复选框后的问题由本库编写，供个人读后自检。原课程配套的测验和作业另见 [[#原课自测与实践作业]]。

### 第 00 课 课程环境配置

课程用 Jupyter 笔记本演示智能体。按第一个要跑的示例确定依赖：使用云端时，项目端点决定连接哪个项目，部署名决定调用哪个模型，身份凭据决定能访问什么。第 5、16 课用到的 Azure AI Search 有单独的配置说明，本机推理则有 Foundry Local 路线。

- [ ] 如果笔记本能打开却无法调用模型，怎样区分解释器、身份和部署配置这三类问题？

原文《Course Setup》 · [Running the Code](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/00-course-setup/README.md#running-the-code)

### 第 01 课 智能体与适用场景

用旅行助手辨认环境、观察与行动：读取票价得到新的信息，提交预订则会改变外部状态。微软也把规则驱动的反射型系统列入智能体分类；和 DS018 对读时，应先写清讨论采用的定义。

- [ ] 在只需查询固定班次的任务里，哪一步真的需要系统临时决定？

原文《Introduction to AI Agents and Agent Use Cases》 · [What are AI Agents?](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/01-intro-to-ai-agents/README.md#what-are-ai-agents) · [配套 Python 笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/01-intro-to-ai-agents/code_samples/01-python-agent-framework.ipynb)

### 第 02 课 智能体框架

微软用订票函数示范如何把模型客户端与工具装进一个智能体。示例函数返回一段预订描述，正适合检查工具究竟产生了什么结果。Microsoft Agent Framework 提供组装组件的软件开发工具包（SDK），Foundry Agent Service 承担托管职责。

- [ ] 如果要把演示接入真实订票服务，框架已经管理了什么，还需要业务系统返回什么凭据？

原文《Explore AI Agent Frameworks》 · [Use Modular Components](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/02-explore-agentic-frameworks/README.md#use-modular-components) · [配套 Python 笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/02-explore-agentic-frameworks/code_samples/02-python-agent-framework.ipynb)

### 第 03 课 面向用户的智能体设计

课程从交互环境、时间和智能体自身三个角度讨论设计。旅行助手可以让用户查看过去的请求、修改偏好或删除会话。这些具体操作让透明度、用户控制和交互一致性成为可以检查的设计要求。

- [ ] 旅行助手沿用了一条过时偏好时，用户能在哪里发现、纠正并确认这项修改？

原文《AI Agentic Design Principles》 · [The Guidelines to Implement These Principles](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/03-agentic-design-patterns/README.md#the-guidelines-to-implement-these-principles) · [配套 Python 笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/03-agentic-design-patterns/code_samples/03-python-agent-framework.ipynb)

### 第 04 课 工具使用

查询城市时间的例子展示了函数调用（function calling）的一次往返。模型读工具描述，给出函数名与参数，应用执行函数并把结果送回模型，之后才形成用户看到的答复。这里能直接看出工具选择和工具执行各由谁负责。

- [ ] 怎样从一次调用记录判断，模型只提出了查时间，还是确实收到了时区换算后的结果？

原文《Tool Use Design Pattern》 · [Function/Tool Calling](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/04-tool-use/README.md#functiontool-calling) · [配套 Python 笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/04-tool-use/code_samples/04-python-agent-framework.ipynb)

### 第 05 课 智能体检索增强生成

检索增强生成（retrieval-augmented generation，RAG）让回答可以使用检索到的资料。新品上市案例要综合市场报告、竞争信息和内部销售数据。智能体根据已获证据决定换来源、改写查询、再检索或结束，检索顺序也因此成为需要评价的对象。

- [ ] 如果三个来源对销量的描述互相矛盾，下一次检索要查清什么才值得继续？

原文《Agentic RAG》 · [Owning the Reasoning Process](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/05-agentic-rag/README.md#owning-the-reasoning-process)

### 第 06 课 可信智能体与人工复核

课程先用系统消息约定助手的职责，再讨论人在回路（human-in-the-loop）如何介入运行。正文的诗歌示例是在生成后征求反馈，配套笔记本还展示了操作前审批。放行一项操作和评价一份已生成的结果，发生在不同时间。

- [ ] 旅行助手可以先草拟行程。如果要代为下单，审批应放在哪一步，用户需要看到哪些信息？

原文《Building Trustworthy AI Agents》 · [Human-in-the-Loop](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/06-building-trustworthy-agents/README.md#human-in-the-loop) · [人工复核笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)

### 第 07 课 任务规划

家庭旅行案例把总目标拆成机票、住宿和活动等子任务，用结构化输出记录任务及负责者，供下一步路由。计划列出要做的事；判断哪些任务已完成，还要看相应执行者返回了什么。

- [ ] 假设房间已经订满，计划里的哪些子任务要重排，哪些结果可以保留？

原文《Planning Design》 · [Task Decomposition](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/07-planning-design/README.md#task-decomposition) · [配套 Python 笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/07-planning-design/code_samples/07-python-agent-framework.ipynb)

### 第 08 课 多智能体协作

退款案例把风险核查、支付和合规分给拥有不同工具和权限的角色。群聊（group chat）允许共同讨论，交接（handoff）则把后续处理交给指定角色。读这个例子时，可以沿着一次退款查清谁发起、谁判断、谁有权执行。

- [ ] 什么条件值得引入专门角色？如果所有步骤都使用同一组工具，额外的交接解决了什么问题？

原文《Multi-agent design patterns》 · [Scenario: Refund process](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/08-multi-agent/README.md#scenario-refund-process) · [客服设计参考解](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/08-multi-agent/solution/solution.md)

### 第 09 课 元认知与纠错

元认知（metacognition）在这里指系统检查先前选择并调整策略。纠错检索先评价已有结果，再决定是否重查。酒店示例展示从低价转向高质量的推荐，但反馈来自模拟，后一次调用也显式指定了新策略。

- [ ] 若要验证系统学会了何时调整策略，怎样设计一个事先没有指定第二步策略的测试？

原文《Metacognition in AI Agents》 · [Corrective RAG Approach](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/09-metacognition/README.md#corrective-rag-approach)

### 第 10 课 运行追踪与评价

一次任务对应一条追踪记录（trace），其中的模型调用、检索和工具执行各可记录为跨度（span）。离线评价用有已知答案的测试集检验回归，在线评价从真实交互观察成功率、延迟和用户反馈；两种结果回答的问题不同。

- [ ] 一次报销处理变慢但最终答对，应该检查哪段耗时？又该怎样判断新版本是否比旧版本更可靠？

原文《AI Agents in Production: Observability & Evaluation》 · [Agent Evaluation](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/10-ai-agents-production/README.md#agent-evaluation) · [报销处理笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/10-ai-agents-production/code_samples/10-expense_claim-demo.ipynb)

### 第 11 课 智能体通信协议

在同一旅行场景里，模型上下文协议（Model Context Protocol，MCP）让应用发现并调用工具，智能体间协议（Agent-to-Agent Protocol，A2A）支持把任务委派给另一个智能体。NLWeb 则让用户或应用用自然语言查询网站内容，例如搜索酒店目录。

- [ ] 查询航空工具、委派给酒店智能体、搜索酒店网站，这三种请求各自期待收到什么？

原文《Using Agentic Protocols (MCP, A2A and NLWeb)》 · [MCP Example](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/11-agentic-protocols/README.md#mcp-example)

### 第 12 课 上下文工程

上下文工程（context engineering）决定下一次模型调用能看到什么。课程用工作便笺保存当前进度，将较长历史压缩为摘要，并讨论如何检查实际送入窗口的信息。这个选择会影响下一步是否仍看得见用户的约束。

- [ ] 历史记录变长后，怎样压缩行程讨论，同时保留日期、预算和用户最后一次更正？

原文《Context Engineering for AI Agents》 · [Managing Context](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/12-context-engineering/README.md#managing-context)

### 第 13 课 智能体记忆

工作记忆保留眼前任务所需的信息，短期记忆维系本次会话，长期记忆让某条偏好跨会话被检索。课程用连续两轮旅行询问解释短期指代，又用以后的旅行仍可取回住宿偏好来解释长期存储。

- [ ] “那里”的指代与“以后优先住安静的房间”各应保存多久？偏好变更后，如何避免取回旧值？

原文《Memory for AI Agents》 · [Types of Memory](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/13-agent-memory/README.md#types-of-memory) · [记忆示例笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/13-agent-memory/13-agent-memory.ipynb)

### 第 14 课 微软智能体框架实作

在 Microsoft Agent Framework 中，执行器（executor）处理输入并发出消息，边（edge）决定下一个执行器。旅行工作流可以在客房售罄时走另一条分支；会话保存历史，检查点（checkpoint）则用于保存工作流进度。

- [ ] 若任务在酒店返回售罄后中断，恢复时需要知道哪段对话，以及工作流已经走到了哪里？

原文《Exploring Microsoft Agent Framework》 · [Workflows](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/14-microsoft-agent-framework/README.md#workflows) · [LangGraph 托管示例](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)

### 第 15 课 浏览器与界面操作

计算机使用智能体（computer use agent，CUA）的房源案例先在动态网页中找到斯德哥尔摩的搜索结果，再用结构化字段提取房源、价格和评分，交给程序比较。页面导航与稳定步骤可分别交给模型和 Playwright；从比价转到预订时还要取得用户许可。

- [ ] 如果页面布局发生变化，怎样区分导航失败、价格提取错误和比价算法错误？

原文《Building Computer Use Agents (CUA)》 · [Architecture Overview](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/15-browser-use/README.md#architecture-overview) · [浏览器实作笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/15-browser-use/15-browser-user.ipynb)

### 第 16 课 部署与扩展

客服案例比较应用自行托管、服务托管和工作流编排。多实例部署时，把会话状态放在进程外，其他实例才能接手。课程把上线前的离线评价、部署后的基本可用性检查（smoke test）与处理线上问题的运行追踪串在一起。

- [ ] 如果一次简单调用在部署后成功，哪些有关多轮恢复、人工审批和回答质量的问题仍要另行测试？

原文《Deploying Scalable Agents with Microsoft Foundry》 · [Agent Deployment Patterns](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/16-deploying-scalable-agents/README.md#agent-deployment-patterns) · [客服部署实验](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb)

### 第 17 课 本地智能体

本地工程助手让 Qwen 选择工具，由工具读取项目文件，并用 Chroma 检索已索引的文档。小语言模型（small language model，SLM）、检索索引和文件访问可以留在本机；是否交给云端处理，要结合数据边界、任务难度和延迟判断。

- [ ] 同一个项目里，查设计意图、读某个配置值和定位待办注释，分别需要什么证据？

原文《Creating Local AI Agents Using Microsoft Foundry Local and Qwen》 · [Local RAG](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/17-creating-local-ai-agents/README.md#local-rag) · [本地助手实验](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb)

### 第 18 课 用签名回执审计工具调用

密码学回执（cryptographic receipt）把工具调用的关键字段与签名绑定。验证者使用独立取得的可信公钥检验记录，连续回执中的前序摘要还可用于检查所给链条的顺序。动作是否符合用户意图、所引政策是否真正执行，仍需相应业务证据。

- [ ] 一张签名有效的预订回执能支持哪些判断？若用户对预订金额提出异议，还需核对什么？

原文《Securing AI Agents with Cryptographic Receipts》 · [What is a Cryptographic Receipt?](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/18-securing-ai-agents/README.md#what-is-a-cryptographic-receipt) · [签名回执实验](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/18-securing-ai-agents/code_samples/18-signed-receipts.ipynb)

## 原课自测与实践作业

按英文课文的 *Knowledge Check(s)* 小节核对，5 课合计 28 道编号自测。第 8 课把答案放在独立文件，第 15–18 课在题后提供可展开的答案。

| 课次 | 原课编号自测 | 实践任务与参考材料 |
| --- | --- | --- |
| 08 | [第 1–2 题](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/08-multi-agent/README.md#knowledge-checks)，判断何时选用多个智能体。[选择题答案](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/08-multi-agent/solution/solution-quiz.md) | 为客服流程设计分工、权限和交接。[原作业](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/08-multi-agent/README.md#assignment) · [设计参考解](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/08-multi-agent/solution/solution.md) |
| 15 | [第 1–5 题](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/15-browser-use/README.md#knowledge-check)，涉及浏览器与 API 的选择、动态导航、人工确认和数据验证。 | 在房源比价笔记本里对照模型导航和程序提取的步骤。[配套笔记本](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/15-browser-use/15-browser-user.ipynb) |
| 16 | [第 1–8 题](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/16-deploying-scalable-agents/README.md#knowledge-check)，涉及托管、外部状态、模型路由与上线评价。 | 把客服改为订阅计费助手，加入账单工具与政策文档，分别检验审批规则和调用成本。[作业与提交要求](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/16-deploying-scalable-agents/README.md#assignment) |
| 17 | [第 1–8 题](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/17-creating-local-ai-agents/README.md#knowledge-check)，涉及本地模型、工具、检索与云端分工。 | 建立本地文档审阅器，索引项目文件，分别计时检索、读文件和查找待办三类任务。[作业与提交要求](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/17-creating-local-ai-agents/README.md#assignment) |
| 18 | [第 1–5 题](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/18-securing-ai-agents/README.md#knowledge-check)，涉及离线验签、字段完整性与信任边界。 | 笔记本含签发、校验、串联和工具调用回执四部分，另有两个拓展挑战。[练习说明](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/18-securing-ai-agents/README.md#practice-exercise) |

第 01、04、05 课还各有一项可选的部署后基本检查，便于对照第 16 课的验证方法。[第 01 课](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/01-intro-to-ai-agents/README.md#smoke-testing-this-agent-optional) · [第 04 课](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/04-tool-use/README.md#smoke-testing-this-agent-optional) · [第 05 课](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/05-agentic-rag/README.md#smoke-testing-this-agent-optional) · [第 16 课验证说明](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/16-deploying-scalable-agents/README.md#validating-a-deployed-agent-with-smoke-tests)

官方学习指南另有 7 个综合自检问题和一项结课项目。项目要求搭建课程导学助手，按用户主题查找课次、给出学习顺序和一项练习，并展示所用来源。拓展任务再加入偏好记忆、计划、自检和工具日志。[综合自检](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/STUDY_GUIDE.md#quick-self-check) · [结课项目](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/STUDY_GUIDE.md#suggested-capstone-exercise)

## 来源问题与边界

英文目录与单课标题有时不同。第 03 课的目录强调设计模式，正文从设计原则讲起。第 13 课在目录中写作 *Managing Agentic Memory*，正文题为 *Memory for AI Agents*。第 18 课的目录标题是 *Securing AI Agents*，正文聚焦密码学回执。导读采用正文标题，保留各课原始定位。[课程总目录](https://github.com/microsoft/ai-agents-for-beginners/blob/3bee2ddf8e7aab27b17ef9e1d4a3f2c541a1913e/README.md)

已核对第 00–18 课的英文正文小节、列出的测验题号和配套材料入口。中文概括和自检问题为本库编写。笔记本、云端部署和浏览器示例均未在本轮运行，译文、视频和代码实现未逐项复核。

## 学习与阅读

个人学习状态为「尚未开始」。可在读完每课后用该课的复选框记录自检进度。

## 习题归档

上面的原课自测和作业已定位至原文。本页下表按来源编号显示另行建成的习题笔记，当前归档数为 0。

```dataview
TABLE WITHOUT ID
  source_chapter AS "章节",
  source_exercise AS "原书题号",
  file.link AS "习题",
  choice(difficulty = "beginner", "入门", choice(difficulty = "intermediate", "中级", "进阶")) AS "难度",
  choice(status = "completed", "已完成", choice(status = "in-progress", "正在学习", "尚未开始")) AS "学习状态"
FROM #exercise
WHERE this.source_id AND source_id = this.source_id
SORT number(source_chapter) ASC, number(split(source_exercise, "[.]")[1]) ASC
```
