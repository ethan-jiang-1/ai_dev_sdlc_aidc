# 10-dimensions — 维度定义层（一维一文件）

九个维度（v1.3 起），每个一个 MD，序号连续 01–09。当前权威定义总表见 [`../00-framework-v1.md`](../00-framework-v1.md) §3.4；本目录是各维的展开定义，checklist-v1 的判据按维归入。

| # | 文件 | 维度 | 角色 |
|---|------|------|------|
| 01 | [01-context-supply.md](01-context-supply.md) | 上下文供给与预算 | 加权 |
| 02 | [02-verifiability-and-proof.md](02-verifiability-and-proof.md) | 可验证性与证明 | 加权 |
| 03 | [03-executable-environment.md](03-executable-environment.md) | 可执行环境（冷启动） | 加权 |
| 04 | [04-modifiability-locality.md](04-modifiability-locality.md) | 可修改性 / 局部性 | 加权 |
| 05 | [05-safety-guardrails.md](05-safety-guardrails.md) | 安全护栏 | **门禁** |
| 06 | [06-failure-recoverability.md](06-failure-recoverability.md) | 失败可恢复性 | 加权 |
| 07 | [07-instruction-asset-metabolism.md](07-instruction-asset-metabolism.md) | 指令资产新陈代谢 | 加权 |
| 08 | [08-drift-governance.md](08-drift-governance.md) | 漂移治理（SDD） | 加权 |
| 09 | [09-vcs-collaboration.md](09-vcs-collaboration.md) | 版本控制与协作面 | 加权（B 下一等） |

每个维度文件的固定结构：核心问题 / 为什么独立成维 / 边界声明 / 判据族 / 依据 / 泛化注意 / 开放问题。

**增维或改边界时**：先过目录 README 的正交纪律（宁拆不混、边界成文、同词异义拆开），再改本表与 `00-framework-v1.md` §3.4，两处必须同步。
