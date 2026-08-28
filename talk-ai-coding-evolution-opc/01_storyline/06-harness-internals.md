# Harness 里头干啥 · 抓要害的讲法

> 这是第二幕的核心讲法。目的：让听众用一句话记住 harness 到底在干什么。
> 源：Böckeler 定义（`../_reference/rawdata_ai-coding-evolution-final/final_v4/03-2026-harness-era.md`）。

## 一句话

**模型给能力，harness 给可靠性。** Harness = 模型之外的一切，它干的事是
**把一个"很强的模型"变成一个"可靠的交付"。**

## 两套控制（Böckeler 的框架）

- **Guides（引导 / 前馈）**：在 agent 行动**前**约束它——"按这个样式写"、"必须过这个 lint"、"只能用这些工具"。
- **Sensors（感知 / 反馈）**：在 agent 行动**后**把结果喂回——"测试挂了"、"用户拒绝了这个 diff"、"exit code 非零"。
- 每套再分两档：
  - **computational（确定性）**：测试 / lint / 类型 / schema——可复现、可审计。
  - **inferential（概率性）**：AI review / LLM-as-judge——不可审计。
- **原则：能交给确定性的，绝不靠概率性的。** 确定性优先，模型判断只做兜底。

## 抓要害：三个动词

harness 里头干的事，归成三个动词：

1. **圈住（bound）** —— 沙箱 + 权限：让它只能碰该碰的文件、连该连的网、做被授权的操作。
   文件系统 + 网络双重隔离（bubblewrap / seatbelt），实测减少 84% 权限提示。
2. **拦住（gate）** —— 工具协议 + 验证门禁：把"对错"变成机器可判的关卡，在错误离源头最近的地方就地拦下。
   授权要点：**authorize at execution, not at generation**（2026 CVE 的教训）。
3. **看清（see）** —— 可观测性 + provenance + CI：trace / metrics / logs 记下每一步
   （工具调用、重试、模型步骤、产出），provenance 记下"产物谁造的、从哪来"，接进 CI 让每次交付可审计。

## 六个构件（落到"装了什么"）

| 构件 | 干什么 | 归到 |
|---|---|---|
| 沙箱 | 文件 + 网络双重隔离 | 圈住 |
| 权限模型 | 什么能做、什么先问；执行时授权 | 圈住 |
| 工具协议 | 模型能调什么工具、怎么执行、结果回哪（MCP） | 拦住 |
| 验证门禁 | 测试 / lint / 类型 / schema，尽量确定性 | 拦住 |
| 可观测性 | trace / metrics / logs 还原 agent 决策 | 看清 |
| provenance + CI | 产物可追溯、交付可审计 | 看清 |

## 为什么这一层最重要（承接第二幕）

- loop / graph 都站在它上面：loop 每次迭代实例化一个 harness；graph 每个 agent 节点跑在自己的 harness 里。
- 三层本质是同一件事：**用反馈 + 确定性约束模型，换可靠结果**——harness 给单次反馈（Sensors），loop 把它连成循环（反馈驱动迭代），graph 把它编排起来（workflow / DAG + 门禁）。
- 2026 安全事件集中爆发在这层——因为"可靠性"就住在这里，风险也住在这里。
