# `_reference/` —— 三份原始数据（只读素材）

本目录统一收纳 talk 的三份**原始数据** symlink。它们指向工作区外的只读素材，
**只在里面读，不在里面写**。本 talk 的推敲产物（故事线 / 证据 / 大纲 / 讲稿）都在
`talk-ai-coding-evolution/` 下各自编号目录里，`_reference/` 只是它们的**上游来源**。

## 三个 symlink 一览

| symlink | 指向（绝对路径） | 装了什么 | 在 talk 里干什么 |
|---|---|---|---|
| `rawdata_ai-coding-evolution-final/` | `ai_tool_deepresearch/dpt_rb_ai-coding-evolution/final` | 五层演变**最终研究报告**（`final_v4.md` + `final_v4/` 六个 era 章节） | 宏观故事线 / 论点骨架（①） |
| `rawdata_dsh-faq-on-digested/` | `deepseek-harness/_faq_on_digested` | DSH Harness 机制**二次研究问答**（`01_repository-organization` … `07_borrowing-harness-idea`） | Harness 层的 "show, don't tell" 实证（②） |
| `rawdata_dsh-digested/` | `deepseek-harness/_digested` | DSH 源码**消化分析**（`system` / `composition` / `session-and-loop` / `capability-seams` / `tools-prompt-llm` / `surfaces` 等） | 第四幕"灵活性"的底层证据（③） |

三者分工：① 讲"为什么和往哪走"（宏观弧线），② 讲"具体长什么样"（机制问答），
③ 讲"底层机制怎么实现"（源码消化）。详见 `../README.md`「三份原始数据是什么」。

## 引用约定

- 从 `talk-ai-coding-evolution/` 任意子目录引用素材，统一走本目录相对路径：
  `../_reference/rawdata_*/…`（例如 `03_outline/` 下写 `../_reference/rawdata_dsh-digested/tools-prompt-llm/00-map.md`）。
- 素材索引里常见的简写：`final_v4/…` = `rawdata_ai-coding-evolution-final/final_v4/…`；
  `FAQ 0N` = `rawdata_dsh-faq-on-digested/0N_*`；`_digested/…` = `rawdata_dsh-digested/…`。
- 每张证据卡片 / 页面素材都标注来源路径（见 `../02_evidence/README.md`）。

## 规则

- **只读**：这里是原始数据，只在里面读，不在里面写；有口径调整写进 `02_evidence/`，不要改源文件。
- symlink 指向工作区外，绝对路径失效时（迁移机器 / 目录改名）请在本目录重建或更新 symlink。
