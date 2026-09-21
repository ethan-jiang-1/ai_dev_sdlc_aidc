# AGENTS.md — repo_agent_friendliness 评估系统 · agent 操作手册

本目录是一套**仓库无关的"repo 对 coding agent 友好度"评估系统**。你（执行评估的 agent）被叫来时，通常是用户给了一个**目标仓库**并要求评估。本文件是你的操作手册：按它走，不需要其他上下文。

**上游纪律**：受仓库根 `AGENTS.md` 约束；本文件只管本系统内部的操作规程。

---

## 0. 调用契约

- **输入**：用户给的目标仓库路径（通常在仓库外）+ 可选信息：实际使用的 harness 集合（Claude Code / Codex / Cursor / …）、关注维度。缺 harness 信息时**先问**，不猜——同一仓库对不同 harness 得分不同（framework §1）。
- **输出**：一份评估报告，落在本目录 `30-runs/<日期>-<目标仓库名>-<harness集>/report.md`，附 `manifest.md`。
- **铁律**：目标仓库**只读**。一切写入只发生在本目录 `30-runs/` 下。

## 1. 评估仪式（七步，顺序执行）

1. **读法**：`10-spec/framework.md`（体系法律，当前权威）→ `10-spec/archetypes.md`（形态分型）→ 按分型读 `10-spec/line-a-traditional-repo.md` 或 `10-spec/line-b-agentic-repo.md`（评估面与重心维）→ `10-spec/dimensions/`（九维边界与判据族）。
2. **分型**：按 archetypes §1 判定目标仓库是形态 A（确定性应用）还是 B（智能体产品）。分型依据是**正确性模型**，不是"代码由谁写"。混合形态按产出物拆开分评。拿不准 → 停下来问用户。
3. **建 run 目录**：`30-runs/YYYY-MM-DD-<repo>-<harness集>[-pilot]/`，先写 `manifest.md`（模板见 `30-runs/README.md`）——钉住本轮用的 spec 版本（git commit hash）、checklist 版本、harness 及其版本、模型、观测日期。**没有 manifest 的报告无效**。
4. **Tier-0 静态扫描**（便宜证据先采）：判据族中机器可判条目逐条过（文件存在性、体量、lockfile、CI 配置、契约测试存在性、VCS 惯例等）。有 `20-instruments/scan/` 脚本则跑脚本，没有则手工执行 probe。
5. **Tier-1 注入验证**：在用户声明的每个实际 harness 内，确认指令真实加载、无静默失败、无超预算截断（如 Claude Code `/context`、Codex "Summarize the current instructions."）。记录 harness 版本。
6. **Tier-2 演练与评审**：仅对 tier-0/1 无法判定的问题启用——一次真实小改动闭环演练（卡点映射到 ②③⑨ 条目）、协议化抽样评审（①④ 主观条目；抽样协议按判据的 sampling 字段，未落条时在报告中写明你抽了什么、抽了几处）。
7. **产出**：`report.md`（模板见 `30-runs/README.md`）——门禁判定 + **A–D 总评评级**（framework §4.2 刻度，校准前可用）+ 各维短板分 + 加权数值分（权重未定型则留空）+ 按序整改清单（⑤❌ 置首 → 门禁 ⚠️ 次段 → 其余 ❌ 按维度短板分升序 → ⚠️ 随其维）；回本目录 `CURRENT.md` 登记一行。

## 2. 打分纪律（违反即报告作废）

- **无证据不打分**：✅/⚠️/❌ 三档，⚠️ 与 ❌ 必须引用 probe 的实际观察（命令输出、文件行号、演练记录）。
- **tier 是判据的固定属性**：按 framework §3.2 采证顺序，不许用 tier-2 印象替代 tier-0 可判事实。
- **判据只写行为描述**：目标仓库的具体做法可进证据列，不进合格标准。
- **边界不双算**：一个事实只归一个维打分（各维边界声明优先；①④⑨ 的共享表面按各维"泛化注意"的归属执行）。
- **checkpoint 隔离**：权重未校准前，报告给 **A–D 评级与分维短板分**，不给加权数值分与总分（framework §4.4）。
- **内部命名不出门**：报告中不出现本仓库内部代号、姊妹项目名、"参考另一场 talk"类表述。

## 3. 现状标注（执行前必读，避免空转）

截至 2026-09-21，系统处于**定义层已定型、器械层未落条**阶段：

| 组件 | 状态 |
|---|---|
| framework（九维、聚合结构、度量语义） | ✅ 已定型（v1.4：映射 1.0/0.5/0.25、A–D 刻度、门禁 ⚠️ 封顶 B） |
| 九维判据族（定义级草案） | ✅ 在 `10-spec/dimensions/` |
| checklist-A / checklist-B（逐条判据） | ❌ 待建（`20-instruments/`） |
| harness-profiles | ❌ 待建 |
| tier-0 扫描脚本 | ❌ 待建 |
| 权重数值 | 有意不给，待效标回归（framework §4.4） |

因此现阶段产出的是**定义层评审版报告**：以九维判据族为框架人工采证，报告中显著标注"判据未逐条落条版本"；它可用于结构性诊断与试测，不等于器械齐备后的正式审计。不要为凑"正式感"而虚构 checklist 条目编号。

## 4. 改体系的规矩（如果你被叫来改 spec 而不是跑评估）

- 改 framework / dimensions 前先读 `10-spec/adr/`——结构性裁决（如"为什么是九维"）一文件一裁决，新裁决新建 ADR，framework 只留结论。
- 维度增删改边界：先过目录 README 的正交纪律，`dimensions/README.md` 与 framework §3.4 两处同步，ADR 记录理由。
- 器械（checklist、profiles、脚本）变更不改 spec；spec 变更须评估已存 runs 的可比性，并在 CURRENT.md 记录断代。
