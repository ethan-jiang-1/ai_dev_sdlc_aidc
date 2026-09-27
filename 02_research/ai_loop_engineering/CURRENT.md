# 当前状态（热区）

> 最近一次更新：**2026-09-27（P0 补证据轮 + 多 Agent 采样协议）**：新增 E/F/G/H 四路回源与 `digested/06`；补充“弱模型高召回、主 Agent 低信任收口”的并行采样协议。

## 一句话

**第一轮命名/构件研究已完成，P0 补证据把问题推进到控制面层**：`evidence-e` 找到 Anthropic Managed Agents 的单 session 状态/验收/恢复 API 与 OpenClaw detached task/flow ledger，但两者都不是统一 feature backlog；`evidence-f` 找到动作类别、沙箱/信任、关键歧义、拒绝预算、工具级 interrupt 和授权作用域等事件判据，但没有通用“跑 N 轮必须人看”；`evidence-g` 钉住 DSH goal/driver/todo/plan/session 的原生边界；`evidence-h` 支持“harness 让 loop 更可设计/可观察”的机制解释，不支持 harness 单向引发 loop。`digested/06` 已形成初步判读；实践层仍待用户逐段确认，且不自动吸收新建议。**

## 状态

| 件 | 状态 |
|---|---|
| `raw/evidence-2026-09-26-{a,b,c}-*.md` ×3 | ✅ **A**（词源四人：Runkle/Osmani 全取得；Cherny/Steinberger 定性碎片级）· **B**（停止条件/调度，9 个一手记录块）· **C**（自主度/收敛/归属修正）；**09-27 增量**：Osmani D5–D10 实践细节补入 evidence-a（不新建重复档案） |
| `raw/evidence-2026-09-27-{e,f,g,h}-*.md` ×4 | ✅ **E**（Managed Agents 单 session 状态/验收/恢复；OpenClaw detached task/flow ledger；feature_list 尺度边界）· **F**（动作/环境/歧义/拒绝预算/授权 scope 判据；无通用 N 轮阈值）· **G**（DSH goal/driver/todo/plan/session 一手机制边界）· **H**（automation/autonomy/harness/loop 时间轴、竞争解释、因果边界） |
| `raw/research-plan.md` | ✅ v0.2：问题树、A–H 分路、文章/KOL/判读映射、Agent 委派协议、低成本多 Agent 采样协议、P-existence/P-mechanism/P-outcome 证据等级、P0–P2 backlog 与每轮收口格式；已追加 automation→autonomy→harness→loop 竞争解释 |
| `digested/06-automation-autonomy-harness-loop.md` | ✅ 初步判读：控制对象逐层外移与叠加；harness 是 loop 可设计/可观察的条件之一，不是单向历史原因；DSH 执行循环与 feature control plane 分离 |
| `raw/kol-roster.md` | ✅ §A **6 条全部收口**（4 条一手全文＋2 条部分一手＝Cherny/Steinberger 词源碎片级定性）；huntley / chase / **openai_org**（素材属窗口前）移 §B（**有窗口内新发声则升回**）；Cherny/Steinberger **不建卡**；alchaincyf 降级出册；Viv Trivedy 与 Jesse Vincent 候选；Osmani 行拆分定义/建议/个人观察 |
| `raw/00-timeline.md` | ✅ 词源周精确锚定（06-02 → 06-07 → 06-08 → 06-16 → 06-30，snowflake 解码）；新增 2026 上半年厂商落地三事件；三条归属修正入册 |
| `digested/01-命名谱系.md` | ✅ 词源＝热度碎片、定义＝事后工程化；最小模型与外层调度扩展已按 Osmani 增量分层；四人核心同指、外延不兼容；实践层命名依据 |
| `digested/03-构件.md` | ✅ 停止条件三件骨架收敛；外层调度降为长程扩展（两种已观察形态）；自主度位置词汇/运行模式有材料、量化未成型；来源独立性与效果证据边界已补 |
| `digested/05-边界判定.md` | ✅ 三层分工；收敛成立且双向；**三条引用归属修正**（影响全仓） |
| ~~`raw/org/` · `raw/community/`~~ | ✅ **已撤销**（2026-09-26 评审决定 5）：evidence 档案为素材常态形态，纪律要点已并入 README §1「回源档案纪律」 |
| 实践层 `03_practice/loop_governance/` | ✅ README + CURRENT + result/README + **result/backbone.md（§0–§6 七节＋§0.2 诊断轴）+ result/manual.md（12 节操作规程）**——**均待用户逐段确认** |

## 下一步

1. **研究层下一轮（P0→P1）**：把 E/F/G/H 的机制证据做成跨来源控制矩阵，重点补两项：统一 feature-level ledger 的候选/授权/优先级/验收字段；以及 DSH 小 feature 对照实验的 P-outcome（催问、漂移、返工、提前完成、人工时间）。
2. **用户复核实践层 backbone（§0–§6 七节＋§0.2 诊断轴）与 manual（12 节）**——对照着过（manual 是 backbone 的操作化展开）；F 路的动作边界/升级可达性先作为研究层候选，不自动写进规程。
3. **跨仓修正三处**（本轮一手证据触发，不属本主题但已查明）：
   - `talk-harness-201/02_evidence/01-kol-alignment-2026.md`：公式 "Agent = Model + Harness" 归属改为 **Trivedy/LangChain 原创 → Böckeler 传播锚点化**；
   - `01_sources/reference/kol/_raw_kol/10_kief_morris.md`：三档 → **四级**（+ agentic flywheel），且 flywheel 是节标题；
   - Böckeler "False sense of control?" 的出处标注改为 **2025-10-15 sdd-3-tools.html**（凡引用处）。
4. **可跟踪预言**（登记防丢）：若出现第一条可复核自主度/质量放行阈值，回本主题补档、再评估实践层 §3；当前不以固定 N 轮作为目标。


## 缺口

1. **《Unwinding Codex's Agent Loop》正文未取得**（openai.com 站点级 403，B 路对照实验实锤）——"四拍循环 / assistant message 终止态"**上屏前必须回源**；库内 `ai_sdlc_frontier/raw_OpenAI_Michael Bolin/` 是中文编译二手版，只作线索。
2. **通用轮次自主度分档**仍为 0 一手来源——F 路确认应转向动作/环境/歧义/拒绝预算/升级可达性，不制造“跑 N 轮必须人看”。
3. **统一 feature-level 在途可见性**仍是开放缺口——E 路已找到 Managed Agents 单 session 状态与 OpenClaw detached task/flow ledger，但尚无统一候选、授权历史、priority 变化、业务阻塞与跨 feature 验收总览。
4. **真实 P-outcome**仍缺——当前主要是机制存在/设计说明；尚无跨机构或 DSH 对照证明减少催问、漂移、返工或人工时间。
5. **行为面验证**（门拦得住动作、拦不住“没做该做的事”）仍是已知短板；F 路的授权可达性反例也说明“有升级入口”不等于实际可接手。
6. **Cherny 访谈句三个流传版本措辞不一致**（A 路已列对照表）——上屏引用须先人工核验视频原声。

## 铁律速记

- **素材权威在 evidence 档案与 `01_sources/`，判读权威在 `digested/`，操作权威在 `03_practice/loop_governance/`**。
- **`⏳ 待回源` 不进结论**；**B 路**四条负结论（Unwinding 正文 / CC CHANGELOG / auto mode 公告正文 / Codex auto-review docs）已如实归档（A 路 12 条、C 路 7 条见各档案负结论节；台账 §E 收跨路汇总）。
- 姊妹仓 FAQ 15 的旧判定（切片层/管线层）**只作对照**——本主题全部结论以自己的回源为准。
