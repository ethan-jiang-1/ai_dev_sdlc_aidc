# 跨人物主题分析：共识区、分歧区、预测

> 当 ThoughtWorks、Martin Fowler、Dave Farley、Simon Willison、Kent Beck 这些塑造了现代软件开发方法论的人同时谈论 AI 时——他们同意什么？在什么事上打架？我们能从中推导出什么？

---

## 一、所有人都同意的事（共识区）

### 1. 经典工程实践不是过时了——是 AI 的制衡力

**Fowler, Farley, Beck, ThoughtWorks — 全票通过。**

AI 加速了代码生成 → 质量风险被放大 → TDD、CI/CD、模块化、小批量成为**抵抗风险的唯一防线**。

- Farley: *"If you're already working well, AI will be a big win. If you're working poorly, you'll just dig a deeper hole faster."*
- Beck: TDD 为 Agent 提供确定性 spec——这是结构性的匹配，不是巧合
- ThoughtWorks Vol.34 主题一就是"保留原则，放弃旧模式"
- Fowler: 敏捷的小增量 + AI 速度 = 更强协同

### 2. 验证成为瓶颈——"写代码"不再是稀缺资源

**Fowler, Farley, Willison — 全票通过。**

- Fowler: *"The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right.'"*
- Farley: 验证成为三个结构性问题之一
- Willison: 整个 SDLC 是围绕"一天几百行"设计的，10x 后全崩
- ThoughtWorks: 引入"Cognitive Debt"概念——代码能跑但对人类不可知

### 3. Vibe Coding 对生产系统不负责任

**Fowler, Farley, ThoughtWorks — 全票通过。Willison — 同意但在自己实践中越来越接近。**

Fowler 明确区分了 Vibe Coding 和 Agentic Engineering。ThoughtWorks 将 Vibe Coding 标记为反模式。Farley 认为不看代码就是放弃工程责任。

唯一的不同意见来自 Jim Highsmith 的"好奇式的着迷"——但他也明确是针对个人/实验场景，不是生产。

### 4. 资深工程师的杠杆被放大，初级工程师需要新路径

**Willison, Farley, ThoughtWorks — 全票通过。**

- Willison: 中层工程师风险最高——经验足够昂贵但不够资深成为编排者
- Farley: AI 暴露那些从未学会工程师思维的人
- ThoughtWorks: 只有资深工程师能有效驾驭高自主性 AI

---

## 二、在打架的事（分歧区）

### 打架 1：AI 是黑盒还是白盒？

| 黑盒派（信任） | 白盒派（验证） |
|--------------|--------------|
| Willison（实践中） | Farley |
| Yegge | Fowler |
| StrongDM 黑暗工厂 | ThoughtWorks |
| "没人读代码" | "必须用确定性传感器验证" |

**为什么在打架**：这不是技术分歧——是**哲学分歧**。黑盒派认为"既然读不了那么多，就别读了，信任直到出问题"。白盒派认为"不能验证的东西不能拥有，必须发明新的验证机制"。

**可能的和解**：Fowler 的"Verified 含义变了"——检查仍然存在，但不是在人脑子里。这个中间道路可能最终让两派走到一起。

### 打架 2：SDLC 需要微调还是重写？

| 微调派 | 重写派 |
|--------|--------|
| Beck, Fowler | Willison |
| 敏捷核心不变 | "整个 SDLC 是围绕'一天几百行'设计的——现在不是了" |

**为什么在打架**：这取决于你在 SDLC 的哪个位置。如果你在写代码那一段，10x 是翻天覆地的。如果你在定义产品方向那一段，AI 没改变什么。**两个人都对，但看到的问题不同。**

### 打架 3：AI 让我们更好还是更累？

| 更好 | 更累 |
|------|------|
| Yegge（12,000 行/天！） | Willison（"上午 11 点我就被榨干了"） |
| Farley（55% 提升是真的） | ThoughtWorks（审查疲劳、认知债） |

**为什么在打架**：AI 的生产力增益和认知成本很可能是**同一个现象的两面**。产出更多 → 审查更多 → 更累。解决这个矛盾可能意味着：不是少用 AI，而是重新设计流程让 AI 的产出不需要全部人类审查——这正是 Harness Engineering 在做的事。

---

## 三、五个预测

基于这些人的共识和分歧，可以推导出以下预测：

### 预测 1：Harness Engineering 将成为一个独立学科

Fowler 亲自推广、ThoughtWorks 列为 Vol.34 核心主题、Böckeler 在 QCon 的主题演讲——这个概念的势能太大，不会停留在"值得探索"的阶段。**2027 年将出现 Harness Engineer 的职位描述。**

### 预测 2：DORA 指标将取代"代码行数"成为 AI 时代的生产力标准

ThoughtWorks 明确将"代码吞吐量作为生产力"标记为 Caution。Farley 和 Willison 从不同角度论证了传统指标的失效。**推动力不是理想主义，而是测量错误的代价在 AI 速度下被放大。**

### 预测 3：中层工程师将经历最剧烈的角色转型

Willison 和 ThoughtWorks 独立得出相同结论。中层工程师面临的不是失业，而是需要**从"写代码的人"变成"设计 harness 的人"**。这和 2000 年代从"程序员"到"软件工程师"的转型类似。

### 预测 4：Vibe Coding 和 Agentic Engineering 的界限将继续模糊

Willison 已经在自己的实践中看到了趋同。当 Agent 能力继续提升，Fowler 画的线可能需要重画。**"不审查每一行"可能从不可接受变成必要的实践。**

### 预测 5：AI 将成为推动工程实践的"强制函数"

Farley 最乐观的预测：AI 不是威胁，而是**有史以来最好的机会让团队最终内嵌正确实践**。不是因为理想主义，而是因为不这样做**肉眼可见地危险**。

---

## 四、最值得记住的五个判断

| 人物 | 判断 |
|------|------|
| **Martin Fowler** | "The game is not 'how fast can we build' anymore. It is 'how fast can we tell whether this is right.'" |
| **Dave Farley** | "AI won't replace software engineers, but it will expose the ones who never learned to think like engineers." |
| **Simon Willison** | "If you can go from 200 lines of code a day to 2,000, what else breaks?" |
| **Kent Beck** | "We remain skeptical and we remain human." |
| **ThoughtWorks** | "The maturity of a coding agent lies not in making it more autonomous, but in building better control systems around it." |

---

*本文件为 `_raw_kol` 目录的收束篇。前五篇为各人物的深度拆解，本篇为跨人物主题分析。*
