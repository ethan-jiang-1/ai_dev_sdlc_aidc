# mclayer / plugin-codeforge

- 身份：`mclayer/plugin-codeforge` 公开仓库；主要执行者是维护者 `mccho-mclayer`
- 角色定位：不是模型公司样本，而是一个公开工程系统在 GitHub 上明确编排 Fable 5 采用策略的 maintainer / workflow 样本
- 为什么值得单列：它不是泛泛而谈“Fable 很强”，而是把 Fable 5 限定到 10 个 agent 角色上做 surgical adoption，并写清楚哪些角色不用、为什么不用
- 核心贡献：把“最强模型不该默认全上”这件事制度化，拆成 agent lane、版本 floor、fallback、retro gate 和治理边界
- 最重要的判断：Fable 5 只在 `chief-author / long-horizon / adversarial` 这类高价值角色上值得采用，其他位置继续留给更便宜或更稳的模型

## 这条样本到底说明了什么

- 这条线最有价值的地方，不是“他们支持了 Fable 5”，而是他们明确写了只做 **surgical adoption**。
- issue `#2134` 里把目标角色限定为 10 个 agent，覆盖 design / develop / review / requirements 四条 lane，而不是把 orchestrator 或所有 worker 一把切过去。
- 他们还显式规定了 `Claude Code >= 2.1.170` 的兼容性 floor，说明这里不是单次试用，而是把 Fable 5 当成需要版本治理的运行时依赖。
- 更关键的是，Epic 后续状态更新里还继续补了 runtime fallback gap：当 Fable 运行时不可用时，自动 fresh respawn 到 `opus`，把“采用 Fable”这件事继续压回到治理链里。

## 最值得记住的判断

- 这里展示的不是“谁在夸 Fable 5”，而是“谁已经开始给 Fable 5 规定岗位、版本门槛和失败恢复路径”。
- 这正好补上了你这套资料库里目前还比较薄的一层：GitHub 上公开可复核的、带治理边界的 Fable 5 采用样本。

## 我的判断

- `plugin-codeforge` 值得保留，因为它同时满足几个硬条件：公开 issue / PR 痕迹、角色分配、成本判断、兼容性门槛、fallback 设计。
- 它不是 `Every` 那类“团队内部 workflow 口述”，而是更像“把 Fable 5 进生产编排体系的制度稿”。
- 这类样本对后续横向比较很有帮助，因为它能和 `Every` 线形成非常清楚的对照：前者更像组织口述 workflow，后者更像显式治理与 agent 角色编排。
