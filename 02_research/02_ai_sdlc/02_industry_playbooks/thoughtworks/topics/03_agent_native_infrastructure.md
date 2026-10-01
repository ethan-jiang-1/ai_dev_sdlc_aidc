# Deep Research Topic 03: 智能体原生的底层基础设施
(Agent-Native Tech Infrastructure)

## 1. Topic 核心定义
现存软件生态在设计时默认操作者为“人类”，因此在向“智能体全自动化”过渡时遇到了严重的能力短板。企业亟需为真正的“数字员工”构建属于它们的底层技术栈，核心包括：让智能体拥有操作身份、记忆和资源调度的 Agent OS；支撑系统自愈机制的显性化“知识图谱与语义层”；以及更易验证的智能体专属语言。

## 2. 行业宏观与技术商业视角 (Industry & Tech-Business View)
* **基建破局点**：只在应用层做 AI 提效的空间容易触达天花板，真正决定未来十年研发大盘效能优劣的，是企业能否构建一套类似“AI 时代 Kubernetes”的底层自动化编排中枢与智能体运行态。
* **技术演进与实践方向**：企业内部 Agent OS 服务和“工作任务账本”的工程化落地；将系统存量暗知识（老代码和历史维保文档）自动化转化为适用语义大图的平台工程（Platform Engineering）升级。

## 3. 深度的背景与上下文 (Imported Context)
* **智能体操作系统（Agent OS）构想**：必须拥有：身份与权限管理、记忆和上下文窗口、一个类似金融区块链的不可篡改的“工作账本”（记录它当前被授权的技能、预算约束、验收标准）。仅替换模型不足以管理 Agent，其“做了什么”的历史记录才是定义底层 OS 状态的基石。
* **自愈系统的难题与“隐性知识”**：自愈代码变更应是最后手段。大厂的资深老兵在响应故障时依赖大量“心智模式”和“隐性知识（Latent knowledge）”（比如：某服务 CPU 高优先检查连接池）。若要建立自愈智能体，必须先将历史 post-mortems 提取构建为一个企业级的“智能体潜意识”网或语义知识图谱。
* **面向智能体的编程语言**：现有语言倾向于人类的高级表达或认知减负。未来的代码可能是“永不存储的基础产物”或者是通过极端约束、强类型的规范，将逻辑限定在可证明空间之内，这不仅让智能体产出一致，也使人类能更低成本地反向验证。
* **智能体群体协作（Agent Swarms）的幻象与实际**：完美的单体智能体不如一群普通智能体会聚拢重要。但目前大部分“群体协作”其实只是在跑循环数据清洗和 ETL“巡防”的后端孤岛任务，真正的群体编排亟需优质的顶层 API 和任务下发机制架构。

## 4. Deep Research 核心切入点 / Open Questions
1. **真正的 Agent OS “工作账本”级调度器形态会是什么？** 我们是不是可以从 Web3 治理或分布式系统的概念里汲取构建架构安全的核心经验？
2. **“企业数字潜意识”的工程链路**：从死去的遗留代码、Jira Issue 和老旧日志中提纯领域本体模型（Ontology）并在 24 小时内形成大模型认知的有效方式是什么？
3. **“愤怒智能体”范式**：在自修复和容灾系统中，大模型总是过度倾向于同意。如何设计架构来让多组 Agent 进行红蓝对抗，还原真实世界人类救火团队里的“逆耳忠言”动态？

## 5. 历史摘要（保留，不修改）

本文件现有第 1-4 节即为历史摘要，保留原文，不做删改。

## 6. 本轮新增证据

- Anthropic 的 production multi-agent system 证明，长时运行 agent 至少需要 orchestration、memory、artifact persistence 与 resume capability。参考：`_reference/03-agent-native-infrastructure-01-anthropic-multi-agent-research-system.md`
- Anthropic 的 managed agents 文章指出，agent harness 的很多假设会随着模型进步而失效，因此运行时接口必须稳定、可演化。参考：`_reference/03-agent-native-infrastructure-02-anthropic-managed-agents.md`
- Claude Agent SDK 文章表明，file system、搜索、外部工具和上下文更新机制本身就是 agent runtime substrate 的一部分。参考：`_reference/03-agent-native-infrastructure-03-anthropic-agent-sdk.md`
- A2A 作为 agent-to-agent 开放协议，明确把 capability discovery、long-running task collaboration、streaming 和 secure interoperability 拉到协议层。参考：`_reference/03-agent-native-infrastructure-04-a2a-protocol.md`
- AutoGen 把多智能体协作定义成一种可编程的 conversation infrastructure，而不只是“并行调用多个模型”。参考：`_reference/03-agent-native-infrastructure-05-autogen-multi-agent-framework.md`
- MemGPT 明确把 LLM memory 管理上升为类似操作系统的分层内存问题。参考：`_reference/03-agent-native-infrastructure-06-memgpt-virtual-context-management.md`
- GraphRAG 论文与 Microsoft Research blog 都表明，面对 private corpus 的 global reasoning，entity graph 与 community summaries 比 baseline RAG 更适合作为企业知识层。参考：`_reference/03-agent-native-infrastructure-07-graphrag-paper.md`, `_reference/03-agent-native-infrastructure-08-graphrag-microsoft-blog.md`
- OpenTelemetry 已开始把 agent spans、GenAI metrics、MCP prompt/tool/RPC 标准化，这说明 observability 正从 ad hoc logging 走向基础设施层。参考：`_reference/03-agent-native-infrastructure-09-opentelemetry-genai-semconv.md`, `_reference/03-agent-native-infrastructure-10-opentelemetry-mcp-semconv.md`
- Temporal 的 Event History、LangGraph 的 checkpoints、OpenAI Agents SDK 的 resumable state/traces、Inngest 的 durable step state 共同说明：所谓“工作账本”已经可以被拆成一组可实现 primitives，而不是纯概念。参考：`_reference/03-agent-native-infrastructure-11-temporal-event-history.md`, `_reference/03-agent-native-infrastructure-12-langgraph-persistence-checkpoints.md`, `_reference/03-agent-native-infrastructure-13-openai-agents-results-state.md`, `_reference/03-agent-native-infrastructure-14-openai-agents-tracing-observability.md`, `_reference/03-agent-native-infrastructure-15-inngest-durable-execution.md`

## 7. 本轮新增机制理解

- Agent OS 的最小现实形态并不是“一个超级模型服务”，而是由 `runtime orchestration + external memory + tool/agent protocols + knowledge substrate + observability` 组成的分层系统。
- 多智能体系统的关键不在“agent 数量”，而在 orchestration contract 是否清晰：谁分解任务、谁持有计划、谁写 artifact、谁恢复失败。
- 企业数字潜意识如果要成立，必须把 latent knowledge 转成图结构、摘要层或可追溯 artifact，而不能只把所有内容堆进向量库。
- 可观测性不是后续补件；如果没有统一 span、prompt、tool、RPC 语义，长时运行 agent 几乎无法调试、审计和优化。
- `work ledger` 最现实的工程分解目前看起来像是三层拼合：`durable execution record`、`checkpoint or step state`、`observability and interruption boundary`。它还没有统一成单一产品，但已经不再只是模糊想象。
- 如果未来要把权限、预算、技能与验收标准并入工作账本，最自然的落点不是 prompt 内存，而是挂接在这些 durable records 之上的 control metadata。

## 8. 本轮新增趋势与难点

- 趋势：agent runtime 会越来越强调 `stable interface, swappable harness`，而不是把模型能力和运行时策略硬编码死。参考：`_reference/03-agent-native-infrastructure-02-anthropic-managed-agents.md`
- 趋势：enterprise agent stack 很可能形成 `MCP for tools / A2A for agents / OTel for observability` 这样的多协议分层。参考：`_reference/03-agent-native-infrastructure-04-a2a-protocol.md`, `_reference/03-agent-native-infrastructure-10-opentelemetry-mcp-semconv.md`
- 趋势：graph substrate 会越来越多地承担 private data reasoning 与 provenance 责任。参考：`_reference/03-agent-native-infrastructure-07-graphrag-paper.md`, `_reference/03-agent-native-infrastructure-08-graphrag-microsoft-blog.md`
- 趋势：agent runtime 会逐渐把 event history、checkpoint state、interrupt boundary 和 traces 从框架内部细节升级为显式平台能力。参考：`_reference/03-agent-native-infrastructure-11-temporal-event-history.md`, `_reference/03-agent-native-infrastructure-12-langgraph-persistence-checkpoints.md`, `_reference/03-agent-native-infrastructure-13-openai-agents-results-state.md`, `_reference/03-agent-native-infrastructure-15-inngest-durable-execution.md`
- 难点：公开材料里虽然已经能拼出 `work ledger primitives`，但仍缺一个真正成熟的统一范式，把权限、预算、能力、历史操作与验收标准合成一个 enterprise-grade ledger。参考：`_reference/03-agent-native-infrastructure-11-temporal-event-history.md`, `_reference/03-agent-native-infrastructure-12-langgraph-persistence-checkpoints.md`, `_reference/03-agent-native-infrastructure-14-openai-agents-tracing-observability.md`
- 难点：multi-agent orchestration 在 research 类任务里很强，但在 coding 类任务里何时值得上、何时会过度复杂，公开证据仍有限。参考：`_reference/03-agent-native-infrastructure-01-anthropic-multi-agent-research-system.md`, `_artifacts/W1-03-agent-native-infrastructure-question-list.md`

## 9. 当前判断（本轮综合后）

- 当前最可信的判断不是“企业需要更多 AI 中台”，而是“企业需要可持续运行 agent 的系统软件层”，其中 memory、protocol、artifact persistence 和 observability 都是硬组成。参考：`_reference/03-agent-native-infrastructure-01-anthropic-multi-agent-research-system.md`, `_reference/03-agent-native-infrastructure-03-anthropic-agent-sdk.md`, `_reference/03-agent-native-infrastructure-09-opentelemetry-genai-semconv.md`
- Agent OS 概念是成立的，但目前公开证据更支持“分层组合栈”而不是“单一产品形态”。参考：`_reference/03-agent-native-infrastructure-02-anthropic-managed-agents.md`, `_reference/03-agent-native-infrastructure-04-a2a-protocol.md`, `_reference/03-agent-native-infrastructure-06-memgpt-virtual-context-management.md`
- 企业数字潜意识最现实的路径不是神秘长期记忆，而是 `private corpus -> graph/summary substrate -> provenance-backed retrieval`。参考：`_reference/03-agent-native-infrastructure-07-graphrag-paper.md`, `_reference/03-agent-native-infrastructure-08-graphrag-microsoft-blog.md`
- 未来可验证的 agent-native 基建很可能同时依赖三个层次的标准化：连接工具、连接 agent、连接 telemetry。参考：`_reference/00-shared-06-model-context-protocol-spec-2025-11-25.md`, `_reference/03-agent-native-infrastructure-04-a2a-protocol.md`, `_reference/03-agent-native-infrastructure-10-opentelemetry-mcp-semconv.md`
- 当前最有价值的新判断是：`work ledger` 作为 enterprise recommendation 已经有足够多的 primitives 可被正式讨论，但它应被定义成统一控制面之上的复合记录系统，而不是单一日志表或单一 memory store。参考：`_reference/03-agent-native-infrastructure-11-temporal-event-history.md`, `_reference/03-agent-native-infrastructure-12-langgraph-persistence-checkpoints.md`, `_reference/03-agent-native-infrastructure-13-openai-agents-results-state.md`, `_reference/03-agent-native-infrastructure-14-openai-agents-tracing-observability.md`, `_reference/03-agent-native-infrastructure-15-inngest-durable-execution.md`
