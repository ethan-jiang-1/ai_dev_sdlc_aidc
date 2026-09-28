# ② 硬性资源上限兜底 — 工程实践做法库

> 每行：谁 | 做法一句 | 机制细节 | 强度 | 指针。
> **逐字引句回 evidence 档案**。初盘 2026-09-28，全部来自既有回源，未做新抓取。

| 谁 | 做法 | 机制细节 | 强度 | 指针 |
|---|---|---|---|---|
| Anthropic 2024 | **最大迭代数写进停止条件** | 官方原句形态 "stopping conditions (such as a maximum number of iterations) to maintain control"——与"任务完成即终止"并列的兜底 | 一手 · 官方博客 | [evidence-b](../../raw/evidence-2026-09-26-b-stop-and-scheduling.md) §2 |
| Claude Code `/goal` | **上限子句＋无进展熔断＋错误分级** | 条件里可写 `or stop after 20 turns`；连续数轮无 tool use → 停、警告、**goal 保留**还给人；四类不可恢复错误（认证/额度/上下文溢出/模型不可用）**清空** goal；其余错误三次自动重试后暂停 | 一手 · 厂商文档 | evidence-b §4a |
| Claude Code auto mode | **双阈值拒绝熔断** | 3 连拒或累计 20 拒 → 停机升级给人；headless（`claude -p`）无 UI → 直接终止进程；**阈值官方写明不可配置** | 一手 · 官方博客＋文档 | evidence-b §4b |
| Claude Code `/loop` | **硬过期＋续排兜底** | 定时任务创建 7 天后自动过期（最后跑一次再自删，官方明说是"被遗忘的循环"的上界）；一次迭代未续排/未停 → 约 20 分钟后一次兜底 wakeup，仍未续排 → 终止 | 一手 · 厂商文档 | evidence-b §4c |
| OpenAI auto-review | **反复拒绝后自动停轨迹** | 监控 game the Auto-reviewer 的情形，repeated denials 后停轨迹；未公布具体阈值（与 CC 的 3/20 同型不同参） | 一手 · 官方博客 | evidence-b §4d |
| Codex（未合并 PR） | **轮内熔断改人工、记账分离** | 一轮内 auto-review 拒绝次数碰到熔断 → **触发那一次的动作改交人工**，机器拒绝和人的决定分开记账，人决定后重置熔断。源码证据，非已发布行为 | 一手 · 源码（固定 commit） | [evidence-f](../../raw/evidence-2026-09-27-f-autonomy-gates.md) |
| GitHub Copilot cloud agent | **产品级时间硬上限** | 每会话最长 59 分钟，不可延长不可绕过；跑在一次性 Actions 环境里；一次任务写范围＝单仓库/单分支/单 PR | 一手 · 厂商文档 | [evidence-i](../../raw/evidence-2026-09-27-i-high-influence-control.md) Source 8 |
| Codex compact | **上下文耗尽的资源兜底** | 早期要人敲 `/compact`；现在超过 `auto_compact_limit` 自动调 `/responses/compact`；阈值数字未公布。**compact 是资源兜底，不是质量验收** | ⚠️ 候选 · 未独立复核（直接页面 403） | [evidence-k](../../raw/evidence-2026-09-27-k-unrolling-codex-agent-loop.md) |
| Huntley · Ralph | **反例极：故意无限，上限外置给人** | `while :;` 无内建上限，前提是工具不限用量；失控时人判断 `git reset --hard` 还是换 prompt 救；与 Claude Code 家的"上限做成原语"构成两极 | 一手 · 个人实践 | evidence-b §1 |

**同向票数**（判定归 digested/03）：硬上限构件五处一手同向（Anthropic 2024 / CC `/goal` / auto mode / `/loop` / OpenAI auto-review），I 路 Copilot 59 分钟为独立补强。
