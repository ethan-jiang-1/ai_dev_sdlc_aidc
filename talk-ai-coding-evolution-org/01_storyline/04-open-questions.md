# 悬而未决的问题（随手记，推敲中不断增删）

## 已决（v0.2）

- [x] **对象扩为「研发整体组织」**：从产品一路到底到实施、再到运维；不再是「组织 + harness 单焦点」。
- [x] **篇幅档位 = A**：单场加长 Keynote，75–90 min，目标 ~45–60 页，不再受 23 页约束。
- [x] **独立成篇**：不依赖、不承接 `04_output/deck_ai_sdlc_keynote`（听众不同）。
- [x] **去掉「航海」**：题目方向 = AI-Native 研发组织 / 高科技组织。
- [x] 两轴合成：宽轴（六阶段 SDLC）+ 深轴（五层 + Harness）；harness = 整条链的平台层 + 治理层。

## 主题层（已定 v0.2）

- [x] **题目已定**：AI-Native 研发组织：从产品到实施的 SDLC 转型之道（用户拍板「你来吧」，采用推荐候选 ①）。
- [x] **slogan 已定**：代码不再是瓶颈，流程才是。

## 结构层（已定 v0.5）

- [x] **SDLC 六阶段是主轴**（Plan→Design→Build→Test→Deploy→Maintain），第二幕占 26 页。
- [x] **五层 + DSH 不强扭成独立章节**，各在自然接点作「引子」插入：Plan=Prompt、Design=Context、Build/Test/Deploy=Harness、Test/Maintain=Loop、跨阶段编排=Graph、收束=DSH。
- [x] **harness 开场先立住（P5）**，Build/Test/Deploy 再展开（第四幕→Build 引子 P20 等）。
- [x] **DSH = 给不同视角/环节定制的可组合 runtime**（registry/adapter/seam/gate/session log），不是结尾一块硬货。
- [ ] 是否需要补组织特有的反面案例（各团队各装一套 harness 的重复建设 / 供应链事故）——playbook 已给 managed settings 的「regulated enterprise」案例，可作起点。

## 呈现层

- [x] **页数与时间**：骨架 **50 页**已定（75–90 min），逐页内容已铺完；第三幕 DSH 已加厚（三条腿 → 10 页）；待逐页 review 后校准。
- [ ] **模板选型（用户明确：风格不限制，按内容找最配合的）**：到 PPT 生产阶段再定，不预设 CLAWTIME。候选方向见 `_asset/README.md`，可加「六阶段 loop 图 + 工件链审计链」为视觉主线。

## 素材与口径

- [x] 六阶段 + 15 play 进货单已产出：`../02_evidence/00-absorption-plan.md`。
- [ ] 信息脉络图（上游 → 加工 → 页面 + 反向索引）待补：`../02_evidence/01-info-flow-map.md`。
- [ ] 引用口径沿用 `-opc` 红线 + 新增「代码不再是瓶颈是 Anthropic 论点、playbook 是 Claude 视角」两条。

## 推敲流程

- [x] 工作区脚手架（README / AGENTS / 目录 / symlink）。
- [x] 故事线 v0.1（harness 单焦点）→ v0.2（全 SDLC）→ v0.3（五层各成一幕）→ **v0.5（SDLC 主轴 + 五层/DSH 引子）**。
- [x] 六阶段 + 15 play 进货单。
- [x] ~46 页页面骨架（`03_outline/00-page-structure.md`）。
- [x] 题目 / slogan 已定（「AI-Native 研发组织：从产品到实施的 SDLC 转型之道」/「代码不再是瓶颈，流程才是」）。
- [x] 信息脉络图（`02_evidence/01-info-flow-map.md`）。
- [x] 46 页逐页内容（`03_outline/01`–`03`）→ **加厚为 50 页（第三幕 DSH 三条腿）**。
- [x] 挖 DSH 素材（digested + FAQ 07/08/09 + plugin ladder/seam maturity）→ 落 `02_evidence/00-absorption-plan.md` §四。
- [ ] 用户 review 页面职责 → 校准页数/时间 → 生产事实稿（`04_drafts/`）→ 选模板（`_asset/`）→ PPTX（`05_output/`）。
