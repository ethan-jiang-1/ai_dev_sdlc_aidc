# 维度 02 · 可验证性与证明

> 角色：加权维。形态适用：A+B，**B 子族为本维重心**（见 §形态 B 子族）。判据归族待 checklist-A/B 逐条落。

## 核心问题

Agent 能否自主确认"我改对了"，并产出可供 review 的证据？

## 为什么独立成维

2026-06 后社区共识已从"能跑测试"升维到"proof is the bottleneck"（[AAIF, 2026-09](https://aaif.io/blog/code-is-cheap-proof-is-the-bottleneck)）：生成快于验证，瓶颈迁移到证明。本维因此包含两段：**闭环判定**（改后对错）与**证据产出**（交付物自带可审查材料）。后者是 v1.1 新扩，raw 清单基本没有。

## 边界声明

- 归此维：确定性验证命令文档化、快速子集、测试确定性、外部依赖替身、本地=CI、格式归 CI、flaky 出口、失败信息可行动、集成测试层厚度、**证据产出义务**（handoff 附测试/截图/日志/边界探索）、**评测基建**（T7 的仓库侧落点：评测集、transcript 留存）。
- 归他维：跑不起环境归 03；卡住出不来归 06；"测试钉住约束"的约束本身若来自规格，其漂移归 08。

## 判据族（草案）

1. **闭环命令**：安装/构建/单测/lint 四类齐备且文档化；单函数级入口存在。
2. **确定性**：无网络/时间/随机顺序隐式依赖；flaky 显式标记有出口。
3. **替身**：record-replay / in-memory server / 离线回放存在。
4. **门禁同源**：本地与 CI 同命令同基线；无隐蔽 CI-only 门禁。
5. **测试布局**：镜像源码布局；为 agent 做厚"确定性快的集成层"（契约/replay/compose 类）。
6. **证据产出义务**：交付前自证清单成文（跑过什么、看过什么）；handoff 可回灌（reviewer 能把上下文送回执行循环）。
7. **评测基建**（T7 仓库侧）：agent 行为有评测集或轨迹留存放，改动工具描述/指令时能做对照验证。

## 形态 B 子族（评估分离，v1.2）

正确性机制从断言变为统计评估后，本维重心移到"评估系统本身的质量"：

1. **评估器与生成器分离**：模型自评有系统性乐观偏见（Anthropic 实测：评估 agent 会"识别出问题再说服自己不算严重"）；解法是生成/评估分离（GAN 式架构）+ 评估器**单独调严**。
2. **评估资产独立性**："用 AI 生成的测试验证 AI 生成的代码 = 用同一双眼睛检查作业"（Böckeler）——evals/测试基线须有独立于生成路径的来源或人工锚点。
3. **统计正确性报告**：B 产品交付指标为任务成功率、工具调用正确率等统计量，且须声明可接受阈值（同一分数在不同场景判定不同）。

**成熟度标注：本子族为"探索"级**——"验证 agent 做对了事"是行业级未解问题（共识核对 2026-09）。checklist 落条时不进硬门禁，进观察项，靠试测喂。

## 依据

- raw 05 篇全篇（六原则 + 测试即指令的边界 + 金字塔重排）。
- [AAIF: Code Is Cheap. Proof Is the Bottleneck.](https://aaif.io/blog/code-is-cheap-proof-is-the-bottleneck)（2026-09-08：generation-verification asymmetry、comprehension debt、Amazon 6000+ trajectory 审计）。
- [Datadog: harness-first agents](https://www.datadoghq.com/blog/ai/harness-first-agents/)（observability 闭合验证环）。
- [Anthropic: writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)（验证器不过严、eval-driven）。

## 泛化注意

- 案例锚点一律不进体系（仓库无关纪律）；相关条目以行为描述落 checklist。
- 证据产出义务与评测基建是本维新增判据族，checklist-A/B 补。

## 开放问题

- "证据产出"的可判定标准：清单式成文算 ✅，还是要求模板/工具化？
- 评测基建判据对小仓库是否过重（需规模分档）？
