# ① 机器可核判据逐轮闸门（machine gates）

**本点回答**：每轮"接受/拒绝"由什么判？判据从哪来？怎么防判据被当事人废掉？

**判定句**（权威在 [`../../digested/03-构件.md`](../../digested/03-构件.md) §一）：
测试/类型/linter/静态分析/构建退出码做逐轮闸门（Huntley 称 back pressure，LangChain 称 grader）；
判据的可核性来自**环境 ground truth**，编码域天然适合（"Code solutions are verifiable through automated tests"，Anthropic 2024）。
≥2 独立一手同向：Huntley / Anthropic 2024 / Anthropic 2025 / LangChain 四家。

## 看板

| 件 | 状态 |
|---|---|
| [`practices.md`](practices.md) | ✅ **自说明版**（2026-09-28 用户定硬要求）：18 条，每条自带核心片段（原句/代码/参数）＋机制＋源；覆盖 coding/docs/data/math/security 五域＋框架源码缺省 |
| [`insights.md`](insights.md) | ✅ 初盘 6 条＋深挖批 6 条（65% 量化、闸门分层、测试外置双源汇合、闸门自锁与放行、防削测试工程化） |
| 新回源 | ✅ 2026-09-28 补采收口：Aider（auto_lint 默认开＋confirm 回灌）/ OpenHands（auto-lint 默认关）入 [evidence-q](../../raw/evidence-2026-09-28-q-framework-defaults.md)；SWE-agent/LangGraph 的 cap 侧记在 02 |

## 待挖清单

1. ~~grader 选型依据~~ → **部分推进**：promptfoo/Braintrust 给出生产配置面与 judge 选型法（evidence-m S7/S8）；deterministic/agentic 的错误类别边界仍开放。
2. ~~grader 失败模式~~ → **大幅推进**：isitdone 削弱测试检测器＋192 例基准（evidence-p S1）、METR 独立裁判被攻破实录（evidence-n S8）、裁判四类失效实证（evidence-m）。剩余：生产 grader 被讨好的具体案例。
3. ~~非编码域~~ → **大幅推进**：docs/data/math/security 四域已有形态（evidence-p S5–S8）；SQL/Great Expectations 负结论待补。
4. **端到端自验证的工程细节**——仍开放（官方 demo 只给方向）。
5. ~~行为面验证~~ → **推进**：65% 量化＋检测器工程化（evidence-p S1）；对照组缺失仍开放。
6. **判据的维护**：谁写、谁更新、失效怎么发现——仍开放（新条目只添了"测门本身"一个实例）。
