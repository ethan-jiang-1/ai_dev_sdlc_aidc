# 30-runs — 本仓库自举 bundle 归档 + pilot 索引（append-only）

> 结构裁决（ADR `../10-spec/adr/2026-09-21-stateless-auditor-run-bundle.md`）：**run bundle 归属被测仓库**。
> 本目录只收两样东西：① 本仓库自身自举审计的 bundle（被测对象就是本仓库，bundle 随仓库走）；
> ② 外部仓库 pilot 的 **索引**（指针，不复制内容）。评估系统运行期对被测仓库之外零写入。

## 内容

| 东西 | 说明 |
|---|---|
| `<日期>-ai-dev-sdlc-aidc-<harness>[-pilot]/` | 本仓库自举审计 bundle，格式见 [`../20-instruments/bundle-format.md`](../20-instruments/bundle-format.md) |
| `pilot-index.md` | 外部 repo pilot 的登记表：bundle 路径指针 + 一行摘要（供 framework §4.4 校准取数） |

## 规矩

- append-only：落盘不改原文；重评开新目录，旧 bundle 留作本仓库的时间线。
- 外部仓库的审计**不落这里**——bundle 在各自仓库的 `agent-friendly-runs/`，此处只留指针。
- 本仓库自举的第一个 run = checklist-A 落条后的自举试测（见 `../CURRENT.md` 下一步 3），目前为空。
