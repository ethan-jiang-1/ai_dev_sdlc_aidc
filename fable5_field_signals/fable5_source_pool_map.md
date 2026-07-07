# Fable 5 高信号来源池地图

> 这份文档不收人物本身，而是收“去哪里找人物、找工作流、找原话、找落地痕迹”。
> 你刚刚提到的 `every.to` 确实是一类，但它不是唯一入口。

---

## 先说结论

- 如果要找“第一时间有高手围观和吵架的地方”，先看 `Hacker News`
- 如果要找“高手愿意认真写长文、谈限制和风险”的地方，先看 `LessWrong`
- 如果要找“自己真跑过、真踩过坑、真写了细节”的地方，优先看独立博客，尤其是 `Simon Willison`
- 如果要找“真有人拿模型干活了，不是嘴炮”的地方，优先看 `GitHub Issues / PR / Discussions`
- 如果要找“AI-native 团队怎么把模型塞进工作流”的地方，优先看 `Every`

---

## A 档：一手实战池

### 1. 独立技术博客

- 代表：
  - `Simon Willison`
  - 其他高密度独立开发者博客
- 为什么强：
  - 这类地方通常不是媒体转述，而是作者自己上手之后写“我怎么试、哪里卡、哪里惊到我”
  - 很容易出现具体 prompt、具体 bug、具体命令、具体工作流
- 适合挖什么：
  - `run_个人/公司_名字`
  - `raw_*.md`
  - 代表性原话
- 当前强信号例子：
  - `Initial impressions of Claude Fable 5`
  - `Claude Fable is relentlessly proactive`

### 2. GitHub Issues / PR / Discussions

- 代表：
  - 公开仓库的 issue、PR、discussion、commit message
- 为什么强：
  - 最接近“证据链”
  - 能直接看到“谁用 Fable 5 做了什么”“产出了什么”“有没有返工”
  - 有时甚至能看到“Action by Claude Fable 5”这种非常硬的执行痕迹
- 适合挖什么：
  - 非模型公司的真实应用样本
  - 真正落地的工程动作，而不是感想文
  - agentic / harness / review / rollout pattern
- 当前强信号例子：
  - `ForumHFR/redface2` issue 里直接写 `Action par Claude Fable 5`

### 3. 公司工程博客 / 产品团队博客

- 代表：
  - 公司 engineering blog
  - founder / staff engineer 的 build in public 博客
- 为什么强：
  - 这类内容最容易带组织上下文
  - 能看出它到底是个人爽文，还是团队级 workflow 变化
- 适合挖什么：
  - `run_公司_名字`
  - 团队角色分工变化
  - Fable 5 在非模型公司里的真实位置

---

## B 档：AI-native 团队媒体池

### 4. Every

- 站点：
  - `every.to`
  - `Source Code`
  - `Context Window`
  - `Chain of Thought`
  - `AI & I`
- 为什么它特别值得看：
  - 它不是普通媒体，更像“边做边公开 workflow 的 AI-native 团队”
  - 同一主题会在团队文章、访谈、周报、产品实验里反复出现
  - 很容易从一篇文章扩到一串人物和一整个组织方法
- 它最适合挖什么：
  - Fable 5 用后感
  - 角色差异：增长、平台、咨询、应用 AI、产品负责人分别怎么用
  - 组织级模式：谁负责定义任务、谁负责 review、谁负责 compound
- 当前已经挖出的强样本：
  - Austin Tedesco
  - Kieran Klaassen
  - Willie Williams
  - Mike Taylor
  - Nityesh Agarwal
- 额外说明：
  - `Every` 值得长期盯，因为它经常不是“发布一次就结束”，而是后面还会追加 camp、podcast、知识库回顾、方法论总结

---

## C 档：高密度讨论池

### 5. Hacker News

- 站点：
  - `news.ycombinator.com`
- 为什么强：
  - 新模型一出来，老工程师、创始人、基础设施派、怀疑派都会第一时间冒出来
  - 非常适合看“首波共识”和“首波争议”
- 它最适合挖什么：
  - 大家最在意什么：价格、速度、限制、数据保留、模型策略
  - 哪些外部链接被反复提到
  - 哪些名字/项目/工具在讨论中被自然带出来
- 它不太适合什么：
  - 不适合直接当人物样本来源
  - 噪音大、立场多、容易吵架
- 使用方式：
  - 把它当“雷达站”，不是当“资料库正文”

### 6. LessWrong

- 站点：
  - `lesswrong.com`
- 为什么强：
  - 高手密度高，而且愿意写长文
  - 很适合看系统卡、安全边界、能力断点、成本与约束
- 它最适合挖什么：
  - 高认知密度的模型评估
  - “什么时候不用 Fable 5” 这类负向判断
  - 高水平用户的个人基准和实际体感
- 它不太适合什么：
  - 不一定总能落到 coding workflow 细节
  - 更像分析池，不总是落地池
- 当前强信号例子：
  - Zvi 的 `Claude Fable 5 and Mythos 5: The System Card`

---

## D 档：待持续观察池

### 7. Lobsters

- 为什么值得盯：
  - 人少但更工程化，理论上噪音比 HN 小
- 当前状态：
  - 这轮没有撞到特别强的 Fable 5 线索
- 结论：
  - 保留为观察池，不作为当前主战场

### 8. Reddit

- 为什么值得盯：
  - 新模型热度高时会有很多使用体感
- 当前状态：
  - 公开搜索里这轮没冒出高信号的 Fable 5 工程样本
- 结论：
  - 偶尔扫一眼可以，但不适合当主来源

### 9. Latent Space / Interconnects / 其他 AI 评论型站点

- 为什么值得盯：
  - 有时会有非常好的二手综述和高质量访谈
- 当前状态：
  - 这轮没有直接撞上特别硬的 Fable 5 条目
- 结论：
  - 更适合当补充，不适合当第一入口

---

## 怎么用这张地图

### 如果目标是找“新人物”

- 先从 `Every`、独立博客、GitHub 开始
- 再用 `Hacker News` 和 `LessWrong` 反查哪些人/项目正在被高手提到

### 如果目标是找“新方法”

- 先看 `Every`
- 再看 `Simon Willison`
- 再看 `LessWrong`

### 如果目标是找“真落地证据”

- 先看 `GitHub`
- 再看公司工程博客
- 再看个人长文里的代码、截图、命令、PR 叙述

---

## 收录规则

- 明确是 `Fable 5` 用后感、工作流、组织变化的，优先进入 `fable5_field_signals/`
- 不是 `Fable 5` 专属，但 agentic / context engineering / harness engineering 价值很高的，进入 `agentic_field_signals/`
- 只会喊“很强”“很快”“太惊艳了”的，不单独立目录
- 能提供具体任务、角色、边界、限制、证据的，优先立目录

---

## 当前最值得长期盯的池子

1. `Every`
2. `Simon Willison`
3. `GitHub Issues / PR / Discussions`
4. `Hacker News`
5. `LessWrong`
