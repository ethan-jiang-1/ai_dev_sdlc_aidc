# ② 硬性资源上限兜底（hard caps）

**本点回答**：循环失控/空转/被遗忘时，什么东西保证它停？上限触发之后发生什么？

**判定句**（权威在 [`../../digested/03-构件.md`](../../digested/03-构件.md) §一）：
最大迭代/轮数/时间/拒绝计数/过期做兜底停止——**是资源熔断，不是质量分**。
五处一手同向：Anthropic 2024、CC `/goal`、CC auto mode、CC `/loop`、OpenAI auto-review（+I 路 Copilot 59 分钟补强）。

## 看板

| 件 | 状态 |
|---|---|
| [`practices.md`](practices.md) | ✅ **自说明版**：25 条（原 24 条＋第三轮深挖批 1 条：LangGraph RemainingSteps 主动预算感知模式）：厂商产品层 8＋框架缺省 4＋失控检测闸门 3＋失控实录与补救 4＋Ralph 反例＋候选 2＋学术层 3＋运行时预算感知 1 |
| [`insights.md`](insights.md) | ✅ 初盘 6 条＋深挖批 11 条（四件套、默认无限实证、闸门误报与逃生、动作梯子、缓存经济学、effective bound coverage 区分、rate limit 杀手效应、被动崩溃 vs 主动 RemainingSteps 降级） |
| 新回源 | ✅ 2026-09-28 第一批：evidence-q；第二批：IAL-Scan / ReliabilityBench / OpenHands stuck detector 入 [evidence-r](../../raw/evidence-2026-09-28-r-ial-scan-reliability.md)；**第三批**：LangGraph RemainingSteps 主动预算感知入 [evidence-s](../../raw/evidence-2026-09-28-s-langgraph-dbt-civ.md) |

## 待挖清单

1. ~~参数选择逻辑~~ → **大幅推进**：框架层默认值全景到手（OpenHands 500 轮次/预算 None、SWE-agent $3.0 成本/调用 0、LangGraph 1000↔10007、CrewAI 20↔25）——"为什么选这个维度"仍无人公开，但**缺省无共识**本身已成立（insights #13–#14）。
2. ~~熔断后的恢复语义对照~~ → **大幅推进**：quickstart（重试而非停机）、isitdone（闸门放行）、OpenAI PR#20672（熔断转人工审批）、LangGraph `RemainingSteps`（耗尽前 1 步主动优雅降级，避免 `GraphRecursionError` 异常崩溃丢失上下文，practices #25）。
3. ~~deny-and-continue 恢复率~~ → 仍开放（仍只有 auto-review >50% 一条）。
4. **被遗忘循环的真实频率** → **推进**：#46787 给出一手 zombie 实录（194h 孤儿进程）；仍无频率统计。
5. ~~上限的适应性~~ → **推进**：escalate 档（换更强模型＋花费帽）是新的"适应性"形态；动态调整本身仍开放。
6. **新开口**：缓存经济学与计费对齐（间隔 vs TTL）作为上限维度——只有转述级证据，需一手战报；孤儿清理/心跳的厂商内建化进展（截至 2026-09-28 无内建）。
