# talk-harness-201

> **DSH harness 解剖场（advanced）。** 与 `talk-harness-101`（入门场：模型外面那一圈，五个地方）和
> `talk-ai-coding-evolution-harness`（主线：AI Coding 时代 SDLC 如何变化）**互相独立、不搬运内容**——
> 本场对象是 DSH 这一个具体系统，讲它的 harness 做得有多好、好在哪里、哪部分搬得走。

## 定位

**一句话**：解剖 DSH（DeepSeek Harness）的 harness——一个自称开发主力是 coding agent 的仓库，
凭什么让 fresh agent **不糊涂、不乱发挥**。答案不是"模型聪明"，是**三条立场把成本结构整个反过来**。

**弧线（用户定，2026-09-25）**：**先把"为什么是那三条立场"讲清楚，再走道（五个概念）、分水岭（动手）、术（执行态）**。
顺序不许倒：三条立场是每一段"为什么要有这道"的公共根因，跳过它，后面的机制就只是奇观清单。

**听众（提案，待用户定）**：正在为自己项目／团队搭或维护 coding agent 环境的工程师与技术负责人；
术语可以比 101 硬，但每个自造词首次出现要当场兑现。不要求听过 101，也不依赖主线。

**篇幅（提案，待定）**：约 30–40 张 ＋ 停顿页，45–60 min。

## 素材（仓库外，只读）

- 语料根：`/Users/bowhead/deepseek-harness/_faq_on_digested/07_borrowing-harness-idea/`（18 件，约 1700 行）
  ——**只在里面读，不写**。要引用就摘进 `02_evidence/00-sources.md` 并标注来源路径＋证据强度。
- 语料的证据纪律：DSH 侧事实一律钉版在 commit `46a7f68b09`（`dsh-v0.1.7-rc.1`），以 GitHub 绝对 URL 引用；
  本场沿用同一条纪律（见 `02_evidence/00-sources.md`）。
- 语料自带结构：**道（01–05）→ 分水岭（06）→ 术（07–13）→ 压尾（14）**；`answer.md` 是导读，
  三条立场＋三层模型＋三问自检都在里面——storyline 的骨架就从这里来。

## 目录约定

- 管道：`01_storyline → 02_evidence → 03_outline → 04_drafts → 05_output`（与仓库其他 talk 一致）。
- `CURRENT.md`：热区唯一权威（一句话／状态表／定调／下一步／待定／缺口）。
- `CONTEXT.md`：术语与红线唯一权威——**本场红线本场自治**（例：DSH 是主角，产品名允许上屏；
  这与 101 的"不出现产品名"相反，两场互不套用）。
- 临时产物：仓库根目录、`.tmp-harness-201-` 前缀，不入库，版本收口即清理。
- 暂不需要 `AGENTS.md`：纪律并进本文件与 `CONTEXT.md`；踩坑多了再补。
