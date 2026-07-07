---
type: event_session
event: Pragmatic Summit 2026
session: Simon Willison Fireside Chat — Agentic Engineering
date: 2026-02-11
location: San Francisco
verification_status: verified
source_urls:
  - https://simonwillison.net/2026/Mar/14/pragmatic-summit/
  - https://www.youtube.com/watch?v=owmJyKVu5f8
  - https://github.com/jerrylususu/bookmark-summary/blob/main/202603/2026-03-15-my-fireside-chat-about-agentic-engineering-at-the-pragmatic-summit.md
key_participants:
  - Simon Willison (Django co-creator, Datasette author)
key_concepts:
  - agentic_engineering_stages
  - conformance_driven_development
  - showboat
  - no_read_mode
  - tests_are_free_now
---

# Simon Willison 炉边对话 — Agentic Engineering 的阶段论与实战模式

> 来源：Simon Willison 在 Pragmatic Summit 2026 的炉边谈话。
> 原文链接：[My fireside chat about agentic engineering at the Pragmatic Summit](https://simonwillison.net/2026/Mar/14/pragmatic-summit/) (2026-03-14) · [YouTube 视频](https://www.youtube.com/watch?v=owmJyKVu5f8)

---

## AI 采用的三个阶段

| 阶段 | 描述 |
|---|---|
| **Stage 1: Chat 辅助** | 用 ChatGPT 问问题，偶尔有帮助 |
| **Stage 2: Coding Agent** | Agent 写代码片段，最终写的比人还多 |
| **Stage 3: "No-Read" 模式** | 完全不读代码——Simon 称之为 "clear insanity"（明显的疯狂），以 StrongDM 的"黑暗工厂"为例 |

---

## Conformance-Driven Development（合规驱动开发）

Willison 在 Summit 上详细描述了这项技术：

> *"I had a project recently where I wanted to add file uploads to my own little web framework, Datasette... I told Claude to build a test suite for file uploads that passes on Go and Node.js and Django and Starlette — just here's six different web frameworks that implement this, build tests that they all pass. Now I've got a test suite and I can say, okay, build me a new implementation for Datasette on top of those tests. And it did the job."*

核心思路：**让 AI 从六个实现的共性中反向工程出一个标准，然后基于这个标准实现新的。**

他发布了生成的测试套件：`github.com/simonw/multipart-form-data-conformance`

这意味着：Tests 不再只是 validation——它们变成了**合规检查**。

> *"Tests are no longer even remotely optional — they're free now."*

---

## Showboat — 让 Agent 证明自己

Simon 构建了一个叫 **Showboat** 的工具——生成 Markdown 文档记录 Agent 执行的手动测试，包括 curl 命令及其输出。Agent 不只是写代码，还要**演示/证明它是对的**。

---

## 关键引用

> *"It's almost like you can reverse engineer six implementations of a standard to get a new standard and then you can implement the standard."*

> *"Tests are no longer even remotely optional — they're free now."*
