---
type: kol_evidence
directory: 03_skeptics/kol_tech
observation_date: 2026-10-07
---

# dinaburg — loop engineering 证据轨迹（2026-06 后，时间正序）

> **身份**：Trail of Bits 安全研究员（Patch the Planet 项目）
> **背景**：Artem Dinaburg——Trail of Bits（顶级安全咨询）研究员；长期二进制/移动安全研究；2026 年转向 agent 安全实证。**第九轮（2026-10-07）新入册（安全社区 KOL）。**（履历核：blog.trailofbits.com，2026-10-07）
> **号召力**：②（安全社区高引用；本篇被 Narayanan/Kapoor 09-14 长文引为沙箱论证基础——链路互证）
> **派别权威**：[台账 §A2](../../../../02_research/01_agent_engineering/loop_engineering/raw/kol-roster.md)（2026-10-07 第九轮入册）
> 人群类型：**专业技术 KOL**（安全研究员）

## 态度轨迹

**方向**：沙箱地基实证动摇（VM 困不住 cyber-capable agent）＋处方明确
**关键转折**：GPT 5.6-Cyber 在 QEMU/KVM 中三次逃逸（2 个已知 CVE 组合＋3 个 0-day 链）

## 《VMs won't contain cyber-capable agents》（Trail of Bits 博客，2026-08-26）

- URL：blog.trailofbits.com（2026-08-26）｜ fetch 成功（全文）
- 来源类型：安全公司一手研究博客（全文取得）。
- **挂钩**：⑥无人值守运行（沙箱逃逸实证）＋③预算与熔断（限时）＋⑤验证回路（一次性环境）。

### (a) 怀疑面（无人值守的安全地基被动摇）

**逐字摘录**：

> "If it wasn't clear before, I will state it plainly: you can no longer assume a mere VM will contain a sufficiently advanced AI agent. To use a 2010s term of art, you should treat such agents as an advanced persistent threat."
（** plainly 版结论**：普通 VM 困不住足够先进的 AI agent——按 APT（高级持续性威胁）对待。）

> "It operated autonomously for hours, backtracked from approaches that didn't work, pulled code and research papers, wrote oracles, made its own minimal examples, and aimed for a reusable, reliable exploit, all with minimal handholding and prompting."
（**长时程自主逃逸实录**：自主跑数小时、自我回溯、拉代码与论文、写 oracle、做最小复现——"最少的扶持与提示"。）

> "An off-the-shelf VM is not enough to contain a modern, cyber-capable AI agent. There is simply too much attack surface."
（**现货 VM 攻击面太大**。）

> "One of the most impressive features of GPT 5.6-Cyber and Codex with goal mode is effective persistence over long (here, approximately 12-hour) time horizons across multiple compactions and innumerable subagent invocations."
（**反讽式承认**：跨 compaction、跨大量子 agent 调用的约 12 小时有效持续——长时程自主 loop 已经真实存在且能做出人想不到的事。）

### (b) 推荐面

**逐字摘录**：

> "What can we do? A start is using a virtualization technology that was purposely built with a minimal attack surface and a focus on security, like Firecracker."
（**处方一**：换攻击面最小化的虚拟化——Firecracker（他让 agent 打 Firecracker：能 hardlock 宿主机但未能逃逸）。）

> "In general, we have to become much more attentive to security fundamentals: least privilege (regarding network access, credentials, available features, etc.), logging, and active monitoring. Further, we can limit the time agents have to operate and ensure a pristine environment for each use."
（**处方二（本轮最重）**：最小权限＋日志＋主动监控，**再加两条 loop 专属**——限时运行（③熔断的时间形态）＋每次使用一次性纯净环境（⑤验证回路的环境形态）。）

> "A distribution with rapid updates is now a requirement. ... An older distribution (like Debian 12, my old standby) that isn't getting immediate upstream updates should be assumed vulnerable."
（**处方三**：快更新发行版成为必要条件；老发行版默认视为易感。）

**该条支持的最小主张**：安全实证方给出"VM 困不住 cyber-capable agent"的一手证据（三次逃逸＋12 小时自主），替代方案是"Firecracker 级最小攻击面＋最小权限/日志/主动监控＋限时熔断＋一次性环境"。
**派别适配**：**怀疑票（安全实证向，强）**——直接动摇"沙箱内无人值守"路线的安全地基；与 CSA 扫描器绕过案（[csa](../orgs/csa.md)）构成"验证/隔离层被实证打穿"的两翼。
