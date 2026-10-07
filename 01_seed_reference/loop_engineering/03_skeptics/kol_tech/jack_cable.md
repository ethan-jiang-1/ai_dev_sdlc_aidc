---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-06
---

# jack_cable — loop engineering 证据轨迹（2026-06 后，时间正序）


> **背景**：Jack Cable——安全研究者：2017 五角大楼 Hack the Air Force 冠军（累计报告 350+ 漏洞）→ Stanford CS → 国防部 Defense Digital Service → CISA（选举安全、Crossfeed、Ransomwhere、Secure by Design 联合领导）→ Krebs Stamos Group 安全架构师；现 Corridor（保护 AI coding agent 产出代码的安全公司）联合创始人/CEO（与 Ashwin Ramaswami 联创，Alex Stamos 任 CSO）。（履历核：ai.engineer 讲者页，2026-10-07）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**状态**：单点观察（一手来源已核）；第九轮（2026-10-07）补全推荐面节（见文末增量）。
### Jack Cable（AI 安全研究者；讲中自述 "the work that I was doing in government around the Secure by Design initiative"；曾报告数百个漏洞）· AIEWF 2026《The AI bugpocalypse is here. Now what?》（视频上传 2026-07-12）

- URL：https://ai.engineer/talks/7JgIS42mz7U-ai-bugpocalypse-is-here-now-what （curl 实取全文）
- 号召力口径：③（安全政策/漏洞研究圈号召力；非 dev-tool KOL——按口径标注为安全域 KOL）。
- **挂钩**：无人值守运行（自主度×攻击面）＋验证回路。
- 逐字摘录：

> "It's no longer autocomplete to opt-ins, not even a developer synchronously within Cursor… when we do our own development right now, it's spinning up agents from within Slack or wherever folks are working and having many agents run at once in the background. So this is a tremendous shift in how software is being built."
>（把"多 agent 后台并行"作为安全前提的既成事实陈述。）

> "Models can do a better job finding vulnerabilities. On the other hand, our attack surfaces are growing immensely, as AI becomes the default code writer… both ends of the equation shifting."
>（**双向挤压论**：自主编码扩面、自主攻击提速同时发生。）

- 官方分节："Coding and attacks become more autonomous together""Intelligence does not supply the missing threat model""Put security into the work before the pull request"。
- **最小主张**：bugpocalypse 的根源不是代码质量而是**自主度与攻击自主化的共振**；威胁模型是循环里缺失的一环。
- **派别适配**：**怀疑票（强，安全域）**。

---

# 增量补挖（2026-10-07 第九轮·怀疑者替代推荐专项：推荐面）

> 通道：ai.engineer 讲稿页重取（官方逐字稿＋8 分节全列，fetch 成功）。本轮引句全部当日 fetch 逐字取得；页面 article voice（报告语）与逐字稿分开标注。

**官方分节名（全列）**："More vulnerabilities in the software everyone depends on"／"Coding and attacks become more autonomous together"／"A new discovery need not be a new vulnerability class"／"Safer new code and the case for structural repair"／"Intelligence does not supply the missing threat model"／"Put security into the work before the pull request"／"Defender access to powerful models"／"New code, shared foundations and independent customization"。

## 处方面（安全左移的具体主张）

**逐字摘录（均为仓库新引句）**：

> "our perspective at Corridor is around preventing vulnerabilities before the pull request, um, as well as giving visibility into how AI coding tools are being used."
（**双件套处方**：漏洞拦截前置到 PR 之前＋对 AI 编码工具使用方式的可见性。）

> "security cannot be the blocker when it comes to companies accelerating their development, right? Um, acceleration is always going to win out." ＋ "we really need to have tooling in place that allows, um, security teams to have that assurance, um, and to, to give the blessing to their, their engineering team to accelerate."
（**处方立场**：安全不能当刹车——护栏的目的恰恰是给工程团队放行加速；没有护栏才有漏洞。）

> "the vulnerabilities being introduced are often less so the basic one-liner vulnerabilities and more so contextual issues, right? Things like authorization bugs that require an in-depth understanding of a company's business logic. Um, and that's something, right, even if the model is very smart, it's not being trained on your company's proprietary information or how your own, um, kind of, you know, threat model works."
（**威胁模型缺口**：模型没被训练过你公司的业务逻辑与威胁模型——公司专有信息必须以某种方式送达开发过程（页面 article voice 收束："Those requirements have to reach the development process somehow."——**处方止于"必须送达"，未给机制**，引用勿过度具体化）。）

> "within the next six to 12 months, the majority of code that is being shipped will be reviewed, uh, not by human, but by AI."
（AI 审查 AI 预言——他的前提是"先有 PR 前拦截＋可见性"才可接受；页面标注这是 Corridor 预测非实测。）

> "One was to prevent vulnerabilities in new code going forward." ＋ "second is to harden the open source foundation." ＋ "It really has to be more systemic and start to get into, um, rewrites that can fundamentally reduce the risk of vulnerabilities that can be found, whether by models today or in the future."
（**国会三建议**：新代码防漏洞／加固开源底座／系统性重写。）

> "or we could do a one-time rewrite, for instance, to move some of these critical libraries, um, into, um, a language like Rust, right? And then that will pay dividends for years to come."
（**类级防御＋结构性重写**：一次性 Rust 重写关键库吃多年红利——补单个漏洞不如消灭整类。）

> "What are the fundamental controls that can protect against, um, any vulnerabilities that can be discovered by models today or in the future?"
（收束问句＝处方总纲：找的是面向"未来一切可发现漏洞"的基础控制。）

## 本轮推荐面小结（一句）

Cable 的替代方案：**安全左移（PR 前拦截＋安全团队可见性→换取 AI 审 AI、少人监督合并的自主度）＋威胁模型送达开发过程＋类级防御与结构性重写（Rust 化）**——左移的机制细节他未给全（负结论）。
