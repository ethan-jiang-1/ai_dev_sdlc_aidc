# R4 编排与并发（候选阶 ⏳）——交出任务分解与子代理调度权

> **状态**：**候选阶，不得进结论/对外文字**（[00-map](00-map.md) 判读：六源中仅中文传播层显式落位；
> Osmani/CC 阶梯止于触发方式，编排是框架实现层而非概念共识层）。升正式条件：Anthropic multi-agent 档案
> 给出与之一致或更好的交接面叙述（回源队列 #1），或 ≥2 概念源显式落位。

## 一、交接面（假设版，待回源检验）

人不再拆任务：把"一类活"连同**拓扑与预算**交出去——编排器分解任务、fan-out 子代理并发、合并节点汇总；
人的介入点从"单个循环"上移到"编排脚本的形状＋token/时间预算"。

## 二、支撑条目（自说明）

**① 中文传播层转述（侦察级，[evidence-t](../raw/evidence-2026-09-30-t-shenmejiaoqq-video-zh.md) §2）**：
> "系统会同时生成数十个子代理，一个去扒财报，一个去分析GitHub提交频率，一个去爬用户评论，它们同时开工，最后由一个合并节点把数据汇总。"
> "Agent A写代码，Agent B拿着需求文档逐行审查，发现遗漏直接打回重写。这个循环一直跑到Agent B挑不出毛病为止。"（fan-out+synthesize / adversarial verification）
- 引用限制：机制名与指令名（"effort ultra code"等）在 evidence-t §1 讹变表挂账，**必须回官方一手后才能引用**。

**② Anthropic multi-agent research system** ⏳ 待回源（回源队列 #1）——R4 升降的决定票。

**③ LangGraph supervisor / orchestrator-worker** ⏳ 按控制链归位（evidence-q/s 有部分素材，未按本区格式落）。

**④ 本仓自证**：DSH workflow 工具（pipeline 无栅栏并行 / parallel 栅栏 / 子代理 schema 输出）是编排层的运行实例——
指针位，档案锚 [evidence-g](../raw/evidence-2026-09-27-g-dsh-control-surface.md) ⏳ 对照表待做。

## 三、升阶闸门（若升正式）

全三件＋**token 预算**：并发放大的是**资源面**，硬上限（②）从秒级预算变成"整棵代理树"的预算；
验收分离（③）变成"合并节点谁来当"。与 [`stop_conditions/`](../stop_conditions/README.md) 三件对齐后才有升格资格。

## 四、待补清单

1. Anthropic multi-agent 回源档案（决定升降）。
2. LangGraph 归位。
3. evidence-t 讹变表核销。
4. DSH workflow 对照表（证据 g 扩一段）。
