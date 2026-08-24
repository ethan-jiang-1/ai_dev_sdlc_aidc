# **深度解析需求工程：EARS与用户故事的演进、底层逻辑、AI编程适配性及多维度评估矩阵**

## **1\. 引言**

在软件工程与系统架构的演进历程中，需求工程（Requirements Engineering, RE）始终是决定项目成败的基础基石。长期以来，需求表达的准确性与跨团队沟通的灵活性之间存在着难以调和的内在张力。在敏捷开发（Agile Development）席卷全球软件行业的背景下，用户故事（User Story）凭借其以人为本的设计理念和极低的认知门槛，成为了捕获业务需求的主流事实标准。然而，随着现代系统复杂度的呈指数级上升，尤其是在航空航天、自动驾驶、医疗设备等安全关键（Safety-critical）领域，以及人工智能（AI）辅助编程与大语言模型（LLMs）的全面普及，用户故事在精确性、可验证性以及机器可读性上的固有缺陷日益显现。

在此行业背景下，Easy Approach to Requirements Syntax（EARS，需求语法的简易方法）作为一种轻量级的结构化自然语言规范，常被系统工程界与新兴的AI自动化开发领域评价为在系统级需求描述上“优于用户故事”。本报告旨在对EARS与用户故事进行深度的理论解构与实证对比，详细探讨两者的历史渊源、语法规范的底层逻辑、各自的工程优劣势，并前瞻性地剖析它们在大型语言模型与AI自动化编程（AI Coding）时代中的适配性与转化潜力。通过多维度的对标分析与行业实战案例，本报告将阐明这两种需求范式并非简单的替代关系，而是处于不同系统抽象层级的互补工具。

## **2\. 需求范式的历史脉络与哲学根基**

要深刻理解EARS与用户故事的本质差异及其适用边界，必须追溯它们诞生的工业背景，以及它们各自旨在解决的核心工程痛点。这两种方法论代表了软件工程中两种截然不同的认识论：一种致力于捕捉人类意图与商业价值，另一种则致力于构建严密的系统契约。

### **2.1 用户故事的敏捷基因与反文档化哲学**

用户故事的起源与极限编程（Extreme Programming, XP）及敏捷宣言的诞生密不可分，其发展历程反映了软件行业对传统瀑布模型中冗长文档的强烈反拨。一九九七年，Kent Beck在底特律的克莱斯勒C3项目中首次引入了用户故事的概念，试图用一种极其轻量级的方式来记录系统特性 1。随后在1998年，敏捷先驱Alistair Cockburn访问该项目后，将用户故事精辟地提炼为“对一次对话的承诺（a promise for a conversation）” 1。这一论断奠定了用户故事的理论基础。

到了一九九九年，Kent Beck在其著作《解析极限编程》中正式将用户故事确立为规划游戏（Planning Game）的核心构件 1。二零零一年，Ron Jeffries提出了著名的“3C”原则，即卡片（Card，物理媒介）、对话（Conversation，沟通共创）和确认（Confirmation，验收标准），进一步完善了其操作框架 1。此后，Mike Cohn撰写了被视为行业标准的著作，而Jeff Patton则在二零一四年推出了用户故事地图（User Story Mapping）技术，通过系统化的方法解决了用户故事之间依赖性不可见的问题 1。

用户故事的核心哲学是极端的反文档化。传统的软件工程极度依赖冗长且极易过时的需求规格说明书（SRS）。用户故事通过非正式的短句将大块功能拆解为小颗粒度目标，其实质是将需求的细节推迟到开发即将开始前的对话中去明确 3。它强调以用户为中心，将同理心注入开发流程，确保技术团队交付的是真实的业务价值，而不仅仅是满足技术规格 3。在这一哲学下，需求不是系统边界的硬性约束，而是激发开发者与客户共创的触媒。

### **2.2 EARS的工业严谨与安全关键系统溯源**

与用户故事脱胎于轻量级软件开发不同，EARS的诞生背景充满了高复杂度和高风险的工业严谨性。二零零九年，Alistair Mavin及其在劳斯莱斯（Rolls-Royce PLC）的团队在分析飞机发动机控制系统的适航法规时，面临着巨大的挑战 6。在这个包含数千个组件、涉及多达二十个不同供应商的生命攸关（Safety-critical）的分布式系统中，传统需求文档的质量直接关系到飞行安全 8。

劳斯莱斯团队在对无约束自然语言（Unconstrained Natural Language）需求进行深度审计时，识别出了八大导致系统缺陷的核心问题：歧义性（同一个词汇有多种解释）、模糊性（缺乏精度和结构）、复杂性（包含多个相互关联子句的复合需求）、遗漏（特别是处理异常和有害行为的需求缺失）、重复（对同一需求的冗余定义）、冗长（使用了过多不必要的词汇）、不适当的实现描述（说明了系统如何构建而不是系统必须做什么），以及不可测试性 7。

为了根除这些问题，Mavin及其团队发现，当系统需求的子句始终以相同的顺序出现时，其可读性和无歧义性最高 6。通过提取这些通用模式并加以提炼，他们创立了EARS符号体系，并在二零零九年的IEEE需求工程国际会议（RE09）上正式发布 10。EARS的核心哲学被定义为“轻度约束的自然语言（Gently Constrained Natural Language）” 6。它拒绝引入开发人员难以学习的复杂数学符号或抽象的图形语言，而是通过一套包含少数关键字的时间逻辑（Temporal Logic）模板，强迫作者将前置条件、触发事件、系统名称与系统响应以固定的语法结构排列 6。这种设计在保持英语直观易读特性的同时，赋予了自然语言类似于机器代码的严格确定性。

## **3\. 语法架构、结构语义与典型格式**

用户故事与EARS在格式上的根本差异，直接反映了它们背后的不同逻辑模型：前者是用户意图与商业价值的映射，后者则是有限状态机（Finite State Machine）与事件驱动架构的系统映射。

### **3.1 用户故事的意图驱动模型**

用户故事通常采用基于角色（Persona）的意图表达模板，其最经典的句式结构旨在回答“谁”、“需要什么”以及“为什么需要”这三个核心业务问题 14。这种结构刻意忽略了“如何实现”的系统级细节。典型的语法格式由三个子句构成：作为特定类型的用户，我希望系统提供某种功能或期望的输出，以便于我能够获得某种具体的商业收益或达成个人目标 3。

由于用户故事的主干刻意保持了极度的精简与高维度的抽象，其可执行性必须依赖于配套的验收标准（Acceptance Criteria）。验收标准定义了该故事被视为完成的具体边界与条件。在业界实践中，验收标准通常采用行为驱动开发（BDD）的Gherkin语言格式来补充必要的系统上下文与操作边界。Gherkin语法通过特定的关键字来定义测试场景：首先设定测试运行前必须满足的初始状态或前置条件，其次定义触发场景的特定操作或外部事件，最后规定预期的系统输出或状态的改变 14。这种将高层业务意图与底层测试场景分离的设计，构成了敏捷需求管理的标准范式。

### **3.2 EARS的时间逻辑与核心模式**

与用户故事的主观视角截然不同，EARS采用了一种极其客观的系统工程视角。EARS规定了一个基础的模板语法，条款必须按固定顺序出现，从而模拟系统运行的客观时间线。其基础架构包含可选的前置条件、可选的触发器、系统名称以及必须的系统响应 6。EARS规则集严格规定，一个合规的需求必须包含零个或多个前置条件、零个或一个触发器、唯一的系统名称，以及一个或多个系统响应 6。

通过组合上述不同的关键字与子句，EARS将庞杂的系统行为抽象为五种核心需求模式以及一种复合模式。这种模式化的分类使得需求工程师能够系统性地覆盖正常流程与异常分支，极大降低了需求遗漏的风险。

| EARS模式名称 | 逻辑定位与适用场景 | 语法格式规范 | 典型工业界示例 |
| :---- | :---- | :---- | :---- |
| **无处不在型 (Ubiquitous)** | 定义系统在任何条件下都必须具备的基础属性、约束或非功能性需求（如重量、材质、基础性能）。 | \<系统名称\> 必须 \<系统响应\> | 手机的质量必须小于XX克。 6 |
| **事件驱动型 (Event-driven)** | 规范系统在接收到特定外部触发或内部事件时应作出的即时响应，是软件系统中最常见的模式。 | 当 \<触发器\> 发生时，\<系统名称\> 必须 \<系统响应\> | 当选择“静音”功能时，笔记本电脑必须抑制所有音频输出。 6 |
| **状态驱动型 (State-driven)** | 规范系统在处于特定持续状态或模式期间必须维持的行为，只要状态为真，需求即保持激活。 | 在 \<前置条件/状态\> 期间，\<系统名称\> 必须 \<系统响应\> | 当ATM机内没有插入银行卡时，ATM机必须显示“请插入卡片以开始服务”。 6 |
| **有害行为型 (Unwanted behaviors)** | 专门用于应对错误、失效、非法输入或其他不期望发生的异常事件，确保系统的鲁棒性。 | 如果 \<异常触发器\> 发生，那么 \<系统名称\> 必须 \<系统响应\> | 如果输入的数据格式无效，那么系统必须生成一条详细的错误日志并拒绝执行。 11 |
| **可选特性型 (Optional features)** | 仅在系统部署了特定可选硬件或软件模块（如高级配置包）时才生效的需求约束。 | 在包含 \<可选特性\> 的情况下，\<系统名称\> 必须 \<系统响应\> | 在安装了全景天窗的车型中，车辆控制系统必须提供独立的天窗开闭控制按钮。 11 |
| **复合需求 (Complex Requirements)** | 结合上述多个模式（如同时包含状态和事件触发），用于描述极其复杂的系统时序行为。 | 在 \<前置条件\> 期间，当 \<触发器\> 发生时，\<系统名称\> 必须 \<系统响应\> | 当飞机处于地面状态时，如果接收到反推指令，发动机控制系统必须立即启用推力反向器。 18 |

通过上述表格可以看出，EARS通过简单的词法约束（While, When, If, Where），在自然语言与有限状态机的形式化验证之间搭建了一座桥梁。它强迫撰写者在动笔之前，必须清晰地界定系统的状态空间与事件边界。

## **4\. 多领域融合的实战案例深度剖析**

为了深刻揭示EARS为何在系统工程界号称“比用户故事更好”，我们需要剥离纯粹的理论讨论，将其置于具体的行业上下文中进行平行比较。事实上，两者的差异并不在于绝对的优劣，而是源于抽象层级（Abstraction Level）与适用问题域（Problem Domain）的不同。

### **4.1 互联网金融与SaaS平台的视角碰撞**

在纯软件驱动的互联网产品开发中，用户故事具有天然的沟通优势，它极好地回答了产品为什么要开发某个特性的问题。然而，当需求深入到后端的微服务架构与边界异常处理时，用户故事的模糊性就会引发实现偏差。

以现代手机银行应用程序为例，业务团队希望增加一个账户余额的快捷预览功能。 如果采用用户故事的范式，产品经理通常会这样编写：作为一个银行应用的用户，我希望在应用程序的主屏幕上直接看到我的账户余额，以便于我无需进行繁琐的点击就能随时了解我的财务状况 19。这段描述极其生动地描绘了产品的价值愿景，能够有效地对齐交互设计师、产品负责人与开发团队的目标。但是，它对后端系统工程师而言是远远不够的。它没有说明数据缓存的刷新频率、未登录状态下的掩码处理，或是后端接口超时情况下的系统行为。

如果在同一场景下引入EARS范式进行系统级需求规约，技术规范将会被拆解为极其精确的工程指令集。例如，利用状态驱动模式，可以规定在用户处于已认证登录状态期间，系统必须在主屏幕视图中渲染实时余额数据；利用有害行为模式可以补充，如果后端核心账务系统接口的响应时间超过三秒钟，那么前端系统必须显示缓冲占位符并在后台记录超时事件。在这个对比中，用户故事定义了产品愿景与用户体验旅程，而EARS则定义了系统必须遵守的技术规约与边界条件控制。

### **4.2 自动驾驶与功能安全（ISO 26262）的严苛要求**

在涉及生命安全的硬件与嵌入式系统领域，例如汽车功能安全标准（ISO 26262）、医疗器械合规（FDA准则）以及航空发动机控制中，系统出现哪怕一次单点故障（Single Point of Failure, SPF）都可能导致灾难性后果 20。在这类领域，用户故事的“留白与模糊性”不仅是无效的，更是违规的危险操作。

ISO 26262标准要求根据汽车安全完整性等级（Automotive Safety Integrity Level, ASIL），对电气和电子（E/E）组件进行严格的危险和风险评估（HARA） 22。ASIL等级从A到D，D级代表最严苛的安全要求 23。 尝试在ASIL D级别的自动紧急制动系统（AEB）中使用用户故事是注定失败的。例如，“作为一个驾驶员，我希望汽车在遇到前方有行人时能够自动刹车，以便保证行车安全”。这种表述对于需要编写激光雷达融合算法和执行器底层驱动的工程师来说，毫无指导意义，因为它完全没有界定感知延迟、制动力的梯度、传感器冗余逻辑以及降级策略。

相反，EARS与ISO 26262的合规要求高度契合。针对同一AEB系统，EARS可以生成如下的合规需求矩阵：

* **复合逻辑：** 在本车行驶速度大于十公里每小时且小于八十公里每小时的期间（状态前置条件），当车载激光雷达和毫米波雷达同时探测到前方十米内存在静止障碍物时（复合触发器），制动子系统必须在五十毫秒内施加不低于零点八个G的减速度（系统响应）。  
* **错误处理逻辑：** 如果主雷达传感器在运行中发生信号丢失或硬件失效（有害行为触发），那么系统架构必须立即无缝切换至备用超声波传感器网络，并通过仪表盘发出最高级别的声光报警指令以提醒驾驶员接管（系统响应）。

研究与工业实践表明，在这些安全关键领域，采用EARS等结构化语言重写需求，能够消除传统自然语言中固有的主观形容词和含糊副词，显著降低歧义性和复杂性这两大导致嵌入式软件严重缺陷的核心元凶 8。

## **5\. 优势、局限性与工程应用边界的深度界定**

断言“EARS优于用户故事”是一种严重的工程过度简化。其本质是探讨“系统级契约（System-level Contract）”相较于“用户级意图（User-level Intent）”在技术实现阶段的维数压制。两者都有其不可替代的优势与绝对的工程边界。

### **5.1 用户故事的协作红利与系统性盲区**

用户故事的最大优势在于其以人为本（Human-centric）的沟通属性。它强迫整个技术团队暂时脱离代码逻辑，从最终用户的视角思考问题，从而确保技术交付件直接挂钩真正的商业价值与业务痛点 5。此外，用户故事作为一种“占位符”，其轻量级的特性强制要求开发人员、测试人员和产品负责人在实际编码前进行面对面的沟通，这种沟通往往能暴露出文档无法捕捉的隐性需求 3。在项目管理层面，用户故事极其灵活，非常适合在敏捷待办事项列表（Backlog）中进行高频的优先级排序、规模估算（如使用故事点估算）和快速迭代重构 3。

然而，用户故事在实际工程执行中也暴露出了深层的系统性盲区。首先是上下文丢失与严重歧义。在实践中，“我想要...”这一部分经常被编写得过于规定性（限制了开发者的创新）或过于模糊（导致开发者需要自行脑补大量的异常边界条件和状态转换机），从而导致交付偏差 4。其次，用户故事极难自然地覆盖非功能性需求（Non-Functional Requirements, NFRs）。性能指标、安全性约束、合规性要求很难被套入“作为一个用户，我想要...”的句式体系中 11。最后，缺乏系统工程培训的业务人员往往会将复杂的后台逻辑生硬地塞入用户故事模板，导致形式主义的“拷贝粘贴灾难”，使项目陷入名为敏捷实为混乱的泥潭 4。

### **5.2 EARS的精确性红利与表达边界**

EARS的核心优势在于其极致的清晰度与逻辑同构性。通过强制将系统状态（前置条件）、外部刺激（触发器）和内部动作（响应）进行物理分隔，EARS在文本层面上直接映射了有限状态机和事件驱动架构的底层逻辑 13。它通过排除主观形容词，显著降低了开发和QA团队的误解率，从源头上消除了自然语言的缺陷 8。这种严格的语法结构使得EARS需求能够无缝对接到测试用例的生成环节，其基于条件与事件的触发结构是进行黑盒自动化测试的天然温床 13。对于跨国协作的分布式开发团队而言，即使工程师的母语不是英语，固定且直观的EARS语法模式也极大地降低了阅读和编写高质量需求规格说明书的认知负荷 6。

尽管如此，EARS也并非万能钥匙，它有着明确的工程边界。在处理极端复杂的业务逻辑时，EARS显得力不从心。如果一个需求涉及到超过三个以上的并发前置条件，强行使用EARS格式会将句子拉长至难以阅读的程度；在这种情况下，传统的列表（Lists）或决策表（Decision Tables）是更为合理的表达方式，它们能够将复杂性卸载到结构化的矩阵中，避免单一长句造成的认知过载 12。同样地，对于需要通过数学微积分、复杂加密算法或金融定价模型来表述的核心算法需求，EARS的语言模板也是不适用的，应当直接采用数学公式或伪代码（Pseudocode）进行规约 12。此外，由于EARS纯粹以系统为中心，它在早期探索性产品设计阶段缺乏用户同理心，无法传递功能背后的“商业原因”，这正是它需要与用户故事形成互补的根本原因 13。

## **6\. 智能化转型：适配AI自动化编程与大语言模型的降维打击**

在软件工程正在经历的这场范式转移中，大型语言模型（LLMs，如GPT-4, Claude 3.5, Gemini）和AI辅助编程工具（如Cursor, GitHub Copilot）的全面渗透，正在重塑代码生成的流水线 28。在这一全新的维度上，需求的格式直接决定了AI产出代码的质量与可靠性。正是在AI适配性这一层面上，EARS展现出了对用户故事压倒性的优势。

### **6.1 范式转移与混沌系统中的“初始条件”困境**

传统的敏捷交付流水线高度依赖人类的沟通：从产品理念（Idea）转化为用户故事，经由人类开发者的白板讨论与大脑解析，最终转化为代码 29。而在AI驱动的自动化编程时代，这一流程正在演变为：产品经理通过无代码平台或“直觉编程（Vibe Coding）”进行初步实验，随后通过提示词转换（Prompt Porting）技术，将意图直接输入给AI驱动的虚拟开发者系统，最终生成工程化代码 29。

在这个人机协作的新范式中，提示词工程（Prompt Engineering）成为了核心基础设施。混沌理论中著名的“初始条件”问题在这里得到了完美的体现：系统的初始状态哪怕发生最微小的扰动，也会导致最终结果的巨大偏差（蝴蝶效应） 30。提示词就是LLM生成代码时的绝对初始条件 30。用户故事那种“故意留白以促进后续面对面人类对话”的设计初衷，在面对大模型时反而成了致命漏洞。大模型并不具备人类工程师的业务常识，如果提供极其模糊或带有主观色彩的用户故事，大语言模型只能依赖自身权重的概率分布去猜测（即发生严重的逻辑幻觉 Hallucination），导致生成的代码通常只能覆盖理想状态的主流程（Happy Path），而在遇到边界情况和异常流时极易崩溃。

### **6.2 EARS作为结构化提示词工程的高级形态**

大语言模型在生成结构化数据或代码逻辑时，对输入提示的结构化程度极为敏感。学术界与工业界的实证研究均表明，结构化的格式（诸如JSON、YAML以及受到严格控制的规范自然语言）能够显著引导模型的注意力机制，降低Token成本，并成倍提升逻辑推理路线的准确率 30。EARS本质上就是一种经过系统工程界十余年时间检验的、高度严谨的代码生成Prompt框架。

首先，EARS有效约束了代码大模型的逻辑幻觉。EARS语法中的状态检查语句和事件侦听触发器，直接对应了高级编程语言中的控制流语句（如if/while/switch）和事件回调架构。这种从自然语言到代码抽象语法树（AST）的高度同构性，使得LLM在解析EARS需求时，能够生成极其精准且无多义性的控制流图。

其次，EARS强制实现了对异常分支的早期覆盖。通过内建的错误处理模式，它强制业务架构师在将提示词输入AI之前，就必须在逻辑层面上定义好所有可能的失效路径与兜底策略。这完美切中了LLM生成代码时容易忽视异常处理的痛点。

学术界的量化评估为这一论断提供了强有力的实证支持。在针对多个顶尖大语言模型（如ChatGPT, Gemini, DeepSeek, Claude, Qwen）进行软件需求生成与代码解析的对比研究中，当研究人员引入结构化提示词模式（其核心逻辑高度类似于EARS的规范约束）替代传统的松散用户故事基线时，各大模型的输出质量均实现了阶跃式的提升 33。研究数据显示，ChatGPT在需求解析的语义准确性与无歧义性上暴涨了59.17%，Gemini的提升幅度也达到了26.07%，同时深层逻辑缺陷被大幅剔除 33。另一项采用渐进式提示词（Progressive Prompting）方法论的研究也证实，当输入文档高度结构化时，大模型能够完美模拟一位资深架构师的思维过程，自动提炼功能需求、构建面向对象的类图模型，并最终生成包含全面单元测试的健壮代码组合 36。

### **6.3 交付效能与缺陷密度的实证对比**

如果我们将视线从代码生成扩大到整个研发过程的度量体系，结构化需求相比于传统用户故事的优势便会反映在硬核的效能指标上。在一项对比纯Scrum驱动（以用户故事为主）与敏捷模型驱动系统架构流程（sMBSAP，一种强调在迭代中融入结构化系统建模与需求规约的混合方法论）的准实验研究中，研究人员对十个开发冲刺（Sprint）的效能数据进行了严密的统计学T检验分析 37。

数据结果具有高度的指向性：在承诺可靠性（Commitment Reliability, CR）指标上，采用结构化系统规约的冲刺达到了0.94的极高水准，而以用户故事为主的纯Scrum团队平均仅为0.81 37。在更关键的代码质量指标上，结构化规约驱动的团队其平均缺陷密度（Defect Density, DD）显著降至0.63，而纯用户故事团队的缺陷密度则高达0.91；同时，在缺陷泄露率（Defect Leakage, DL）上，结构化方法也以0.15力压传统方法的0.20 37。不仅如此，结构化团队在保证更高质量的同时，其平均冲刺速率（Sprint Velocity）还从26.8提升至了31.8 37。这从极其严谨的实证层面印证了，在面对具有内在复杂性的现代软件系统时，类似于EARS这样施加一定形式化约束的需求范式，不仅没有拖慢敏捷的节奏，反而通过消除后期的需求返工与沟通摩擦，大幅提升了端到端的研发效能与系统健壮性。

## **7\. 测试驱动开发、行为驱动开发与自动化验证的深度融合**

除了在代码生成端的强大威力，EARS在测试工程领域的适配性同样值得深究。在传统的测试驱动开发（TDD）实践中，开发人员普遍极度抗拒手动编写繁琐且易碎的单元测试用例，这直接导致了TDD在许多企业中名存实亡 38。尽管行为驱动开发（BDD）试图通过用户故事来推导测试场景（即所谓的用户故事驱动开发 USDD），但由于故事本身的模糊性，从故事到测试用例的鸿沟依然巨大 38。

EARS的出现，为彻底打通AI自动化测试与BDD体系提供了终极的桥梁 9。在BDD框架中，Daniel Terhorst-North和Chris Matts推广了Gherkin语法（Given-When-Then结构）作为规范验收测试的事实标准 16。同时，Matt Wynne的实例映射（Example Mapping）技术也极大地推动了这种测试规约的普及 41。令人瞩目的是，EARS的语法结构与Gherkin语法之间存在着完美的同构映射关系：

| EARS语法子句 | 逻辑语义 | Gherkin验收测试映射 (BDD) |
| :---- | :---- | :---- |
| While \<precondition\> (在...期间) | 定义执行核心逻辑前的系统预设环境与依赖状态。 | Given \<initial state\> (假设系统处于...状态) |
| When/If \<trigger\> (当/如果发生...) | 界定诱发系统状态转换的动作输入、API调用或外部事件。 | When \<action/event\> (当用户或系统执行...操作时) |
| The system shall \<response\> (系统必须...) | 规范经过逻辑处理后，系统必须达到的终止状态或对外输出。 | Then \<expected outcome\> (那么系统应当展现...结果) |

这种几乎无缝的逻辑映射意味着什么？在AI辅助工程平台（如Roost.ai）或专用的质量保证工具（如Inflectra AI）的加持下，一旦需求工程师使用EARS规范完成了需求编写，AI系统利用自然语言处理（NLP）技术，可以在零人为干预、零语义损耗的情况下，将这些文本瞬间解析并转换为可执行的Cucumber自动化测试脚本集 27。这不仅彻底免除了开发人员手写测试代码的痛苦，更是真正意义上实现了测试左移（Test-Shift-Left）和验收测试驱动开发（ATDD），使得质量保障内建于需求成型的第一天 38。

## **8\. 需求质量的量化度量与自动化评估体系**

评估一项需求的质量不能仅凭工程直觉。由于用户故事与EARS的理论范式不同，行业内分别演化出了独立的质量评估标准与AI自动化检测工具链。

### **8.1 意图视角的度量金标准：INVEST原则**

对于用户故事而言，敏捷专家Bill Wake提出的INVEST原则是评估其质量的公认行业金标准 3。这不仅是一个缩写词，更代表了评估敏捷需求的六大核心维度：

* **独立性 (Independent)：** 故事之间不应存在复杂的强耦合与前后依赖关系，架构上允许它们以任意顺序被选择、开发和交付，从而保证规划游戏的灵活性。  
* **可协商性 (Negotiable)：** 故事卡片绝对不应被视为固定死板的法律契约。它必须保留足够的开放空间，促使程序员和业务方在开发过程中进行探讨、权衡与共创。  
* **有价值 (Valuable)：** 无论技术实现多么巧妙，该特性都必须能向最终用户或客户交付实际的、可感知的业务利益。  
* **可估算性 (Estimable)：** 描述必须包含足够的上下文信息，使得开发团队能够根据其历史经验给出合理的规模或工作量估算（如使用故事点估算）。  
* **小巧 (Small)：** 故事的颗粒度必须被严格控制，确保其开发周期能够被压缩在极短的时间内（通常需要在一个Sprint迭代内能够完成并验收），这能极大降低交付风险。  
* **可测试性 (Testable)：** 这是故事闭环的关键。如果一个故事由于描述模糊而无法编写出明确的验证标准，那么团队就永远无法证明该故事已经真正做到“完成（Done）”。

### **8.2 系统视角的度量体系：INCOSE规范与自动化合规检查**

由于EARS本身代表了严密且客观的系统工程规范，对其质量的评估必须遵循国际系统工程协会（INCOSE）制定的《需求编写指南》（Guide for Writing Requirements） 13。INCOSE指南定义了多达十四个类别、四十一条极度详尽的规则集来确保需求规约的高保真度 48。在EARS与INCOSE交集的质量维度中，高质量的系统需求必须满足以下几个核心刚性条件：

* **绝对必要性 (Necessary, 对应规则C1)：** 该需求陈述定义的系统能力、特征、约束或质量因素，必须能够直接追溯到更高层级的商业痛点、安全法规或全生命周期概念，禁止任何形式的过度设计 47。  
* **极致的无歧义与清晰度 (Unambiguous & Clear)：** 彻底杜绝使用诸如“快速的”、“足够好的”、“用户友好的”等含有主观评判色彩的形容词或副词，所有性能指标必须转化为可被工程设备精确测量的物理参数或时间边界 46。  
* **逻辑的单一性与原子化 (Stand-alone / Not grouped)：** EARS语法强制一行语句只表达一个完整的系统响应，严禁将多个复杂的“与/或（AND/OR）”布尔逻辑堆砌嵌套在一个冗长不堪的句子里，确保每一条要求都能被独立验证 46。  
* **以系统实体为绝对中心 (System-centric)：** 句子的主语必须且只能是明确的系统模块或物理实体（例如 \<特定子系统名称\> 必须执行...），并强制使用主动语态，严禁使用含混不清的被动语态 33。

### **8.3 质量度量向AI自动化的全面演进**

随着先进自然语言处理技术和深度学习分析算法的成熟，仅仅依靠人类工程师组成评审委员会来对成百上千条需求进行人工走查（Review）的低效方式，正在被自动化工具流所取代。 针对EARS和INCOSE标准的检测，诸如QVscribe和Visure Requirements ALM这类基于AI底座的分析工具，已经可以直接作为插件无缝嵌入到Microsoft Word、Excel或大型需求管理平台中 13。这些工具的智能引擎会在工程师编写需求的瞬间进行后台轮询扫描，自动高亮指出哪些句子包含了不受支持的模糊形容词，哪些句子违背了主动语态原则，或者哪些需求堆叠了超过工具建议阈值（通常为3个）的前置条件 12。AI不仅会标注出问题，还会根据预设的INCOSE规则集与EARS模板计算出实时的“需求质量评分”，促使用户即时进行纠正 48。工业界的大规模应用数据显示，此类基于AI的自动化需求规范审查机制，在需求进入正式开发环节前，能够削减高达百分之五十到百分之七十五的需求评审与错误修正时间 48；部分企业案例研究甚至表明，实施这种结构化的协作工具能在单个大型项目上直接节省出高达十五万美元的返工与沟通成本 50。 同样，针对用户故事的生态体系，Azure DevOps平台中的Copilot等智能助手也已经开始利用大模型能力，实时比对INVEST准则，自动检测积压工作项是否缺少验收标准，甚至运用AI预测该特性的变更对下游其他系统模块可能造成的涟漪风险（Impact Assessment） 45。

## **9\. 多维度综合比较与结语**

通过前述在理论起源、语法结构、领域应用、AI适配性以及质量度量等诸多维度的深度挖掘与剥茧抽丝，我们可以构建出一个全方位的评估矩阵，以此来更直观地展现两者的异同与工程边界：

| 深度评估维度 | 敏捷用户故事 (User Story) | 结构化需求语法 (EARS) |
| :---- | :---- | :---- |
| **理论渊源与哲学背书** | 诞生于轻量级软件运动，由敏捷联盟先驱(如Kent Beck)创立，旨在颠覆重度文档。 1 | 诞生于安全关键型重工业(如劳斯莱斯发动机)，旨在消灭复杂系统中的语言缺陷。 6 |
| **核心关注点与驱动力** | 商业价值驱动。始终关注“是谁”、“想要达成什么意图”以及“为何如此”。 3 | 系统行为与边界驱动。严格定义“在何种状态下”、“什么触发机制”以及“系统绝对响应”。 6 |
| **最佳受众与观察视角** | 面向业务干系人、UX研究员与最终用户。采用外部“黑盒视角”。 44 | 面向系统架构师、底层开发者、QA自动化工程师与合规审查员。采用“灰盒/白盒视角”。 12 |
| **语法强制力与模版** | 极度宽松。作为一个\<角色\>，我想要\<目标\>，以便\<商业价值\>。 14 | 严格的词法时间逻辑。在\<状态\>期间，当\<触发\>时，\<系统\>必须\<动作\>。 6 |
| **处理非功能性需求(NFR)能力** | 表现极差。往往只能通过变通手段(如累加验收标准或技术债卡片)来弥补。 11 | 表现极优。其核心的无处不在(Ubiquitous)模式正是为精准表述系统底层性能和约束而生。 6 |
| **对模糊性的容忍态度** | 刻意拥抱高模糊度。认为“不完美”是优势，必须留白以迫使人类进行高频对话补全。 3 | 零容忍。其诞生使命就是强制消解自然语言歧义，绝不留下未定义的系统边缘死角。 8 |
| **大模型AI编程契合度与Prompt效能** | 较差。极易诱发大模型产生严重的逻辑缺失与异常流幻觉，导致生成不可靠代码。 29 | 极其优异。语法本身即是高级的结构化提示词，能够精准制导LLM生成高度严谨的控制流与错误处理分支。 31 |
| **测试验证(BDD/TDD)自动化映射能力** | 较弱。通常只能靠人工将故事翻译拆解为Given-When-Then结构。 38 | 极强。其条件/触发/响应逻辑能够通过NLP工具被瞬间且无损地编译为自动化Cucumber脚本。 9 |
| **质量评估事实金标准** | 依赖于敏捷领域的INVEST六大准则，强调价值与解耦。 3 | 遵循INCOSE极其严苛的十四大类系统工程语法规则与合规体系。 13 |

### **结语：融合与演进的未来架构**

综上所述，关于“EARS全面优于用户故事”的论调，本质上反映了现代软件工程界对敏捷开发中后期阶段，因过度追求前期沟通灵活性而忽视系统严谨性，最终导致架构失控与交付质量崩塌的深刻反思。

当我们透过表象深入系统工程的本质时会发现，这两种范式绝非势不两立的竞争者，而是现代极其复杂的数字生态系统建设中，处于完全不同抽象层级、肩负不同历史使命的互补工具链 44。用户故事是描绘愿景的“房间装修指南（Room Description）”：它勾勒出用户体验的空间感与功能布局，是探索商业蓝海、验证产品创新假设的绝佳武器；而EARS则是构筑底层的“建筑工程蓝图（Blueprint）”：它精确标定了隐蔽工程的电力管线走向、核心承重墙的位置布局以及抗震防火的硬性合规参数，它存在的终极意义在于确保整个大厦在面对任何极端异常风暴时都不会发生倾覆。

尤其是在当前大语言模型与AI驱动的自动编程时代，自然语言编程带来的产能红利正在呈现爆炸式增长。然而，我们必须清醒地认识到，目前的大型语言模型并非真正具备人类丰富商业常识和同理心的“魔法师”，它们本质上依然是极端依赖上下文的超大规模逻辑推理引擎。在这种全新的人机协作环境下，**EARS凭借其无与伦比的严格时态结构约束、极其清晰的条件触发器界定以及毫无歧义的系统响应指令，毫无争议地成为了比松散的用户故事远为优越和可靠的代码生成Prompt底层框架**。

通向下一代高质量、高可靠性智能软件工程架构的必由之路，在于实现两者的有机融合：在宏观产品规划层，运用用户故事作为指引方向的北极星，确保方向正确、价值对齐；而在微观系统实现与AI交互层，通过EARS语法将宏大的产品故事无损拆解并转化为大模型能够精确无误理解的结构化指令网，最终将其丝滑映射到基于Gherkin的自动化测试防护网中。只有这两种哲学的完美契合，才能真正驾驭日益膨胀的软件复杂性，迎接全面智能开发时代的到来。

#### **Works cited**

1. User story \- Wikipedia, accessed on April 17, 2026, [https://en.wikipedia.org/wiki/User\_story](https://en.wikipedia.org/wiki/User_story)  
2. Evolution of Agile Method of Software Development \- Infosys, accessed on April 17, 2026, [https://www.infosys.com/iki/perspectives/agile-evolution.html](https://www.infosys.com/iki/perspectives/agile-evolution.html)  
3. User Story \- Martin Fowler, accessed on April 17, 2026, [https://martinfowler.com/bliki/UserStory.html](https://martinfowler.com/bliki/UserStory.html)  
4. How we've destroyed user stories \- Sherif Mansour \- Medium, accessed on April 17, 2026, [https://sherifmansour.medium.com/how-weve-destroyed-user-stories-8b36120645c6](https://sherifmansour.medium.com/how-weve-destroyed-user-stories-8b36120645c6)  
5. User stories with examples and a template \- Atlassian, accessed on April 17, 2026, [https://www.atlassian.com/agile/project-management/user-stories](https://www.atlassian.com/agile/project-management/user-stories)  
6. Alistair Mavin EARS: Easy Approach to Requirements Syntax | Official Guide, accessed on April 17, 2026, [https://alistairmavin.com/ears/](https://alistairmavin.com/ears/)  
7. (PDF) Easy approach to requirements syntax (EARS) \- ResearchGate, accessed on April 17, 2026, [https://www.researchgate.net/publication/224079416\_Easy\_approach\_to\_requirements\_syntax\_EARS](https://www.researchgate.net/publication/224079416_Easy_approach_to_requirements_syntax_EARS)  
8. EARS: The Easy Approach to Requirements Syntax | PDF \- Slideshare, accessed on April 17, 2026, [https://www.slideshare.net/slideshow/ears-the-easy-approach-to-requirements-syntax/51558506](https://www.slideshare.net/slideshow/ears-the-easy-approach-to-requirements-syntax/51558506)  
9. Easy Approach to Requirements Syntax and the segue to Behavior Driven Development, accessed on April 17, 2026, [https://conductofcode.io/post/easy-approach-to-requirements-syntax-and-the-segue-to-behavior-driven-development/](https://conductofcode.io/post/easy-approach-to-requirements-syntax-and-the-segue-to-behavior-driven-development/)  
10. EARS: The Easy Approach to Requirements Syntax \- IARIA, accessed on April 17, 2026, [https://www.iaria.org/conferences2013/filesICCGI13/ICCGI\_2013\_Tutorial\_Terzakis.pdf](https://www.iaria.org/conferences2013/filesICCGI13/ICCGI_2013_Tutorial_Terzakis.pdf)  
11. EARS: The Easy Approach to Requirements Syntax | by Oguz Senna | ParamTech \- Medium, accessed on April 17, 2026, [https://medium.com/paramtech/ears-the-easy-approach-to-requirements-syntax-b09597aae31d](https://medium.com/paramtech/ears-the-easy-approach-to-requirements-syntax-b09597aae31d)  
12. When Not to Use EARS \- QRA, accessed on April 17, 2026, [https://qracorp.com/when-not-to-use-ears/](https://qracorp.com/when-not-to-use-ears/)  
13. Adopting EARS Notation for Requirements Specification \- Visure Solutions, accessed on April 17, 2026, [https://visuresolutions.com/alm-guide/adopting-ears-notation/](https://visuresolutions.com/alm-guide/adopting-ears-notation/)  
14. Difference between User stories and Requirements \- PremierAgile, accessed on April 17, 2026, [https://premieragile.com/user-stories-vs-requirements/](https://premieragile.com/user-stories-vs-requirements/)  
15. Looking for feedback from Agile professionals on AI-generated user stories \- Reddit, accessed on April 17, 2026, [https://www.reddit.com/r/agile/comments/1klr6fw/looking\_for\_feedback\_from\_agile\_professionals\_on/](https://www.reddit.com/r/agile/comments/1klr6fw/looking_for_feedback_from_agile_professionals_on/)  
16. Given When Then \- Martin Fowler, accessed on April 17, 2026, [https://martinfowler.com/bliki/GivenWhenThen.html](https://martinfowler.com/bliki/GivenWhenThen.html)  
17. A Formula for Great Gherkin Scenarios (with Given-When-Then Examples), accessed on April 17, 2026, [https://www.businessanalysisexperts.com/gherkin-user-stories-given-when-then-examples/](https://www.businessanalysisexperts.com/gherkin-user-stories-given-when-then-examples/)  
18. Adopting the EARS Notation to Improve Requirements Engineering \- Jama Software, accessed on April 17, 2026, [https://www.jamasoftware.com/requirements-management-guide/writing-requirements/adopting-the-ears-notation-to-improve-requirements-engineering/](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/adopting-the-ears-notation-to-improve-requirements-engineering/)  
19. Requirements vs User Stories vs Acceptance Criteria : r/agile \- Reddit, accessed on April 17, 2026, [https://www.reddit.com/r/agile/comments/123k627/requirements\_vs\_user\_stories\_vs\_acceptance/](https://www.reddit.com/r/agile/comments/123k627/requirements_vs_user_stories_vs_acceptance/)  
20. ISO 26262 \- Automotive Functional Safety \- TÜV SÜD, accessed on April 17, 2026, [https://www.tuvsud.com/en-us/industries/mobility-and-automotive/automotive-and-oem/iso-26262-functional-safety](https://www.tuvsud.com/en-us/industries/mobility-and-automotive/automotive-and-oem/iso-26262-functional-safety)  
21. ISO 26262: The Complete Guide \- Spyrosoft, accessed on April 17, 2026, [https://spyro-soft.com/blog/automotive/iso-26262](https://spyro-soft.com/blog/automotive/iso-26262)  
22. Understanding ISO 26262: What You Need to Know \- New Eagle, accessed on April 17, 2026, [https://neweagle.net/blog/understanding-iso-26262/](https://neweagle.net/blog/understanding-iso-26262/)  
23. Functional Safety for Automotive – ISO 26262 \- DNV, accessed on April 17, 2026, [https://www.dnv.us/services/functional-safety-for-automotive-iso-26262-86905/](https://www.dnv.us/services/functional-safety-for-automotive-iso-26262-86905/)  
24. Advantages of User Stories over Requirements and Use Cases \- Mountain Goat Software, accessed on April 17, 2026, [https://www.mountaingoatsoftware.com/articles/advantages-of-user-stories-for-requirements](https://www.mountaingoatsoftware.com/articles/advantages-of-user-stories-for-requirements)  
25. Easy Approach to Requirements Syntax (EARS) : r/ReqsEngineering \- Reddit, accessed on April 17, 2026, [https://www.reddit.com/r/ReqsEngineering/comments/1hept25/easy\_approach\_to\_requirements\_syntax\_ears/](https://www.reddit.com/r/ReqsEngineering/comments/1hept25/easy_approach_to_requirements_syntax_ears/)  
26. 20220810 Enchantment \- From Fragile to Agile \- INCOSE, accessed on April 17, 2026, [https://www.incose.org/docs/default-source/enchantment/20220810fromfragiletoagile\_final2.pdf?sfvrsn=83a46cc7\_2](https://www.incose.org/docs/default-source/enchantment/20220810fromfragiletoagile_final2.pdf?sfvrsn=83a46cc7_2)  
27. Analyze Your Requirements Against the Easy Approach to Requirements Syntax (EARS) Using Inflectra.ai, accessed on April 17, 2026, [https://www.inflectra.com/Company/Article/analyze-your-requirements-ears-using-inflectra-ai-1916.aspx](https://www.inflectra.com/Company/Article/analyze-your-requirements-ears-using-inflectra-ai-1916.aspx)  
28. Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity \- METR, accessed on April 17, 2026, [https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)  
29. User Stories Are Dead. Long Live User Prompts\! | by Erez Morabia | Medium, accessed on April 17, 2026, [https://emorabia.medium.com/user-stories-are-dead-long-live-user-prompts-d2386a5af93e](https://emorabia.medium.com/user-stories-are-dead-long-live-user-prompts-d2386a5af93e)  
30. Everything You Need to Know About Prompt Engineering Frameworks, accessed on April 17, 2026, [https://www.parloa.com/knowledge-hub/prompt-engineering-frameworks/](https://www.parloa.com/knowledge-hub/prompt-engineering-frameworks/)  
31. Prompt engineering for structured data: a comparative evaluation of styles and LLM performance \- Computer Science, accessed on April 17, 2026, [https://www.cs.wm.edu/\~dcschmidt/PDF/Optimizing\_Prompt\_Styles\_for\_Structured\_Data\_Generation\_in\_LLM.pdf](https://www.cs.wm.edu/~dcschmidt/PDF/Optimizing_Prompt_Styles_for_Structured_Data_Generation_in_LLM.pdf)  
32. Automated Prompt Engineering for Cost-Effective Code Generation Using Evolutionary Algorithm \- arXiv, accessed on April 17, 2026, [https://arxiv.org/html/2408.11198v2](https://arxiv.org/html/2408.11198v2)  
33. Exploring the Use of LLMs for Requirements Extraction from User Stories \- ResearchGate, accessed on April 17, 2026, [https://www.researchgate.net/publication/398149277\_Exploring\_the\_Use\_of\_LLMs\_for\_Requirements\_Extraction\_from\_User\_Stories](https://www.researchgate.net/publication/398149277_Exploring_the_Use_of_LLMs_for_Requirements_Extraction_from_User_Stories)  
34. Large Language Models are Human-Level Prompt Engineers | OpenReview, accessed on April 17, 2026, [https://openreview.net/forum?id=92gvk82DE-](https://openreview.net/forum?id=92gvk82DE-)  
35. Can LLMs Generate User Stories and Assess Their Quality? \- arXiv, accessed on April 17, 2026, [https://arxiv.org/html/2507.15157v1](https://arxiv.org/html/2507.15157v1)  
36. Requirements are All You Need: From Requirements to Code with LLMs \- arXiv, accessed on April 17, 2026, [https://arxiv.org/pdf/2406.10101](https://arxiv.org/pdf/2406.10101)  
37. Comparing Measured Agile Software Development Metrics Using an Agile Model-Based Software Engineering Approach versus Scrum Only \- MDPI, accessed on April 17, 2026, [https://www.mdpi.com/2674-113X/2/3/15](https://www.mdpi.com/2674-113X/2/3/15)  
38. TDD is Dead: The Emergence of User Story-Driven Development \- Roost.ai, accessed on April 17, 2026, [https://roost.ai/blog/beyond-the-10x-developer-the-rise-of-the-100x-developer-and-the-role-of-the-prompt-engineer-0-0](https://roost.ai/blog/beyond-the-10x-developer-the-rise-of-the-100x-developer-and-the-role-of-the-prompt-engineer-0-0)  
39. Looking for Case Studies of How TDD Improved Quality and/or Speed of Development, accessed on April 17, 2026, [https://softwareengineering.stackexchange.com/questions/74580/looking-for-case-studies-of-how-tdd-improved-quality-and-or-speed-of-development](https://softwareengineering.stackexchange.com/questions/74580/looking-for-case-studies-of-how-tdd-improved-quality-and-or-speed-of-development)  
40. Feature-Driven Development vs. Test-Driven Development \- LaunchDarkly, accessed on April 17, 2026, [https://launchdarkly.com/blog/feature-driven-development-versus-test-driven-development/](https://launchdarkly.com/blog/feature-driven-development-versus-test-driven-development/)  
41. Gherkin Rules | Cucumber, accessed on April 17, 2026, [https://cucumber.io/blog/bdd/gherkin-rules/](https://cucumber.io/blog/bdd/gherkin-rules/)  
42. Mastering Gherkin for Software Testing: A Step-by-Step Guide \- testRigor AI-Based Automated Testing Tool, accessed on April 17, 2026, [https://testrigor.com/blog/gherkin-for-software-testing/](https://testrigor.com/blog/gherkin-for-software-testing/)  
43. Test-Driven Development in the Larger Context \- PMI, accessed on April 17, 2026, [https://www.pmi.org/disciplined-agile/how-to-start-with-acceptance-test-driven-development/test-driven-development-in-the-larger-context](https://www.pmi.org/disciplined-agile/how-to-start-with-acceptance-test-driven-development/test-driven-development-in-the-larger-context)  
44. Requirements vs. User Stories: Which Are Better? \- Modern Analyst, accessed on April 17, 2026, [https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/6602/Requirements-vs-User-Stories-Which-Are-Better.aspx](https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/6602/Requirements-vs-User-Stories-Which-Are-Better.aspx)  
45. Copilot4DevOps \- User Stories vs Requirements, accessed on April 17, 2026, [https://copilot4devops.com/user-stories-vs-requirements/](https://copilot4devops.com/user-stories-vs-requirements/)  
46. What is the Point of Requirements? \- INCOSE, accessed on April 17, 2026, [https://www.incose.org/wp-content/uploads/2026/01/INCOSEContent-411.pdf](https://www.incose.org/wp-content/uploads/2026/01/INCOSEContent-411.pdf)  
47. INCOSE Guide to Writing Requirements V4 – Summary Sheet, accessed on April 17, 2026, [https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose\_rwg\_gtwr\_v4\_summary\_sheet.pdf](https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf)  
48. Automating the INCOSE Guide for Writing Requirements \- QRA Knowledge Center, accessed on April 17, 2026, [https://edu.qracorp.com/hubfs/Automating-The-INCOSE-Guide-For-Writing-Requirements.pdf](https://edu.qracorp.com/hubfs/Automating-The-INCOSE-Guide-For-Writing-Requirements.pdf)  
49. Meet INCOSE's Guide to Writing Requirements With AI Quality Checker Webinar, accessed on April 17, 2026, [https://specinnovations.com/blog/meet-incoses-guide-to-writing-requirements-with-ai-quality-checker-webinar](https://specinnovations.com/blog/meet-incoses-guide-to-writing-requirements-with-ai-quality-checker-webinar)  
50. Developing and Modeling an Approach for Requirements Management Optimization \- INCOSE, accessed on April 17, 2026, [https://www.incose.org/wp-content/uploads/legacy/texas-gulf-coast/incose\_meeting\_04\_15\_2021.pdf?sfvrsn=254567c7\_0](https://www.incose.org/wp-content/uploads/legacy/texas-gulf-coast/incose_meeting_04_15_2021.pdf?sfvrsn=254567c7_0)  
51. AI Assistants and Tools for efficient Requirements Engineering \- DevOpsCon, accessed on April 17, 2026, [https://devopscon.io/blog/ai-assistants-and-tools-for-efficient-requirements-engineering/](https://devopscon.io/blog/ai-assistants-and-tools-for-efficient-requirements-engineering/)  
52. (PDF) From Reviews to Requirements: Can LLMs Generate Human-Like User Stories?, accessed on April 17, 2026, [https://www.researchgate.net/publication/403307560\_From\_Reviews\_to\_Requirements\_Can\_LLMs\_Generate\_Human-Like\_User\_Stories](https://www.researchgate.net/publication/403307560_From_Reviews_to_Requirements_Can_LLMs_Generate_Human-Like_User_Stories)