# 已决与待办（v0.7 · 软件 SDLC 定调）

## 已决（当前态）

- [x] **对象收紧为软件 SDLC 上的跨职能研发与交付组织**：从产品意图、需求与设计，到 Build / Test / Deploy / Maintain；不泛化为一般「AI 组织」。
- [x] **目录更名**：`talk-ai-coding-evolution-org/` → `talk-ai-coding-evolution-org-sdlc/`，为今后其他组织类型保留平行拆分空间。
- [x] **篇幅档位 = A**：单场加长 Keynote，75–90 min，**50 页已定**。
- [x] **独立成篇**：不依赖、不承接 `04_output/deck_ai_sdlc_keynote`（听众不同）。
- [x] **范围红线**：不讨论销售、市场、客服、财务、人力或一般企业组织设计。
- [x] 两轴合成：宽轴（六阶段 SDLC）+ 深轴（五层 + Harness）；harness 为整条链提供共享控制基线，领域知识与判断仍由对应 owner 承担。

## 主题层（已定 v0.7）

- [x] **题目已定**：AI-Native 软件研发组织：从产品意图到生产运维的 SDLC 转型之道。
- [x] **slogan 已定**：代码不再是瓶颈，流程才是。
- [x] **中心命题已收紧**：工件可交接、gate 可执行、owner 可问责、feedback 可回流。
- [x] **slogan 口径**：「代码不再是瓶颈」是 Anthropic 观点与诊断假设，不是对每个组织的先验事实。

## 结构层（已定 v0.7）

- [x] **SDLC 六阶段是主轴**（Plan→Design→Build→Test→Deploy→Maintain），第二幕占 26 页。
- [x] **五层 + DSH 不强扭成独立章节**：五层作「外置与控制深度」镜头，不声称某个 SDLC 阶段的「本质」就是某一层；DSH 作参考实现。
- [x] **harness 开场先立住（P5）**，再在 Build / Test / Deploy 展开（P20 / P26 / P30）。
- [x] **DSH = 共享 harness 控制面的参考实现**（registry/adapter/seam/gate/session log），不是唯一选型。
- [x] **六阶段统一四问**：每阶段都回答工件 / gate / owner / feedback。
- [x] **五层只作能力与控制深度镜头**：不等于五个岗位、团队或组织层级；不与六阶段作一对一等式。
- [x] **反面案例不作为内容锁前置条件**：核心机制已经成立。若以后加入具体供应链或安全事件，必须先建独立证据卡片；当前 P30 保持机制表述。

## 呈现层

- [x] **页数与时间**：骨架 **50 页**已定（75–90 min），REVIEW 只在 50 页内调整职责、取舍与转场。
- [x] **内容锁通过**：用户确认继续往前推进，固定 P1–P50 页面职责进入生产。
- [x] **视觉方向**：系统蓝图式技术编辑风；浅色系统底座 + 少量高对比转折页 + 统一 SDLC / 工件链 / 控制面视觉语法。详见 `_asset/README.md`。
- [x] **制作路线**：自定义母版与布局系统，不使用 `-opc` CLAWTIME，不套现成模板，不混用 Codex Grid。
- [ ] 将 50 页内容压成 audience-facing 生产事实稿，控制上屏密度与 speaker notes 分工。
- [ ] 建立布局族、颜色与符号 token，再进入 PPTX 生产。

## 素材与口径

- [x] 六阶段 + 15 play 进货单已产出：`../02_evidence/00-absorption-plan.md`。
- [x] 信息脉络图已按 v0.7 校准：`../02_evidence/01-info-flow-map.md`，可从来源追到 P1–P50，也可从页面反查主张。
- [x] 引用口径已增加「代码不再是瓶颈是 Anthropic 论点、playbook 是 Claude 视角」。
- [x] P2 的听众自证方法已进入 `../02_evidence/02-claim-ledger.md` C1：coding time 占比 + queue / first review / approval / deployment / rework / failure 指标。
- [x] 「工件链承担审计的条件」已进入 `../02_evidence/02-claim-ledger.md` C3，明确区分来源事实与本 talk 综合判断。

## 推敲流程

- [x] 工作区脚手架（README / AGENTS / 目录 / symlink）。
- [x] 故事线 v0.1（harness 单焦点）→ v0.2（全 SDLC）→ v0.3（五层各成一幕）→ v0.5（SDLC 主轴 + 引子）→ v0.6（四问贯穿）→ **v0.7（软件 SDLC 范围收紧）**。
- [x] 六阶段 + 15 play 进货单。
- [x] 50 页页面骨架（`03_outline/00-page-structure.md`）。
- [x] 题目 / slogan 已定（「AI-Native 软件研发组织：从产品意图到生产运维的 SDLC 转型之道」/「代码不再是瓶颈，流程才是」）。
- [x] 信息脉络图（`02_evidence/01-info-flow-map.md`）。
- [x] 46 页逐页内容（`03_outline/01`–`03`）→ **加厚为 50 页（第三幕 DSH 三条腿）**。
- [x] 挖 DSH 素材（digested + FAQ 07/08/09 + plugin ladder/seam maturity）→ 落 `02_evidence/00-absorption-plan.md` §四。
- [x] 完成 v0.7 跨文件一致性校准：目录名、软件 SDLC 范围、五层读法、共享控制面边界、证据口径、50 页结构一致。
- [x] 5–8 分钟口述主线已落入 `00-storyline-map.md`，可从诊断自然走到试点行动。
- [x] 用户已确认 P1–P50 内容锁，进入 v0.8 表现设计。
- [ ] 当前下一步：生产事实稿（`04_drafts/`）→ 布局系统（`_asset/`）→ PPTX（`05_output/`）。
