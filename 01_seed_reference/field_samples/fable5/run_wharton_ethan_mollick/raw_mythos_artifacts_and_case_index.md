# Raw Notes: Ethan Mollick's Fable 5 Artifact and Case Index

来源：

- 原文：`https://www.oneusefulthing.org/p/what-it-feels-like-to-work-with-mythos`

## 这份材料补的是什么

Ethan 的主文已经很强，但它更像一篇总论。

这份 raw 专门把他在文中实际展示出来的 `artifact / demo / software` 线索抽出来，便于后续快速回看“Fable 5 到底做了哪些具体东西”。

## 一组代表性 artifact

### 1. 学术论文

- Ethan 说，Fable 从单条 prompt 加一轮反馈中，生成了他见过“最复杂的 academic social science paper”
- 链接：`https://verdicts-not-evidence-paper.netlify.app/`

这条线的价值在于：

- 说明 Fable 不是只会做代码任务
- 它也能处理高结构、长篇幅、讲究论证组织的产物

### 2. 10 页字母诗

- Ethan 还给出一个偏创意但很能体现约束处理能力的例子
- Fable 产出了一首 10 页长的押韵诗，而且每个词都以字母 `s` 开头
- artifact 链接：`https://claude.ai/public/artifacts/32ebc671-f415-4072-b46d-5353d4ffaad4`

### 3. 三个单 prompt 游戏

Ethan 用 Claude Code 给 Fable 下了模糊 prompt，然后只做少量“make it better”式反馈，就得到了可玩的网页游戏：

- `Flipside`
  - 提示：`Balatro, but for the game of coin flips`
  - 链接：`https://play-flipside.netlify.app/`

- `Snake`
  - 链接：`https://snake-stable-build.netlify.app/`

- `Strata`
  - 链接：`https://strata-descent.netlify.app/`

这组案例的关键点不是游戏本身，而是：

- 没有外部图像素材
- 图像和 3D 对象都是靠数学生成
- 人类只给了非常粗的方向

### 4. 等时线地图

- `isochronic map`
- 链接：`https://isochronic-passage-chart.netlify.app/#nyc`

Ethan 给这个项目下的原始要求非常雄心勃勃：

- 基于真实数据
- 同时考虑机场、火车、步行、驾车
- 风格独特
- 尽可能通用

Fable 随后：

- 拉起多个子 agent 做研究
- 检索了 `2200+` 条具体航班
- 拉取了从 TGV 到新干线的火车时刻
- 从多篇论文里找各国道路速度
- 一边研究一边写代码
- 还会开更多 agent 来测代码和记进度

在 Ethan 指出边远地区数据仍然不够准后，Fable 又继续修：

- 研究 Pitcairn Island 船期
- 研究从 Ottawa 到 Grise Fjord 的路径
- 跑 adversarial groups of agents 交叉研究和测试

### 5. Concord

- 这是 Ethan 最严肃的一个研究软件案例
- GitHub：`https://github.com/emollick/concord`

他先让 Fable 生成一份 `19` 页设计文档，然后执行实现：

- Fable 连续工作了 `9.5` 小时
- 产出了一套能校准 human / AI judgment 的研究软件
- 支持多数据集输入和复杂分析

## 为什么这份 raw 值得留

- 这份材料把 Ethan 从“框架型评论者”补成了“带一串具体 artifact 的样本人物”。
- 后面如果你要横向比较谁更偏 workflow、谁更偏 artifact、谁更偏治理，这份索引会很好用。
