# 30-runs — 运行层（L-instance 归档，只增不改）

每次审计一个子目录，**append-only**：报告落盘后不修改原文（勘误以新版本文件追加，如 `report-v2.md`），spec/器械变更不回写历史报告——历史报告靠 manifest 自证当时依据。

## 目录命名

```
YYYY-MM-DD-<目标仓库名>-<harness集>[-pilot]/
├── manifest.md   先写。没有 manifest 的报告无效
└── report.md     评估报告
```

`-pilot` 后缀标记校准试测（framework §4.4 效标回归的采数 run）；正式审计不带后缀。目标仓库名只用短名，不含路径分隔符。

## manifest.md 模板

```markdown
# Run Manifest
- date:            YYYY-MM-DD
- target_repo:     <名>（<URL 或本地路径>，观测日期 <日期>）
- archetype:       A | B（分型理由一句话）
- form:            定义层评审版 | 正式审计
- spec_version:    repo_agent_friendliness @ <本仓库 git commit hash>
- instruments:     checklist-A/B <版本或"未落条">；harness-profiles <版本或"未建">
- harnesses:       <harness 名及版本，逐个列>
- model:           <执行评估的模型标识>
- scope_excluded:  <未覆盖的维度/判据及原因>
```

## report.md 模板

```markdown
# Repo Agent-Friendliness 评估报告 · <目标仓库名>
> manifest：见同目录 manifest.md；形态：<A/B>；性质：<定义层评审版/正式审计>

## 1. 门禁判定（维度⑤）
<任一 ❌ → 整体 D 级；所有门禁 ❌ 列于此>

## 2. 分维结果（①②③④⑥⑦⑧⑨）
| 维 | 判据族要点 | 得分 | 证据（probe 实际观察） |
每条 ⚠️/❌ 必须附证据；无证据不打分。

## 3. 加权分
<权重未定型 → 写"按 framework §4.4 留空">

## 4. 整改清单
<排序：⑤ ❌ 置首 → 其余 ❌ 按维度短板分升序 → ⚠️ 随其维；每条附判据 id 与依据>

## 5. 采证记录
<tier-0/1/2 各做了什么；tier-2 写明抽样对象与数量>
```

## 效标数据（pilot run 专用）

pilot run 除 report 外，另存 `criteria.md`：真实 agent 会话的任务完成率、返工轮数、token 消耗、绕过/放弃点（采法承 framework §4.4）。这是日后权重校准的唯一数据源，缺了 run 就白跑。
