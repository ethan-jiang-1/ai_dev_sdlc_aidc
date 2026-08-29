# Talk 页面结构（现场版 v0.7 · 固定 50 页 · 75–90 min）

> **A 档单场加长，50 页已锁定**。主轴 = SDLC 六阶段；五层作深度镜头，DSH 作共享控制面的参考实现。
> 六阶段均回答四问：**工件是什么 / gate 在哪里 / owner 是谁 / feedback 怎么回流**。
> 每页 play 细则见 `../02_evidence/00-absorption-plan.md`。

## 开场（~6 min · P1–P5）

| 页 | 页面结论 | 引子 |
|---|---|---|
| P1 | 封面 | — |
| P2 | 当 Build 变快，端到端交付为什么没同步变快 | — |
| P3 | Anthropic 的诊断：瓶颈已从 Build 移向代码两侧 | — |
| P4 | 五层是观察外置与控制深度的镜头 | 五层 |
| P5 | **模型给能力，harness 给可靠性；组织要共建控制面** | Harness |

## 第一幕：为什么整条 SDLC 要转型（~10 min · P6–P12）

| 页 | 页面结论 |
|---|---|
| P6 | 代码不再是瓶颈 → 三个后果 |
| P7 | 传统 SDLC 是围绕「代码稀缺 + 人执行」设计的 |
| P8 | 产出与控制容量失配：要么排队，要么欠审 |
| P9 | 新控制模型 = 工件交接 + 机器守确定性 gate + 人守判断 gate |
| P10 | 工件链是审计的骨架，但还需身份、证据、审批与不可绕过的 gate |
| P11 | 六阶段 shifts 总表（传统 vs AI-native） |
| P12 | 全场导航：六阶段逐段回答工件 / gate / owner / feedback，五层说明控制深度 |

## 第二幕：六阶段转型（~48 min · P13–P38）

| 页 | 阶段 | 页面结论 | 引子 |
|---|---|---|---|
| P13 | 总览 | AI-native SDLC = loop；工件链接力 | — |
| P14 | **Plan** | Prompt 镜头：先把意图外置成可交接工件 | Prompt |
| P15 | Plan | intent.md：意图一次捕获 | — |
| P16 | Plan | 四问收口：intent / acceptance gate / product owner / survival + elapsed time | — |
| P17 | **Design** | Context 镜头：在 Build 之前把政策与矛盾外置 | Context |
| P18 | Design | spec.md + skills：政策在写 spec 时就施加 | — |
| P19 | Design | 四问收口：spec / concern gate / product+policy owner / rework | — |
| P20 | **Build** | Harness 镜头：把执行圈住、拦住、看清 | Harness |
| P21 | Build | plan.md：计划先于代码 | — |
| P22 | Build | AGENTS.md + skills：制度知识外置 | Context |
| P23 | Build | hooks：确定性 guardrail | Harness |
| P24 | Build | 并行会话 + 子 agent | Graph 雏形 |
| P25 | Build | 四问收口：plan+diff / build guardrails / engineer+platform / rework+plan match | — |
| P26 | **Test** | Sensors / Loop 镜头：同时验产品改动与 harness 配置 | Harness+Loop |
| P27 | Test | feedback loop：会话自己验证 | — |
| P28 | Test | evals：对 harness 配置的回归测试 | — |
| P29 | Test | 四问收口：test evidence / merge threshold / QA+config owner / pass+failure trend | — |
| P30 | **Deploy** | Harness 镜头：提议权与执行权在生产 gate 分离 | Harness |
| P31 | Deploy | PR review：职责分离 | — |
| P32 | Deploy | hooks as gates + managed settings | — |
| P33 | Deploy | CI/CD：提议/执行分离 | — |
| P34 | Deploy | 四问收口：PR+release evidence / production gate / code+release owner / wait+failure | — |
| P35 | **Maintain** | Loop / Graph 镜头：确定性触发让事实沿同一受控路径回流 | Loop+Graph |
| P36 | Maintain | 关 loop：control-band → intent.md | — |
| P37 | Maintain | scans：定时扫描走同一 gate | — |
| P38 | Maintain | 四问收口：incident / triage+PR gates / service owner / recurrence+recovery | — |

## 第三幕：共享控制面 + DSH 参考实现（~20 min · P39–P48）

| 页 | 页面结论 |
|---|---|
| P39 | 工件链加上身份、版本、证据、审批和不可绕过的 gate，才具备审计能力 |
| P40 | 机器守确定性 gate，人守判断 gate；两者都要可留痕 |
| P41 | DSH 作参考实现：知识外置 / 正确路径 / 可执行反馈 |
| P42 | 共享控制面需要同时回答「现在由什么组成」和「刚才做过什么」 |
| P43 | 知识外置：一个事实一个 owner、负知识外置 |
| P44 | 正确路径 + 参与阶梯：分层参与、各有门与合同 |
| P45 | 可执行反馈 + 门禁：门禁本身被测试、invariant |
| P46 | 定制/替换：capability seam 三角色——换后端 Consumer 不改 |
| P47 | 审计与重建事实：append-only + asked/decided + fail-closed |
| P48 | 四项治理决定 + 采用顺序：先工件 → 再 gate → 最后关 loop |

## 收尾（~6 min · P49–P50）

| 页 | 页面结论 |
|---|---|
| P49 | 带走一句：代码不再是瓶颈，流程才是 |
| P50 | 从最慢的一次交接开始：选一条价值流，补齐一个工件、一道 gate、一个 owner、一个 feedback |

## 叙事检查

1. P2 提出需要用自身数据验证的张力，P3 引入 Anthropic 诊断，P4–P5 只给深度镜头和共享控制面的必要性。
2. P6–P10 完成因果：瓶颈转移 → 旧控制失配 → 新控制模型 → 工件链只是审计骨架。
3. P12 建立全场四问；P13–P38 沿六阶段累计答案，P16/P19/P25/P29/P34/P38 分别收口。
4. P39 解开 P10 留下的条件，P40–P47 解释共享控制面如何工程化，P48 收成采用顺序。
5. P49 回答开场，P50 把论点变成一个可以在会后启动的试点选择。

## 口径红线

- 见 `../02_evidence/00-absorption-plan.md` §三（「代码不再是瓶颈」是 Anthropic 论点；playbook 是 Claude 视角；DSH 不是 MCP）。
