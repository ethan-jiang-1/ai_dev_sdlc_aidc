---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-07
---

# tim_bray — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：ongoing 博主；前 AWS VP／Principal Engineer；XML 与 JSON 规范编辑
> **背景**：Tim Bray——亚马逊基础设施时代元老（曾负责 AWS S3 等团队）、Sun Microsystems 前员工、XML/JSON 规范共同编辑；Quamina 作者（开源事件匹配库）；长期独立技术写作。**第九轮（2026-10-07）新入册。**（履历核：ongoing.by，2026-10-07）
> **号召力**：②＋③＋④（技术社区高声望个人作者；一手亲历账本）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)（2026-10-07 第九轮入册）
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：接受能力、拒绝产出进主线（对 loop 产出的**政策性拒收**）
**起点**：接受 Claude-authored PR → **终点**：拒绝（除漏洞报告例外）
**关键转折**：逐 PR 审查没有累积出系统级理解——"my reviewing was ineffective"

## 《Clankers and Data Races》（ongoing，2026-09-01）

- URL：ongoing.by（2026-09-01；09-02 有更新与勘误评论）｜ fetch 成功（全文）
- 来源类型：个人一手博客（全文取得）。
- **挂钩**：⑤验证回路（PR review 回路失效的亲历反证）＋①循环结构（loop 产出的接受政策）。

**逐字摘录**：

> "I have been accepting Claude-authored PRs but, to the extent I can detect them, I'm stopping."
（**政策改变**：开始拒收 clanker PR——注意他的理由不是能力。）

> "Claude and its competitors can write perfectly decent code, particularly where the task at hand can be narrowly focused."
（**前提声明**：代码本身可以"相当不错"——拒收基于负外部性与信任，不是质量必差。）

> "Interestingly, we got to the current epsilon-closure code in a sequence of reasonable-looking PRs that I reviewed, asking for changes in most. But in the big picture my reviewing was ineffective, because it ended with a large lump of code that I don't understand or, at the end of the day, trust. I wonder how typical that outcome is?"
（**本轮最重的验证回路反证句**：每个 PR 都审了、多数还要求了修改，最后仍得到一大坨"不理解也不信任"的代码——**逐 PR 人审叠加不等于系统级理解**。与 Ronacher《Tower》"塔不倒只是继续长高"同构的亲历版。）

> "This will have a real cost; some of those PRs yielded big performance boosts."
（**拒收的自认代价**：有些被拒 PR 带来过大性能提升——政策是有意识付出代价。）

## 处方面（替代做法）

**逐字摘录**：

> "I don't really understand the 500 or so lines of clanker code and test that compute epsilon closures... Sufficiently so that I've written an issue to think it over, understand it, and with any luck, simplify it."
（**理解债显式化**：不理解的代码立 issue 消化——把"review 过但不理解"变成待办而不是默认接受。）

> "There's an exception to my new policy: Vulnerability reports. I think it'd be irresponsible to ignore them and penalize Quamina's users because I don't like the source."
（**例外通道**：漏洞报告照收——clanker 用途收窄到"可独立验证"的场景。）

> "First, believe what the profiler is telling you! Second, if you're having trouble understanding unit test output, dig around a bit and make sure it's doing what you think it is."
（**验证纪律两条**：信 profiler；看不懂单测输出就去挖，确认它真在测你以为的东西——后者直接来自一次被 agent 发现的数据 race＋自写基准误导读骗的经历。）

**该条支持的最小主张**：一线维护者给出"逐 PR 人审回路失效"的亲历账本（review 了每一环、仍不理解整体），并以政策响应：拒收 clanker PR（自担性能损失）＋例外只留可独立验证的漏洞报告＋理解债立 issue 显式化。
**派别适配**：**怀疑票（验证回路向，亲历账本）**——他反的不是 agent 写码能力，是"人审能兜底"的默认假设。
