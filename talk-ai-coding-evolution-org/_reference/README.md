# `_reference/` —— 上游原始数据（只读素材）

本目录统一收纳 talk 的上游**原始数据** symlink，与 `../talk-ai-coding-evolution-opc/_reference/` 指向**同一批源**
（只读，只在里面读、不在里面写）。本 talk 的推敲产物（故事线 / 证据 / 大纲 / 讲稿）都在
`talk-ai-coding-evolution-org/` 下各自编号目录里，`_reference/` 只是它们的**上游来源**。

## symlink 一览

| symlink | 指向 | 装了什么 | 在 org talk 里干什么 |
|---|---|---|---|
| `rawdata_ai-coding-evolution-final/` | `ai_tool_deepresearch/dpt_rb_ai-coding-evolution/final` | 五层演变**最终研究报告** | 宏观故事线 / 论点骨架（①） |
| `rawdata_dsh-faq-on-digested/` | `deepseek-harness/_faq_on_digested` | DSH Harness 机制**二次研究问答** | Harness 层实证（②） |
| `rawdata_dsh-digested/` | `deepseek-harness/_digested` | DSH 源码**消化分析** | 第四幕"治理边界"的底层证据（③） |
| `rawdata_dsh-plugin-business-ladder/` | `deepseek-harness/_faq_on_digested/09_plugin-business-ladder` | 插件收益阶梯 | 组织可验证的能力组合 |
| `rawdata_dsh-plugin-ecosystem-distribution/` | `awesome-dsh-plugin/_faq_on_digested/01_ecosystem-distribution` | 插件生态分布快照 | 扩展面信号与口径边界 |
| `rawdata_dsh-plugin-seam-maturity/` | `deepseek-harness/_faq_on_digested/08_plugin-seam-maturity` | 插件接缝与成熟度 | 合同、门禁、事实记录（治理机制） |
| `rawdata_anthropic-ai-native-sdlc-playbook.md` | 本仓库 `02_research/anthorpic_ai_sdlc/org/ai-native-sdlc-playbook.md` | Anthropic 官方 **AI-Native SDLC Playbook** 全文（英文原版） | 组织级 AI-native SDLC 的官方实践蓝本：闭环 + 六阶段 + 治理门禁（对照锚点） |

前三份主源分工：① 讲"为什么和往哪走"，② 讲"具体长什么样"，③ 讲"底层机制怎么实现"。
后三份专题源只补生态、收益与成熟度证据。Anthropic Playbook 是**组织视角的官方对照物**：同讲"闭环 + 六阶段 + 人在门禁"，可作为 org talk 论点的官方背书（注意：它是 Claude 生态实现，引用时类比而非照搬）。

## 引用约定

- 从 `talk-ai-coding-evolution-org/` 任意子目录引用素材，统一走本目录相对路径：
  `../_reference/rawdata_*/…`。
- 简写：`final_v4/…` = `rawdata_ai-coding-evolution-final/final_v4/…`；`FAQ 0N` = `rawdata_dsh-faq-on-digested/0N_*`；
  `_digested/…` = `rawdata_dsh-digested/…`。

## 规则

- **只读**：这里是原始数据，只在里面读、不在里面写；有口径调整写进 `02_evidence/`。
- symlink 指向工作区外，绝对路径失效时（迁移机器 / 目录改名）请在本目录重建或更新 symlink。
- **org 视角**：引用同一批源，但摘录落点要服务于"组织分工 + 治理"，不照搬 `-opc` 的个人视角卡片。
