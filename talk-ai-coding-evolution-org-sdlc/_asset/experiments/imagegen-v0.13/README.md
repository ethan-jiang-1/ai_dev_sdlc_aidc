# GPT Image 2 v0.13 非样片页重构实验

本轮不是为既有图元增加装饰，而是验证非样片页面能否由“概念占位”变成真正承担论证的图文主体。

使用工作区 `.env` 当前 `IMAGE2_*` 配置，经 Packy 主入口调用 `gpt-image-2` CLI，尺寸 `2048x1152`，质量 `high`。密钥未写入目录。

## 入选资产

- `generated/p6-pressure-migration-alpha.png`：等待转移、控制失配和例外增加成为同一个压力迁移场景。
- `generated/p30-execution-authorization-alpha.png`：proposal 与 production 物理断开，执行时授权令牌临时闭合通路。
- `generated/p35-production-feedback-alpha.png`：生产事实进入诊断，形成 `intent.md` 并回到受控闭环；人的判断在闭环之上。
- `generated/p43-authority-collage-alpha.png`：碎片知识收敛为权威事实，ADR 与未选方案保留理由和负知识。

P35、P43 的第一轮输出因擅自加入阶段名、代理名、日期和版本而被否决；入选版本是第二轮，确保只有 prompt 指定的文字可读。所有入选资产经 chroma 提取为真实透明 PNG，进入 `_asset/samples/v0.13/` 的视觉证明稿。

## 提示词

- `p6-pressure-migration-prompt.txt`
- `p30-execution-authorization-prompt.txt`
- `p35-production-feedback-prompt-v2.txt`
- `p43-authority-collage-prompt-v2.txt`

Visual Master Language 仍为工程素描 + 编辑标注；未切换到 3D 玩具、纸模或微缩建筑语言。
