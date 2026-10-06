---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# lance_martin — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Anthropic（LangChain 前工程师）
> **背景**：Lance Martin——LangChain 前工程师（RAG/agent 课程与 LangChain Academy 作者），现 Anthropic（Claude Agent SDK 长时任务方向，AIEWF 2026 workshop 主讲）。
> **号召力**：③
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察——待补挖。
### Lance Martin（Anthropic）· AIEWF 2026 Workshop《Claude for long-horizon tasks》（视频上传 2026-07-22）

- URL：https://ai.engineer/talks/9QebvrrY3KY-claude-long-horizon-tasks （curl 实取全文）
- 身份：Anthropic（Managed Agents 方向）。
- 号召力口径：③＋④。
- **挂钩**：无人值守运行＋验证回路＋外层调度（Managed Agents 产品化）。
- 逐字摘录：

> "Back in the Opus 3 days… models could only do, maybe, ten to twenty minutes of autonomous work. This is measured by METR… In order to really unlock async, we needed longer task horizons, and so we're starting to see that now."
>（用 METR task horizon 给"无人值守何时成立"定量分期——自主度分档的时间轴版。）

> "It's quite effective to separate verification into a separate context window… when you build loops, you can have a loop of a build context and a verifier context, and this can be a build agent, verifier agent… this continues in a loop until verification is complete. And this is really the big idea behind this whole loops trend that you might have heard about."
>（**厂商自述"loop 风潮的本体＝build/verifier 双上下文回路"**——验证回路的定义级引句。）

> "What happens if the harness dies or the container dies? …the harness becomes a stateless process that talks to a session. The session is an append-only event log… credentials are never actually added to the sandbox. They're stored in a separate vault."
>（长时程架构三件套：脑手解耦、append-only 会话、凭据外置金库。）

- **最小主张**：无人值守成立条件＝task horizon 足够长＋会话状态与执行环境解耦＋独立 verifier 回路；Anthropic 已把该套件产品化（Managed Agents）。
- **派别适配**：**推动票（强）**。
