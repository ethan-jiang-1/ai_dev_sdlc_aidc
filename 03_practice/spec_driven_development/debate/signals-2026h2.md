# SDD（Spec-Driven Development）赛道信号全景：2026 年 6 月–9 月

```yaml
topic: spec-driven development 2026H2 最新信号
window: 2026-06-01 ~ 2026-09-20（时间权重最高，早期背景一律未收）
accessed_at: 2026-09-20
collector: SDD debate 子任务（captain 为内部会话占位说明，无检索含义）
sources_type: GitHub Releases API / HN Algolia API / 官方博客一手源
caveat: 全部为观测日快照，未做历史曲线回溯；权重为采集者主观评级（高/中/低）
```

---

## 1. 最新产品/版本信号

- **2026-09-19 | https://github.com/obra/superpowers/releases/tag/v6.4.1 | superpowers v6.4.1：Native 执行模式成为 subagent-driven development 的"更便宜替代品"，新增 OpenCode 2.0、Muse、Qwen Code 三个 harness 支持；`executing-plans` 从"每几个任务停下来确认"改为整计划跑完再一次 review；plans 增加 Review Focus 区块。 | 方向：利好（工程化深化：SDD 内部在降本、降仪式感，但范式仍活着）| 权重：高**

- **2026-09-17 | https://github.com/github/spec-kit/releases/tag/v1.0.8 | spec-kit 进入 1.0.x 高频发布期：v1.0.3（9/1）→ v1.0.4（9/2）→ v1.0.5（9/8）→ v1.0.6（9/10）→ v1.0.7（9/15）→ v1.0.8（9/17），约每 2-4 天一版。1.0.8 预告 `/speckit.taskstoissues` 将从核心移入捆绑的 `github` extension——核心在做平台化/插件化拆分；社区 extension/preset 目录爆发式增长（Figma、Linear、Azure Cosmos DB、MAQA、PDaC、OpenUP Governance 等）。 | 方向：利好 | 权重：高**

- **2026-09-17 | https://github.com/Fission-AI/OpenSpec/releases/tag/v1.13.1 | OpenSpec v1.13.1"Hardened CLI, safer archives"：安全加固（防 config.yaml 指令注入、防 `.npmrc` 劫持更新检查），`openspec status` 输出 Next 行指导下一步。OpenSpec 8-9 月保持约每 1-2 周一个 minor 的节奏（v1.12.0 9/3、v1.13.0 9/9、v1.13.1 9/17）。 | 方向：利好 | 权重：高**

- **2026-09-16 | https://kiro.dev/changelog/models/claude-fable-5-1-for-enterprise/ | Kiro（AWS）：Claude Fable 5.1 Preview 进入 Kiro Enterprise；9/14 IDE 1.1 推出 Agent Artifacts（agent 产出可持久化审阅的 artifact，替代埋在聊天记录里）；9/1 Kiro Web GA，官网口径仍是"shape work with Specs"。注意：Kiro 的 changelog 主题已明显转向 models/IDE/多 harness（Crew 可选 Claude Code/Codex/KAS 后端），"Specs"从主叙事降为特性之一。 | 方向：中性（Kiro 活着且在扩张，但叙事重心在离开 spec）| 权重：高**

- **2026-09-04 | https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.12.0 | BMAD v6.12.0 核心口号："Build decides how much ceremony a change needs after investigating it, not before"——简单变更只需两节 spec、一个 session 完成。这是 BMAD v6.11.0（8/10，Quick Dev→Build、核心 skill 从 14 砍到 8、净删 1900 行）路线的延续：**去仪式化、按需 ceremony**。 | 方向：中性偏利空（对"重型 SDD 流程"是自我否定，对 BMAD 自身是利好）| 权重：高**

- **2026-09-03 / 08-26 / 08-19 | https://github.com/Fission-AI/OpenSpec/releases | OpenSpec v1.12.0（Findings 报告、code-grounded planning：先读代码再写 spec）、v1.11.0（spec diff 视图、`status --all` 批量巡检）、v1.10.0（Zed 支持、任务计划必须写"怎么算完成"）。 | 方向：利好 | 权重：中**

- **2026-08-21 | https://www.manorrock.com/blog/2026/08/21/spec_kit_turns_one.html （另见 spec-kit v1.0.0 release，2026-08-20 前后）| spec-kit 周年发布 1.0.0，42 个 reaction（31 hooray）。该评论文章点出关键转折：1.0 的承诺从"稳定性"转向"适应性"——"value moved from stability to adaptability"。 | 方向：利好（里程碑）+ 中性（承诺语义弱化）| 权重：中**

- **2026-08-05 | https://github.com/github/spec-kit/releases/tag/v0.16.0 | spec-kit 0.16.0：Copilot 集成默认从 slash commands 改为 **skills**（`.github/skills/speckit-*`）——与 Google Conductor 转插件（见 §3）同向：SDD 工具的载体形态从"命令序列"转向"skills/插件"。 | 方向：中性（形态迁移信号）| 权重：中**

- **2026-07-24 | https://github.com/obra/superpowers/releases/tag/v6.2.0 | superpowers v6.2.0：SDD workspace 改为 plan-scoped（修复跨 plan 污染），全库"压缩运动"——删除 recap、social proof、推销式文字，每个删减用 subagent probe 微测。SDD 语义本身（spec 指针进 plan、controller 依 spec 裁决冲突）在强化。 | 方向：利好 | 权重：中**

- **Tessl | https://github.com/tesslio/cli （pushed_at 2026-03-05）、https://github.com/tesslio/spec-driven-development-tile （pushed_at 2026-03-30）| 2026 H2 无任何公开 release/commit；官方描述已从 spec 工具改写为 "your Agent Enablement Platform"。 | 方向：利空（头部初创公开停摆 + 术语自我撤离）| 权重：高**

## 2. 最新舆论信号（HN / 博客）

- **2026-09-17 | https://news.ycombinator.com/item?id=49739484 （https://geekyants.com/antflow-ai）| Show HN: AntFlow AI "Agentic AI Framework for Spec-Driven Development"——新进入者仍在用 SDD 作为卖点立项。 | 方向：中性偏利好 | 权重：低（0 评论，冷启动）**

- **2026-09-02 | https://martinelli.ch/why-spec-driven-development-tools-fail-in-the-enterprise/ | 《Why Spec-Driven Development Tools Fail in the Enterprise》：直接断言 SDD 工具在企业落地失败，HN 上 2 分 0 评论。 | 方向：利空 | 权重：中（观点文，传播有限）**

- **2026-08-31 | https://news.ycombinator.com/item?id=49505591 （https://sddobservatory.com/）| Show HN: SDD Observatory——追踪各 SDD 框架与真实项目的开放目录，"评估不同方法在实践中的有效性"。出现第三方观测/评测基础设施，是赛道进入"比拼实效"阶段的标志。 | 方向：中性偏利好 | 权重：中**

- **2026-08-05 | https://news.ycombinator.com/item?id=49182353 | Ask HN: "What Happened to Spec-Driven Development?"——提问者称"所有 SDD 工具（Kiro、OpenSpec/SpecKit、Tessl）都有点掉队了，但抱怨还在：agent 依旧自由发挥，我们是不是集体认定 /plan mode 就够了？"高赞回复：spec 与代码之间没有 Python→汇编那种确定性抽象，"大多数人似乎同意代码才是唯一真相源"；反驳者：models 变好后 plan.md + 验证循环即可，无需重型 SDD 工具。 | 方向：利空（本轮最重要的转向帖）| 权重：高**

- **2026-08-05 | https://medium.com/@ramtop/spec-driven-development-the-new-waterfall-8426a908d4da | 《Spec-Driven Development: The New Waterfall》——把 SDD 类比为瀑布回归。 | 方向：利空 | 权重：中**

- **2026-07-24 | https://news.ycombinator.com/item?id=49041530 | Ask HN: "What are your thoughts on spec-driven development?"——同期第二个泛 SDD 提问帖，评论寥寥（2 条）。 | 方向：中性（舆论注意力整体偏低）| 权重：低**

- **2026-07-17 | https://news.ycombinator.com/item?id=48948824 | Google 官方 SDD 文章上 HN 仅 2 分 0 评论——大厂动作未能撬动社区讨论热度。 | 方向：中性偏利空（热度维度）| 权重：低**

- **2026-06-26 ~ 07-25 | https://news.ycombinator.com/item?id=48687461 等 | 散点实践文："Beyond Vibecoding: SDD with OpenSpec"、Ludwig SDD MCP、"Spec driven development with my 8-year-old"（SDD 作为教学/业余场景）、GRID 框架、opsx toolkit CLI（11 分，6 月 HN 上 SDD 工具帖的最高分）。 | 方向：中性偏利好（长尾活跃、无爆点）| 权重：低**

## 3. 最新行业信号

- **2026-07-16 | https://developers.googleblog.com/evolving-spec-driven-development-conductor-now-supports-antigravity/ | Google 官宣：Conductor（去年以"Context-Driven Development for Gemini CLI"推出）从 Gemini CLI 扩展**转为 Conductor Plugin**，可装进 Antigravity CLI、Claude 等；明确宣称"去除严格命令序列的摩擦"，改为会话式动态生成 spec/plan；称在 TerminalBench 最难子集上"使用 SDD 成功率更高"。 | 方向：利好（大厂制度化 SDD）+ 中性（同时把"严格命令流 SDD"软化为对话式）| 权重：高**

- **2026-09-01 ~ 09-16 | https://kiro.dev/changelog/ | AWS/Kiro 下半年连续动作：Kiro Web GA（9/1，主打浏览器端"shape work with Specs"）、Crew 0.6 可选 Claude Code/Codex/KAS 后端（9/5）、GPT-5.6 1M context（9/14）、Claude Fable 5.1 Enterprise Preview（9/16）。 | 方向：利好（AWS 持续投入该产品线）| 权重：高**

- **2026-08（spec-kit v1.0.5 内收录 "August 2026 newsletter"，#4442；7 月 newsletter 见 v0.16.0 #3987）| https://github.com/github/spec-kit | GitHub 官方为 spec-kit 维护月度 newsletter，并引入月度 review、extension 目录治理、`gh-aw` agentic workflow 体系。 | 方向：利好 | 权重：中**

- **2026-06-18（背景边界）| superpowers v6.1.0 release notes 记载 Google 于 2026-06-18 EOL Gemini CLI——直接牵动 SDD 工具链的 harness 生态（superpowers 一度移除后又恢复 Gemini 支持）。 | 方向：中性（生态底盘在重组）| 权重：低**

- 未发现 2026 H2 Anthropic/OpenAI 以 "spec-driven" 为名的官方表态或新报告；行业叙事重心在 agent harness / skills / plugins，spec 是其上的一个工件类型。（观测缺口，非否定）

## 4. 社区结构信号

- **2026-09-20 快照 | https://api.github.com/repos/github/spec-kit | spec-kit：138,035 stars、12,366 forks、307 open issues、最后 push 2026-09-18、subscribers 706。issue 体量大且持续有维护动作（stale 策略收紧为 60 天 stale/30 天关闭，v1.0.6），releases 由 bot 每数日一版、单版即合并 15-20 个 PR。 | 方向：利好（吞吐极高）| 权重：高**

- **2026-07~09 | https://github.com/Fission-AI/OpenSpec/releases | OpenSpec 每个 release 都在批量欢迎 first-time contributors：v1.7.0（7/29）"90 merged PRs from 19 contributors"；v1.8.0（8/5）34 PRs / 15 contributors；v1.9.0（8/13）起每个版本 4-6 名新贡献者。贡献面在变宽，非单一维护者项目。 | 方向：利好 | 权重：高**

- **2026 H2 | https://github.com/github/spec-kit/issues（经 releases 与 release notes 侧面观测）| spec-kit 近期争论/工作主题集中在：extension 信任模型（catalog trust model、社区提交 allowlist 加固）、供应链安全（catalog URL 必须 tag-pinned、拒绝私有端口、UTF-8 加固）、AI 披露要求（"require agent, model, and settings in AI disclosure"）。议题已从"怎么写 spec"迁移到"平台治理与供应链"。 | 方向：中性（成熟期议题）| 权重：中**

- **2026-09-19 | https://github.com/obra/superpowers/releases/tag/v6.4.1 | superpowers 引入 `diagnosing-superpowers` skill（读会话 transcript、给 path:line 证据诊断"为什么这轮跑砸了"），并要求所有 PR/issue 披露 AI 制作方式。社区讨论主题是"让 SDD 跑得便宜、可诊断"，而非是否需要 SDD。 | 方向：利好 | 权重：中**

## 5. 反信号（退潮/转向）

- **2026-08-05 | https://news.ycombinator.com/item?id=49182353 | "Did we all just collectively decide that /plan mode was enough?"——SDD 独立工具范式被"plan mode + 验证循环"吸收替代的公众论断首次明确成形。 | 方向：利空 | 权重：高**

- **2026 H2 持续 | https://github.com/tesslio/cli | Tessl 公开仓库自 2026 年 3 月起零 push，描述改为 "Agent Enablement Platform"——头部玩家弃用 spec-driven 定位改押 agent 平台。 | 方向：利空 | 权重：高**

- **2026-07-16 | https://developers.googleblog.com/evolving-spec-driven-development-conductor-now-supports-antigravity/ | Google 把 Conductor 的卖点从"Spec-Driven"改述为"Context-Driven Development"，并主动移除"严格命令序列"——术语层已出现 SDD→context/context-driven 的漂移。 | 方向：利空（对 SDD 作为独立品类而言）| 权重：中**

- **2026-08-10 / 09-04 | https://github.com/bmad-code-org/BMAD-METHOD/releases | BMAD 两连版的核心叙事都是"减少 ceremony、缩小 skill 目录、简单变更两节 spec 完事"——最重流程的方法论在系统性自我瘦身。 | 方向：利空（对重型 SDD）| 权重：中**

- **2026-08-05 | https://medium.com/@ramtop/spec-driven-development-the-new-waterfall-8426a908d4da | "SDD 是新瀑布"的类比开始流通，与 2025 年的正面叙事形成对仗。 | 方向：利空 | 权重：中**

- **对冲观察 | 2026-09-17 AntFlow（SDD 命名新进入者）、SDD Observatory（9/8）表明"退潮"并非全面：工具供给端仍在以 SDD 名义进入，只是社区热度与叙事权重下移。 | 方向：中性 | 权重：低**

---

## 2026H2 走向判读

**结论：工具侧加速、话语侧降温——赛道处于"结构性企稳 + 热度退潮"的分化期。** 开源头部（spec-kit 1.0 后每 2-4 天一版、OpenSpec 双周一版且贡献者面扩大、superpowers 连续大版）工程投入在 7-9 月实际是加速的；GitHub/Google/AWS 三家均以官方身份把 SDD 工件（spec/plan）制度化进自家 agent 平台。但公众话语明显冷却：HN 上 SDD 帖分数个位数、8 月出现"plan mode 就够了 / SDD 是新瀑布"的范式替代论，Google 用 context-driven、Tessl 用 agent enablement 等新词自我置换。方法论本身在收敛而非消失：重型仪式（BMAD 砍目录、superpowers 去 recap、Kiro 降 spec 叙事权重）普遍让位于"轻 spec + 会话式 + 验证循环"。判读：SDD 作为独立品类的高光期已过（利空），作为 agent 工作流的默认工件层则正在被大厂固化（利好）——三季度净走向为**企稳，结构重组，非加速亦非崩塌**。
