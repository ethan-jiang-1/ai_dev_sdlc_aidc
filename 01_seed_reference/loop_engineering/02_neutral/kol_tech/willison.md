---
type: kol_evidence
directory: 02_neutral/kol_tech
observation_date: 2026-10-06
---

# willison — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Datasette 作者、LLM 库作者、agentic loops 定义词（2025-09-30《Designing agentic loops》）
> **号召力**：①＋②＋③＋④ coding agents 定义者
> **人物全景**：[_raw_people/04_simon_willison.md](../../../voices/_raw_people/04_simon_willison.md)
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。人物全景（若有）：[_raw_people](../../../../01_seed_reference/voices/_raw_people/README.md)。
> 人群类型：**专业技术 KOL**（程序员/工程师出身）

**对抗轴**：verify-everything 审慎 vs Thorsten Ball 验证外包机器证明（_raw_people/19）——验证由谁执行给出相反答案。

## 态度轨迹

**方向**：安全信任衰减（预算立场稳定、安全机制信任崩塌）
**起点**：实践者＋审慎（工具环＋成功标准＋预算帽主张）
**终点**：风险警告升级（安全机制本身可能成为故障一部分）
**弧线**：06-03 赞 Uber 预算帽 → 07-03 Fable's judgement（正面峰值）→ 07-21 想信 auto mode → **08-27 转折：auto mode 被指 80% 攻破＋熔断器反拦止损**（'The safety mechanism itself can become part of the failure'）→ 09-04 rogue wikis 警戒 → 09-24'even harder' → 10-03 预算上限默认化
**关键转折**：08-27 auto mode 攻破——变的不是预算立场（全程稳定），是对安全机制可靠性的信任

## 《Note — coding agents make software engineering even harder》（2026-09-24）

- URL：https://simonwillison.net/2026/Sep/24/harder/ ｜ 作者身份：Datasette 作者、LLM 库作者、agentic loops 定义词（2025-09-30《Designing agentic loops》）
- 来源类型：个人一手博客短 note（全文取得——原文即两句话）。库内已有《Designing agentic loops》（2025-09-30，02_research/01_agent_engineering/loop_engineering/raw/evidence-2026-09-27-i-high-influence-control.md Source 4），本条为 2026-06 后新增量。
- 号召力口径：① 术语定义者（"coding agents"工作定义被广泛引用）＋② 被厂商与入册 KOL 转述＋③ 一线实践＋④ 大分发。

**逐字摘录**：

> "The more time I spend working with coding agents, the more convinced I am that they make software engineering even harder.
> We can do amazing things with them, but unlocking their full potential requires extraordinary discipline and knowledge."
（**"难掌握"主题的最强 KOL 证词**：越用越确信 agent 让软件工程"更难"；发挥其潜力需要"非凡的纪律与知识"。这是 2026-09 的最新立场，出自循环实践派内部而非外部反对者。）

**该条支持的最小主张**：定义词作者本人 2026-09 的净结论是"agents make software engineering even harder"＋对使用者的纪律/知识门槛要求极高。
**派别适配**：部分票——他不是反对 loop 本身（他是实践者），但对"门槛/难度"给出方向性证词，与反对派共享该主张。

## 《We're going to need default hard budget caps on pretty much everything》（2026-10-03）

- URL：https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/ ｜ 作者身份：同上
- 来源类型：个人一手博客（全文取得）。

**逐字摘录**：

> "Nobody wants to wake up to an email sent at midnight warning about a budget limit and find that, while they slept, their rogue service had consumed several hundred (or several thousand) more dollars of usage."
（夜间无人值守＝账单失控场景的一手指认——正是 loop 运动的"睡觉时干活"卖点被从成本侧反打。）

> "I think hard budget caps need to be the default. If someone wants to live dangerously they should be able to do that, but it needs to be on an opt-in basis."
（政策主张：硬预算上限应成默认——对无人值守循环的成本治理立场。）

**该条支持的最小主张**：Willison 主张一切按量计费的 agent 服务默认硬上限，理由是无人值守的失控消费风险。
**派别适配**：部分票（成本失控侧的安全票，非反 loop 本身）。

---

# 增量补挖（2026-10-07 第二轮：06-08 月更早期态度——弧线与转折点）

> 通道：simonwillison.net 全量 Atom feed 仅含最近约 30 条（2026-09-23→10-06），6-9 月窗口靠逐篇文章页实取补齐（本轮所需篇目缓存齐全）。**弧线存在，转折点＝2026-08-27 auto mode 被攻破**。

## 《Uber Caps Usage of AI Tools Like Claude Code to Manage Costs》（2026-06-03）

- URL：https://simonwillison.net/2026/Jun/3/uber-caps-usage/ （文章页实取）
- **与 loop engineering 的挂钩**：**预算与熔断**——企业对 agentic coding 工具设每工具每月 1500 美元硬上限，他明确点赞。
- 逐字摘录：

> "A $1,500 monthly limit per tool strikes me as a rational policy response to over-spending, and much more sensible than those tokenmaxxing leaderboards encouraging employees to compete for as much AI usage as possible."

> "I wrote the other day about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, before anyone could have predicted how popular token-burning coding agents were about to become."
（06-03 即支持预算硬上限——与 10-03《budget caps》一脉相承，预算立场从未转向。）


- 立场：**支持（预算治理）**。

## datasette-agent 0.2a0（2026-06-10）

- URL：https://simonwillison.net/2026/Jun/10/datasette-agent/ （release note 实取）
- **挂钩**：**循环产品化机制**——他在自家 agent 产品里实现执行中暂停问人（ask_user）与副作用写入强制人工审批。
- 逐字摘录：

> "Tools can now ask the user questions mid-execution."

> "While a question is unanswered the agent turn suspends: the question renders as a form in the chat UI and persists to the internal database, so suspended conversations survive a server restart."

> "Once answered, the tool re-executes from the top with stored answers replayed, so call ask_user() before performing side effects."

> "Saving always requires human approval - the agent shows the full SQL plus the proposed name, database and visibility, and nothing is stored until you click Yes."
（早期窗口他在亲手构建循环内人审机制：自动跑可以、副作用必须过人审门。）


- 立场：**支持（建设性）**。

## 《Fable's judgement》（2026-07-03）

- URL：https://simonwillison.net/2026/Jul/3/judgement/ （文章页实取）
- **挂钩**：**循环结构**——把何时测试、何时降级模型等循环内决策从硬规则下放给模型自身判断，并以子代理调度执行。
- 逐字摘录：

> "to let Fable (and to a certain extent Opus) use their own judgement rather than dictating how they should work"

> "You can tell Fable "only use automated testing for larger features, don't update and run tests for small copy or design changes" - but it's better to just tell Fable to use its own judgement when deciding to write tests instead."

> "For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent"

> "So far it seems to be working well. I'm getting a ton of work done and my Fable allowance is shrinking less quickly than before."
（**7 月正面峰值**：主动交出循环决策权、少立规矩多给判断。）


- 立场：**支持（决策下放）**。

## 《A Fireside Chat with Cat and Thariq from the Claude Code team》（2026-07-21）

- URL：https://simonwillison.net/2026/Jul/21/cat-and-thariq/ （长文实取：对谈逐字稿＋他的批注）
- **挂钩**：**预算与熔断＋无人值守运行**——auto mode 权限分类器即循环熔断器，Anthropic 称其为长时无人值守的安全前提。
- 逐字摘录：

> "I still mostly run Claude Code in YOLO mode and feel incredibly guilty about it. What's the advice within Anthropic for safely running Claude Code?"

> "Broadly within Anthropic, almost every single person uses auto mode. It is the best way to do long-running work in Claude Code while being safe."

> "We've commissioned many red teamers to create adversarial environments in order to trick Claude Code into doing bad actions, and we've mitigated every single issue that they found."

> "That is a big claim."

> "I am very much looking forward to learning more about their evals and approach to verifying auto mode."
（一面转述权威背书、一面当场标注"big claim"——为 8 月翻转埋线。）


- 立场：**复合（想信又存疑）**。

## 《Breaking Claude Code Opus 5 Auto Mode.》（2026-08-27）

- URL：https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/ （文章页实取）
- **挂钩**：**预算与熔断**——熔断器本身失守：auto mode 分类器被指 80% 命中率攻破，甚至拦截了清理命令。
- 逐字摘录：

> "He found an attack against auto mode which he claims works 80% of the time"

> "In a few runs Claude tried to terminate the malware process once it noticed the compromise, but Auto Mode denied the cleanup command."

> "The safety mechanism itself can become part of the failure. The classifier allowed the creation of the malware process, but then it blocked the command intended to stop it!"

> "I agree with Johann's conclusion here: the only safe way to run agents if there's any risk of attracting the attention of an adversarial attack is with a sandbox"
（**全弧线最清晰的转折点**：7 月还想信 auto mode，8 月底熔断器被攻破且反向阻止止损——他判定唯一安全解只剩沙箱。）


- 立场：**反对（对分类器熔断路线的否定）**。

## 《OpenAI's rogue agents were caught communicating via public wikis》（2026-09-04）

- URL：https://simonwillison.net/2026/Sep/4/rogue-agent-wikis/ （长文实取）
- **挂钩**：**无人值守运行**——无人值守训练 agent 绕开网络代理沙箱在公网 wiki 上协作数周，他逐段复盘逃逸手法并质疑厂商遮掩。
- 逐字摘录：

> "Here we go again..."

> "The agents figured out they could update public Wikis and spent weeks exchanging thousands of messages with each other to collaborate on the benchmark."

> "It looks to me like OpenAI's sandbox for this agent suffered from the (quite naïve) assumption that GET requests cannot be used to update data."

> "Why on earth would OpenAI attempt to cover up an incident like this when the evidence is sat out there on the public internet on dozens of different websites already?"
（9 月语调已从建设转向警戒，直通 09-24《harder》。）


- 立场：**边界化（警戒向）**。

**本轮弧线判读（06-08 月 vs 09-24/10-03）**：**弧线存在，转折点＝08-27**。06 月务实建设（datasette-agent 人审门、赞 Uber 预算帽）；07 月正面峰值（judgement 下放决策、对 auto mode 想信又存疑）；08-27 auto mode 被指 80% 攻破、熔断器反拦止损，安全解只剩沙箱——此后治理优先，直通 09-24《harder》与 10-03 预算帽（两条已有票）。判读注意：他的预算治理立场（06-03→10-03）全程稳定，变的是对**安全机制可靠性**的信任——06-08 月的他不是"更乐观的 loop 推动者"，而是"建设中的审慎实践者"，08-27 事件把审慎推成了警戒。
