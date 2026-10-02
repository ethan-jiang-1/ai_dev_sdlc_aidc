# 入门场练习讲者卡与判卷指南（Facilitator Guide）

> 本文件供 Keynote 讲者在现场主持练习时使用，包含判分红线、标准参考答案、典型误区剖析与追问引导。

---

## 练习一（工件契约合规性诊断）

### 判分红线
- **必须指出 3 条核心违规**：
  1. **自然语言传话脆弱性**：使用自然语言口头交代意图，无 Schema 强约束，导致下游随意解释（如“看着起一个”）；
  2. **缺失单一事实来源黑板**：私下直接发送消息，交付物未通过全局状态机黑板（Blackboard）登记归档；
  3. **无法通过机器静态校验**：非结构化文本无法被机器校验器拦截，缺失接口契约（Spec JSON）。
- **重构工件要求**：必须给出包含 `task_id`、明确的表结构变动定义（精确到字段名与类型）、以及目标版本的强类型数据。

### 标准参考答案（工件重构）
```json
{
  "$schema": "https://specs.sdlc.ai/v1/task-spec.json",
  "task_id": "task_add_points_field_001",
  "artifact_type": "TaskSpec",
  "target_service": "order_db",
  "schema_migration": {
    "table": "orders",
    "operation": "ADD_COLUMN",
    "column_name": "points_deducted",
    "column_type": "INTEGER",
    "nullable": true,
    "default_value": 0
  },
  "compatibility_guarantee": "FORWARD_COMPATIBLE_V1"
}
```

---

## 练习二（故障自愈层级判断）

### 判分红线
- **指出反模式**：这是典型的**“全量重新生图风暴（Meta Doom Loop）”**，把单点语法小错当成了系统架构故障，抹杀了已有的成果，导致状态剧烈抖动与预算浪费。
- **准确判断自愈层级**：这纯粹属于 **L1 局部微循环（Loop 层）** 职责。
- **标准处理流程**：Worker B 在自己的独立物理沙箱（Git Worktree）内，依据本地编译器语法错误堆栈进行就地退避修改，重试次数严格限制在 Hard Cap ≤ 3 次以内。只要单测退出码为 0 即可通过，整个过程对上层 DAG 与其他节点完全透明，绝不可上升为 L2 拓扑切片，更严禁全图重新规划。

---

## 练习三（HITL 审批门禁设卡）

### 判分红线
学员必须准确选出**三道标准门禁（P0 / P1 / P2）**：
1. **P0 架构方案门禁（Pre-Code Gate）**：
   - 位置：Planner 拆解完 Task DAG 与各任务 TaskSpec 之后、并发拉起 Worker 执行之前；
   - 职责：人类架构师审查子任务拆解的合理性、接口契约的自洽性，防止在大方向错误的方案上盲目消耗算力。
2. **P1 破坏性变更门禁（Destructive Action Gate）**：
   - 位置：任何涉及数据库 Schema 修改（ALTER TABLE/DROP）、核心基础设施配置变更的节点执行前；
   - 职责：DBA 或资深技术专家审查迁移脚本与回滚方案，杜绝误删索引与锁表灾难。
3. **P2 最终集成发布门禁（Release Gate）**：
   - 位置：所有 Worker 绿灯汇聚、并通过全量自动化集成回归测试之后、合并主干并部署前；
   - 职责：版本负责人比对总 Diff 视图与测试安全报告，行使最终上线审批权。
