---
type: evidence_archive
collected_by: 委派回源子代理（AE 路 · T4 反馈路径问题：人的变更与在途处置）
collected_at: 2026-10-04
serves: 新判读与变更走读（主代理撰写）——人改目标/判据/授权后，旧证据与在途 worker 如何处置；拒绝后是否可达恢复
status: 受限回源：本轮直连抓取全部被会话网络沙箱拦截（详见 §1）；已归档证据只放指针不复制正文；未取得的新机制一律登记「未见/待核」，不造机制
quality_bar: P-existence / P-mechanism / P-outcome 分列；文档逐字（固定 commit）＞转引概述；本轮新增逐字＝0，全部增量是访问失败登记、指针复用与未见登记
---

# Evidence AE：人的变更与在途处置（T4 · 反馈路径问题）

- 观测日期：2026-10-04
- 研究问题：人改了目标/判据/授权之后，旧证据与在途 worker 如何处置；拒绝之后是否可达恢复。
  拆成四个可核子问：
  - **Q1 挂起真实性**：interrupt/审批挂起时，worker 是否真停？
  - **Q2 恢复起点**：Command resume 从哪个状态开始？旧证据（中断前的工具结果）在恢复后是否还在输入里？
  - **Q3 拒绝/编辑回传**：reject 与 edit 分别如何回传给 agent？拒绝后 agent 拿到什么信息？新的一次批准如何与旧授权区分？
  - **Q4 在途副作用**：已启动未完成的动作（in-flight），文档有没有处置表述？
- 拟回源主页面：https://docs.langchain.com/oss/python/langchain/human-in-the-loop （LangChain 官方 HITL 文档）

---

## 1. 访问失败登记（待核，本轮最重要的负结果）

2026-10-04 本会话内对所有目标主机做直连抓取，**全部被网络沙箱以同一类错误拒绝**（域名解析被判定为非公网 IP，非页面 404/超时）：

| 尝试 URL | 用途 | 结果 |
|---|---|---|
| `https://docs.langchain.com/oss/python/langchain/human-in-the-loop` | 指定主页面 | 拦截：「URL hostname "docs.langchain.com" resolves to a non-public IP address」 |
| `https://raw.githubusercontent.com/langchain-ai/docs/main/src/oss/langchain/human-in-the-loop.mdx` | 同文档仓库 main 分支最新版 | 拦截：「raw.githubusercontent.com resolves to a non-public IP address」 |
| `https://api.github.com/repos/langchain-ai/docs/commits?path=src/oss/langchain/human-in-the-loop.mdx` | 查该文档页的 commit/版本号锚 | 拦截：「api.github.com resolves to a non-public IP address」 |

- **搜索通道可用但拿不到逐字**：`web_search` 在 2026-10-04 只返回来源 URL 列表，未返回页面摘要或逐字片段。
- **由此确立本档证据边界**：
  - 2026-10-04 **未能取得** LangChain HITL 文档当前版本的任何新逐字引句；
  - 文档 commit 锚**维持** evidence-f 归档的 `933a2f9217f6293a54fa59d40ce69b619aaa1172`（观测 2026-09-27）；
  - 2026-10-04 当日该页是否有 commit/版本号变化：**未能观测，待核**；
  - Q2（恢复起点/旧证据存留）与 Q3 后半（新批准与旧授权的区分）在已归档引句内**没有答案**，本轮又无法补抓——按纪律如实登记「未见」，等网络放开后回源。
- **搜索结果列表本身的可用信息**（仅证明相关页面存在，不构成机制证据，P-existence·弱）：
  - 存在 markdown 直出变体 `docs.langchain.com/oss/python/langchain/human-in-the-loop.md` 与 JavaScript 版同题页；
  - 存在 [LangGraph Interrupts](https://docs.langchain.com/oss/javascript/langgraph/interrupts) 与 [use-time-travel](https://docs.langchain.com/oss/python/langgraph/use-time-travel) 两个相邻官方页——提示 interrupt 与 time-travel 在 LangGraph 文档中是分开两页讲的，**时间旅行（回滚到中断前）与 HITL 恢复的关系需要回源这两页**；
  - 搜索列表出现 `langchain-ai/langgraph` PR #7498「fix: time travel when going back to interrupt node」（作者 sydney-runkle）——**标题级线索**：提示「time-travel 回退到 interrupt 节点」是一个出过 bug/需要专门修的工程交互点。逐字、状态、合并与否均未核，待核，不作为机制主张。

---

## 2. 已归档证据指针复用（唯一 home 在原档案，本节不复制正文）

### 2.1 主指针：evidence-f Source 7（LangChain HITL middleware，固定 commit）

唯一 home：[`raw/evidence-2026-09-27-f-autonomy-gates.md` Source 7](evidence-2026-09-27-f-autonomy-gates.md)。
URL（文档固定 commit）：https://raw.githubusercontent.com/langchain-ai/docs/933a2f9217f6293a54fa59d40ce69b619aaa1172/src/oss/langchain/human-in-the-loop.mdx ；页面入口：https://docs.langchain.com/oss/python/langchain/human-in-the-loop ；文档 commit `933a2f9217f6293a54fa59d40ce69b619aaa1172`；该处观测日期 2026-09-27。

该档案已归档的逐字引句与本档四个子问的对应关系（**逐字见原档案，此处只记「能答什么/不能答什么」**）：

| 子问 | 原档案已归档引句能回答的 | 不能回答的（本档登记） |
|---|---|---|
| Q1 挂起真实性 | 「middleware issues an `interrupt` that halts execution and wait[s] for a decision」——**文档层**宣称执行 halt 并等待决定；挂起点在 after_model hook、即模型产出之后、工具执行之前 | 「halts execution」是**图执行语义**，不含进程/worker 级语义（进程是否存活、是否只是暂停消费）——文档未表述，**未见** |
| Q2 恢复起点 | 「The graph state is saved using LangGraph's persistence layer, so execution can pause safely and resume later」＋「You must provide a checkpointer to persist the graph state across interrupts」——恢复依赖 checkpointer 持久化的 graph state | **恢复从哪个 checkpoint 状态开始、中断前的工具结果是否仍在恢复后的输入里**——已归档引句无此逐字，**未见**；需回源 LangGraph persistence / interrupts / time-travel 页 |
| Q3 回传 | 「the action can be approved as-is (`approve`), modified before running (`edit`), or rejected with feedback (`reject`)」——reject 携带 feedback、edit 是执行前修改参数 | **拒绝后 agent 精确拿到什么**（回传的消息形态：tool message 内容？是否强制回到 model 重新规划？）——原档案判读行「拒绝反馈回对话」是**档案判读不是逐字**，**未见**逐字；新的一次批准与旧授权如何区分，**未见** |
| Q4 在途副作用 | 已归档引句**无**任何在途动作处置表述 | LangChain HITL 文档对 in-flight 副作用：**未见**（含本轮，仍未见） |

补充（同属 evidence-f 已归档内容的判读行，供变更走读用）：原档案 Source 7 判读提到文档警告「大幅修改参数可能导致模型重新规划、多次执行或意外动作」——这是 **edit 传播风险**的唯一已归档表述，说明「改了再跑」并非把人的编辑当作无条件生效的授权，而是把修改后的参数重新送回 agent 流程；其精确语义同样**待逐字复核**（该行在原档案标注为判读，非逐字）。

### 2.2 辅助指针一：interrupt 的时机主张（evidence-i Source 2，Dex Horthy）

唯一 home：[`raw/evidence-2026-09-27-i-high-influence-control.md` Source 2](evidence-2026-09-27-i-high-influence-control.md)（观测 2026-09-27）。
已归档逐字：「we need to be able to interrupt a working agent and resume later, ESPECIALLY **between the moment of tool selection and the moment of tool invocation**」。
用途：与 evidence-f 的 after_model 挂起点**互相印证**——可恢复的挂起窗口在「工具已选定、未执行」之间。这正是「人的变更还能不能赶上」的关键窗口：变更（edit/reject）若发生在此窗口内，动作尚未产生副作用。这是**实践者主张 + 官方文档机制**两个独立来源的汇合点，但仍是文档/主张级，不是运行观测（P-mechanism 级，非 P-outcome）。

### 2.3 辅助指针二：在途工作的处置表述——另一机构的对照（evidence-w W6，Anthropic Managed Agents）

唯一 home：[`raw/evidence-2026-09-30-w-ladder-runtime-detail.md` W6 机制卡](evidence-2026-09-30-w-ladder-runtime-detail.md)（观测 2026-09-30）。
已归档逐字（Anthropic 官方文档）：「The request in flight when the cap is crossed still finishes, so the final list cost can land a fraction past the budget.」；机制卡动作行：「在途请求完成；随后暂停；只接受 `user.tool_confirmation`、`user.tool_result`、`user.custom_tool_result`、`user.interrupt` 等结算在途工作的事件」。
用途：**LangChain HITL 已归档引句对 Q4 未见表述，但本主题另一机构（Anthropic Managed Agents）有明确的在途结算语义**：在途请求不被打断、跑完后才挂起，且暂停态只接受「结算在途工作」类事件。这是 Q4 的**互补对照**：说明「在途动作如何处置」在公开产品机制中是可被文档化的设计点（打不打断、暂停后接受哪些事件），不能因为 LangChain 文档没写就断言行业无此概念。**注意机构边界**：这是 Managed Agents 的 budget/事件机制，不是 LangChain HITL middleware，不能互相套用。

### 2.4 辅助指针三：取消传播三面核查与授权绑定（rung-03 + evidence-f 判据候选）

- LE3 的取消三面核查（核调度器、worker、副作用三处都停）：唯一 home：[`capability_ladder/rung-03-time-event-driven.md`](../capability_ladder/rung-03-time-event-driven.md) §一与 §二⑩（孤儿自动化 issue「the kill did not propagate to the actual tmux sessions」）。本档用途：T4 的「人改了授权后在途 worker 怎么办」与「人取消后 worker 停没停」是同一族问题——rung-03 已证明「控制面收到指令」≠「worker 实际停止」，这是变更走读必须继承的核查面。
- 授权作用域（动作×目标×有效期，授权不可从历史模糊继承）：唯一 home：evidence-f 判据候选 3「授权作用域门」与 Source 4（Claude issue #95749「Authorization for one push must not become standing authorization for later pushes」）。本档用途：**旧授权与新批准的区分**（Q3 后半）在已有证据里只有「应当区分」的设计主张与反例，**没有任何产品公开「区分机制」的文档表述**——维持 evidence-f 的空白登记，本轮未找到新材料。

### 2.5 跨主题指针（转引级，非本主题 home，仅作线索）

[`02_research/02_ai_sdlc/02_industry_playbooks/thoughtworks/topics/_reference/03-agent-native-infrastructure-12-langgraph-persistence-checkpoints.md`](../../../02_ai_sdlc/02_industry_playbooks/thoughtworks/topics/_reference/03-agent-native-infrastructure-12-langgraph-persistence-checkpoints.md)（LangGraph persistence 官方文档**转引概述**，accessed 2026-04-17）：该转引记录 LangGraph persistence「explicitly linked to human-in-the-loop workflows, conversational memory, time-travel debugging, and fault-tolerant execution」，并注明「docs do not define a unified schema for authorization, budget, capability contracts, or acceptance criteria」。
- 用途：为 Q2 的「time-travel/回滚」分支提供**存在性线索**（官方文档把 HITL 与 time-travel 并列为 persistence 用例）。
- 强度：**转引概述，非逐字，且 home 在另一研究主题**——按本主题纪律标「转引·待回源」，不作主张依据；待回源目标页：https://docs.langchain.com/oss/python/langgraph/persistence 、`/use-time-travel`、`/langgraph/interrupts`。

---

## 3. 与已有档案的对照登记

| 类型 | 内容 |
|---|---|
| **一致** | 挂起窗口在「工具选定之后、执行之前」：evidence-f Source 7 的 after_model hook 逐字与 evidence-i Source 2 的 Horthy 主张独立汇合；本档未发现任何相反表述 |
| **冲突** | **未发现**。本档没有新材料（直连全被拦截），构不成冲突；唯一需要将来注意的潜在张力点已登记为待核：LangGraph PR #7498 标题提示 time-travel 回退到 interrupt 节点曾有专门修复——若实核成立，说明「回滚+恢复」组合并非平凡操作，届时应核对 evidence-f「pause safely and resume later」的表述边界，而不是预先改写它 |
| **互补** | Q4 在途处置：LangChain HITL 文档**未见**表述，但 evidence-w W6（Anthropic Managed Agents）提供了完整的在途结算语义（在途跑完→挂起→只接受结算类事件）；两者合并说明「在途动作处置」是公开机制中真实存在的设计维度，且**不同产品处置不同**——变更走读不能假设统一行为 |

---

## 4. 未见与待核总清单（本档核心产出之一）

**未见（已按可达材料核实其缺席）**：
1. 挂起时 worker/进程级的真实停机语义（已归档引句只有「halts execution」图执行层表述）——LangChain HITL 文档已归档部分未见。
2. Command resume 的恢复起点、以及中断前工具结果在恢复后是否仍在输入——已归档引句未见。
3. 拒绝后 agent 收到的精确信息形态（消息类型/内容/是否强制重新规划）——已归档引句未见，原档案相关句是判读不是逐字。
4. 新批准与旧授权的区分机制——本主题全部已归档材料均未见（维持 evidence-f 空白登记）。
5. 在途副作用处置——LangChain HITL 文档未见（Anthropic Managed Agents 有，见 §2.3，属另一机构另一机制）。

**待核（本轮无法取得，须网络放开后回源）**：
1. https://docs.langchain.com/oss/python/langchain/human-in-the-loop 当前版本全文逐字（含本档 Q1–Q4 四问）＋当日 commit/版本号锚。
2. LangGraph 三页：`/oss/python/langgraph/persistence`（HITL×time-travel 并列用例的逐字）、`/oss/python/langgraph/use-time-travel`（回滚后旧证据存留）、`/oss/python/langgraph/interrupts`（resume 状态起点）。
3. langgraph PR #7498「fix: time travel when going back to interrupt node」的逐字、状态与合并情况。
4. `interrupt`/`Command(resume=...)` 的 API reference（`reference.langchain.com`，搜索列表显示存在 humanInTheLoopMiddleware 条目）中 resume 参数语义与 reject/edit 的回传类型定义。

---

## 5. 对 plan 完成条件的材料齐备度评估（供主代理判断，非本档判定）

条件原文：「一个版本走读＋取消/恢复真实机制；旧版只作历史不默默覆写当前控制状态」。

- **取消/恢复真实机制**：**半齐**。恢复的持久化前提（checkpointer/thread）有一手逐字（evidence-f Source 7）；挂起窗口有两个独立来源汇合（§2.1/§2.2）；但「resume 从哪个状态开始、旧证据是否留存」**缺一手逐字**——正是走读需要的那一环。材料缺口明确、回源目标页明确（§4 待核 1–4），补抓即可闭合。
- **旧版只作历史不默默覆写当前控制状态**：**缺**。整个本主题已归档材料中，没有一手来源给出「目标/判据/授权版本化 + 旧版本降级为历史」的机制表述；最接近的只有授权作用域/新鲜度的设计主张与反例（§2.4）。这一半完成条件目前**只能以「未见」入走读**，不能引用任何产品文档冒充已有机制。

## 6. 负结论（本轮没有取得/不能据此推出）

- 未取得 2026-10-04 当日 LangChain HITL 文档的任何新逐字；本档全部逐字材料均属 2026-09-27/09-30 已归档内容，本档只做指针与对应关系。
- 不能因「搜索列表显示相关页面存在」推出任何机制语义；搜索列表只作 §1 标注的 P-existence·弱线索。
- 不能把 Anthropic Managed Agents 的在途结算语义套用到 LangChain HITL 上（机构与机制都不同）。
- 不能把 PR #7498 的标题写成「LangGraph time-travel 已知有 bug」的机制主张——标题级线索，未核。
