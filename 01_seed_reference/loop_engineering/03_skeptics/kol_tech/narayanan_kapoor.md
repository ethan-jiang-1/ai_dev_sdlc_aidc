---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-07
---

# narayanan_kapoor — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Arvind Narayanan（Princeton 计算机科学与公共事务教授）＆ Sayash Kapoor（Princeton 研究学者）；《AI as Normal Technology》作者
> **背景**：Princeton "AI as Normal Technology" 学派双主笔；substack 迁址自 aisnakeoil.com 至 normaltech.ai（8.7 万+ 订阅）——AI 政策/安全侧最高引用度的学术组合之一。**第九轮（2026-10-07）新入册。**（履历核：normaltech.ai，2026-10-07）
> **号召力**：② 被主流政策/学界引用＋④ 大分发（8.7 万订阅）＋① 学术框架提出者（AI control 路线）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)（2026-10-07 第九轮入册）
> 人群类型：**专业技术 KOL**（学者）

## 态度轨迹

**方向**：反对"放权让渡"默认（"we don't have to cede control"）——AI control 派
**起点**：decide-execute-deliver sandwich（06-11）→ **终点**：AI control 五件套＋"AI control should become a job"（09-14）
**关键转折**：09-14 长文把怀疑落到机制清单与组织治理

## 《Why AI hasn't replaced software engineers, and won't》（normaltech.ai，2026-06-11）

- URL：normaltech.ai（原 aisnakeoil.com，已 301 迁址）｜ fetch 成功（全文）
- **挂钩**：⑥无人值守运行（反对当然论）＋⑤验证回路＋②停止条件（人问责）。

**逐字摘录**：

> "Writing code isn't, and never was, the bottleneck."
（**开篇定调**：写码从来不是瓶颈——对"产码速度＝工程效率"叙事釜底抽薪。）

> "software engineers' work consists of a "decide-execute-deliver" sandwich (with understanding being a prerequisite for all three). AI has compressed the middle of the sandwich, but has left the two ends largely unchanged."
（**三明治模型**：decide-execute-deliver，理解是三者前提——AI 只压扁了 execute 层，两端没变。）

> "engineers are discovering that supervising coding agents is surprisingly time consuming."
（监督 agent 意外地耗时——引 Willison"11 点心力耗尽"作证（Willison 已归档，此处只作指向）。）

> 引 SWE-chat 数据集（arXiv 2604.20779，转引级——论文正文未 fetch，引用须保留标注）："The study found that only 44% of agent-produced code survives into user commits, that vibe-coded commits introduce vulnerabilities at nine times the human-only rate, and that the most common user intent is understanding existing code, not generating new code (19% vs 13%)."
（**44% 存活率＋9 倍漏洞率＋最大意图是理解存量代码**——对"agent 产能"叙事的三连反证。）

> "Even if the technical barriers go away in the future, we don't have to cede control to AI."
（**反"无人值守当然论"的直接宣言**：技术可行≠必须放权。）

> "we can collectively choose to keep humans accountable through shared norms, law, and policy. This is a much more resilient way to control the speed of AI impacts and improve safety than trying to slow the development of technical capabilities."
（推荐面（社会层）：靠规范/法律/政策保人问责，比拖慢技术更 resilient。）

> "AI agents will do most of the cognitive heavy lifting; supervising the agent and keeping it in control becomes most of the human's job."
（推荐面（个人层）：人的主要工作变成**监督 agent 并保持控制**（crane operator 类比）。）

## 《The AI-as-Normal-Technology view of loss-of-control incidents》（normaltech.ai，2026-09-14，1.3 万字）

- URL：normaltech.ai ｜ fetch 成功（全文）。直接挂钩 OpenAI/Hugging Face 事故（与怀疑档 dwarkesh.md《Agent Civilizations》同事件谱系）。
- **挂钩**：⑥无人值守运行＋③预算与熔断（shutdown）＋⑤验证回路（logging/monitoring）＋②停止条件（tripwires）——**AI control 五件套直接对应 loop 七类中的四类**。

**逐字摘录**：

> "But note that the incident occurred when OpenAI had disabled most mechanisms for controlling their agents."
（**事故定性**：失控发生在"控制机制大多被关掉"的时候——不是 agent 必然失控，是治理被撤。）

> "Engineers work long days, spin up thousands of experiments, and there's insufficient human oversight of these experiments."
（对"实验室跑几千个 loop 实验"文化的直接批评——引 Joshua Saxe"Wild West feeling"二手证词（转引级）。）

> "This includes improvements to sandbox security (to prevent AI models from taking unanticipated actions outside the sandbox), implementing the principle of least privilege, comprehensive logging, automated tripwires for unsafe behaviors, rapid shutdown mechanisms, and monitoring the agent to detect and prevent harmful actions."
（**AI control 五件套＋沙箱**：sandbox security／least privilege／comprehensive logging／automated tripwires／rapid shutdown／monitoring——本轮怀疑派中最系统的替代机制清单。）

> "we identify three areas where investment is necessary to address loss-of-control risks: research to develop better methods for controlling increasingly capable agents, translating existing research and known control techniques into usable tools, and organizational changes to ensure that these tools are actually adopted."
（**三层投资**：控制方法研究→已知技术工具化→组织变革保证真的被采用。）

> "In our view, standards for organizational governance should be a key way to pace the frontier..." ＋ "AI control should become a job (and a part of every job), just like cybersecurity"（章节标题）
（**AI control 岗位化**——像 cybersecurity 一样成为职业与每份工作的一部分。）

> 引 Dinaburg（见 [dinaburg](dinaburg.md)）："we need to dramatically increase the scrutiny that sandbox security receives, such as by stress-testing and improving sandbox security through offensive agents on a routine basis with models of increasing capability."
（**沙箱必须被常态化对抗测试**——引 Trail of Bits 实证后的加码要求。）

**该条支持的最小主张**：AI 只压缩了工程三明治的 execute 层；"技术可行"不等于"必须放权"；替代方案是 AI control 路线的完整机制清单（沙箱/最小权限/日志/tripwire/急停/监控）＋研究→工具→组织三层投资＋control 岗位化。
**派别适配**：**怀疑票（范式/治理向，强）**——反的是"放权让渡"默认，不反 agent 本身（"agents will do most of the cognitive heavy lifting"）。
