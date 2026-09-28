# ① 机器可核判据逐轮闸门 — 工程实践做法库

> 每行：谁 | 做法一句 | 机制细节 | 强度 | 指针。
> **逐字引句回 evidence 档案，此处只写机制概括**。初盘 2026-09-28，全部来自既有回源，未做新抓取。

| 谁 | 做法 | 机制细节 | 强度 | 指针 |
|---|---|---|---|---|
| Huntley · Ralph | **back pressure：任何能拒绝无效生成的都能接进闸门** | 安全扫描、静态分析、类型系统（静态类型语言内建；动态类型语言必须补 type checker，文中点名 dialyzer / pyrefly）；每轮实现后跑该单元测试；无 build/test 错误 → 打 git tag（patch +1）作为该轮绿灯 | 一手 · 个人实践 | [evidence-b](../../raw/evidence-2026-09-26-b-stop-and-scheduling.md) §1 |
| Anthropic 2024 | **每步从环境取 ground truth** | 工具结果/代码执行即进度依据；编码域四条件：可自动化测试验证 / 可用测试结果迭代 / 问题空间结构化 / 输出可客观测量 | 一手 · 官方博客 | evidence-b §2 |
| Anthropic 2025 · Effective harnesses | **feature_list.json 逐条判定** | 粗目标展开成 200+ 条 feature（category / description / steps / passes），初始全 `false`，"全真"＝完成的机器可核定义；标记通过的前置是**端到端自验证**（browser automation 像人一样测），不是单测/curl | 一手 · 官方博客 | evidence-b §3 |
| Claude Code `/goal` | **官方"可核条件"写法三要素** | 可度量终态（测试结果 / 构建退出码 / 文件数 / 空队列）＋声明式检查（`npm test` exits 0 / `git status` clean）＋路径约束（不得改其他测试文件） | 一手 · 厂商文档 | evidence-b §4a |
| LangChain · Runkle | **grader 分两类** | verification loop ＝ rubric ＋ grader；deterministic（测试 / CI / 链接检查）与 agentic（LLM-as-judge）；不合格带反馈回环重试。注意厂商动机（推 RubricMiddleware / LangSmith） | 一手 · 厂商博客 | evidence-b §4e |
| Kent Beck | **单测试节拍** | 人说 go → 只实现计划里下一条未标记测试 → 只写刚好能过的代码；把**删/关测试列为作弊信号**；两次尝试因复杂度累积停摆，靠人插手设计才继续 | 一手 · 个人实践 | [evidence-i](../../raw/evidence-2026-09-27-i-high-influence-control.md) Source 3 |
| Huntley · Ralph | **防作弊条款** | 测试当场写明"为什么存在"——因为 future loops 看不到当时的推理（上下文窗口里没有） | 一手 · 个人实践 | evidence-b §1 |
| Anthropic 2025 | **判据保护条款** | 强措辞"删改测试不可接受"＋ **JSON 格式选型**（模型更不容易不当改写/覆写 JSON，相比 Markdown） | 一手 · 官方（单源但机制成型） | evidence-b §3 |
| Yegge | **行为面反例** | 上下文将尽时 "A missing test is a passing test"、否认既有失败——**判据存在 ≠ 判据被诚实执行** | 一手 · 个人观察 | evidence-i Source 5 |

**同向票数**（判定归 digested/03，此处仅提示）：机器闸门构件＝Huntley、Anthropic 2024/2025、LangChain 四家同向；Beck / Yegge 为 2026-09-27 I 路新增独立作者补强，不改收敛票数。
