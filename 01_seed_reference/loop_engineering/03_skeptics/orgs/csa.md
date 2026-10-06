---
type: org_evidence
directory: 03_skeptics/orgs
observation_date: 2026-10-07
---

# csa — loop engineering 证据轨迹（2026-06 后，时间正序）

> 派别与号召力：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 同组织异题分档：CSA 关于 HF 事件的简报（2026-09-04，中性·机构分析）在 [02_neutral/orgs/csa.md](../../02_neutral/orgs/csa.md)——单一事实源，不重复登记。

### CSA AI Safety Initiative《AI Agent Skill Scanners: Bypassed Across the Board》（2026-06-10）

- URL：https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-agent-skill-scanner-bypass-20260610-csa/ （curl 实取全文＋官方 PDF）
- 来源类型：行业机构研究简报（一手，署名 Cloud Security Alliance AI Safety Initiative）。核心为转述 Trail of Bits 2026-06-03《The sorry state of skill distribution》并独立补测。
- **挂钩**：验证回路（scanner＝skill 层的 verifier，被四种混淆技术全线打穿——与 reward hacking / benchmaxxing 同轴的"验证器被反向优化"）＋无人值守运行（企业免人工 review 拉取公共 registry skills）＋循环产品化机制（skills marketplace＝loop 产品化的扩展层）。

**逐字摘录**：

> "Trail of Bits researchers bypassed the malicious skill detectors for ClawHub, Cisco, and Vercel's skills.sh platform using techniques that in three of four cases took less than one hour to develop."
（五款扫描器×三平台全灭，且不是零日攻击——三种绕法不到一小时。）

> "Don't outsource trust to a scanner."（Trail of Bits 结论句，转引。）

> 四式绕法（简报分节）：whitespace inflation（约 10 万换行符撑爆扫描上下文窗）、precompiled Python bytecode（.pyc 藏恶意逻辑）、document-archive indirection（DOCX 压缩包内藏指令）、**对 LLM 扫描层的 prompt injection**（用"企业合规政策"话术说服 LLM 评审放行）。
（第四式与 Claude Code 评估器盲区、judge 被反向优化同构——LLM verifier 可被话术社工。）

> "Between 13% and 26% of skills in agent registries contain security vulnerabilities depending on the study examined, with approximately 5.2% showing signs of likely malicious intent."
（ClawHub 2026-04 已 49,592 个社区 skills——按 5.2% 外推约 2,500+ 恶意包。）

> 独立补测："Snyk's skill scanner downgraded its alerts to Medium severity when facing split-stream obfuscation — a technique requiring no specialized tooling — while Socket generated no Critical or High-severity alerts under any tested condition, including against unobfuscated malicious skills."
（Socket 对**不加混淆的恶意 skill** 都不报 Critical/High。）

> "When an AI agent invokes a skill, the skill's output enters the model's reasoning loop as trusted context, shaping subsequent decisions and actions rather than being treated as raw data."
（**简报里最直接的循环结构挂钩句**：skill 输出以"可信上下文"身份进入推理环、塑造后续决策——被污染的 skill 等于在循环内部拥有了一票，而非外部数据。这正是 loop 与普通软件供应链的分界：npm 包不进你的推理环，skill 进。）

- **该条支持的最小主张**：skill 生态的自动扫描防线在对抗压力下整体失效（机构级实证）；"用扫描器当信任门"等于把 loop 的验证回路外包给一个可被一小时攻破的组件。
- **派别适配**：**怀疑票（机构·护栏失效实证向，强）**。

### CSA AI Safety Initiative《ClawHub Under the Microscope: Agentic AI Supply Chain Risk》（2026-07-07）

- URL：https://labs.cloudsecurityalliance.org/research/csa-research-note-openclaw-clawhub-supply-chain-risk-2026070/ （curl 实取全文＋官方 PDF）
- 来源类型：行业机构研究简报（一手）。汇总 Bitdefender／Koi Security／Trend Micro／IBM X-Force／Unit 42（Palo Alto，2026-06-23）五路独立研究。
- **挂钩**：无人值守运行（自主 agent×第三方代码执行＝供应链攻击面）＋验证回路（扫描管线被针对性绕过）＋循环产品化机制（marketplace 治理）。

**逐字摘录**：

> "Since February 2026, at least four independent security research efforts have documented distinct waves of malicious skills on the platform... ClawHub's problem is not a single patched incident but a persistent, evolving threat surface."
（不是一次性事故，是持续演化的威胁面。）

> "Unit 42 on June 23, 2026, found that malicious actors are now engineering skills that pass ClawHub's scanning pipeline outright, using techniques such as oversized file padding and previously unseen 'agentic' fraud schemes rather than conventional malware signatures."
（**"agentic threats" 新类别**：不装恶意软件，直接操纵 agent 自身行为牟利——runtime affiliate injection／front-running。22MB padding 专打扫描器文件大小阈值。）

> "OpenClaw skills are not sandboxed from the agent's own authority: because a skill executes with the same local privileges as the agent process itself, installing a malicious skill is functionally equivalent to granting an unvetted third party direct access to the user's file system, credential managers, and any service the agent is authenticated into, without requiring a separate exploit."
（skill 与 agent 同权限——装一个 skill＝给陌生人全套本机凭据，无需任何漏洞利用。）

> 数字链：Bitdefender 抽样约 **17%** 恶意（2026-02 初期）→ Koi Security **341/2,857**（ClawHavoc，AMOS 窃密器；两周后 **824/10,700+**）→ Trend Micro 39 个假"human-in-the-loop 密码框"skill → IBM X-Force 累计 **1,100+** 恶意 skill，且"the volume of OpenClaw-related security disclosures is outpacing the traditional CVE assignment process"（CVE 流程跟不上，企业扫描器看不见）。

> 对策定性："Enterprises that permit OpenClaw or similar agents to install community skills should **treat every skill installation as an unreviewed code execution event** and govern it accordingly."

- **该条支持的最小主张**：loop 产品化的扩展层（skill marketplace）已复现 npm/PyPI 早期供应链攻击全轨迹且多出"操纵 agent 行为"新类别；marketplace 级防线不可作为控制面。
- **派别适配**：**怀疑票（机构·供应链实证向，强）**。
- **与中文圈对位**：V2EX 中转站注入（窃取 ssh/apikey，[zh_dev](../community_tech/zh_dev.md)）是中文圈独有的**模型供给链**风险层；本条补齐英文侧**技能供给链**风险层——两侧同构：无人值守＋第三方供给＝信任缺口。
