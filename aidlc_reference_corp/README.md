---
type: index
content_type: readme
directory: aidlc_reference_corp
description: 企业/厂商/分析机构的 AIDLC 参考材料——AWS 方法论 + 生态全景
---

# aidlc_reference_corp — 企业与生态参考材料

> 两个子目录：AWS 官方 AI-DLC 方法论 + 非 AWS 生态全景（Google、Microsoft、Gartner、分析机构、社区）

---

## 子目录

| 目录 | 内容 | 来源类型 |
|---|---|---|
| `_raw_aws/` | AWS AI-DLC 方法论：三阶段模型、14-Node AgentCore、开源实现、v2 Preview | **厂商一手材料**（AWS 官方博客、GitHub、合作伙伴白皮书） |
| `_raw_ecosystem/` | 非 AWS 生态全景：Google/Microsoft/Gartner/Forrester/Atlassian/学术/社区/声称验证 | **混合**（厂商、分析机构、学术、社区） |

---

## 与相邻目录的关系

```
aidlc_reference_corp/     ← 企业/厂商/分析机构（你在这里）
  ├── _raw_aws/           ← AWS 官方方法论
  └── _raw_ecosystem/     ← 多厂商 + 分析机构 + 社区全景

aidlc_reference_kol/      ← 人物与事件（影响力个体 + 线下聚会）
  ├── _raw_kol/           ← 14 位影响力人物深度拆解
  ├── _raw_frontier/      ← 跨公司变革共识合成
  ├── _raw_fable5/        ← Fable 5 模型变革信号合成
  ├── _raw_promatic_summit_2026/    ← Pragmatic Summit 2026
  ├── _raw_agile_manifesto_2026/    ← Deer Valley Retreat 2026
  └── _raw_engelberg_2026/          ← Engelberg Retreat 2026
```

**`aidlc_reference_corp`** 是**组织视角**——公司、厂商、分析机构在说什么。
**`aidlc_reference_kol`** 是**个体视角**——人、对话、事件在说什么。

---

## 源头特征对比

| | `_raw_aws/` | `_raw_ecosystem/` |
|---|---|---|
| **偏向性** | 强（AWS 的产品输出） | 混合（已做一轮对抗性验证） |
| **可信度** | 高（官方发布，可公开访问） | 分层——claim_verification 文件是可信度最高的 |
| **URL 状态** | 大部分有 `## 来源` URL | 不一致——claim_verification 文件有完整 URL，03/04/05 文件缺 URL |
| **处理建议** | 用于理解 AWS 的框架设计逻辑 + 开源实现参考 | 优先看 claim_verification* 文件；社区反应和三方文章作为背景 |

---

## 当前状态

- `_raw_aws/`：6 个内容文件 + README + figures/。有 `## 来源` 节但缺少 frontmatter
- `_raw_ecosystem/`：11 个内容文件 + README + figures/。部分文件缺少外部 URL（03/04/05/07）
- 待办：frontmatter + URL 溯源（与 `aidlc_reference_kol` 下的文件同样的处理标准）
