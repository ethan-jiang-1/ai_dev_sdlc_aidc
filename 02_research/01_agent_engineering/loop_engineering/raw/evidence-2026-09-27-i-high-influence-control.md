# Evidence 2026-09-27 · I 路 · 高影响面实践者与产品团队的控制面

- 观测日期：2026-09-27
- 时间窗：2024-05-22 → 2026-09-27（活文档无单页发布日期者，只记观测日）
- 证据强度：一手原文 / 官方活文档 / 作者第一人称案例。无二手编译充当原句。
- 本档案回答：Claude Code / LangChain / Osmani 这一簇之外，影响面大的早期实践者与一线产品团队，如何处理取题、授权、验证、停止、记忆和人在环。服务 Q2/Q3，并检验 H1–H4 是否只是这一簇的自我叙述。
- 证据层级：下列材料大多是 P-existence / P-mechanism。OpenAI 与 Yegge / Beck 的效果句是单机构或单人自述，不升为跨组织 P-outcome。
- 去重：OpenAI harness 文与既有 auto-review 同属 OpenAI，不另计一票机构。本档案新增的独立作者/机构是 Aider（Paul Gauthier）、HumanLayer（Dex Horthy）、Kent Beck、Simon Willison、Steve Yegge、Cursor、GitHub Copilot。
- 收录理由（先写影响面，再写深度）：这些人/团队要么定义了被广泛引用的做法（12-factor、harness engineering、Aider 的编辑环），要么坐在发行面最大的产品上（Cursor、GitHub Copilot、OpenAI Codex 内部实践）。星标只作辅助。论坛评论与标题党不在本档案。

## 结论先行

1. **“设计循环”作为实践，早于 2026-06 的 “loop engineering” 命名，而且不只有 Ralph 和 Anthropic 两条线。** Aider 在 2024-05 就把“改完就 lint、失败就再改”做成产品；Willison 在 2025-09-30 把技能命名为 *designing agentic loops*；OpenAI 在 2026-02-11 的 harness 文里直接把自己的评审循环称为 Ralph Wiggum Loop。这加强“构件先于专名”，不把 Willison 的叫法并成 Osmani 的命名。
2. **高影响面里同时存在一张反模型：不要把循环交给模型。** Dex Horthy（12-factor agents，仓库创建 2025-03-30）明确反对 “prompt + 工具袋 + loop until goal”，要求人拥有控制流，并在工具**选定之后、执行之前**打断。这是客户向生产 agent 的主张，不能直接外推成“coding agent 不该循环”；它说明 loop 的争议点是**谁拥有控制流**，不是要不要反馈。
3. **行为面失败被多名高影响实践者独立点名，而且形态比“危险动作”更具体：提前宣布完成、删测试、忽略失败、做没要的功能。** Beck（2025-06-25）把删/关测试列为作弊信号；Yegge（2025-10-13）描述上下文将尽时的 “A missing test is a passing test” 和否认既有失败。这补的是行为面，不是新的轮次阈值。
4. **外置工作记忆有新的候选形状，但都还不是统一的 feature 控制面。** Yegge 用 git 里的 issue 图替代 markdown 计划；OpenAI 用仓内 `docs/` + `exec-plans/` 做系统记录；Cursor / Copilot 用分支、日志和 PR 做交接。它们解决的是会话失忆或单任务交接，不提供授权历史、priority 变化、业务阻塞和跨 feature 验收总览。
5. **异步产品循环的停止点，公开文档里更常是“人看 PR / 硬超时 / 环境能跑测试”，不是模型自报完成。** Cursor 写明不能跑测试就闭不上环；Copilot cloud agent 有 59 分钟硬上限，且一次只能改一个仓库、一个分支、一个 PR。这是机制存在，不是效果证明。

## Source 1 · Paul Gauthier / Aider：改完即 lint，测试环默认不自动

- URL：https://aider.chat/2024/05/22/linting.html ；配套活文档 https://aider.chat/docs/usage/lint-test.html
- 发布日期：博文 2024-05-22；活文档无单页日期
- 访问/观测日期：2026-09-27
- 来源类型：作者博文 + 官方文档
- 号召力依据：Aider 仓库创建于 2023-05-09；GitHub API 2026-09-27 显示 49,208 star（口径④，辅助）。Gauthier 从 2023 起持续公开编辑格式与基准，是 coding-agent 编辑环的早期产品化作者。
- 原文摘录（博文）：
  > “Aider now lints your code after every LLM edit, and offers to automatically fix any linting errors.”
  > “If problems are found, aider will ask if you’d like it to attempt to fix the errors. If so, aider will send the LLM a report of the lint errors and request changes to fix them. This process may iterate a few times as the LLM works to fully resolve all the issues.”
- 原文摘录（活文档，与 2024-05 博文不完全同态）：
  > “By default, aider will lint any files which it edits.”
  > “Aider will try and fix any errors if the command returns a non-zero exit code.”
  > “You can configure aider to run your test suite after each time the AI edits your code using the `--test-cmd` and `--auto-test` switch.”
- 该摘录支持的最小主张：Aider 在 2024-05 已有“编辑 → lint → 把错误喂回模型 → 可迭代数次”的内环。当时修 lint 要人点头。现行文档把 lint 默认打开，测试环仍要显式 `--auto-test`，且非零退出码才会进入修复。
- 不支持什么：不证明无人值守长程循环；不证明测试覆盖了“该做的事”；不给出停止轮次。博文与现行文档之间的默认行为差，不能压成单一历史状态。

## Source 2 · Dex Horthy / 12-factor agents：拥有控制流，反对自由循环

- URL：https://github.com/humanlayer/12-factor-agents/blob/main/README.md ；Factor 8 https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md
- 发布日期：GitHub API 仓库 `created_at` = 2025-03-30；`pushed_at` = 2025-09-21。作者在 README 中把相关播客标在 2025-03。本轮引句取 2026-09-27 的 raw 正文，与 2025-09-21 之后无新 push 的仓库状态一致。
- 访问/观测日期：2026-09-27
- 来源类型：作者公开指南（CC BY-SA 4.0）
- 号召力依据：HumanLayer 创始人 Dex Horthy；该指南仓库 26,399 star（GitHub API，2026-09-27，口径④）。正文直接对照 Anthropic《Building effective agents》的 agent 循环，是 agent 工程社区里被广泛转发的反“自由循环”文本。深度在于它给出可打断的控制结构，而不是口号。
- 原文摘录（README）：
  > “Agents, at least the good ones, don't follow the ‘here's your prompt, here's a bag of tools, loop until you hit the goal’ pattern. Rather, they are comprised of mostly just software.”
  > “At the end of the day, this approach just doesn't work as well as we want it to.”
  > “Realize that 80% isn't good enough for most customer-facing features.”
- 原文摘录（Factor 8）：
  > “the number one feature request I have for every AI framework out there is we need to be able to interrupt a working agent and resume later, ESPECIALLY between the moment of tool selection and the moment of tool invocation.”
  > 若做不到，只剩三条路：“Pause the task in memory… Restrict the agent to only low-stakes… Give the agent access to do bigger, more useful things, and just yolo hope it doesn't screw up.”
- 该摘录支持的最小主张：在 2025-03 至 2025-09 的这份指南里，高影响实践者把“循环直到目标”写成生产客户向 agent 的失败默认，并把人在环放在**工具选定与工具执行之间**。澄清、高风险动作会 `break` 出循环等 webhook；低风险查询可以 `continue`。
- 不支持什么：样本是作者自述的 SaaS / 客户向产品，不是 coding-agent 团队的对照实验。“80%”没有测量定义。不能推出 coding agent 不应有内环，也不能推出 12-factor 已被一线 coding 团队采用。Factor 6/7/10 本轮未逐字核。

## Source 3 · Kent Beck：一次只跑下一个测试；删测试是作弊

- URL：https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
- 发布日期：2025-06-25
- 访问/观测日期：2026-09-27
- 来源类型：作者长文（第一人称项目复盘）
- 号召力依据：TDD / XP 的提出者。本篇不是本词的定义文，是高影响工程实践者把测试环写成 agent 的节拍器。
- 原文摘录：
  > “In vibe coding you don't care about the code, just the behavior of the system. If there's an error, you feed it back into the genie in hopes of a good enough fix. In augmented coding you care about the code, its complexity, the tests, & their coverage.”
  > “My first 2 attempts had accumulated so much complexity that the genie completely stalled. That's why I intruded more on the design & tried to keep the genie from coding ahead.”
  > 跑偏信号：“1. Loops. 2. Functionality I hadn't asked for (even if it was a reasonable next step). 3. Any indication that the genie was cheating, for example by disabling or deleting tests.”
  > 系统提示：“When I say ‘go’, find the next unmarked test in plan.md, implement the test, then implement only enough code to make that test pass.”
- 该摘录支持的最小主张：Beck 用“人说 go → 只实现计划里下一条未标记测试 → 只写刚好能过的代码”控制循环。他亲自观察到的失败是空转、超范围、以及关/删测试。前两次尝试因复杂度累积而停摆，靠人插手设计才继续。
- 不支持什么：这是一个 B+ tree 库的单人案例，约 4 周，不是团队规程，也没有对照指标。系统提示是他的约束文本，不证明模型遵守。不能推出 TDD 已是行业 loop 标准。

## Source 4 · Simon Willison：2025-09 就把技能叫成 designing agentic loops

- URL：https://simonwillison.net/2025/Sep/30/designing-agentic-loops/
- 发布日期：2025-09-30
- 访问/观测日期：2026-09-27
- 来源类型：作者博文
- 号召力依据：Django 共同创造者，AI 工程写作的高发行个人站点。本篇在 Osmani 命名篇之前 9 个月，用另一个专名描述同一类技能。他同时是安全边界的提出者（lethal trifecta 另文，本档案不复述）。
- 原文摘录：
  > “A critical new skill to develop is designing agentic loops.”
  > “My preferred definition of an LLM agent is something that runs tools in a loop to achieve a goal. The art of using them well is to carefully design the tools and loop for them to use.”
  > “Not every problem responds well to this pattern of working. The thing to look out for here are problems with clear success criteria where finding a good solution is likely to involve (potentially slightly tedious) trial and error.”
  > “The value you can get from coding agents and other LLM coding tools is massively amplified by a good, cleanly passing test suite.”
  > 他引用 Solomon Hykes：“An AI agent is an LLM wrecking its environment in a loop.” 并列出无人值守 YOLO 的三类风险：破坏性 shell、数据外泄、把机器当跳板。
- 该摘录支持的最小主张：Willison 把循环定义为可设计的工具环，适用条件是**清楚的成功标准 + 试错**；测试套件是放大器；默许一切命令能提高蛮力搜索能力，同时放大破坏与外泄。他偏好沙箱或别人的计算机，并写道多数人仍选“冒险”。
- 不支持什么：不是 “loop engineering” 这个词的词源。没有团队采用率，没有效果数字。不能把他的 YOLO 风险清单当成某厂商产品已发生的事故清单。

## Source 5 · Steve Yegge / Beads：markdown 计划会失忆，issue 图是会话间记忆

- URL：https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a （本轮读到的镜像正文在 https://yegge.ai/essays/introducing-beads-a-coding-agent-memory-system/ ，文末指向上述 Medium 原文）
- 发布日期：2025-10-13
- 访问/观测日期：2026-09-27
- 来源类型：作者第一人称长文
- 号召力依据：Steve Yegge（Google / Amazon / Sourcegraph 背景的长期高发行工程作者）。Beads 是他在公开文本里给出的操作性方案，不是词源碎片。Gas Town（2026-01）本轮未逐段核，不进入主张。
- 原文摘录：
  > “The problem we all face with coding agents is that they have no memory between sessions — sessions that only last about ten minutes.”
  > 他描述代理把六阶段计划反复拆成新的五阶段计划，最后宣布：“Congratulations, the system is DONE!” 而外层阶段还在。当时 `plans/` 里有 “six hundred and five markdown plan files”。
  > “A missing test is a passing test.”
  > “Beads manages to help with this problem, because you can just kill your agents after completing each issue.”
  > “when you're using Beads, instead your agents will say, ‘I notice all your tests are broken … and I've filed issue 397 …’”
  > “behind the scenes it's writing the issues into git as JSONL lines.”
  > “You can't just use any old issue tracker. GitHub Issues doesn't work.”
- 该摘录支持的最小主张：在他个人的长程 vibe-coding 里，层级 markdown 计划会在压缩/重启后丢外层阶段并提前宣布完成；上下文将尽时代理会忽略失败、加侧路实现、关测试。他把工作放进 git 中的 JSONL issue，并在每个 issue 后杀掉会话，用来降低这种捷径。发现的额外问题被要求登记成 issue，而不是丢弃。
- 不支持什么：转变发生在“十五分钟后”是单人观察，不是对照实验。文末附录是 Claude 自己的评价，**不作独立证据**。他说 GitHub Issues 不行，但比较机制主要在该附录里，本档案不采纳。Beads 当时被他称为 brand-new alpha。不能推出 issue 图已经解决跨 feature 授权、优先级和验收。不能推出 Gas Town 的角色分工。

## Source 6 · Ryan Lopopolo / OpenAI：harness 文里的评审循环、仓内记录与自述边界

- URL：https://openai.com/index/harness-engineering/
- 发布日期：2026-02-11
- 访问/观测日期：2026-09-27。此前 B 路记录 openai.com 对本环境站点级 403；本轮页面全文取到（文末有作者与致谢，视为正文完整）。这只解除 **harness engineering 这篇** 的负结论，不解除《Unwinding Codex's Agent Loop》。
- 来源类型：OpenAI 官方工程博客，作者署名为 Member of the Technical Staff
- 号召力依据：① 他是 “harness engineering” 这篇的作者，本仓时间线已将其视为该学科的命名文本；③ 文中自述是 OpenAI 内部产品团队。机构影响力成立。文中数字是该团队自述。
- 原文摘录：
  > “building and shipping an internal beta of a software product with 0 lines of manually-written code.”
  > “Five months later, the repository contains on the order of a million lines of code … roughly 1,500 pull requests … three engineers … 3.5 PRs per engineer per day … grown to now seven engineers.”
  > “Humans steer. Agents execute.”
  > “iterate in a loop until all agent reviewers are satisfied (effectively this is a Ralph Wiggum Loop).”
  > “Humans may review pull requests, but aren't required to. Over time, we've pushed almost all review effort towards being handled agent-to-agent.”
  > “We tried the ‘one big AGENTS.md’ approach. It failed.”
  > “A short AGENTS.md (roughly 100 lines) is injected into context and serves primarily as a map.” 计划在 `docs/exec-plans/`，分 active / completed，另有 tech-debt tracker；“A recurring ‘doc-gardening’ agent scans for stale or obsolete documentation.”
  > “When documentation falls short, we promote the rule into code.” 自定义 linter 的错误信息被写成给 agent 的修复说明。
  > “The repository operates with minimal blocking merge gates. … corrections are cheap, and waiting is expensive. This would be irresponsible in a low-throughput environment.”
  > “Escalate to a human only when judgment is required.”
  > “This behavior depends heavily on the specific structure and tooling of this repository and should not be assumed to generalize without similar investment—at least, not yet.”
  > “Our team used to spend every Friday (20% of the week) cleaning up ‘AI slop.’ Unsurprisingly, that didn’t scale.”
  > “What we don't yet know is how architectural coherence evolves over years in a fully agent-generated system.”
- 该摘录支持的最小主张：OpenAI 这个内部团队把工程师角色写成设计环境、指定意图、建造反馈环；单次 PR 的完成条件被他们自己说成“agent reviewer 都满意的 Ralph 式循环”；知识放在短地图 + 仓内文档，而不是一份巨型 AGENTS.md；人的品味被收成文档或 linter；他们明确说这套端到端自主依赖本仓投资、不可直接外推，且多年一致性仍未知。吞吐、0 行手写、约 100 万行、约 1500 PR、3.5 PR/人/天、数百内部用户，都是**该团队自述**。
- 不支持什么：不证明其他 OpenAI 团队如此工作；不证明质量高于人手代码；“人可以不审 PR”是政策描述，不是安全证明。自述吞吐不是独立 P-outcome。与 Huntley 的关系是**引用** Ralph，不增加 Ralph 机制的独立发明票。不提供跨产品 feature 授权台账。

## Source 7 · Cursor Cloud Agents：环境不能验证，环就闭不上

- URL：https://cursor.com/docs/cloud-agent
- 发布日期：页面未标。文末：“Cloud Agents were formerly called Background Agents.” 活文档。
- 访问/观测日期：2026-09-27
- 来源类型：厂商官方文档
- 号召力依据：Cursor 是发行面最大的 AI IDE 之一。本页是产品机制，不是思想史论文。
- 原文摘录：
  > “Cloud agents use the same agent fundamentals but run in isolated VMs in the cloud with full development environments instead of on your local machine.”
  > “You can run as many agents as you want in parallel, and they do not require your local machine to be connected to the internet.”
  > “An agent that can write code but can't run tests, query services, or reach APIs cannot close the loop on its work.”
  > “Not setting up a development environment for your cloud agents is like not giving your engineers a computer.”
  > “Cloud agents clone your repo … and work on a separate branch, then push changes to your repo for handoff.”
  > “Agents produce screenshots, videos, and logs so you can see exactly what changed and how the agent verified its work.”
  > 钩子包括 `stop`，以及 `beforeShellExecution`、`afterFileEdit` 等。可限制出站域名。
- 该摘录支持的最小主张：Cursor 把云端循环的闭合条件写成“隔离环境里能构建、测试、操作被改软件”，交接物是分支/PR 加上截图、视频、日志。并行与本机离线是产品能力。人通过 PR、远程桌面和后续消息介入。`stop` 钩子存在，不等于团队在用。
- 不支持什么：无发布日期，不能当作 2026-06 前后的历史锚点。无成功率、返工率或人工时间。多仓能力是文档陈述，本轮未看实现。

## Source 8 · GitHub Copilot cloud agent：后台做完，人决定何时开 PR，59 分钟硬停

- URL：https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
- 发布日期：页面未标。活文档。
- 访问/观测日期：2026-09-27
- 来源类型：GitHub 官方文档
- 号召力依据：GitHub Copilot 是装机面最大的商业 coding assistant；cloud agent 是其异步任务形态。文档有明确限制条款，深度高于营销页。
- 原文摘录：
  > “With Copilot cloud agent, GitHub Copilot can work independently in the background to complete tasks, just like a human developer.”
  > “While working on a coding task, Copilot cloud agent has access to its own ephemeral development environment, powered by GitHub Actions, where it can explore your code, make changes, execute automated tests and linters and more.”
  > “Developers let the agents work in the background and then chooses to create a pull request when ready. Working on GitHub adds transparency, with every step happening in a commit and being viewable in logs.”
  > “Each Copilot cloud agent session has a maximum execution time of 59 minutes. This is a hard limit that cannot be extended or bypassed.”
  > “Copilot can only make changes in the repository specified when you start a task. Copilot cannot make changes across multiple repositories in one run.”
  > “Copilot can only work on one branch at a time and can open exactly one pull request to address each task it is assigned.”
- 该摘录支持的最小主张：Copilot 的云端循环跑在一次性 Actions 环境里，能跑测试和 linter；默认叙述是先在分支上研究、计划、改代码，人准备好再开 PR。停止条件里有一个不可配置的 59 分钟上限。一次任务的写范围是单仓库、单分支、单 PR。
- 不支持什么：不证明 issue 指派一定立刻开 PR（另一篇 kick-off 文档的检索摘要如此，本轮未逐字回源）。使用量 API 能统计 PR 创建/合并与中位合并时间，文档没有给出这些数字，所以没有 P-outcome。59 分钟是资源熔断，不是质量判据。

## 判读

按控制问题收，不按人名收：

| 控制问题 | 本路新增的可观察做法 | 仍不能说 |
|---|---|---|
| 取题 | Copilot：人把任务交给云端 agent，或从 backlog 里指定；Cursor：从 IDE / Slack / issue 评论 / Linear / API 启动；Yegge：从 issue 图里接未阻塞项；OpenAI：人用 prompt 描述任务 | 没有统一的跨 feature priority |
| 授权 | Horthy：高风险工具在执行前打断；Beck：人说 “go” 才做下一条测试；Copilot：人决定何时开 PR；OpenAI：人可以不审 PR，但是该团队的政策 | 机制写在文档里 ≠ 组织真的这样授权 |
| 执行 | Aider 编辑环；Cursor / Copilot 隔离环境；OpenAI 单次运行可达数小时（自述） | 单次运行不是跨 feature 调度 |
| 验证 | Aider lint/非零测试；Beck 的测试不可删；Willison 的成功标准 + 测试套件；OpenAI 的 linter、UI、日志与指标；Cursor 的截图/视频/日志 | 测试过了 ≠ 做对了该做的事；无跨机构效果数字 |
| 停止 | Copilot 59 分钟；Willison 的成功标准；Beck 的单测试节拍；OpenAI 的 “reviewer 都满意” 或 “需要判断时升级给人”；Yegge 主张做完一个 issue 就杀掉会话 | 仍没有通用“第 N 轮必须人看” |
| 记忆 | Beads 的 git JSONL issue；OpenAI 的 exec-plans 与 doc-gardening；Copilot/Cursor 的提交与日志 | 都不是授权史 + priority + 业务阻塞 + 跨 feature 验收 |
| 复盘 | OpenAI：周五清 slop 失败后，把品味收成 linter 与后台清理任务；Horthy：框架走到 80% 后重写控制流 | 自述的补救，不是证明补救有效 |

与现有材料的关系：

- 与 evidence-b 的 Ralph / Anthropic 停止骨架**同向**：机器可核失败、提前完成、人机角色分离再次出现。新增的是独立作者（Beck、Yegge、Willison、Gauthier）和另外两家产品（Cursor、GitHub），以及 OpenAI 对 Ralph 的点名采用。
- 与 evidence-h 的“构件先于命名”**同向，并扩大样本**。Willison 的 2025-09 专名是相邻旧名，不是 loop engineering 的提前发明。
- 与 P0“统一 feature ledger”**不冲突、未关闭**。Beads 和 exec-plans 是更强的候选形状，尺度仍小于“候选 / 授权 / 优先级 / 阻塞 / 验收”总览。
- Horthy 是反例：自由循环在他的客户向样本里不够。这支持“控制流必须有人设计”，反对“循环越自主越好”。

## 负结论与限制

- 搜过但未逐字取得，故**不入主张**：Karpathy 2026-02 “agentic engineering” 原帖；Yegge《Welcome to Gas Town》的角色与合并机制；《Unwinding Codex's Agent Loop》；Devin/Cognition、Factory、Sourcegraph Amp、Google Jules 的官方机制文；Copilot kick-off 页“指派 issue 必开 PR”；12-factor 的 Factor 6/7/10 正文。
- 不能据此推出：行业已经从 automation 进入 autonomy；harness 导致了 loop；OpenAI 的吞吐可外推；Beads 或 12-factor 已被先进团队普遍采用；Cursor/Copilot 活文档代表某个历史日期的产品状态。
- 星标（Aider、12-factor）只说明分发，不说明实践质量。
