# 当前状态（热区）

> 最近一次更新：**2026-10-02（第二轮精修打磨）**：针对生产环境脏活硬仗补强五大机制——① 双形态拓扑治理光谱（显式 DAG vs 动态委派树）；② 工件语义版本（`@v1/@v2`）与级联失效传播（反幽灵读取）；③ 汇聚代码冲突解决器（Merge Conflict Resolver SOP）；④ 图级经济与 Token 硬配额（双硬上限）；⑤ 节点级最小特权（Node RBAC & Sandboxing）矩阵。

## 一句话

**立题初稿与工业级打磨全面收口**：建立拓扑双轨骨架、双形态拓扑光谱、Session 外持久化状态机、强类型工件版本契约、两层自愈与汇聚冲突协议、模型病态防御与节点 RBAC 的工业级实践规程（`backbone.md` 与 `manual.md` 均就绪，待用户复核）。

## 状态

| 件 | 状态 | 说明 |
|---|---|---|
| `README.md` | ✅ 已落盘 | 定位 / 命名理由（三维治理闭环） / 分工边界 / 核心主张速览 |
| `result/README.md` | ✅ 已落盘 | 实践入层判据与命名规则 |
| `result/backbone.md` | ✅ 已落盘 | §0–§7 实践主干（拓扑双轨骨架、状态机分层、工件契约、两层自愈协议、模型病态防御、HITL 门禁、接口分工） |
| `result/manual.md` | ✅ 已落盘 | §0–§7 操作规程（病征自检、运行时选型、Schema 规范、子图切片突变 SOP、配额隔离、防御实施、落地梯子 P0-P3、反过度工程） |
| 证据层支撑 | ✅ 充足 | 机制来自 [`graph_engineering`](../../02_research/01_agent_engineering/graph_engineering/README.md)；生态来自 `harness_langgraph_ecosystem/` 与 `harness_frontier_systems/` |

## 下一步

1. 待用户复核 `result/backbone.md` 与 `result/manual.md` 内容细节；
2. 保持与上游研究层及下游演练的指针一致性；
3. 跟踪业界关于动态拓扑自愈算法与跨仓一致性的最新进展并持续补强。

## 缺口与开放挑战

1. **动态子图切片的泛化边界**：目前工业界有成熟支持的仅为三大原子突变（前置补丁注入、任务细分降级、检查点回滚）；更复杂的拓扑动态变异（如运行时并发度动态重组）仍缺乏标准化实现。
2. **异构模型通信配额的动态自适应**：目前主要依赖硬阈值（如 Chatter Throttling 和单节点 Token Cap），动态根据上下文负载自适应调整配额的策略尚未完全收敛。
3. **跨多仓库/多服务工作流的分布式协调**：多数实践集中在单代码库（Monorepo 或 Single Repo）内多模块场景，跨企业多微服务 Git 仓的分布式 DAG 事务一致性是一线留待攻克的开放难题。

## 铁律速记

- **证据权威在对应研究主题**：拓扑机制与论辩证据来自 [`graph_engineering`](../../02_research/01_agent_engineering/graph_engineering/README.md)；单节点循环机制看 [`loop_governance`](../loop_governance/README.md)；沙箱环境看 [`harness_governance`](../harness_governance/README.md)。
- **坚决消灭伪 Multi-Agent 群聊**：严禁在实践主干中出现让大模型通过自然语言互相自由聊天的方案，节点间只允许强类型工件通信。
- **元图静态编译，动态留给数据**：严禁在生产执行阶段让大模型现场生成并重新编译代码级图拓扑。
- **本层状态不记下游**：本文件只记实践层事实，下游 deck 或演说稿进度由下游独立维护。
