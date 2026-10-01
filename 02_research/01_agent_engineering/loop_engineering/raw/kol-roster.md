# KOL 台账 — Loop Engineering（2026-06 起）

> ★ **本文件是本主题「谁在说」的唯一名单权威。** 收录判据见 [`../README.md`](../README.md) §1；
> 一手素材统一在 [`01_sources/reference/kol/_raw_loop_engineering/`](../../../../01_sources/reference/kol/_raw_loop_engineering/README.md)
> （本文件**只放台账与指针，不放人物卡片**）。

**观测日期**：2026-09-26；**2026-09-27 I 路**追加谱系与候选注记，**§A 六人名单不增**。三路回源见 [evidence-a](evidence-2026-09-26-a-originators.md) / [evidence-b](evidence-2026-09-26-b-stop-and-scheduling.md) / [evidence-c](evidence-2026-09-26-c-autonomy-and-convergence.md)。簇外高影响面见 [evidence-i](evidence-2026-09-27-i-high-influence-control.md)；I2 档案混合主验与侦察回源，侦察条目不计票。**「待回源」= 不可作主张依据。**

> ⚠️ **质量门槛（2026-09-26 用户定，先于本表的一切口径）**：只收真正有影响力的 KOL，
> 且内容必须有深度（操作性洞察）。**论坛评论者不算 KOL、聚合媒体与标题党不入册、碎片推文不作深度证据**——
> 完整判据见 [`../README.md`](../README.md) §1「硬性排除」。

---

## §A 入册名单（2026-06 起对本主题有公开发声，且号召力口径至少满足一条）

| slug | 人物 | 身份 | 号召力口径 | 主张一句话 | 证据强度 | 卡片状态 |
|---|---|---|---|---|---|---|
| `andrew_ng` | **Andrew Ng** | DeepLearning.AI 创始人 / *The Batch* 作者 | ① 术语定义者 | 三环嵌套（agentic coding / developer feedback / external feedback），外环修正内环方向；人类的价值是**上下文优势**而非"品味" | **一手**（X post 已归档） | ✅ 四件套齐 |
| `anthropic_org` | **Anthropic** | 厂商官方（Claude Code / 工程博客 / Applied AI） | ① 术语定义者 + ③ 一线规模 | loop 原语的**最完整厂商落地**：`/goal`（条件驱动，三值判定）· `/loop`（时间驱动，7 天硬过期）· auto mode（deny-and-continue + 3/20 熔断）· feature_list.json · AI-Native SDLC playbook（工件触发 loop + σ 分层自主度）· Managed Agents（外层接口化） | **一手**（evidence-b/c 全文已归档） | ✅ 素材在 [`raw/evidence-*.md`](.) 与 [`02_research/02_ai_sdlc/02_industry_playbooks/anthropic/`](../../../../02_research/02_ai_sdlc/02_industry_playbooks/anthropic/README.md)（既有主题，只引用不复制） |
| `sydney_runkle` | **Sydney Runkle**（LangChain） | LangChain 工程团队 | ① 术语定义者 | **四环模型**（agent / verification / event-driven / hill-climbing）——"loop engineering" 一词的厂商级体系化定义；grader 分 deterministic 与 agentic 两类；hill-climbing 环"改写 harness 本身" | **一手**（2026-06-16 全文已归档，evidence-b §4e） | ✅ 已回源（素材在 evidence-b §4e——**回源档案为常态形态，不建卡**） |
| `addy_osmani` | **Addy Osmani** | Anthropic（Claude Code 团队 MTS；此前 14 年 Google，最高任 Google Cloud AI Director——一手 bio，evidence-a/c） | ① 术语定义者（**本词的命名者**） | **两篇一手全取得**：命名篇 2026-06-07《Loop Engineering》＋操作篇 2026-08-14《Practical Loop Engineering》。**定义**：替代人逐轮提示；分层实为**四级运行模式**（agentic loop → `/goal` → `/loop`/`schedule` → proactive 事件触发无人值守）。**建议**：五件套＋memory spine、`/loop`/`/goal`/`/schedule` 组合、verification skill、最简方案优先。**个人观察**：约 5–10 agents/日、通常最多约 5 个并发，review bandwidth 是上限；敏感/复杂任务需密切观察。`/goal` 评估器只核 transcript 硬规则、不判内容好坏；不要把品味和判断委托给 agent（增量见 evidence-a 补充回源 D5–D10） | **一手**（evidence-a） | ✅ 已回源 |
| `boris_cherny` | **Boris Cherny** | Claude Code 创作者 | ① **词源**（2026-06-02 访谈句） | **词源是碎片级的**：名句 "My job is to write the loops" 逐字未核验（三个流传版本措辞不一致）；YC transcript（2026-02-17）里 "loop" 出现 **0 次**（他用 swarm / "Mama Claude" / spec+Asana 描述同一机制）；**无个人书面操作定义**（CC 团队 06-30 官方定义 ≠ 本人） | **部分一手**（evidence-a） | ✅ 定性完成：词源位记入时间线，**不建深度卡**（无深度内容可卡） |
| `peter_steinberger` | **Peter Steinberger** | OpenClaw 创作者 | ① **词源**（2026-06-08 推文） | **词源是碎片级的，无深度内容**（A 路明确结论）：两句话推文（06-08 02:58 CST，正文未取得）；博客停在 2026-02-14。**重要 nuance**：其 2025-12-28 长文明确**反对自动编排**（"usually I'm the bottleneck"）——与 6 月推文立场相反。深度替代材料＝OpenClaw 官方 docs（standing orders / heartbeat / automation） | **部分一手**（evidence-a） | ✅ 定性完成：同上 |

**降级出册（2026-09-26 C 路定性）**：

- ~~`alchaincyf`（花叔）~~ —— 《Loop Engineering 橙皮书》经 C 路核实为**英文谱系的中文转述/编译，非独立发明**（作者 README 明写 "based on Addy Osmani's founding post and the official Claude Code / Codex docs"）。按质量门槛**不入册**；保留一条价值：它是**术语在中文圈的传播载体**证据，登记在 [`00-timeline.md`](00-timeline.md) §一，不建卡片、不作引用源。

---

## §B 谱系背景（2026-06 前，**不入名册**，只登记在 [`00-timeline.md`](00-timeline.md)）

| 人物 / 机构 | 贡献 | 时间 | 回源 | 已有卡片 |
|---|---|---|---|---|
| **Kief Morris**（Thoughtworks） | **四级阶梯**：outside / in / on the loop → **agentic flywheel**（C 路：四级非三级；脚注澄清 ralph 原始形态里 operator 在 steering） | 2026-03-04 | ✅ evidence-c | [`_raw_kol/10`](../../../../01_sources/reference/kol/_raw_kol/10_kief_morris.md)（卡片为三档版，**待按四级修订**） |
| **Birgitta Böckeler**（Thoughtworks） | steering loop / guides-sensors：**spec 降格为 feedforward guide 而非审批门**；"False sense of control?"（⚠️ 出处是 **2025-10-15 sdd-3-tools.html**，非 2026-04 harness-engineering） | 2025-10-15 / 2026-04-02 | ✅ evidence-c | [`_raw_kol/01`](../../../../01_sources/reference/kol/_raw_kol/01_thoughtworks.md) |
| **Viv Trivedy**（LangChain） | **"Agent = Model + Harness" 公式原创**（Osmani 明写是 Trivedy 的 one-liner；Böckeler 文把公式链到 LangChain；marmelab 记功给 Böckeler 是传播锚点化） | 2026 上半年 | ✅ evidence-c | 无卡片（**候选**：是否入册待判——公式原创者 + LangChain 工程师，可能满足口径①） |
| **Anthropic** | 《Building effective agents》机制句 + stopping conditions 首次成文 | 2024-12-19 | ✅ evidence-b §2 | 见 §A `anthropic_org`（机构连续体） |
| **Anthropic** | 《Effective harnesses for long-running agents》：feature_list.json | 2025-11-26 | ✅ evidence-b §3 | 同上 |
| **marmelab**（François Zaninotto） | "Natural Language Development" 命名 + "SDD adds little benefit" / "False Sense of Security"（⚠️ 两条名言出处是 **2025-11-12《The Waterfall Strikes Back》**，非 2026-09-24 审计文——C 路全文 grep 实锤） | 2025-11-12 / 2026-09-24 | ✅ evidence-c | 无卡片（候选） |
| **OpenAI**（Ryan Lopopolo） | 命名 "harness engineering"。**2026-09-27 正文已取得**：0 行手写 / 约百万行 / 约 1500 PR 为该团队自述；评审循环自称为 Ralph Wiggum Loop；短 AGENTS.md + 仓内 exec-plans；不可外推 | 2026-02-11 | ✅ [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 6 | [`_raw_kol/09`](../../../../01_sources/reference/kol/_raw_kol/09_ryan_lopopolo.md) |
| **Paul Gauthier**（Aider） | 2024-05-22 起把「编辑 → lint → 喂回模型」做成产品内环；测试环须显式 `--auto-test`。窗口前，不入 §A | 2024-05-22 | ✅ evidence-i Source 1 | 无卡片 |
| **Dex Horthy**（HumanLayer） | 12-factor agents：反对自由 “loop until goal”，要求在工具选定与执行之间打断。客户向生产 agent 的反模型，不是 coding-agent 采用率证据。窗口前，不入 §A | 2025-03-30 | ✅ evidence-i Source 2 | 无卡片 |
| **Kent Beck** | 《Augmented Coding》：人说 go 才做下一条测试；删/关测试是作弊信号。单人案例。窗口前，不入 §A | 2025-06-25 | ✅ evidence-i Source 3 | 无卡片 |
| **Steve Yegge** | Beads：用 git JSONL issue 替代会失忆的 markdown 计划；做完一个 issue 就杀掉会话。单人观察，alpha。Gas Town 机制本轮未逐段核。窗口前，不入 §A | 2025-10-13 | ✅ evidence-i Source 5 | 无卡片 |
| **Andrej Karpathy** | 终结自创的 "Vibe Coding"，提 "Agentic Engineering" | 2026-02 | ⏳ | [`_raw_kol/07`](../../../../01_sources/reference/kol/_raw_kol/07_andrej_karpathy.md) |
| **Stripe**（Beswick & Epsteen） | 《You can't whisper at an AI agent》hard/soft steering——"errors block progress but warnings don't"（C 路逐字到手） | 2026-05-14 | ✅ evidence-c | 无卡片（候选：属 harness 侧，与停止条件的同层性待判） |
| **Geoffrey Huntley** | Ralph Wiggum loop 原语（故意无限 bash 循环、无内建停止条件、back pressure、signs、greenfield 限定）——本词公认起点文献，2026 年仍被 LangChain/marmelab 引用 | 2025-07-14 | ✅ evidence-b §1 | 无卡片（素材在 evidence-b；**窗口内本人新发声待查，有则升 §A**） |
| **Harrison Chase**（LangChain CEO） | "harness engineering is an extension of context engineering"（播客转述）；LangChain 四环文页尾致谢含他（evidence-b）但非本人署名 | 2026-03 | ⏳ | 无卡片（**窗口内本人新发声待查，有则升 §A**） |
| **OpenAI**（alignment / Codex 团队） | 《Auto-review of agent actions without synchronous human oversight》：人工同步审批退出调度回路、独立审批 agent（"The separation of roles matters"）、反复拒绝熔断——loop 侧自主度治理的厂商一手 | 2026-04-30 | ✅ evidence-b §4d | 无卡片（机构条目；素材在 evidence 档案） |
| **Thorsten Ball**（Amp co-creator） | 《How to Build an Agent》（⚠️ 一手标题；流传《How to Build a Coding Agent》为二手变体）："It's an LLM, a loop, and enough tokens"——机制本体最短表述的传播源头之一。<400 行可教学。窗口前，不入 §A | 2025-04-15 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D1【主验】 | 无卡片 |
| **Walden Yan**（Cognition 联创） | 《Don't Build Multi-Agents》：单线程 agent ＋ Principles of Context Engineering（Share context / Actions carry implicit decisions）；反并行立场在命名前成形。影响力峰值在 2025-09-01 HN 重投。窗口前，不入 §A。**后续立场修订线索（multi-agents-working）待回源** | 2025-06-12 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D2【主验】 | 无卡片 |
| **Yichao "Peak" Ji**（Manus 联创兼首席科学家） | 《Context Engineering for AI Agents》：最完整的 "loop until the task is complete" 机制句＋KV-cache 命中率为生产 agent 第一指标＋文件系统外部记忆支撑长循环。窗口前，不入 §A | 2025-07-18 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D3【主验（loop/KV-cache 段）】 | 无卡片 |
| **Armin Ronacher**（Flask/Werkzeug 作者） | 两篇：《Agentic Coding Recommendations》（派活全权等待完成的实践自述；agentic loop 作性能工程对象，HN 296 分）＋《Building an Agent That Leverages Throwaway Code》（MAX_STEPS＋reachedEndCondition＋逐步缓存的一手伪代码）。窗口前，不入 §A | 2025-06-12 / 2025-10-17 | ✅ [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) Source D4/D5【主验】 | 无卡片 |

---

## §C1 候选池（有线索、未判）

| 候选 | 线索 | 待判什么 |
|---|---|---|
| **Simon Willison** | 2025-09-30《Designing agentic loops》已回源：他是循环实践者（工具环 + 成功标准 + 测试套件），同时指出 YOLO 的破坏/外泄风险。这不是对本词的反方论文，也不是语义纠偏 alone。**2026-06 后对本词 “loop engineering” 的专门发声仍未核，故不升 §A** | 人物全景已在 [`_raw_kol/04`](../../../../01_sources/reference/kol/_raw_kol/04_simon_willison.md)；本主题引句在 [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 4 |
| **Gergely Orosz** | 六预测；"Something precious is being taken away" | 怀疑派代表，是否构成本主题的对照声部。人物全景已在 [`_raw_kol/12`](../../../../01_sources/reference/kol/_raw_kol/12_gergely_orosz.md) |
| **swyx**（latent.space） | 《loopcraft: the art of stacking loops》——**被 LangChain 官方博客引用并致谢**（"This is what loop engineering — or loopcraft, as swyx puts it — actually looks like in practice"） | 个人 newsletter，按质量门槛暂不入册；但被厂商一手引用这一点值得记着——若后续发现更多厂商引用，可升入册（B 路线索） |
| **Jesse Vincent**（obra / Superpowers 作者） | Superpowers（289k★，口径④＋③一线规模）；其 Fable 5 时代的 `/goal` 实验（过夜 25 实验＋失败日志）是实践层 backbone §1 的例证来源；素材在 [`field_samples/fable5/run_superpowers_jesse_vincent/`](../../../../01_sources/field_samples/fable5/run_superpowers_jesse_vincent/profile.md)（既有，只引用） | **待判**：其 `/goal` 写法是否独立于 CC 官方文档（与 backbone §1 例证的降级标注是同一件事）——确认独立后升 §A |

---

## §C2 已排除（按质量门槛出局的线索，登记在案防止反复）

| 被排除项 | 排除理由 |
|---|---|
| **腾讯云社区《最近疯传的 Loop Engineering，是台印钞机，还是绞肉机？》** | 标题党 + 中文聚合转述。按用户 2026-09-26 质量门槛**直接丢弃**，连"热度旁证"都不作——热度本身不是思考 |
| **HN 评论者**（yoaviram、gsadaka、sermakarevich、constantcrying、conartist6 等） | 论坛随机评论 ≠ 有影响力的 KOL。其观点**不得进入本主题的 KOL 证据**；若需"社区情绪"佐证，单独标注、不与 KOL 证据并列 |
| **openai/codex issue #32389** 等用户 bug 报告 | 官方仓库用户报告非厂商立场文件；仅作《Unwinding Codex's Agent Loop》的**存在性旁证**（B 路已放「不入册·仅社区情绪」，其中 wire 层终止语义句引用须标注"官方仓库用户报告"） |
| **社区镜像仓库 / 媒体转述**（SiluPanda 等 codex-loop 镜像、Ars Technica、Turing Post、Simon Willison/gigazine/36kr 的二手报道） | 非官方复制品与媒体转述，一律不作证据（B 路执行记录） |

---

## §D 线索来源（供复审追溯）

| 来源 | 性质 | 提供了哪些线索 / 已核实哪些 |
|---|---|---|
| [`01_sources/reference/kol/_raw_loop_engineering/andrew_ng/raw_ng_x_post_en.md`](../../../../01_sources/reference/kol/_raw_loop_engineering/andrew_ng/raw_ng_x_post_en.md) | **一手**（已归档） | Andrew Ng 三环；**Cherny / Steinberger 两个词源人物** |
| [`raw/evidence-2026-09-26-a-originators.md`](evidence-2026-09-26-a-originators.md) | **一手回源档案**（A 路·词源与定义者四人） | Cherny 访谈句三版本对照与 YC transcript「loop 出现 0 次」；Steinberger 推文 snowflake 定位与「无深度内容」结论；Runkle 四环逐字；Osmani 两篇全取得（分层四级）；CC 团队 06-30 官方定义交叉核验——**「词源＝热度碎片、定义＝事后工程化」的判定依据** |
| [`raw/evidence-2026-09-26-b-stop-and-scheduling.md`](evidence-2026-09-26-b-stop-and-scheduling.md) | **一手回源档案**（B 路，9 个一手记录块全文） | Ralph 原文、Anthropic 两篇工程文、Claude Code `/goal`//`/loop`/auto mode 官方文档、OpenAI auto-review、LangChain 四环；**停止条件与外层调度两问判定收敛**；负结论 4 条 |
| [`raw/evidence-2026-09-26-c-autonomy-and-convergence.md`](evidence-2026-09-26-c-autonomy-and-convergence.md) | **一手回源档案**（C 路） | Kief Morris 四级阶梯、Böckeler steering loop 与归属修正、marmelab 两篇辨析、Stripe steering 原句、OpenSpec/Spec Kit 官方动作、橙皮书定性；**自主度位置分档成立/量化分档未成型**；**收敛判定成立** |
| [`talk-harness-201/02_evidence/01-kol-alignment-2026.md`](../../../../talk-harness-201/02_evidence/01-kol-alignment-2026.md) | 本仓证据（2026-09-25 web 检索） | Karpathy、Harrison Chase、Osmani、Böckeler、Huntley、Lopopolo、Stripe。⚠️ 其中"公式出自 Böckeler"已被 C 路一手链推翻，**该文件待复核修正** |
| [`raw/evidence-2026-09-27-i-high-influence-control.md`](evidence-2026-09-27-i-high-influence-control.md) | **一手回源档案**（I 路·簇外高影响面） | Aider lint 环、Horthy 反自由循环、Beck 单测试节拍、Willison 2025-09 相邻专名、Yegge Beads、OpenAI harness 全文、Cursor / Copilot 云端循环。**不升 §A** |
| [`raw/evidence-2026-09-27-i2-teams-evals-outcome.md`](evidence-2026-09-27-i2-teams-evals-outcome.md) | **批次回源档案**（I 路批次 2·五切口；主验与侦察回源混合） | (a) 厂商控制面候选形态；(b) evals 思想；(c) 定量效果成对地图；(d) 谱系候选；(e) SDD×loop 厂商组合。主验条目可进入判读，侦察条目待复验，不增加独立票；**不升 §A** |
| `/Users/bowhead/deepseek-harness/_faq_on_digested/15_loop-engineering-vs-sdd/`（**仓库外**） | 外部研究·转引 | LangChain / Osmani 的日期与定义分界、命名时间线序列、SDD 阵营反方线索——**全部仅作检索方向，本主题结论一律以自己的回源为准** |

---

## §E 本轮已确认的负结论（"搜过什么、没找到什么"）

1. **《Unrolling the Codex agent loop》（OpenAI，Michael Bolin，2026-01-23）**已有检索工具取得的候选文本（[evidence-k](evidence-2026-09-27-k-unrolling-codex-agent-loop.md)）。库内旧题 Unwinding 是错的；assistant message 终止态和「四拍」否定仍待独立一手复核。本环境直接 HTTP 仍 403。不升 §A。harness engineering 全文仍见 [evidence-i](evidence-2026-09-27-i-high-influence-control.md) Source 6。
2. **Claude Code 官方 CHANGELOG 不可达**（raw.githubusercontent.com 网络超时）——auto mode/`/goal`/`/loop` 引入日期未从 changelog 取得，已用官方文档版本锚点替代（v2.1.228 / v2.1.283 / v2.1.269）。
3. **Claude Code auto mode 公告博客正文截断**——标题经搜索逐字确认（"Auto mode is now the default in Claude Code for Pro, Max, and Team plans"），页面发布日期未取得；机制证据已由官方文档 + 工程博客覆盖。
4. **Cherny 访谈句逐字原文 / Steinberger 推文正文未取得**（X 全域不可达）——Cherny 名句三个流传版本措辞不一致（对照表见 [evidence-a](evidence-2026-09-26-a-originators.md)）；Steinberger 推文正文**已获 Osmani 06-07 帖逐字转引**（"You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."，见 evidence-a 补充回源节）——从「未取得」升级为「有日期转引」，直接引用仍须标「经 Osmani 转引」。另两条开放问题：LangChain 帖中 "Boris"→`0xwhrrari` 身份待核、swyx《loopcraft》原文 404（详见 evidence-a §6 与 [`../digested/01-命名谱系.md`](../digested/01-命名谱系.md) §五）。
5. **B 路第 4 条负结论**：Codex auto-review 官方 docs 页 403（机制证据已由 alignment.openai.com 官方博客全文覆盖，见 [evidence-b](evidence-2026-09-26-b-stop-and-scheduling.md) 负结论#4）。
6. ~~Osmani 的 O'Reilly 书名两档案矛盾~~——**已裁决**（2026-09-26 晚补充回源，Osmani 官网 O'Reilly 链接实锤）：正确书名《Agentic Engineering》，evidence-c:57 的《Beyond Vibe Coding》为误（见 evidence-a 补充回源节）。
7. **I-2 批次负结论**（详见 [evidence-i2](evidence-2026-09-27-i2-teams-evals-outcome.md) 线索登记与负结论节）：DORA 2025 年报正文具体系数 gated 未取得（官方摘要页口径可用，系数不引）；GitClear 白皮书全文需邮箱下载（落地页摘要已核）；Kiro docs 正文客户端渲染未取得（以官方博客＋官方 README 替代）；Devin docs.devin.ai 被 Mintlify 壳层截断（官方博客一条已回源）；Thorsten Ball 文章一手标题为《How to Build an Agent》（《…Coding Agent》系二手变体，Wayback 本环境不可达未核原始快照）；Manus 文件系统段经第三方镜像补齐（主站截断，主验待补）；AlphaEvolve 白皮书 §2.4–2.5 截断（摘要＋§1–2.1＋图注已核）。
