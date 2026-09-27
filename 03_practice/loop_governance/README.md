# Loop Governance —— loop 层的实践主干

> **定位（2026-09-26 用户定）**：五层框架（Prompt → Context → Harness → **Loop** → Graph）第 4 层的实践主题——
> 治理 **agent 循环的自主度**：停止条件（跑到哪算完）、外层调度（下一轮跑什么/何时跑）、
> 自主度分档（人在哪一站）、检查点（什么时候必须人看）。
>
> **命名理由**：不沿用 KOL 词 "loop engineering"——研究层三路回源判定该词**词源＝热度碎片、外延未收敛**
> （四人核心同指但两处硬分歧），沿用即把热度误当收敛、且即站队。按仓库自己的五层框架命名，
> 与 [`../harness_governance/`](../harness_governance/README.md) **同构成对**：
> **harness 治理管「约束写进环境」（知识/环境轴）；loop 治理管「循环怎么跑、谁决定下一轮、人站在哪」（控制/分配轴）。**
> 命名判定全文：[`../../02_research/ai_loop_engineering/digested/01-命名谱系.md`](../../02_research/ai_loop_engineering/digested/01-命名谱系.md) §四。

## 一句话分界

**门禁是 harness 的传感器；什么时候够格再跑一轮、由谁决定、人站在哪，是 loop 的治理。**

## 目录结构

```text
loop_governance/
├── README.md            # 你在这里：定位 / 命名 / 分工 / 信息流
├── CURRENT.md           # 热区：当前态 / 下一步 / 缺口
└── result/
    ├── README.md        # 入层判据与命名规则
    ├── backbone.md      # ★ 实践主干（§0 定义与判据＋失败模式诊断轴 / §1 停止条件 / §2 外层调度 / §3 自主度阶梯 / §4 检查点与反例 / §5 接口 / §6 升格依据）
    └── manual.md        # ★ 操作规程 12 节（诊断 → 写法 → 选型 → 保护 → 进度规格 → 触发器 → 熔断 → Ralph → 升档 → 验收独立性 → 落地梯子 P0→P4 → 反过度工程）
```

**没有 `research/` 层**：循环机制证据与判读在 [`02_research/ai_loop_engineering/`](../../02_research/ai_loop_engineering/README.md)；goal/eval 如何构造及判据困难的分析在 [`02_research/agent_goal_eval/`](../../02_research/agent_goal_eval/README.md)。本主题只引用各自的控制接口，不复制研究正文或案例数值，防双权威。
引用写法须带主题路径：`ai_loop_engineering/evidence-*` 与 `agent_goal_eval/digested/01/02/03` 不混称；库内一手如 `fable5/run_*/` 的整理者转述句 ≠ 逐字引句（见 backbone §1）。

## 分工边界（与兄弟主题，冲突时以本表为准）

| 主题 | 它管 | 本主题不管 |
|---|---|---|
| [`harness_governance`](../harness_governance/README.md) | 单次运行受控：门禁 / 传感器 / 漂移清理（诊断轴＝agent 缺哪句话 ①–⑦） | ——（本主题的前提层） |
| **本主题** | 多轮的治理：停止条件 / 外层调度 / 自主度分档 / 检查点 | 单次运行内的约束（→harness）；跨 agent 编排（→Graph 层，未立题）；SDD 工件链与工具生态（→spec_driven_development）；intent/spec 写法（→requirements_engineering） |
| [`spec_driven_development`](../spec_driven_development/README.md) | SDD 工具生态与辩论谱系 | ——（与本主题是收敛关系，证据互引） |
| [`agent_goal_eval` 研究主题](../../02_research/agent_goal_eval/README.md) | goal 完成条件与 eval 的构造、校验、设计不出来时的处理 | 本主题只用其判读决定自动续跑、验收、升档或交人，不重写 goal/eval 方法 |

## 核心结论速览（展开在 [`result/backbone.md`](result/backbone.md)）

1. **两个硬判据**：停止条件不依赖上次结果＝重试不是 loop；单次运行不受控＝loop 只是错误复制机。
2. **停止条件三件骨架**（各 ≥2 独立一手）：机器可核判据逐轮闸门 ＋ 硬性熔断上限 ＋ 验收与干活分离。**目标敌人＝提前宣告完成**。
3. **外层调度两种已观察形态**：文件即队列（进度外置、每轮重读并取未完成项）＋触发器即节拍（条件/时间/事件/脚本）；人工逐动作审批在部分公开机制里移向检查点，不能推断真实组织已全面退出。多 feature 的工作行只是待验证补法（见 [`manual §5`](result/manual.md)）。
4. **自主度位置分档成型**（两个独立四级阶梯：Morris 的 outside→in→on→flywheel、Osmani 的 agentic→`/goal`→`/loop`→proactive；＋Anthropic 官方路径），**量化分档未成型**——没有一手源给出"跑几轮必须人看"的判据，这是如实登记的开放缺口。
5. **升档判据**：机械门可信度之外，还要验证动作授权不跨轮泛化、拒绝后审批入口可达且能恢复；裁判与人判冲突时先暂停自动验收和升档。资源停机、产出过闸与外部业务结果分账（见 [`manual §2/§7/§9/§10`](result/manual.md)）。

## 信息流

1. **单向加工**：对应研究主题的 evidence → 该主题 digested → 本主题 result；review 改变主干 → 反向核对并同步对应研究层判读。
2. **result/ 只收过筛结论**（≥2 独立一手或单源标注）；未采纳线索留研究层原位。
3. **过程件不入流**：仓库根 `.tmp-` 纪律。

## 升格依据

三条触发问题（停止条件 / 外层调度 / 自主度分档）的评估结果与证据指针见
[`result/backbone.md`](result/backbone.md) §6 和研究层 README §4——**两条全过、一条半过（量化分档空白如实登记）**。
