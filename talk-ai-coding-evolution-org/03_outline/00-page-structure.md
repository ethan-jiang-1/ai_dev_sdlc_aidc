# Talk 页面结构（现场版 v0.5 · 50 页 · 75–90 min · SDLC 主轴 + 引子）

> **A 档单场加长**。主轴 = SDLC 六阶段；五层 + DSH 作「引子」在自然接点插入，不强扭成独立章节。
> 每页 play 细则见 `../02_evidence/00-absorption-plan.md`。

## 开场（~6 min · P1–P5）

| 页 | 页面结论 | 引子 |
|---|---|---|
| P1 | 封面 | — |
| P2 | 代码产出翻倍，交付没快 | — |
| P3 | 转型对象是整条 SDLC，不是编码 | — |
| P4 | 五层预告：Prompt→Context→Harness→Loop→Graph 会沿 SDLC 亮相 | 五层 |
| P5 | **harness 先立住：模型给能力，harness 给可靠性** | Harness |

## 第一幕：为什么整条 SDLC 要转型（~10 min · P6–P12）

| 页 | 页面结论 |
|---|---|
| P6 | 代码不再是瓶颈 → 三个后果 |
| P7 | 传统 SDLC 的控制假设：每一步都是人做的 |
| P8 | 传统控制失效：逐行 review 崩了、治理成本上升 |
| P9 | 转型 = 从「人执行」到「harness 执行 + 人守 gate」 |
| P10 | 贯穿主线：工件链 = 审计链 |
| P11 | 六阶段 shifts 总表（传统 vs AI-native） |
| P12 | 引子地图：五层在六阶段的落点 |

## 第二幕：六阶段转型（~52 min · P13–P38）

| 页 | 阶段 | 页面结论 | 引子 |
|---|---|---|---|
| P13 | 总览 | AI-native SDLC = loop；工件链接力 | — |
| P14 | **Plan** | 引子：Plan 的本质 = Prompt | Prompt |
| P15 | Plan | intent.md：意图一次捕获 | — |
| P16 | Plan | 治理与度量：merge=accept，存活率 | — |
| P17 | **Design** | 引子：Design 的本质 = Context | Context |
| P18 | Design | spec.md + skills：政策在写 spec 时就施加 | — |
| P19 | Design | 治理：spec+prompt+skill 版本全进库 | — |
| P20 | **Build** | 引子：Build 的本质 = Harness（圈住/拦住/看清） | Harness |
| P21 | Build | plan.md：计划先于代码 | — |
| P22 | Build | AGENTS.md + skills：制度知识外置 | Context |
| P23 | Build | hooks：确定性 guardrail | Harness |
| P24 | Build | 并行会话 + 子 agent | Graph 雏形 |
| P25 | Build | 小结：harness 主战场 | — |
| P26 | **Test** | 引子：Test 的本质 = Sensors + Loop 起点 | Harness+Loop |
| P27 | Test | feedback loop：会话自己验证 | — |
| P28 | Test | evals：对 harness 配置的回归测试 | — |
| P29 | Test | 治理：确定性门禁 | — |
| P30 | **Deploy** | 引子：Deploy 的本质 = 拦住/看清 + authorize at execution | Harness |
| P31 | Deploy | PR review：职责分离 | — |
| P32 | Deploy | hooks as gates + managed settings | — |
| P33 | Deploy | CI/CD：提议/执行分离 | — |
| P34 | Deploy | 小结：生产 gate 由 hook 强制 | — |
| P35 | **Maintain** | 引子：Maintain 的本质 = Loop 收口 + Graph 编排 | Loop+Graph |
| P36 | Maintain | 关 loop：control-band → intent.md | — |
| P37 | Maintain | scans：定时扫描走同一 gate | — |
| P38 | Maintain | on-call：channel 即审计 | — |

## 第三幕：DSH + 治理收束（~24 min · P39–P48）

| 页 | 页面结论 |
|---|---|
| P39 | 工件链 = 审计链（收束） |
| P40 | 人守 gate + 确定性优先 |
| P41 | 引子：DSH 如何帮助流程——三条腿（知识外置 / 正确路径 / 可执行反馈） |
| P42 | DSH = 可组合 harness runtime：插件图 + 事件流 + loop |
| P43 | 知识外置：一个事实一个 owner、负知识外置 |
| P44 | 正确路径 + 参与阶梯：分层参与、各有门与合同 |
| P45 | 可执行反馈 + 门禁：门禁本身被测试、invariant |
| P46 | 定制/替换：capability seam 三角色——换后端 Consumer 不改 |
| P47 | 审计与重建事实：append-only + asked/decided + fail-closed |
| P48 | 四项治理决定 + 组织怎么落地 + 度量总表 |

## 收尾（~4 min · P49–P50）

| 页 | 页面结论 |
|---|---|
| P49 | 带走一句：代码不再是瓶颈，流程才是 |
| P50 | 谢谢 |

## 叙事检查

1. P4–P5 先把五层预告 + harness 立住；P12 再给「引子地图」，让听众知道五层会怎么沿 SDLC 亮相。
2. P6–P12 论证为什么整条 SDLC 要转型；P10 埋工件链主线。
3. P13–P38 是主轴：每阶段一个「引子」点破本质，再讲机制/治理/度量。
4. P39–P48 收束：工件链/审计/DSH 三条腿/落地；P49 回到开场。

## 口径红线

- 见 `../02_evidence/00-absorption-plan.md` §三（「代码不再是瓶颈」是 Anthropic 论点；playbook 是 Claude 视角；DSH 不是 MCP）。
