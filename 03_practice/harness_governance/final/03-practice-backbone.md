# 03 · Harness Governance 实践主干（定稿层·总纲）

> **本文件是什么**：本主题"工程实践主干"的定稿——多源 KOL 共识与真实规模化采用的 harness 治理实践，按**宪法 / 工件 / 回路 / 节奏 / 组织与边界**五段组织；每条带"防哪个缺口"标签、源强度与证据指针（指向 `../research/`，不复制正文，单一事实来源）。手册级操作规程（SOP / 模板 / 判据表 / 统一落地梯子）在 `04-practice-manual.md`（规划中）。

```yaml
topic: Harness / Context Governance —— AI 形态下新的 SDLC
doc_layer: final（定稿层 · 总纲，清单级）
produced_at: 2026-09-21
provenance:
  - 宪法 / 工件 / 回路：经用户逐段确认（2026-09-21）
  - 节奏 / 组织与边界：同日生产，待用户复核（进度见 ../CURRENT.md）
filter: 多源 KOL 共识或真实规模化采用 → 主干；单源强实践 → 标注"单源"；学术线挂起（不进主干论证；已被工程侧吸收的结论句按 practitioner 口径保留）
first_party_instance: DeepSeek Harness（DSH）—— /Users/bowhead/deepseek-harness/_faq_on_digested/07_borrowing-harness-idea/（基线 dsh-v0.1.5-rc.2，commit fb2c4b9e69；2026-09-21 观测；不搬正文，只指针）
---
```

## 0. 筛选判据与诊断轴

### 0.1 KOL 名单与被过滤清单

**工程侧 KOL 名单（"多源"由它定义）**：OpenAI / Anthropic（工程博客 + Claude Code 团队）/ Thoughtworks（Böckeler）/ Hashimoto（Ghostty）/ Stripe / Cloudflare / Vercel / Shopify / LangChain（Trivedy）/ Osmani（Claude Code MTS）/ HumanLayer / Teleport / Ronacher / AAIF·agents.md / Figma（安全域内）/ Umans / Upsun。第一方实例：DSH（见 yaml 指针）。

**被过滤（学术挂起）**：arXiv 2609.00252 八机制分类学、Meta-Harness、NLAH、SWE-Bench Mobile、CTXbench/Lulla 数字（详见 research/02b）。唯一保留句：CTXbench 的"勿 /init 自生成巨文件"教训——已被工程侧吸收（Upsun / HumanLayer 转述），按 practitioner 口径计入。"context ⊂ harness"判定保留为框架前提（另有 Chase / Cole Medin / OpenAI 用法三个工程源支撑，见 research/01c）。

### 0.2 诊断轴：两失败七缺口（①–⑥ 借自 DSH 消化稿；**⑦ 为 2026-09-21 用户实战补充**——agent 迭代中的概念叠层/沉积淹没现行。作全文"防什么"标签）

| 缺口 | agent 缺的句子 | 缺了之后的症状 | 主要由哪些主干件填 |
|---|---|---|---|
| ① 必须遵守什么 | "这里有什么铁律？" | 违反约定、绕过约束 | 宪法 3；工件 1/2；回路 1/2 |
| ② 系统由什么组成 | "有哪些部分，谁依赖谁？" | 抓不住主线、读散读偏 | 工件 1/3/4；回路 6 |
| ③ 为什么这样设计 | "当初为什么选这条路？" | 重走已否定路径、历史误当现状 | 工件 4/5（含负知识） |
| ④ 改动落在哪里 | "这个需求该改哪个机制？" | 改错地方、发明新接入方式 | 工件 8 |
| ⑤ 用什么流程 | "这类任务按什么步骤做？" | 现场发明流程、漏步骤 | 工件 3；回路 3 |
| ⑥ 怎么算做对 | "什么证据证明没做错？" | 交付无法验证的半成品 | 回路 1/5/6/7；节奏 1 |
| **⑦ 现行共识（哪一版生效）** | "我们此刻做的是哪一版？哪些已废弃？" | 概念叠层 A→A′→B→A″；现行被沉积淹没；信噪比崩塌、概念技术债；**人机同晕** | 工件 4（docs 只写 now）、工件 5（现行共识唯一 home + ADR 生命周期 + 负知识）、回路 4（改事实只改 home）、节奏 2（清扫含概念沉积归档/删减） |

糊涂 = ①②③**⑦**；乱发挥 = ④⑤⑥。（⑦ 根子在"分辨"，归糊涂侧；其后果也触发乱发挥——拿废弃版当现行去干。③与⑦是同一条"现行/历史"边界的两个塌法：③历史缺失、⑦历史淹没现行。）四问自评（知识外置 / 正确入口 / 反馈延迟 / **现行可辨**）为手册级 Phase 0 工具，见 04 §1。

## 1. 宪法（✅ 用户确认 2026-09-21）

1. **Agent = Model + Harness，harness 是你拥有的一等工程对象**——"a decent model with a great harness beats a great model with a bad harness"。（Trivedy 命源 + OpenAI 组织化 + Böckeler 框架化 + Osmani 系统化；research/02a A1/A9）
2. **棘轮律：每次真实犯错 → 工程化消灭该错误类别**；加约束必须有真实失败锚点，删约束要等强模型使其冗余。（Hashimoto / Osmani / HumanLayer / Böckeler / Cloudflare；research/01 §2.1、research/02a A9）
3. **guide 与 enforcement 分离：文件只指引，CI / 沙箱 / 分支保护才执行**——写进 AGENTS.md ≠ 被执行。（AAIF 判词 + Cloudflare / codex / Stripe 实践；research/01 §8.5、research/01b D1）

## 2. 工件（✅ 用户确认 2026-09-21——八件）

| # | 工件 | 主流做法 | 防缺口 | 源与指针 |
|---|---|---|---|---|
| 1 | **入口路由文件** | 只放路由 + 红线 + agent 自己发现不了的事实（精确命令含例外开关）；~100 行 TOC 教条（OpenAI）/ <60 行（HumanLayer）；**实态旗舰 5–7k tokens**（next.js 524 行 / codex 320 / airflow 246）；判据 = "每行是否路由或红线"而非行数；禁 /init 自生成 | ①② | 主干（research/01 §2/§7、research/01a B8） |
| 2 | **可追溯规则行** | 一行 = 一次真实坏行为；Recent Learnings 式追加日志节，固定"现象 → 处置 → 为什么"（openai-cookbook）；ghostty 的 sad-dumb 硬红线条款 | ① | 主干（research/01 §2，实物三例） |
| 3 | **按需披露层** | 入口 → README 链 / skills 按需：三层预算（~100 tok 常驻 / <5k 触发、正文 <500 行 / 附属零直到读取）；Cursor 四态规则；README 链按编辑路径触发（next.js）；降级协议（airflow：runtime 不支持 skill 发现就读 SKILL.md）；**嵌套语义三家三种实现（Codex 32KiB 截断 / Cursor 合并 / Claude 拼接）→ 必须按目标工具实测** | ②⑤ | 主干（research/01 §3/§7、research/01a B2–B8） |
| 4 | **深文档 / 知识库（system of record）** | "agent 看不见的就不存在"；**docs 只写 now（当前事实层，不写 change history——与工件 5 配对填缺口⑦）**；OpenAI 三目录：product-specs（行为语义真源）/ design-docs（为什么）/ exec-plans（active + completed + tech-debt-tracker；recovery note 给无记忆的新 agent）；有 index / owner / 保鲜期 | ②③⑦ | 主干方向·OpenAI 主导（research/02 §1.2） |
| 5 | **契约与决策工件（含负知识）** | 跨服务语义契约落 OpenAPI / schema / 显式契约文件，入口只放"改前必读哪个契约"的路由；决策史落 ADR——"值得写的变更才写"；**负知识也要 owner：记"为什么不做 X"、rejected 方案与 Known Limitations，带生命周期（proposed→implemented→rejected/archived）**——防"把明确的缺席当遗漏、反复提已否定方案"；**现行共识唯一 home——"当前怎么做"只在一处维护，历史决策全部降级进 ADR/notes 并带状态标记**（⑦ 的主填件） | ③⑦（含暗面） | 主干方向 + DSH 强化（research/01 §4） |
| 6 | **单源化** | 防双文件漂移：CLAUDE.md→AGENTS.md symlink（next.js"They are the same file"）；一行 `@AGENTS.md` 引用（goose）；工具间兼容层（Shopify） | ①（双权威漂移） | 主干（research/01b B1–B3 + A2，实物） |
| 7 | **元数据（owner / 新鲜度 / 版本）** | 规范层无 schema、无版本化（AAIF 设计选择）；治理层需要 owner/freshness → **团队自造**；工具层全是长尾（agentlinter / agnix / claudemd-pro），且无 repo 在 CI 直接 lint 规则文件内容 | ①②（时间维） | ⚠ **最不成熟**：共识是"需要"，做法未收敛（research/01 §1.2/§5、§8.2/§8.4） |
| 8 | **正确路径 / 归属表** | "目标 → 机制"归属表（新行为该接哪里）+ 改动半径分层（配置→扩展点→完整 seam→核心循环）+ 每层**升级条件**；**归属问题先于实现问题**；阶梯不是价值排序——L0 是完整能力，L3 只是影响半径最大，乱发挥的典型形态是"本可 L0 表达却爬到 L3 改核心" | ④ | DSH 单源（实例化"扩展点优先"通用传统） |

## 3. 回路（✅ 用户确认 2026-09-21——七条三链）

**A · 修错链**（棘轮的机器面｜防①⑥）：

1. **快反馈 + 门禁可信度**：本地 <5s lint + 失败自动修好再进 CI（Stripe shift-left）；stop-hook"成功静默、失败才回注"（HumanLayer）；**负例控制准入——每个门禁必须证明自己会红（引入回归→看红→还原），未做负例的检查视为摆设**（DSH）。【原则多源（Böckeler 之问"传感器从不触发是检测不足吗"），操作单源 DSH；research/01 §8.5、research/02 §7.4、research/02a A3】
2. **错误信息写给 agent 读**：不只说错、还说怎么修（"positive prompt injection"）——OpenAI taste linter 与 Böckeler 独立同构，Stripe 同向。【主干 3 源；research/02 §1.4、research/02a A3】
3. **升格通道**：review 评论里第二次出现的规则 → 升格为 lint/doc；AGENTS.md 里的约定固化成 CI lint（codex 的 argument-comment-lint 实例）。【主干；research/01 §8.2、research/02 §5.2】

**B · 漂移链**（防"地图过期"——⑦ 的主力回路、所有缺口的时间维）：

4. **保鲜**：生成类文档"必须新鲜或明确标 stale"+ `git diff --exit-code` 兜底（OpenAI）；"stale 的 AGENTS.md 比没有更糟"+ AI Code Reviewer 反向触发更新（Cloudflare）；文档侧等价实现 = 防漂移三件套：verify 脚本（UTF-8/链接/锚点）+ 基线钉（"以 X commit 为准"）+ 改事实只改 home（DSH）。【主干 + DSH 单源操作；research/02 §1.3、research/01 §8.1】

**C · 真相链**（防②⑥的运行时面）：

5. **评审外置**：agent review 从 advisory 起步、分角色、findings 分类；**evaluator 必须外置**——agent 自评必然自信地自夸（Anthropic 负结果）；语义 review 只拥有语义判断。【主干；research/02 §7.5、research/02a A5】
6. **运行时可查询**：agent **问**系统实际状态而非猜源码——per-worktree 栈（OpenAI）+ DSH 三查询面（最终配置 dump / 声明面 catalog / 活进程 inspect）；原则 = Hashimoto"给 agent 验证手段"（多源）；重型实现按需上（Teleport 复杂 harness 有害反证）。"看 agent 行为的遥测"归组织段第 4 条，不在本条。【原则多源，重型栈 OpenAI 特化；research/02 §1.4、research/02 §4.3】
7. **反馈分层**：六层光谱——编译 / load / 局部测试 / 组装 / invariant / 语义 review；**每层只拥有自己能观察的性质，绿一层不代表层层绿**；错误在离源头最近的层被抓，本地跑相关、CI 跑穷举。【DSH 归纳 + Stripe 分工同向】

## 4. 节奏（✅ 用户确认 2026-09-21——含两处修订：快慢双通道、模型升级日绑定大扫除）

> **快慢双通道（2026-09-21 用户复核补充）**：节奏 1 与节奏 2 不是并列节拍，是互补通道——棘轮**快而糙**（当场止血，但可能修错：错根因 / 过宽过窄 / 规则冲突），清扫**慢而准**（纠错通道）。机制：棘轮产物标记"新增（待复核）"，下次清扫优先校对——即 ⑦ 的生命周期用于规则自身（**棘轮提议、清扫转正**；Vercel 双闸门 / collector-judge 分离同构）。

1. **犯错时 → 棘轮**（宪法 2 的操作面）：同类失败第二次出现即动手（第一次只记录）；产物当场生效但**标记"新增（待复核）"**，进下次清扫的优先校对清单；操作规程（触发 / 分流 / 验收 / 转正 / 退出）为 04 手册级第一篇。【主干 5+ 源｜防①⑤⑥】
2. **周期清扫 → 已成编制岗位**：doc-gardening 直接开 fix-up PR（OpenAI）、"清洁工军团"（Thoughtworks）、季度 13 工程师 pressure washing（Teleport，安全漏洞清扫场景）、janitor 常驻 agent 岗位（AssemblyZero）——"清扫"隐喻 ≥4 源独立发明，命名收敛本身即证据；**清扫对象含概念沉积：废弃方案、过期术语、叠层决策记录的归档与删减（⑦ 的节奏面）**。【主干｜防⑦及所有缺口的时间维；research/02 §7.11、research/02a A10】
3. **模型升级时 → 复检触点**：每个 harness 组件都编码了"模型做不到"的假设，升级后拔枯枝（Anthropic / LangChain / Osmani 沙箱案例 / Ronacher tool schema）。**依赖 / 基线升级同理**：上游合入后按 change log 只复核被引文件、不全文重写（DSH）。**执行绑定（2026-09-21 用户复核定）**：模型升级日 = 大扫除日——拔枯枝与深度清扫合并执行（Teleport 的 pressure washing 原文即"每次新模型发布就重复一遍"），不为它单独维护第三种日程。【主干 4 源 + DSH 同构；research/02a A5/A6】

## 5. 组织与边界（⏳ 待用户复核）

1. **规则变更一律 PR、有 owner**（codex / next.js / goose 三 repo 共同点 + Cloudflare MR 审 + Vercel）。【主干；research/01 §8.2、research/01b B4】
2. **规模化路：机器生成 + 人审 + 反向触发更新**（Cloudflare 3900 repo、93% R&D 采用）。【单源·大规模采用；research/01b A4】
3. **规则当产品**：准入双闸门（current-source verification + human acceptance）、淘汰条款、coverage-gaps、**触发与内容分开测**（Vercel：56% 失败是触发失败而非规则失败）。【单源强实践 → 主流候选；research/01b A3】
4. **用量遥测**：PreToolUse hook 找过热/欠触发（Anthropic）+ evals（Vercel）。【2 源；research/01b A1/A3】
5. **反过度工程**：复杂 harness 有害（Teleport 实测）；工具面 -80% → token -37%、3.5× 提速（Vercel，n=5 注意样本量）；预装几十 skills / 每次全量跑测试 = 失败清单（HumanLayer）；start empty → incremental → prune（Upsun）。**"组合压力"产物（插件图 / seam / 完整 inspect）确有压力才做**（DSH）。【主干，独立反例群；research/02 §7.12、research/02a A10】
6. **merge 姿态按风险分级**：fix cheap / wait expensive 仅在真实 agent 吞吐 + 低修复成本下成立；高风险类目（auth / billing / 破坏性变更）保留人审 + 回滚计划。【单源（OpenAI 自认）+ research/02 §4.4 矩阵，标注】
7. **四个不能混淆的边界**（DSH）：可读 ≠ 简单；Skill ≠ enforcement；清理 ≠ 回滚（disposer 不补偿已发生的外部写入）；运行时查询 ≠ 安全沙箱（bash-equivalent trust）。【DSH 单源，防迁移误读】

## 6. 信息流与指针规则（本层纪律）

- **单向加工**：`../research/` 证据档案 → 分篇判读 → 本文件；review 改变本文件结论 → 反向同步 research/ 对应分篇（信息流三规则见主题 README）。
- **指针写法**："research/01 §2.2" 式短引（层前缀 + 编号 + 节号），禁用裸"01 文档"式指代（防旧编号歧义复发）。
- **手册级下钻**（SOP / 模板 / 判据表）→ `04-practice-manual.md`；条目级下钻直接落 04，框架级重构先回 `.tmp-` 磨。
