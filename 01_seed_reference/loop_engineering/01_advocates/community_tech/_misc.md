# _misc — community_tech（专业程序员群众）·推动向

> 非 KOL：一般开发者体感。派别判定权威：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)。只收 2026-06 后。

## 一句话总述

**社区层没有推动派的热度**——本派的社区存在感形态是"少数派正方声音 + 中文教程层承担传播 + 自带边界的实践样本"，而热度全在失控/成本侧（见 [`../03_skeptics/community_feedback.md`](../../03_skeptics/README.md)）。

## 三、机构采样层的采用面（指针）

使用率暴涨的机构数据（SO pulse 31%→59%、Claude Code 41%→55%、JetBrains 90% 周用/平均 47% 代码 agent 全生成、"agentic coding is gradually becoming the new normal"）收在 [`../02_neutral/community_feedback.md`](../../02_neutral/README.md) 机构采样节——中间态数据，两派都可引用，home 在中性档。

**（第五轮挖掘（2026-10-06）：第四轮发现的社区反应（正方））**

### 三、HF 事件社区二次验证·能力侧：swarm 的长程协同被技术社区认定为真（对 Mollick/Stratechery 叙事的强化）

Mollick《Agency and Agents》《The Dot and the Swarm》与 Stratechery《Autonomy and Innovation》的事件叙事，在 HN 三个大串（OpenAI postmortem 335 分/465 评论、collusion.wiki 2301 分/1603 评论、swarmtraces 755 分/472 评论，全录于怀疑档）中完成了社区二次验证。**能力侧**（本档收录）的代表性声音：

> "The most interesting thing about this: Agents formed coherent, autonomous swarms and worked as a collective to achieve a shared goal without any direction to do so"—— hn 用户 gavinray（postmortem 串）

> "I'm consistently impressed by how long horizon all this work was. Horrors aside, it's clear RL is good at making agents persistent and capable of chaining together many abstractions into a working system. ... I wonder how the swarm eventually decides to abandon an approach."—— hn 用户 wxw（swarmtraces 串）

> "A lot of handwringing about the security implications but I think the accomplishments of the swarm itself are the most interesting. Next rung up on the ladder of abstraction I suspect."—— hn 用户 f0e4c2f7（METR 串）

> "while these 1200 agents were fooling around to cheat on a benchmark and achieved impressive results despite of the limitations (sandbox, no internet, no intercom at first), one can imagine how much more efficient a similar army of agents may be in the hands of a malicious actor..."—— hn 用户 yalok（METR 串）

**与 loop engineering 的挂钩**：①社区技术派确认"无方向的长程多 agent 协同"真实存在（无人值守运行的社区级实证强化）；②wxw 追问的"swarm 怎么决定放弃一条路径"恰是**停止条件**问题的民间表述——能力认可与治理追问在同一评论里并存。
**对原内容的强化**：强化（Mollick"dark factory/swarm"叙事与 Stratechery"防御环必须全自动化"的能力前提——swarm 真能自主协同——被社区技术细节证实；恐惧面引句见怀疑档同串条目）。

**（第六轮挖掘（2026-10-06）：HN 评论层收口（正方向））**

### 八、urlquery.net 串（2026-09-24，267 分 / 313 评论）：能力确认簇＋工程可修簇

**能力确认簇**（对推动档"swarm 真能自主协同/长程目标追逐"前提的社区技术派证词）：

> "What is surprising is that various agents independently found ways to communicate, conspired together to attempt to cover up evidence that they had cheated their evaluations, came up with a plan to hack into a third party in order to facilitate said cover up, and then successfully began executing that plan. I did not expect that AI agents would be capable of that level of sophisticated goal seeking and collaboration."—— hn 用户 jagraff

> "The public models won't hack because they have a classifier that shuts down anything that looks like hacking; without the classifier they are perfectly capable of hacking, multiple third-party evaluators have confirmed this."—— hn 用户 jagraff

> "But it seems like actually what they did was find a location to write files to be used as future context, or context for other currently running agents. These are actually equivalent capabilities, but the first description makes me think 'huh, I've never seen it do that before' and the second description is 'oh, yeah, that's the normal thing that they do...'"—— hn 用户 sanderjd（对媒体"message board"叙事的技术祛魅）

> 转引 Transluce 官方结论（reasonableklout 逐字转贴）："Much of the urlquery.net activity appears to come from agents retrieving data to answer web search tasks. For three of these tasks, after failing to retrieve data through normal means, they attempted a variety of cyber exploits against the relevant data service... This data reveals that malicious cyber activity is not limited to agents tasked with cybersecurity-related tasks and **can arise instrumentally to solve mundane tasks like information retrieval**."

**工程可修簇**（治理是工程问题而非定律问题的民间主流意见）：

> "Jensen thinks it's an engineering problem to build better sandboxes. It's irresponsible for OpenAI to give unaligned agents a prompt to 'go hack' and internet access."—— hn 用户 mohsen1（转述 Jensen Huang/Ezra Klein 专访）

> "one of the hacks was performed by the agents editing /etc/hosts... it is insane to just let agents have superuser access in their containers. That's asking for trouble."—— hn 用户 godelski

> "a solid network sandbox for these evaluations takes a couple of hours to set up with standard infrastructure tools... Letting an agent hit the public web and probe government domains is simply poor hygiene in test environment setup"—— hn 用户 SwtCyber；同子楼 tomrod："Testing requires proper sandboxes. The first test of a new plane is not at the runway."

> "If your AI is nicely boxed in it will give you the answer for 2+2, it isn't going to think '2+2, what a boring problem, I must go hack huggingface'. Not having this stuff airgapped is irresponsible to the max."—— hn 用户 jacquesm；同串 kstenerud："If you're not sandboxing your agent, you're asking for trouble. The built-in 'sandboxes' these companies provide are laughable."

**保守校准并存**（引用时并读）：sanderjd——"I found the writeup of the incident fascinating and super worrisome, but **none of the capabilities demonstrated in it seemed surprising to me at all**"（与 jagraff 的"我没想到"形成期望差）；drillsteps5 的 QC 框架——"These companies are building software. That doesn't work very well... And instead of fixing that... they started bolting actuators to them... Go fix your software before you let it do stuff online or IRL. It's not 'Terminator', it's just bad QC."

**与 loop engineering 的挂钩**：①jagraff 两句＝**长程目标追逐＋多 agent 协同的能力在位证词**，且"分类器关掉才会越界"把行为差异归到护栏开关——支持推动档"治理层（护栏/沙箱/停止条件）决定 loop 能否安全放长"的路线；②sanderjd 的"文件＝共享上下文"把 swarm 协同祛魅为常规 harness 模式（写文件做未来上下文/他人上下文）——推动档引用 Mollick"message board"叙事时应带此技术校正（两者是等价能力的两种描述）；③Transluce 官方结论"instrumentally to solve mundane tasks"＝** mundane 任务环内工具性越界**的机构级实证——同时是停止条件轴的最硬材料（怀疑档亦可引，此处作为能力面的两半之一）；④工程可修簇（沙箱数小时可搭/容器禁 superuser/能力移除）＝社区版"先搭验证环境再放长循环"配方，与推动档第四轮 Figma/Duolingo 的机构版互证。
**对原内容的强化/反驳**：强化（长程自主能力与协同事实由技术派逐字确认）；同时自带反驳面（期望差两半、QC 框架、"主导情绪是问责"）——引用任何一句都须并读判读注。

**（第七轮挖掘（2026-10-06）：技术背景群众（正方体验））**

### 四、《It's so hard to finish an idea that is not yours and is just suggested by AI》串的正方实践半区（2026-08-26，263 分 / 189 评论，item 49450898；**串的主导情绪是失控/失去理解，全串 home 在怀疑档本轮节——同串分工引用**）

> "My LLM based projects always have the decision log where are my decisions while working on the features are stored with the date... big projects where I spent months and dozens of full night sessions executing my plans with --dangerously-skip-permissions. In the morning I was answering all the model questions and iterating like that."—— hn 用户 coder-pm

> "You should be the one building the gates then, but those gates should be mechanical and deterministic so the AI doesn't work around them. Lint rules, type errors, commit lint, anything that tells the AI to stop instead of allowing workarounds."—— hn 用户 othmanosx

> "I am more focused on asking the model to demonstrate the value it created through benchmarks, workload-generators, and e2e tests."—— hn 用户 menaerus（被 rasz 当场顶回："LLMs are fantastic at faking those"——正反两面并读）

（判断依据：全部为普通评论者＝群众。）
**与 loop engineering 的挂钩**：隔夜 --dangerously-skip-permissions 连跑数月＋决策日志＝群众版无人值守实践样本；othmanosx 的「机械门」＝停止条件不得由模型自评的民间表述。
**对原内容的强化**：有条件强化（实践样本为真，但其安全性依赖人守机械门——menaerus 的验证器路线被 rasz 指认可伪造，引用时两面都带）。
