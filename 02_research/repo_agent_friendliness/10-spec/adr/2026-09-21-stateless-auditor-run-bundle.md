# ADR 2026-09-21 · 无状态评估器与 run bundle 归属

> 状态：已裁决（v1.5 起生效）。用户定调：**评估系统是 read-only 的**——评估任何 repo，run bundle 存在那个 repo，需要的 数据都在那边，而不是在本系统这边。
> 关联：[`../framework.md`](../framework.md) §1/§4.4/§7、[`../../20-instruments/bundle-format.md`](../../20-instruments/bundle-format.md)、[`../../30-runs/README.md`](../../30-runs/README.md)、目录 [`../../AGENTS.md`](../../AGENTS.md)。

## 背景

v1.4 及之前的调用契约是"目标仓库只读，一切写入落本目录 `30-runs/`"。这使评估器成为有状态的数据收集器，有三个结构性问题：

1. **数据重力错位**：run 证据描述的是目标仓库，却与目标分离——目标仓库的克隆者看不到审计史，目标仓库自身的 git 时间线（分数随版本的演变）无法利用。
2. **污染与泄漏**：外部仓库的内部问题证据沉积进本系统仓库，随被测数量无限膨胀，且把他家隐私问题清单带进自家 git。
3. **系统纯净性**：评估器混入"数据保管者"角色后，运行期就要写自家目录，"仪器"与"档案柜"两种职责互相干扰。

## 裁决

1. **评估器运行期零状态、零写入**：一次评估运行中，本系统目录不被写入；系统只在**体系演进**（改 spec/instruments）时才被写。
2. **run bundle 归属被测仓库**：默认落 `<目标仓库>/agent-friendly-runs/<YYYY-MM-DD>-<harness集>[-pilot]/`（manifest + report + 效标数据，格式规范见 `20-instruments/bundle-format.md`）。对目标仓库唯一的允许写入就是这个 bundle；无写权限（第三方仓库）则把 bundle 交付用户放置。
3. **`30-runs/` 收窄为"本仓库自己的 bundle 归档 + pilot 索引"**：本仓库自举审计的 bundle 随本仓库走，自然落这里（与裁决 2 一致——"那边"恰好是这边）；外部 repo 的 pilot bundle 留在各自仓库，此处只登记 `pilot-index.md`（路径指针 + 一行摘要）供 §4.4 校准取数，不复制内容。
4. **bundle 格式规范升为器械层组件**：manifest/report 模板、证据引用约定、放置规则，从 30-runs README 移入 `20-instruments/bundle-format.md`——它是审计员产出物的模具，属仪器不属于档案柜。

## 后果

- `AGENTS.md` 调用契约与仪式第 3/7 步改写（写入位置、铁律重述）。
- framework §1（L-instance 归属）、§4.4（试点取数方式）、§7（自举条目措辞）同步；版本 v1.5。
- line-b §6.3 的外部试点改为"bundle 落目标仓库 + 索引登记"；line-a §5.3 自举不变。
- 跨仓库横向比较不再有天然的集中数据集——校准靠 pilot-index 聚合，接受这一成本（换取纯净性与数据重力正确）。

## 变更记录

- v1（2026-09-21）：初版，四条裁决。
