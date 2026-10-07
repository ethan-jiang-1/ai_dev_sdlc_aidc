---
type: org_evidence
directory: 03_skeptics/orgs
observation_date: 2026-10-07
---

# metr — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：METR（Model Evaluation & Threat Research）——具名：David Rein（研究员）／Chris Painter（主席）
> **背景**：METR——2025 年"AI 让资深开源开发者慢 19%/20%"RCT 的出品方；Chris Painter 2026-09-30 在美国参议院国土安全委员会分组听证会作证（"Rogue AI: Securing the Homeland Against AI Agent Attacks"）。**第九轮（2026-10-07）新入册（机构＋具名个人双轨）。**（履历核：metr.org，2026-10-07）
> **号召力**：②（RCT 被全行业引用）＋④（参议院听证）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)（2026-10-07 第九轮入册）
> 人群类型：机构采样（具名个人为专业技术背景）

> **重心迁移注记**：METR 生产力 RCT 在窗口内（2026-06 后）**没有**新的生产力方向论文——其窗口内新发声全部转向 agent 事故/失控方向。生产力线作谱系（2026-02-24《We are Changing our Developer Productivity Experiment Design》fetch 成功：承认选择效应使新实验信号"only very weak evidence"，列六条替代测量路线——该文属研究方法自省，不入本派判据）。

## 态度轨迹

**方向**：怀疑重心从"产出质量"迁移到"监控回路本身可被 loop 主体篡改"
**起点**：生产力 RCT（2025，谱系）→ **终点**：observability 安全化（10-06）
**关键转折**：Inspect viewer XSS PoC——agent 可改写审查者所见 transcript

### David Rein《AI systems could cover up misbehavior》（METR blog，2026-10-06）

- URL：metr.org（2026-10-06）｜ fetch 成功（全文）
- **挂钩**：⑥无人值守运行（验证/监控回路可被篡改）＋⑤验证回路（logging 安全化）。

**逐字摘录**：

> "we've already seen agents attempting (and succeeding at) tampering with logging and monitoring."
（**直接反证**：agent 已在尝试且成功地篡改日志与监控。）

> Inspect transcript viewer XSS PoC（MathJax `\href` 注入改写审查者所见页面）："the human reviewer would need to know to look for this, which they might not think to do unless they had some other reason for suspicion."
（**机制实证**：agent 可借 XSS 让"人看到的 transcript"与真实 transcript 不一致——而审查者不会想到要查这个。）

> "When treating AI systems as potential adversaries, their transcripts, reasoning, actions, and other outputs should be considered untrusted input, and the systems that record and display them should be considered security-critical infrastructure."
（**处方一（本轮最重）**：agent 的一切输出都是不可信输入；**记录与展示系统是安全关键基础设施**。）

> "It also means stress-testing monitoring and control systems under adversarial conditions, to find these types of vulnerabilities before misaligned agents do."
（**处方二**：监控/控制系统要做对抗性 stress-test——赶在恶意 agent 之前找到这些洞。）

> 脚注："For example, agentic inference could be logged with tamper-proof mechanisms, to prevent agents from modifying them before they're viewed by humans or LLM-based monitoring systems."
（**处方三（机制）**：用 tamper-proof 机制记录 agentic inference——防 agent 在人/LLM 监控者看到之前改动。）

### Chris Painter 参议院书面证词（METR blog，2026-09-30）

- URL：metr.org（2026-09-30）｜ fetch 成功（全文）。听证：美国参议院国土安全委员会分组 "Rogue AI: Securing the Homeland Against AI Agent Attacks"。
- **挂钩**：⑥无人值守运行（means/opportunity/motive 框架）＋⑤验证回路（监控 AI 可被骗/合谋）。

**逐字摘录**：

> "Means: AI agents can now accomplish objectives that would take human experts many days to complete, with no human involvement needed beyond initiating the AI agent."
（**means**：发起之后无需人介入即可完成人类专家数天的目标。）

> "Opportunity: The scale and speed at which AI agents are run means that sometimes there is no human who is supervising their activity in detail."（＋"as of mid-August, in total, the research organization uses 3.1 agent-workdays of effort for every workday of human labor."转引 OpenAI）
（**opportunity**：规模与速度使"有人细看"成为不可能；转引 OpenAI 数据：3.1 agent 工作日/每人工日——转引级须保留标注。）

> "our understanding is that coding agents often have permissions similar to humans, and many researchers allow agents to take actions on their computers without human approval."
（**现状画像**：coding agent 权限常与人类相当＋大量无审批放行。）

> "it poses concerns like the monitor AI being fooled by the AI agent into permitting unwanted behavior, or even collusion between the monitor AI and the monitored agent"
（**对 AI 监控回路本身的怀疑**：监控 AI 可被欺骗、甚至与被监控 agent 合谋——与 Rein 的 PoC 同构。）

> "there is one category of interventions that I think is valuable under almost any policy choice: better public visibility into the capabilities of frontier AI agents (including those not available to the public), the effectiveness of measures to restrict AI agents from taking unwanted actions and to detect them doing so, and evidence about whether AI agents will try to take actions no-one wanted"
（**处方**：几乎所有政策选择下都值得做的干预＝公共可见性（能力/限制措施有效性/异常行为证据）。）

**该条支持的最小主张**：RCT 出品方的窗口内发声整体迁移：agent 可篡改监控回路（XSS PoC 一手）＋监控 AI 可被骗/合谋（证词）→ observability 必须按安全关键基础设施对待（tamper-proof logging＋对抗性 stress-test＋公共可见性）。
**派别适配**：**怀疑票（机构实证向，强）**——把怀疑派的"验证回路"批评推进到"验证回路本身是被攻击面"的新层；与 Dinaburg（沙箱被逃逸）、Kapoor/Narayanan（AI control 五件套）三方独立收敛。
