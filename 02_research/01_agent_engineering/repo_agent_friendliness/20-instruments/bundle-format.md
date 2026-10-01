# bundle-format — run bundle 格式规范（审计员产出物的模具）

> 权威来源：结构裁决见 [`../10-spec/adr/2026-09-21-stateless-auditor-run-bundle.md`](../10-spec/adr/2026-09-21-stateless-auditor-run-bundle.md)。
> 本文件定义 run bundle 的规范形态。**没有 manifest 的 bundle 无效。**

## 1. 放置规则（bundle 归属被测仓库）

- **默认**：`<目标仓库>/agent-friendly-runs/<YYYY-MM-DD>-<目标仓库名>-<harness集>[-pilot]/`
- 目标仓库**只读红线**的例外只有两个：本 bundle 的写入，与 tier-2 演练的**一次性 worktree/克隆**（结束即删、不动主干与远程，痕迹只进 bundle 采证记录——ADR 无状态评估器裁决 5）；除此之外目标仓库一个字节都不动。
- 无写权限（第三方仓库）→ 把 bundle 交付用户放置，报告顶部注明存放位置。
- 本仓库（评估系统自身）的自举审计：bundle 落本仓库根 `agent-friendly-runs/`——与外部目标同一规则，无特例（v1.6 修订，原 `30-runs/` 特例已废）。
- `-pilot` 后缀标记校准试测（framework §4.4）；正式审计不带。

## 2. bundle 内容

```
<YYYY-MM-DD>-<目标仓库名>-<harness集>[-pilot]/
├── manifest.md      先写。钉住本轮全部版本事实
├── report.md        评估报告
└── criteria.md      仅 pilot：外部效标数据（喂 §4.4 权重校准）
```

## 3. manifest.md 模板

```markdown
# Run Manifest
- date:            YYYY-MM-DD
- target_repo:     <名>（<URL 或本地路径>，观测日期 <日期>）
- bundle_home:     <本 bundle 所在仓库与路径——按 ADR，bundle 属于被测仓库>
- archetype:       A | B（分型理由一句话）
- form:            定义层评审版 | 正式审计
- spec_version:    repo_agent_friendliness @ <本系统 git commit hash>
- instruments:     checklist-A/B <版本或"未落条">；harness-profiles <版本或"未建">
- harnesses:       <harness 名及版本，逐个列>
- model:           <执行评估的模型标识>
- scope_excluded:  <未覆盖的维度/判据及原因>
```

## 4. report.md 模板

```markdown
# Repo Agent-Friendliness 评估报告 · <目标仓库名>
> manifest：见同目录 manifest.md；形态：<A/B>；性质：<定义层评审版/正式审计>
> B 形态：按双路径评级域分节呈现——"开发时路径 / 运行时路径"各自给分维结果与评级，不合并（framework §3.5、ADR 度量语义 D6）

## 1. 门禁判定（维度⑤）
<任一 ❌ → 总评 D 级，门禁 ❌ 全列于此；有 ⚠️ 无 ❌ → 总评封顶 B，⚠️ 列于此（framework §4.2）>

## 2. 分维结果（①②③④⑥⑦⑧⑨）
| 维 | 判据族要点 | 得分 | 证据（probe 实际观察） |
每条 ⚠️/❌ 必须附证据；无证据不打分。得分按映射 ✅=1.0/⚠️=0.5/❌=0.25 与短板制 §4.3 计算。
N/A 条目列于此并给理由（条件判据，framework §4.1 / ADR D5）；观察项（B 线探索级）单列、不计分。

## 3. 总评
- **评级（A–D）**：<按 framework §4.2 刻度：门禁 + 最弱维；校准前可用；整维全 N/A 的维不参与刻度并标注>
- 加权数值分：<权重未定型 → 写"按 framework §4.4 留空">

## 4. 整改清单
<排序：⑤ ❌ 置首 → 门禁 ⚠️ 次段 → 其余 ❌ 按维度短板分升序 → ⚠️ 随其维；每条附判据 id 与依据>

## 5. 采证记录
<tier-0/1/2 各做了什么；tier-2 写明抽样对象与数量，演练含 worktree/克隆的创建与删除记录（ADR 无状态评估器裁决 5）；tier-0/1 引用原始命令输出>
```

## 5. 证据与可复现约定

- tier-0/1 的证据必须是命令/脚本的**原始输出引用**（framework §3.2，ADR 度量语义 D4），不得转述。
- append-only：bundle 落盘后不改原文；勘误以新文件追加（`report-v2.md`）。目标仓库改版后的重评 = 新日期新目录，旧 bundle 留作时间线。
- 跨仓库横向比较/校准取数：bundle 的 **manifest 即分布式登记表**，无需常设索引；校准时把各目标仓库的 manifest 临时聚合，工作清单放仓库根 `.tmp-` 刮擦区（本仓库既有纪律），用完即弃——运行时状态不入系统。
