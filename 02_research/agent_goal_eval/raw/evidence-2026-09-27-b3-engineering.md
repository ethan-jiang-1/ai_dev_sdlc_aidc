# Evidence 2026-09-27 · B3 · 工程里怎么建检查、数怎么动

- 观测日期：2026-09-27
- 本档案回答：工程帖里的做法。检查写成什么、数据集怎么来、改了实现之后哪个数动了
- 不回答：这些数能不能外推。见解不在这里重复

## Source 1 · Ramp 收据匹配

- URL：https://engineering.ramp.com/post/apple-intelligence-receipt-matching
- 发布日期：2026-04-13。窗边
- 访问/观测日期：2026-09-27【主验】
- 来源类型：公司工程博客
评测怎么跑：Hex 导出几百笔员工交易和收据图的 S3 标识；有权限的脚本把图下到本地；单独一个 iOS target 把图和 CSV 打进包，用 TabularData 解析，跑 `ReceiptDetection`。每张收据既对正确交易，也对无关交易。配对必须 true，其余必须 false。精确率是「说匹配时有多少是对的」，召回是「真匹配里找出了多少」。

2.0 的检查是一次提问、一个布尔值：

```swift
return try await session.respond(
    to: """
    Does the OCR text contain all of the following?

    Merchant name: '\(transaction.merchantName)'
    Date: '\(transaction.date)'
    Amount: '\(transaction.amount)'
    """,
    generating: Bool.self
).content
```

评测集：精确率 35%，召回 7%。小模型会把「看起来像收据」直接判 true，或编出文本里没有的数字。

2.1 拆成三次 `think`，每次只问一个字段。结构体里有一段 rationale，他们不读，只读 `verdict`：

```swift
@Generable
private struct Answer {
    @Guide(description: "Your thinking as a free-form paragraph.")
    let rationale: String
    @Guide(description: "Verdict")
    let verdict: Bool
}
```

三次问题分别是商家名、日期、金额是否出现在 OCR 里，三个布尔值取与。评测集精确率 83%，召回 24%。上线后用户会拒绝错配：精确率 66%，召回 18%。

2.1 仍会幻觉，尤其是数字：「金额 $10.99 在文本里」而文本里没有。3.0 只把商家名留给模型；日期和金额用 `String.dataDetectorMatches` 抽，再和交易比对（日期比同一天，金额用包含）。模型调用从三次变成一次。上线：召回 44%，精确率 87%。他们写召回上去，一部分是因为少了两次调用、匹配出示快了三倍，用户来不及先手动上传。

- 该摘录支持的最小主张：同一套配对数据上，检查从「三字段一次布尔」改成「三问加一段不采用的理由」，评测集精确率 35% 到 83%；上线是 66%。再把日期和金额改成确定性抽取之后，上线精确率 87%，召回 44%。
- 不支持什么：不是一个叫「准确率」的数从 35% 到 83%。2.1 的召回停在 24%（上线 18%）。3.0 的召回含有「出示变快、用户少了手动上传」这一截，不只是匹配本身变准。

## Source 2 · Harvey 合同审查

- URL：https://www.harvey.ai/blog/rebuilding-playbook-review-as-a-multi-agent-system
- 发布日期：2026-09-02。作者 Maharshi Patel、Pablo Felgueres、Zach Huang
- 访问/观测日期：2026-09-27【主验】
- 来源类型：公司工程博客
数据集：合同配 playbook，跨合同类型、几百条条款。没有公开基准能盖住整段，所以和内部律师一起建。两面分开打。风险分类是分类题。红线质量是每条例子一份 rubric，问修改是否足够小、位置对、法律上站得住。LLM 裁判按这些 rubric 打分，三只前沿模型各自打、再汇总。

他们用这套去打三种做法：

| 做法 | 质量 | 延迟 | 复杂度 |
|---|---|---|---|
| 按规则瀑布调用模型 | 中 | 很好 | 低 |
| 单只 agent 改到满足 playbook | 很好 | 不能用 | 中 |
| 主 agent 把每条规则分给并行子 agent，再收回来调和 | 很好 | 好 | 高 |

单只 agent 拿着合同和 playbook，用改文档的工具一直改，直到满足 playbook。基准上好，延迟高到不能给用户用。

选中的是主从。主 agent 被提示成主办律师，按 playbook 的每条规则拉起子 agent，最多几十个并行。每个子 agent 做完这些事：读自己那条规则，读或搜索合同，判断是否符合 playbook，选定标准立场或某一条退路，起草修改清单。条款指向附件就去读附件。合同的每一块有唯一标识，用来引用和修改。最后交一份短备忘：这条规则怎么分类、为什么。主 agent 再把结果调和。

子 agent 不改同一份文档。每条规则在自己的分支上起草，不冲突的修改合并，两条规则碰到同一处就交给主 agent。状态留下来，追问时不把整段重跑。

读数：风险分类 59% → 77%（+18）。红线 rubric 53% → 87%（+34）。旧系统平均延迟 2.6 分钟。页上的表里，新延迟那一格就是空的，不是摘录漏了。他们另写延迟和 token 在长合同上明显上升，于是加了按模型、阶段、文档长度设的超时，只重试卡住的那条规则；限制并行；把提示改成共享文档前缀以便缓存；每条规则一完成就流式吐出，用户几秒内能开始看。

- 该摘录支持的最小主张：检查是律师写的分类加逐条 rubric，三只模型投票。单 agent 改到满足 playbook 质量够、延迟不能用。换成按规则并行之后，两个分到 77% 和 87%。
- 不支持什么：升幅没有拆成「某一句 prompt」。新延迟的分钟数页面上没有写。

## Source 3 · Shopify Flow

- URL：https://shopify.engineering/fine-tuning-agent-shopify-flow
- 发布日期：2026-04-22。窗边
- 访问/观测日期：2026-09-27【主验】
- 来源类型：公司工程博客
离线三格，都写在页上：

- 语义：生成的流程是不是该做的那件。LLM 裁判拿输出和期望流程比。
- 语法：会不会跑不起来。条件坏了、引用错了、配置非法，用程序查。
- 延迟：从请求到交出流程的时间。

基准是 300 条手写例子，盖的是他们预期的 Flow 用法。微调的是 Qwen3-32B。1% 流量上，店主是否打开生成的流程，微调模型比原来的提示代理低 35%。基准没盖住的真实请求是：改已有流程、配邮件、第三方集成、只提问不创建。打开率被判成噪声，因为它是商人行为，不是模型质量。接着优化的是领域专家校准过的 LLM 裁判。他们写用生产数据两周补上缺口，没有给出打开率回到多少。2.2 倍快、便宜 68% 是相对被换掉的前沿模型，不是这条打开率。

另外一条工程事实：训练数据和线上工具必须同形。训练里工具叫 `flow_app_agent_task_search`，线上叫 `task_search`，去掉前缀之后准确率上去。工具返回的 JSON 键若训练时按字母排序、线上顺序不同或多一个字段，准确率就掉。系统提示里工具的顺序训练和线上不一致，也会掉。
- 原文摘录：
  > “An LLM evaluation framework compares the generated workflow against the expected one for semantic correctness, and validates syntactic correctness programmatically.”
  > “The benchmark covered what we expected merchants to ask. It didn't cover what they actually asked”
  > “Activation rate was our first production signal, but it turned out to be noisy: it reflects merchant behavior, not model quality.”
- 该摘录支持的最小主张：离线检查是「语义裁判 + 语法程序」。上线第一信号和离线分不一致时，他们换掉信号，不把打开率继续当模型分。
- 不支持什么：不证明两周补洞之后打开率回到了原来的水平。文中没有这个回升数字。

## Source 4 · 租赁助手上的标注

- URL：https://www.lennysnewsletter.com/p/advanced-evals-how-to-find-and-fix
- 发布日期：2026-09-22。Hamel Husain、Shreya Shankar。第三步的聚类计数表在付费墙后
- 访问/观测日期：2026-09-27【主验公开部分。前两步全文；第三步只有标题】
- 来源类型：作者本人。他们把这一步从 error analysis 改称为 error discovery，并写若只有时间做一段，先做这段
- 例子：潜在租客说「这超出预算了，谢谢」。助手说「不客气，以后有变化再来」。自动检查把它当成功。产品要的是接着卖：更便宜的户型，或同一公司的别的房子。他们说，这条要等人看过这条 trace，才知道该加进标准。
- 公开部分写明的操作：trace 落到本地 `traces/traces.jsonl`，一条会话一个 JSON，含用户输入、系统提示、每次工具调用和结果、检索、中间模型调用、最后给用户的输出。没有 trace 就让 coding agent 先加日志。合成查询按固定维度拼，租赁例子是三列：任务（约看房、问价、问宠物）、租客类型、请求清楚还是含糊还是越界。每个组合单独打一次模型，不许一次生成全部。
- 标注：先亲手看至少 10 条，只写失败，停在上游第一处。句子要让同事看得懂。他们给的句子是「工具输出写着已租出，助手却说还能租」，不是「回复很差」。不做根因。审阅界面按用户看到的样子渲染。标完至少 10 条之后，模型可以提议更多失败，人接受或拒绝，不要照单全收。到大约 100 条再让模型按失败模式聚类。插件入口是 `npx skills add https://github.com/ai-evals-course/evals-skills`，然后点 `/evals-start`。
- 该摘录支持的最小主张：工程上先把会话落成一条 JSON，人先标 10 条能转述的失败，再让模型找同类，提议要人点头。上面那段对话是一条会被自动检查放过的失败。
- 不支持什么：第三步的聚类计数表和优先级没有读到。文首转述的 Ramp「35% 到 83%」、Shopify、Cursor、Harvey 以各公司自己的帖为准，不以这篇转述为准。文首点名的 Rippling、Glean、ElevenLabs 这轮没有打开。Robinhood 与 Abridge 另见 B4。

## 判读

- 观察：四处都是先有一套能反复打的检查，再改系统。Ramp 的检查从一次三字段布尔，拆成三次单字段，再把日期和金额交给确定性抽取；精确率沿评测集 35% → 83%，上线 66%，再上线 87%。Harvey 的子 agent 按一条规则读合同、选立场、起草修改。Shopify 的离线分和打开率不是同一个数，他们后来不优化打开率。租赁那条是检查还没写成时，人先标下来的句子。
- 推断：工程帖里的「调优」是换检查的形状或换信号，然后重跑同一套数据。数会动，也会在上线后缩回去。
- 与现有材料关系：B2 写的是全过就退役、合不上就改成功定义。这里是同一类动作的实现和读数。不并成一步。Abridge 的逐条规则和 91% 在 [`evidence-2026-09-27-b4-abridge.md`](evidence-2026-09-27-b4-abridge.md)，不并进上面三家。

## 负结论与限制

- Cursor 2026-08-06《How Cursor Router chooses the right model》（https://cursor.com/blog/how-cursor-router-works）：Auto Balance 比 Opus 4.8 便宜 41%，满意信号再高 3 个点。Compass 判最可能成功的轮次，96% 收到正向信号；判最不可能的，71%。这是路由分，不是一条任务做完没有。不并进上面的任务检查。
- Ramp、Shopify 在 2026-04，标窗边。
- 不能推出：拆开提问就会得到 83%；83% 就是用户看到的精确率；三模型投票是红线质量上升的原因。
