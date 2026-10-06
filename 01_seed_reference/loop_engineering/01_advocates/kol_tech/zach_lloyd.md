---
type: kol_evidence
directory: 01_advocates/kol_tech
observation_date: 2026-10-06
---

# zach_lloyd — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Warp 创始人/CEO
> **号召力**：③＋④ 终端平台
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

## 态度轨迹

**方向**：稳定推动·激进化
**起点**：推动·布道（self-improvement loop）
**终点**：推动·实证（七段自动化＋合并率爬坡）
**弧线**：06-16 自改进循环博客 → 07-01 Latent Space 访谈 → 08-06 SED 访谈（SE 主环七段自动化＋自动合并率 20%→60% 爬坡）
**关键转折**：08-06 从'倡导循环'转为'实测爬坡数据'——自动合并率从 20% 升到 60%
### Zach Lloyd（Warp 创始人/CEO）· Latent Space 访谈《why software factories are the next phase of coding》（2026-07-01，Richard MacManus）

- URL：https://www.latent.space/p/software-factories （curl 实取全文）
- 身份：在册 KOL（Warp）；本条为 **Latent Space 访谈新载体**（SEDaily 1941 逐字稿另立推-16）。
- 号召力口径：①＋③＋④。
- **挂钩**：循环产品化机制（工厂＝SE 主环自动化）＋无人值守运行＋外层调度（meta-engineering）。
- 逐字摘录：
  - "Then it became: run an agent in the cloud on a timer. The next question was, what is the most valuable loop to automate? The answer is basically the main loop of software engineering: **triage, specification, implementation, review, verification, shipping and monitoring**."（**SE 主环七段清单**——本运动迄今最完整的"该自动化哪个环"表述。）
  - "Companies will start with specific use cases, certain types of issues or lower-risk repositories. Those are places where they may be comfortable not having a human review every single line of code. They will see how it performs. Then the engineering challenge becomes: instead of merging 20% of pull requests automatically, can we get to 30%, 40%, 50% or 60%?"（**自动合并率爬坡＝自主度分档的工程化指标**。）
  - "I think it can be extremely interesting if you view the job as meta-engineering: building the system that builds the product."（与 swyx "build the thing that builds the thing" 同构。）
  - "My prediction is that every significant software project will have some engine of code — something resembling a factory — continuously driving it forward. It will become similar to GitHub or CI/CD: a standard part of how serious software projects operate."（循环产品化的 GitHub/CI 化预言。）
  - "Perhaps code review is the bottleneck… You only discover those problems by trying to build the loop."（把"验证回路是第一瓶颈"写进建环方法论。）
- **最小主张**：软件工厂＝把 SE 主环（triage→spec→实现→review→验证→shipping→monitoring）整体自动化并按仓库风险分档放权；人的位置由"每行必审"退到"低风险仓库免审＋合并率爬坡"。
- **派别适配**：**推动票（强）**。

### Zach Lloyd · Software Engineering Daily #1941《The Terminal as an Agentic Interface》（2026-08-06，官方 transcript .txt 实取）

- URL：https://softwareengineeringdaily.com/podcasts/the-terminal-as-an-agentic-interface/ ；transcript：https://softwareengineeringdaily.com/wp-content/uploads/2026/08/SED1941-Zach-Lloyd.txt （curl 实取）
- **挂钩**：预算与熔断＋无人值守运行（云侧治理件）。
- 逐字摘录：
  - "we increasingly, we hear that companies want cost controls on these agents… They want auditability. If an agent does something that causes a problem, you want to be able to go see what it did. They want handoff from cloud to local."
  - "You want these things running in Sandboxes. You want them having lease privilege… They have limited network egress. They have the minimum number of MCP privileges and secrets to other internal tools… we're going to go into a phase where the maturity of these tools becomes more important."
  - "Oz is cloud agent infrastructure… it could be automated code review, or it could be automated debt code cleanup, code migrations. It could be issue triage. It could literally just be implementing features and fixing bugs. The way that's going to happen in the future, I strongly believe, is… you're going to scale it is if you move it to the cloud."
- **最小主张**：企业采购 agent 循环的三件套＝成本控制＋可审计＋最小权限沙箱；循环的规模化解在云侧基础设施而非本地。
- **派别适配**：**推动票（治理翼）**。
