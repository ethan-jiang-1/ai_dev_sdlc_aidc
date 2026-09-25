# 来源卡片（本场外部来源 · 证据权威）

> **本文件是本场外部来源的唯一登记处。** 引用一律回这里取，不在别处重复摘录（单一事实来源）。
> 纪律：一手源优先、来源可溯、标注观测日期；证据强度按 `../CONTEXT.md` 第六节四档，不发明新词。
> **观测日期**：2026-09-22（下列 URL 均于该日逐条复验；v4 新增 §3 Anthropic 一手源，v5 新增 §5 行业侧）。
> **本场于 2026-09-22 首次引入外部来源**——此前口径是"原则上不引数字"，
> 见 `../CURRENT.md` 定调「本场原则上不引数字」条（不再按条号引用，避免 v4 增条后指针失效）。

---

## 1. Trivedy《The Anatomy of an Agent Harness》★ 核心命题的来源

| 项 | 内容 |
|---|---|
| 来源 | Vivek Trivedy（LangChain Blog；Osmani 文中简称 "Viv Trivedy"） |
| 发布 | 2026-03-10 |
| URL | https://www.langchain.com/blog/the-anatomy-of-an-agent-harness |
| 观测日期 | 2026-09-22 |
| **证据强度** | **一手**（`harness engineering` 术语由该作者提出）；其中基准数字为 **⚠️ 厂商自述** |

**逐字直引**（v4 于 2026-09-22 逐条复验，全部逐字无误）：

- "Agent = Model + Harness"
- "**If you're not the model, you're the harness.**"
- "The model contains the intelligence and the harness is the system that makes that intelligence useful."
- "Harnesses today are largely delivery mechanisms for good context engineering."
- "Today's models suffer from early stopping, issues decomposing complex problems, and incoherence as work stretches across multiple context windows."
- "we improved our coding agent Top 30 to Top 5 on Terminal Bench 2.0 by only changing the harness"（**⚠️ 厂商自述**）

**harness 组件面（原文列举）**：System Prompts／Tools, Skills, MCPs + descriptions／
Bundled Infrastructure（filesystem, sandbox, browser）／Orchestration Logic（subagent spawning, handoffs,
model routing）／Hooks & Middleware（compaction, continuation, lint checks）。

**推导模式（原文）**：`Behavior we want (or want to fix) → Harness Design to help the model achieve this.`

**本场怎么用**：P5 核心命题的来源；第三段五件事的工程对应——
① 上下文（context rot／compaction／progressive disclosure）；② 记忆与知识注入（AGENTS.md 式）；
③ bash／沙箱／工具面；④ planning + Ralph Loop；⑤ self-verification + hooks。

**未采用**：compaction／offloading 实现细节（本场听众不需要）。

> **Top 30 → Top 5 的回源结论（v4 新增）**：该句是**作者自述**，原始出处指向其**另一篇公司博客**，
> 未在本场核验；公开基准榜（Terminal Bench）**本场观测时已换代到 4.0，2.0 榜名次表为空**——
> 也就是说这个名次**既不能独立核验，也已经漂移**。按 `../CONTEXT.md` 第六节"会漂移的值标观测日期"，
> 本场**默认不上屏**（见本文件 §7 红线 2）。原句**没有说模型被固定**；
> "同一个模型"这层意思是 Osmani（本文件 §4）的解读，不是原文。

---

## 2. MAST《Why Do Multi-Agent LLM Systems Fail?》★ 症状分类的来源

| 项 | 内容 |
|---|---|
| 来源 | Cemri, Pan, Yang 等（UC Berkeley／Intesa Sanpaolo） |
| 发布 | arXiv 2503.13657；**NeurIPS 2025 Datasets & Benchmarks Track** |
| URL | https://ar5iv.labs.arxiv.org/html/2503.13657 |
| 观测日期 | 2026-09-22（14 个频率与 3 个类别占比逐条复验，全部一致） |
| **证据强度** | **一手（同行评审）** |

**方法**：7 个多 agent 框架、200+ 条执行轨迹（每条平均 15,000 行）、6 位专家标注；
标注者一致性 Cohen's Kappa **0.88**。

**14 种失败模式／3 大类**（括号内为出现频率）：

**FC1 规范问题（41.77%）**

| 模式 | 频率 |
|---|---:|
| 未遵守任务要求 | 10.98% |
| 未遵守角色设定 | 0.5% |
| **步骤重复** | **17.14%（全场最高频）** |
| 上下文丢失 | 3.33% |
| 未识别任务已完成 | 9.82% |

**FC2 agent 间错位（36.94%）**

| 模式 | 频率 |
|---|---:|
| 对话意外重置 | 2.33% |
| **用错误假设继续而不澄清** | **11.65%** |
| 任务脱轨 | 7.15% |
| 隐瞒关键信息 | 1.66% |
| 忽略其他 agent 的输入 | 0.17% |
| **推理与行动不一致** | **13.98%** |

**FC3 任务验证（21.30%）**

| 模式 | 频率 |
|---|---:|
| 提前终止 | 7.82% |
| 未验证／验证不完整 | 6.82% |
| 验证错误 | 6.66% |

**可直接引用的结构性结论**：

1. 失败**主要来自系统设计与协调，不是单个模型能力不足**——原文：
   "many MAS failures arise from the challenges in organizational design and agent coordination rather than
   the limitations of individual agents"。
2. **有验证者也不够**——"current verifiers often only perform superficial checks"（编译通过、有没有注释）。
3. **加一层高层目标验证 → ChatDev 成功率 +15.6%**（原文 **absolute improvement，绝对改进**；
   v3 误记为"相对改进"，v4 已改正）。
4. **只改角色／规格设定、不换模型 → ChatDev 成功率 +9.4%**（原文："+9.4% increase in success rate
   for ChatDev, when running on the same user prompt and base LLM"）——**这是本场 ②「懂你的业务」的直接底稿支撑**。
5. **验证错误 + 验证不完整合计 13.48%**（原文："incorrect or incomplete verification (FM-3.2 + FM-3.3)
   accounting for 13.48% of all observed failures"）——P12 用这个数，**不要**用 FC3 整类 21.30%（含提前终止）。
6. 效率问题不在分类法内：绕路可致成本／延迟 **10 倍以上**。

**本场怎么用**：P3 五种症状的分类底稿——**14 个模式中 13 个归位到五件事，1 个未采用**
（未采用：隐瞒关键信息 1.66%，属多 agent 间信息共享，本场听众用不上；③ 无 MAST 对应）。
归位逐条见 `../01_storyline/00-storyline-map.md` 第一段；P12「怎么验」的直接支撑。

> **口径警告**：MAST 的研究对象是**多 agent 系统**，而本场多数听众在**第 1–2 档**（单 agent／固定流程）。
> 引用时**只说"失败模式"这一类结论，不引"多 agent 更容易失败"**——否则与本场四档口径打架。
> **该警告同样适用于 P15 四档表的风险列**（第 3–4 档的风险描述借自多 agent 场景，只作方向提示）。

---

## 3. Anthropic《Harness design for long-running application development》★ P4 趋势判断的一手源

| 项 | 内容 |
|---|---|
| 来源 | Anthropic Engineering（作者 Prithvi Rajasekaran，Anthropic Labs） |
| 发布 | **2026-03-24** |
| URL | https://www.anthropic.com/engineering/harness-design-long-running-apps |
| 观测日期 | 2026-09-22 |
| **证据强度** | **一手（官方工程博客）** |

> **v4 新增本节的原因**：v3 把"这一圈不会消失，只会移动"记在 Osmani 名下并评**趋势级**，
> 缺口清单还写着"P3 的趋势判断只有一个趋势级来源，需回源 Anthropic 原文"。
> **回源发现：这句话的原始出处就是 Anthropic 本文**，Osmani 是转引。v4 把它升为**一手（官方）**，
> 缺口关闭。（原编号：本节为新增 §3，原 Osmani 卡片顺延为 §4。）

**逐字直引**（2026-09-22 于原文核验）：

- "every component in a harness encodes an assumption about what the model can't do on its own, and those
  assumptions are worth stress testing, both because they may be incorrect, and because they can quickly go
  stale as models improve."
- "my conviction is that the space of interesting harness combinations doesn't shrink as models improve.
  Instead, it moves, and the interesting work for AI engineers is to keep finding the next novel combination."
- "agents reliably skew positive when grading their own work"
- "Separating the agent doing the work from the agent judging it proves to be a strong lever to address this issue."
- "In some cases, that will mean the scaffold surrounding the model matters less over time, and developers can
  wait for the next model and see certain problems solve themselves. On the other hand, the better the models
  get, the more space there is to develop harnesses that can achieve complex tasks beyond what the model can do
  at baseline."
- "even on tasks that do have verifiable outcomes, agents still sometimes exhibit poor judgment"
- 另有 "context anxiety"（模型快到它以为的上下文上限就提前收工）与 context reset 的观察。

**本场怎么用**：

- **P4「这一圈不会消失，只会移动」= 本卡直接支撑**（含"等下一代模型"这个反驳的正面回答）。
- **P12 验证者分离**（generator／evaluator 分开；干活的和验收的，不能是同一个人）。
- **①／④ 的底稿**：context anxiety、context reset、把一个长任务拆成可续的块（**不上屏**）。

**未采用**：具体成本与时长数字（$124／3h50m 一类）、GAN 类比、前端设计评分部分、多 agent 架构细节。

---

## 4. Osmani《Agent Harness Engineering》（原 §3，v4 顺延）

| 项 | 内容 |
|---|---|
| 来源 | Addy Osmani（个人博客；作者为 Anthropic MTS） |
| 发布 | 2026-04-19 |
| URL | https://addyosmani.com/blog/agent-harness-engineering/ |
| 观测日期 | 2026-09-22 |
| **证据强度** | **趋势级**（实践者综述，非一手研究） |

**逐字直引（Osmani 本人的结论）**：

- "A decent model with a great harness beats a great model with a bad harness."
- "anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent
  never makes that mistake again."
- "Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong."
- "success is silent, failures are verbose."（**Osmani 明说这是 HumanLayer 的提法**，不是他的原创）
- "The gap between what today's models can do and what you see them doing is largely a harness gap."

> **归因校正（v4）**：v3 把下面三条也登记为 Osmani 的"逐字直引"，**属误记**——它们是 Osmani **转引 Anthropic**：
> "every component in a harness encodes an assumption about what the model can't do on its own."／
> "Harnesses don't shrink, they move"／"agents reliably skew positive when grading their own work"。
> **本场引用这三条时一律引 §3（Anthropic 一手）**，并已据此把 P4 的证据等级从趋势级升为一手。
> Osmani 保留的独有贡献：上述五条、以及把 Anthropic 的"移动"观察整理成可讲述的一节。

**本场怎么用**：

- P9 棘轮律（"Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong."）
  = 隐性知识显性化的操作面。
- P5／P4 的论证（"The gap between what today's models can do and what you see them doing is largely a
  harness gap."）。
- **"同一个模型换那一圈"这层解读**（原文只说改了 harness，见 §1 回源结论）——趋势级解读，可作方向，不作基准。

> **转引警告**：该文引用的 HumanLayer（"it's not a model problem. It's a configuration problem."、
> AGENTS.md <60 行）与 Anthropic 长任务 harness 文，**本场未直接核验 HumanLayer 原文**，属转引；要用先回源。
> （Anthropic 那篇已于 2026-09-22 回源，见 §3。）

---

## 5. Strands Agents《Introducing Strands harness》★ 行业侧：harness 与模型解耦被做成了产品

| 项 | 内容 |
|---|---|
| 来源 | Strands Agents 官方博客（AWS；作者 Arron Bailiss、Tim Moreton、Albert Zhao） |
| 发布 | 2026-09-21 |
| URL | 博客 https://strandsagents.com/blog/introducing-strands-harness/ ／ 官方仓库 https://github.com/strands-agents/harness-sdk ／ 文档 https://strandsagents.com/docs/user-guide/harness/reference/configuration/ ／ 基准仓库 https://github.com/strands-labs/benchmark-harnesses |
| 观测日期 | 2026-09-22 |
| **证据强度** | **⚠️ 厂商自述**（官方自测，**论文未发**——原文："Keep an eye out for a follow-up paper from our researchers regarding these benchmarks"）；"确实开源了这套 harness（Apache 2.0）"这一事实本身为**一手（官方）** |
| **中文界转述** | `../../../01_sources/weixin/raw_aws_strands_harness/aws_strands_harness_change_model_not_body.md`（DataFunTalk，2026-09-22）——**属二手，只作"中文界怎么说"的记录；引用一律回本卡** |

**逐字直引（官方博客与文档，2026-09-22 核验）**：

- "Today we're releasing Strands harness: a fully assembled state-of-the-art agent harness you can easily run locally or deploy to your favorite provider."
- "All you need is one line of Python or TypeScript to get it working with your **choice of model**."
- "Strands harness **costs 28% less** when using the same Claude or GPT models across six benchmarks."
- "With Fable 5, Strands harness **cost 77% less** than Claude Code _and_ **scored higher** on Terminal Bench 2.1."
- "Deepseek Harness proved to be the most token-efficient overall, however, it typically reported the lowest accuracy scores."
- "Our testing setup was distributed benchmarking on EC2 with Harbor."
- "tool results over ~1500 tokens get truncated, summarization (compaction) triggers when the context window hits above 85%, and context recovery runs within the loop if there's an overflow."
- "It's built to be a general-purpose agent rather than a coding agent."
- 文档 `Configuration reference`：`builtin_tools` 默认 shell／read／write／edit／web_fetch／web_search／programmatic_tool_caller／subagent；`caching` 默认 `"auto"`；`context_manager` 默认 `"auto"`；`memory` 默认开（`./.agent/memory`）；`skills` 默认 `./.agent/skills`；`session` 可按 id 持久化与续跑（`./.agent/sessions`）；**`interventions` = "Gate tool calls behind approval or a policy"**；`builtin_plugins` 默认 `["todos", "environment"]`。

> **归因更正（回源的关键收获）**：中文界那篇的标题句「**只换模型、不换身体**／脑子继续换，身体不用每次重新造」
> **官方博客里没有这句**——它是公众号的提炼。**可以当比喻用（而且很好用），但不能说成"AWS 说"**。
> 官方自己的说法是"**一行代码 + 随便换模型**"（"your choice of model"）。

**本场怎么用（只作底稿与口播，不上屏）**：

- **P5 命题的行业旁证**：这套东西的官方卖点就是"一行代码 + 随便换模型"——**模型和那一圈可以分开**。
  口播一句即可，**不点产品名、不报数字**。
- **P4 同方向证据**："Agent 的 Scaling 对象正在从模型，向模型外面的运行系统扩散"。
- **① 的机制底稿**：工具结果超约 1500 token 就截头尾、**原文外置到磁盘需要时再取回**（不是删掉）；
  利用率超 85% 触发压缩；溢出在循环内恢复。
- **② 的机制底稿**：`session`（这一段干过什么，可持久化续跑）／`memory`（跨会话还值得知道什么）／
  `skills`（按需加载）**分层**，各有默认目录。
- **③④⑤ 的机制底稿**：`interventions` 把工具调用挡在审批或策略后面（= 划圈／停手条件）；
  todos 插件跟踪多步（= 步骤）。
- **P12／P18 的支撑**：值得评的不是"哪个模型更强"，而是**这套组合在具体任务上花多少钱、成功率多少**。

**边界（必须与主张同段说，否则是软广）**：

- **换模型，不等于性能不变**——与 P5 新口径一致：**模型决定上限，那一圈决定能发挥出多少**。
- **诚实反例**：官方自己承认另有一套 harness 更便宜但准确率更低——**省 token，不等于更强**。

**未采用**：全部产品名（Strands／Claude Code／Codex／DeepSeek Harness／oh-my-pi／OpenCode 等）、
全部成本与分数数字、Terminal-Bench 2.1 名次、多 provider 清单。
**基准仓库 `strands-labs/benchmark-harnesses` 本场未读**（抓取失败）——若要引用方法学细节须先回源。

---

## 6. 待回源（候选，尚未核验）

| 线索 | 出处 | 用途 |
|---|---|---|
| 《When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops》 | 检索命中（Semantic Scholar），**未读全文** | P12「自己评自己总说好」的学术支撑，可替或补 §3 的口径（§3 现为一手，故只作加固） |
| Chroma《Context Rot》，2025-07 | 已在母版 `../../talk-ai-coding-evolution-harness/02_evidence/` 登记 | P8「塞得越满漏得越多」 |
| HumanLayer《Skill issue: harness engineering for coding agents》 | 经 Osmani 转引 | 棘轮律与入口文件尺寸 |

**引用前必须回源**；本场当前不依赖**这三条**。

---

## 7. 口径红线（本场自用）

1. **MAST 的频率数字不上屏**（本场原则上不引数字）——只作症状排序的底稿。
2. **P5 的 Top 30 → Top 5：默认不上屏**（v4 改，原为"上屏并标厂商自述"）。
   理由：该名次**无法独立回源**（原始出处为另一篇公司博客），且公开基准榜在观测时**已换代、原榜名次表为空**，
   属"会漂移的值"。**若用户坚持上屏**，必须同时标 **⚠️ 厂商自述 + 观测日期**，并接受它只作方向性信号（待定项见 `../CURRENT.md`）。
3. **不引 MAST 的"多 agent 更容易失败"**——与本场四档口径冲突，且对**第 1–2 档**听众是误导（同见 §2 口径警告）。
4. **上屏只留作者／机构 + 年份**（如 "Trivedy, 2026"、"Anthropic, 2026"、"UC Berkeley 等, NeurIPS 2025"）；
   **不留产品名、工具名、公司名**。
5. **每处引用必须能回指本文件的条目号**；讲稿里的 `[Sources]` 块按条目号写。
6. **行业侧旁证只作方向（v5 补）**：§5 一律**不点产品名、不报数字**——连口播也不点
   （CONTEXT 第四节禁具体产品名）。它的作用是证明"这件事正在发生"，不是提供案例。
