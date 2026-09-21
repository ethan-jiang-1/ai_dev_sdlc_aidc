# 20-instruments — 器械层（判据 operational 化 + 扫描工具）

spec（`../10-spec/`）回答"体系是什么"；本目录回答"拿什么去测"。器械变更不改 spec；spec 变更时器械跟着升版本，已存 runs 的可比性影响记录在 `CURRENT.md`。

## 规划中的组件

| 文件/目录 | 内容 | 状态 |
|---|---|---|
| `checklist-a.md` | 形态 A 逐条判据（tier-0/1 优先、⑧挂条件判据、每条带 probe/pass/tier/basis/sampling） | 待建，来源：A 线定义 §5（[`../10-spec/line-a-traditional-repo.md`](../10-spec/line-a-traditional-repo.md)） |
| `checklist-b.md` | 形态 B 逐条判据（②⑥⑦⑧⑨ B 子族优先、逐条标共识/探索） | 待建，来源：B 线定义 §6（[`../10-spec/line-b-agentic-repo.md`](../10-spec/line-b-agentic-repo.md)） |
| `harness-profiles.md` | 各 harness 消化机制事实（指令载体、注入时机、预算、静默失败模式），harness-specific 判据落此不进 L-core | 待建 |
| `scan/` | tier-0 扫描脚本（机器可判条目自动化，可进 CI 常驻） | 待建 |

## 纪律

- 判据一律行为描述，不含任何仓库锚点；harness-specific 参数（如行数建议、扩展名要求）标观测日期与复验条件。
- ①④⑨ 共享表面条目互相注明归属，防双算（见各维"泛化注意"）。
- checklist 落条时同步回填各维文件的"判据族（草案）"小节为指针，不复制正文。
