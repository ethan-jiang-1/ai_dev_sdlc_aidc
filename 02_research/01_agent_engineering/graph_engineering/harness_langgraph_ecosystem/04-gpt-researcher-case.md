# 04 · 生产实战标杆: GPT Researcher v3 的动态 Map-Reduce DAG

> **摘要**：解剖基于 LangGraph 重构的开源深度研究标杆——**GPT Researcher (v3)**。深入分析其如何通过 LangGraph 的 Plan-and-Execute 模式与 `Send()` API，在未知并发度下实现多智能体动态分解、并行 Map 检索与 Fan-in 聚合，为严肃工程系统提供标杆样本。

---

## 1. 业务场景的工程挑战

在严肃的深度研究与跨文件分析场景中，系统面临典型的“动态拓扑”挑战：
- **子任务数量未知**：面对“分析 2026 年欧洲碳中和政策对汽车制造业的供应链冲击”这一 Prompt，系统在静态编译时根本无法预测需要拆分成 3 个、5 个还是 12 个子研究方向；
- **各方向独立检索**：不同子课题的 Web 检索和文档分析必须高度并发，不能单线程串行等待；
- **多源数据汇聚与交叉检验**：所有并发子代理产出的结论必须汇总到总编（Editor）节点，经过质量门禁审查，若有缺失则动态补充分支。

---

## 2. GPT Researcher 的 LangGraph 拓扑实现

GPT Researcher 没有采用混乱的多 Agent 自由聊天群，而是通过 LangGraph 构建了一个**高度确定性的动态 Map-Reduce 图**：

```
[START]
   │
   ▼
[Chief Planner (总编规划)] ──(动态输出 N 个子课题大纲)──┐
   │                                                 │
   ▼                                                 ▼
[Human Review (可选 HITL 大纲核准)]               [Send API 动态分发]
   │                                                 │
   └──────────────────────────┬──────────────────────┘
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
     [Sub-Researcher 1] [Sub-Researcher 2] ... [Sub-Researcher N]
             │                │                │
             └────────────────┼────────────────┘
                              │ (Fan-in 汇聚)
                              ▼
                   [Fact Checker (事实复核)]
                              │
                              ▼
                   [Publisher (终稿成书)]
                              │
                              ▼
                            [END]
```

### 2.1 动态扇出（Dynamic Fan-out）源码机理
总编规划节点解析用户意图后，动态生成子课题列表，并在条件路由中返回 `Send` 对象列表：

```python
def route_to_subresearchers(state: ResearchState):
    # 如果处于人工核准模式且尚未批准，停在人工节点
    if state.get("requires_approval") and not state.get("approved"):
        return "human_feedback_node"
    
    # 动态产生 N 个 Send 指令（N 随 Prompt 动态变化）
    subtopics = state.get("subtopics", [])
    return [
        Send("sub_researcher_node", {
            "topic": subtopic.title,
            "queries": subtopic.search_queries,
            "parent_id": state["research_id"]
        })
        for subtopic in subtopics
    ]
```

### 2.2 状态归集与 Reducer 机制
在 `ResearchState` 中，子研究员返回的产物通过带 `operator.add` 或去重合并函数的 Channel 收集：
```python
class ResearchState(TypedDict):
    research_id: str
    main_topic: str
    subtopics: List[SubTopic]
    # 使用 Annotated 配合自定义 reducer，实现多分支并发写回时不冲突
    collected_sections: Annotated[List[SectionReport], merge_sections_reducer]
    visited_urls: Annotated[Set[str], operator.or_]
```

---

## 3. 生产级工程教训

从 GPT Researcher 的 LangGraph 落地中，可以沉淀三项核心工程经验：

1. **避免在 Worker 内部相互通讯**：
   子研究员之间绝对禁止互相聊天或跨节点传递信息。每个子研究员是纯净的无状态算子（Stateless Operator），仅对分配给自己的 `subtopic` 负责，输出强类型报告。这从根本上杜绝了多 Agent 通信死循环；
2. **容错信封隔离**：
   如果 N 个并发子研究员中只有 1 个因网络超时报错，LangGraph 的 Checkpointer 允许捕获该分支异常并记录错误信封，不会让整个研究流程抛出未捕获异常而前功尽弃；
3. **关键节点设立 HITL 门禁**：
   在耗费大量 Token 并发拉起 10 个子 Agent 之前，系统支持调用 `interrupt()` 原语暂停执行，将大纲推送到前端让用户勾选删除不需要的子方向，确认后再一键 Resume。

---

## 4. 总结与启示

GPT Researcher 证明了：**完全基于 LangGraph 原生的静态编译元图 + `Send()` 动态并发原语，足以构建工业级、高吞吐、强容错的 Dynamic Workflow 系统。** 这为企业级 Coding Harness 的动态多模块重构提供了极佳的范式参考。
