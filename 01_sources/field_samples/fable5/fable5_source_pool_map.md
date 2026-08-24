# Fable 5 来源池备忘

> 这份文档现在只保留采集视角。
> 如果你是来读内容的，请先看 `README.md`。
> 如果你是准备继续扩样本，再看这份备忘。

---

## 当前最值得长期盯的池子

1. `Every`
2. `Simon Willison`
3. `GitHub Issues / PR / Discussions`
4. `Hacker News`
5. `LessWrong`

---

## 这些池子各自适合挖什么

### `Every`

最适合挖：

- 组织级 workflow
- 同一团队里不同角色的用法
- 同一主题的后续跟进和追加总结

当前已经证明最值钱，因为一篇 Every 文章往往能扩成多个人物目录。

### `Simon Willison`

最适合挖：

- 真实 debugging 个案
- 行为证据
- sandbox / injection / transparency 边界

价值在于细节密、原话硬，而且常有 follow-up。

### `GitHub Issues / PR / Discussions`

最适合挖：

- 产品集成样本
- agent 编排 / rollout / fallback / review 证据
- 可复核的工程动作

这条线最接近“证据链”。

### `Hacker News`

最适合挖：

- 首波争议
- 被反复提到的人和项目
- 该继续去哪里深挖

把它当雷达站，不要直接当正文来源。

### `LessWrong`

最适合挖：

- 系统卡
- 限制与风险分析
- “什么时候不用 Fable 5” 这类负向判断

它更像分析池，不总是 workflow 正文池。

---

## 当前采集顺序

如果要继续找新样本，建议按这个顺序：

1. 先看 `Every` 有没有新增人物或 follow-up
2. 再扫独立博客，尤其是 `Simon Willison` 一类高密度作者
3. 再扫 GitHub 上公开可复核的 issue / PR / discussion
4. 用 `Hacker News` 和 `LessWrong` 反查有没有新的高信号名字

---

## 收录规则

- 明确是 `Fable 5` 用后感、工作流或组织变化的，优先进入 `fable5_field_signals/`
- 不是 `Fable 5` 专属，但 agentic / harness / context engineering 价值很高的，进入 `agentic_field_signals/`
- 只会喊“很强”“很快”“很震撼”的，不单独立目录
- 能提供具体任务、角色、边界、限制、证据的，优先立目录
