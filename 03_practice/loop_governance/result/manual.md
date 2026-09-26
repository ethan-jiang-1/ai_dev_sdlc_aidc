# Loop Governance 实践手册（定稿层·操作规程）

> **本文件是什么**：loop 层操作规程的定稿——把 backbone §0–§4 的主张展开成**可照做的步骤、模板、判据表**；
> 每条带证据指针（回研究层 evidence 档案与库内一手，本层不复制证据）。
> 主张与为什么在 [`backbone.md`](backbone.md)；本文件只管**怎么做**。

```yaml
topic: Loop Governance —— 实践手册（backbone §0–§4 的操作化）
doc_layer: result（定稿层 · 操作规程，SOP 级）
produced_at: 2026-09-26
provenance: 全部内容自研究层三路回源档案（evidence-a/b/c）与库内一手（anthropic_ai_sdlc playbook、fable5 样本、harness_governance backbone）挖掘；未回源材料不入册
filter: 官方一手逐字 > 实践者第一人称 > 本主题编排（编排处显式标注）
---
```

## 0. 用法

backbone ＝ 主张（what/why，清单级）；本手册 ＝ 规程（how，SOP 级）。新场景从 §1 诊断进入，
按 §11 落地梯子逐档爬升；backbone §0.2 失败模式表的最后一列指到本手册对应节（§1 的自检表是它的入口版）。
引用写法与 backbone 一致：`evidence-a/b/c §节号`、`digested/编号`、库内一手按路径。

## 1. Phase 0 · 诊断（要不要 loop 治理｜操作化：backbone §0 判据）

**三问**——前两问是判据层（任一答"否"就**先别上循环**，见 §12 反过度工程）；第三问是外置层（答"否"**可以上会话内循环**如单会话 `/goal`，但**跨轮 / 多 feature 循环前必须先补外置**）：

1. **停止条件依赖上次结果吗？**——不依赖的是重试，不是 loop（backbone 判据一）；
2. **单次运行受控吗？**——不受控时循环只是把错误复制得更快（判据二；先治 harness 层）；
3. **跨轮状态外置了吗？**——没外置（文件/git/session log），每轮都在交对话税，人退化成催促者。

**失败模式自检**（编号对应 backbone §0.2；①②已由三问覆盖；症状对上就翻对应节）：
③ one-shot 冲动→§5｜④ 提前宣告完成→§2/§5｜⑤ 未验证标 done→§2/§5/§10｜⑥ 无进度盘→§5｜⑦ 自主度超前于门禁可信度→§9｜⑧ 操纵裁判→§4/§7。

## 2. 停止条件写法规程（操作化：backbone §1｜CC 官方文档，evidence-b §4a 一手）

**模板（官方三要素 + 上限子句）**：

```text
目标（一个可度量终态；官方例类别：测试结果 / 构建退出码 / 文件数 / 空队列——CC 官方）：
  "All tests in test_status.py pass" / "the endpoint returns 200 with the new field"
  / "the screenshot matches the attached mock"（playbook 例句）
检查（声明式——怎么证明，写明用哪条命令、看哪个退出码或输出）：
  "`npm test` exits 0" / "`git status` is clean"（CC 官方例句）
约束（路径上不许变的东西）：
  "no other test file is modified"
上限子句（推荐常备）：
  "… or stop after 20 turns"（轮次或时间均可）
```

**三值判定语义**（停止条件是状态机不是布尔）：**Not yet met**→继续，且评估理由作为下一轮指导；
**Met**→清空目标并在 transcript 记 achieved；**Impossible**→评估器判永不可满足，停。

**写法红线（Osmani 操作篇逐字，evidence-a 补充回源）**：① 含糊目标不配循环——"a vague goal would be 'keep going until this UI design is good'. What does that mean? Good to who? How is it being evaluated?"；② **别把品味和判断一起委托**——"check yourself, that you are not delegating the taste and the judgment to your agent. You're delegating the task, and then you are actually checking back that it's meeting your bar."；③ 评估器只核 transcript 硬规则、**不判内容好坏**——"It doesn't look at the content to see if it's good or bad in any way, shape, or form"（判好坏的是人或上级环——前两句逐字·evidence-a 补充回源；"上级环"为本主题依 Ng 三环补的推断）。

**实战例（Osmani 逐字，全部要素一次配齐）**：`/goal Refactor the data-fetching layer in Dashboard.tsx until Lighthouse performance score is >= 92 and LCP is under 1.8s as shown by the Lighthouse CLI output. Do not change the public API of any hooks. Each turn must improve at least one reported metric; abort if two consecutive turns show no improvement. Stop after 10 turns.`——可度量终态（Lighthouse ≥92 / LCP <1.8s）、声明式检查（Lighthouse CLI 输出）、约束（不改 public API）、无进展中止（连续两轮无改进即 abort）、轮次上限（10 turns）。

实践例证：Jesse Vincent 的过夜 `/goal`（25 实验例，中文转述·非逐字，仅作用法样本——fable5 样本）。

## 3. 裁判权选型规程（操作化：backbone §1 未收敛点→选型表）

| 裁判 | 适用 | 成本/风险 | 源 |
|---|---|---|---|
| 人判（taste） | greenfield 探索、清单语义撑不住 | 不可规模化；TODO 耗尽与否凭 taste | Huntley，evidence-b §1 |
| 文件清单逐条判定 | 功能型长跑、目标可枚举 | 清单本身须保护（→§4） | Anthropic，evidence-b 问题2 §1 |
| 独立小模型每轮判定 | 会话内 goal | 评估器自身的可信度（→§4 第 3 条） | CC `/goal`，evidence-b §4a |
| 干活模型自判 | 默认形态——**最弱** | 必须配 §4 保护与 §7 熔断作补偿 | Anthropic 2024，evidence-b §2 |
| 被审批方提出、审批方判定 | 越界动作 | 审批 agent 可被操纵（red-team 实证："should not be treated as a guarantee of security"） | OpenAI，evidence-b 问题2 §3 |

**选型次序（本主题编排）**：优先机器可核的裁判；必须人判的，把判断点集中在门（backbone §4.1）。

## 4. 保护裁判规程（"agent 修代码时不得削弱对代码的检查"｜四件，各源见注）

1. **测试不可删改**：强措辞条款（"It is unacceptable to remove or edit tests…"）＋ test-file hook 硬拦（evidence-b §3 一手；hook 做法 playbook Test 节）；
2. **清单选 JSON 不选 Markdown**：模型对 JSON 整文件改写的概率更低（evidence-b §3 一手）；
3. **评估器输入防操纵**：分类器只看用户消息与工具调用、剥掉模型自述——"reasoning-blind by design"（evidence-b §4b 一手）；
4. **测试当场写明为什么存在**：因为"future loops will not have the reasoning in their context window"（evidence-b §1 一手）。

## 5. feature_list 进度规格规程（操作化：backbone §2 形态一｜evidence-b 问题2 §1 一手全套）

**七步**：

1. **initializer 展开**：粗目标 → 逐条 feature（结构 `category / description / steps / passes`，初始全部 `passes: false`；官方一例 200+ 条，如 "a user can open a new chat, type in a query, press enter, and see an AI response"）；
2. **建三件套**：feature_list + progress 文件 + 初始 git commit；
3. **每轮固定开场序列**：定位工作目录 → 读 git log 与 progress → **选清单里最高优先级的未完成项** → 先过基线（init.sh 拉起开发服务器跑基线端到端——环境已被留在坏状态时先修它，别在上面积新功能）；
4. **一次只做一件**（对抗 one-shot 冲动）；
5. **完成判定**：端到端自验证（browser automation / 真实用户路径）后才翻 `passes`——单测或 curl 过不算（官方失败模式三的原话对策）；
6. **干净收尾**：描述性 commit + progress 更新（让下一轮冷启动可接上）；
7. **允许的动作收敛**：coding agent 只被允许改 `passes` 字段。

**官方失败模式对照**（逐字，evidence-b §3）："declares victory on the entire project too early"→设 feature list；
"marks features as done prematurely"→self-verify all features，只在认真测试后标 passing。

## 6. 触发器选型规程（操作化：backbone §2 形态二｜官方对照表逐字，evidence-b 问题2 §2）

| 方式 | 下一轮何时开 | 何时停 |
|---|---|---|
| `/goal`（条件驱动） | 上轮结束；或闲置检查点；或自动重试到期 | 模型确认条件满足 / 判不可能 / 轮内错误需人修 / 显式清除 |
| `/loop`（时间驱动） | 时间间隔到 | 你停它，或 Claude 判工作完成 |
| Stop hook（脚本驱动） | 上轮结束 | 你的脚本或 prompt 决定 |

**`/loop` 三种拍法**：`/loop 5m check the deploy`（固定间隔+prompt）｜`/loop check the deploy`（间隔模型自选）｜
`/loop`（无 prompt——读内置维护 prompt 或 `.claude/loop.md`，项目级优先）。
**动态间隔机制**：省略间隔时模型按观察自选 1 分钟–1 小时（构建在跑短等、无事长等）。
**内置维护 prompt 的边界**（固定优先级：继续未完工作 → 照料当前分支 PR（评论/CI/冲突）→ 清理），
且**不开范围外新动作；不可逆动作（push/删除）只继续 transcript 已授权的事**。
**三档调度面**：云 Routines（≥1h，无需开机）｜桌面 cron｜会话内 `/loop`（≥1min）。
auto mode 不在此列——它只管轮内审批，不开新轮。

## 7. 熔断与终止规程（六道闸｜evidence-b §4a/4b/4c/2.3 一手）

1. **拒绝熔断**：3 连拒或累计 20 拒 → 停机升级给人（阈值官方写明不可配置；headless 无 UI 直接终止进程）；
2. **无进展熔断**：连续数轮无工具调用 → 停 + 警告 + 返还控制（goal 保留不清）；
3. **不可恢复错误**（四类，清空目标）：认证失败｜额度耗尽｜压缩解决不了的上下文溢出｜模型不可用；其余错误 3 次自动重试后暂停；
4. **单次拒绝不终止**：deny-and-continue——拒绝带理由回给模型换安全路径（内部部署中过半场景模型自寻可接受方案）；
5. **未续排兜底**：一轮既未续排也未停 → 约 20 分钟后 fallback wakeup，再不续排则终止；
6. **硬过期**：定时任务 7 天自动过期删除（官方原话："bounds how long a forgotten loop can run"）。

**反操纵监控**：监控"反复尝试绕过审批"的行为，反复拒绝后自动停轨迹（OpenAI，evidence-b 问题2 §3）。

## 8. Ralph 式循环规程（greenfield 专用｜evidence-b §1 一手）

**适用警告先行**："There's no way in heck would I use Ralph in an existing code base"——存量库禁用；预期用它做到 ~90%。

1. **循环本体**：`while :; do cat PROMPT.md | claude-code ; done`（工具须不设调用上限）；
2. **back pressure 配置**：静态类型语言自带（类型系统）｜动态语言**必须**接静态分析（文中列举 dialyzer、pyrefly）｜测试｜安全扫描——"Anything can be wired in as back pressure to reject invalid code generation"，但"the wheel has got to turn fast"（反馈要快）；
3. **signs（牌子）**：踩坑教训写成环境内持久的提示，让下轮自己看见（原文实例，parrallel 为原文拼写、此处径改，引句有节略："Before making changes search codebase (don't assume an item is not implemented) using parallel subagents. Think hard."；"DO NOT IMPLEMENT PLACEHOLDER OR SIMPLE IMPLEMENTATIONS. WE WANT FULL IMPLEMENTATIONS."）；
4. **每轮确定性重装栈**：fix_plan.md + specs/ 每轮重新装入（跨轮状态全在文件，不在会话记忆）；
5. **主上下文当调度器**：重活派 subagent；**build/test 限 1 并发**（原文为 Rust 一例，理由可推广）——几百个 subagent 同时跑 build 会把 back pressure 打失效；
6. **两模式**：planning Ralph 生成 TODO 清单 → building Ralph 消费；
7. **终止**：无内建停止条件——TODO 耗尽或跑偏由人判（"a matter of taste"）；清单可整体扔掉重生成；
8. **绿灯记录**：无 build/test 错误则 git tag 递增 patch（0.0.1→0.0.2…），形成可回退的里程碑链；
9. **恢复决策**（人的活）：`git reset --hard` 重跑，还是换一组 prompt 救——别让 agent 自决；
10. **占位对策**：模型有"最小实现/占位"偏好——用牌子防 + 再跑 Ralph 专找占位实现转成下轮 TODO。

## 9. 自主度升档规程（操作化：backbone §3）

**三个独立阶梯对照**（详表在 backbone §3）：Morris（outside→in→on→flywheel）｜Osmani（agentic loop→`/goal`→`/loop`→proactive）｜playbook（逐手 prompt→门禁审阅→auto-accept→并行 worktree→building and monitoring loops——**五档链条为本主题自 playbook 散点合成，各档有原文落点**）。

**升档前置检查（三条全过才升）**：

1. **门会红吗**——负例控制：引入一个回归看门禁会不会红；未做过负例的检查视为摆设（衔接 [`harness_governance` 回路 1](../../harness_governance/result/backbone.md)）；
2. **评估器独立吗**——过 §10 五式之一；
3. **熔断配了吗**——§7 六道闸至少配了拒绝熔断与硬过期。

**σ 分层响应配置**（无人值守档的成品样板，playbook《Closing the loop》一手）：

- 选**一个**有稳定滚动基线的指标（CI 测试失败率／post-deploy 5xx／PR 周期时间）；
- 检测脚本：均值＋标准差滚动窗口，Western Electric 式规则（抓慢漂移与尖峰）；**脚本版本控制＋单测，检测全程确定性、模型不参与**；
- 响应层级（bands.yaml 式配置）：**1σ 只记录｜2σ 只读诊断｜3σ 可行动但仅限开 PR 进 review 门或触发预批 runbook**；
- 回滚必须是管线里**最演练的路径**：单命令、agent 可执行、staging 定期演练。

## 10. 验收独立性规程（操作化：backbone §1 骨架三）

**原则句**：CC——"completion is decided by a fresh model rather than the one doing the work"；
OpenAI——"The separation of roles matters…（主 agent）creates pressure to treat an approval boundary as just another obstacle to overcome"。

**五式**（按场景选一）：

| 式 | 场景 | 源 |
|---|---|---|
| evaluator-optimizer 工作流 | 有清晰评估准则、迭代有可度量收益 | Anthropic 2024，evidence-b §2 |
| 只许改 `passes` 字段 | 清单判定 | evidence-b 问题2 §1 |
| `/goal` 独立小模型每轮 | 会话内目标 | evidence-b §4a |
| 独立审批 agent | 越界动作 | evidence-b 问题2 §3 |
| verifier subagent 新上下文终检 | 长任务的末次验收 | playbook（"the verdict is not colored by the assumptions that produced the code"） |

**区分**（playbook 逐字）：feedback loop（贯穿全任务、随工作反复跑）≠ verifier subagent（末次终检、新上下文一次性）——分工不同：一个管过程、一个管终点（「配对使用」为本主题观察，非 playbook 原文）。

## 11. 统一落地梯子 P0→P4（操作化：全手册｜**本梯子为本主题编排**，档位依据各有一手、梯子本身是合成）

| 档 | 形态 | 前置条件 | 用到的节 |
|---|---|---|---|
| **P0** 会话内人工驱动 | 人写每轮 prompt＋单命令检查（make test） | 检查能一条命令跑通 | §2 模板雏形 |
| **P1** 目标驱动 | `/goal` 式条件＋三要素＋熔断 | P0 已跑通：同一检查连续多轮一条命令通过 | §2/§3/§4/§7 |
| **P2** 进度规格 | feature_list 三件套＋固定开场＋一次一件 | 目标可枚举成条目；P1 已跑稳 | §5/§4 |
| **P3** 定时/事件 | `/loop`/loop.md/cron/webhook | P1–P2 连续运行且无熔断触发 | §6 |
| **P4** 无人值守 | proactive 事件触发＋σ 分层响应＋生产回写 | 门禁过负例控制；回滚最演练；§9 三条前置全过 | §7/§9/§10 |

**只逐档爬，不跳档**；**退档信号**：熔断频发、假把控症状（backbone §4.3 的两面镜）复现——退一档重新稳住再升。

## 12. 反过度工程清单（操作化：backbone §4）

1. 单次小任务不建循环脚手架——先有真实失控，再上治理；
2. brownfield 禁 Ralph（Huntley 原话）；
3. 门不可信不升档（backbone 判据二——错误复制机）；
4. 评估器别越权判内容好坏——判好坏的是人或上级环（Osmani 澄清）；
5. 复杂 harness 有害的镜像教训同样适用于 loop 侧（Teleport 反例，见 [`harness_governance` 组织 5](../../harness_governance/result/backbone.md)）；
6. **反面声音**：Steinberger 2025-12 长文——"usually I'm the bottleneck"——**通常人自己就是限速环节**（编排不是瓶颈、人是，所以他对自动编排「没看到多大必要」；**原文未说「自动化更慢」**）。与 §3 不冲突：§3 说的是**裁判**（完成判定）优先机器可核，本条说的是**调度自动化**收益有限——两个角色（evidence-a 一手）；
7. **行为面验证缺口**：门拦得住动作、拦不住"没做该做的事"——减监督前先想清这一条还堵不上（登记在 backbone §3，开放缺口）。
