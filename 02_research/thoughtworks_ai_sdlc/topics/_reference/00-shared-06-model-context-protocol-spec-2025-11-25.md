# W0-06 Model Context Protocol Specification

- source_urls:
  - `https://modelcontextprotocol.io/specification/2025-11-25/basic/index`
  - `https://modelcontextprotocol.io/specification/2025-06-18/architecture`
  - `https://modelcontextprotocol.io/specification/2025-11-25/client/sampling`
- source_type: `official protocol specification`
- authority_level: `official standardizing protocol source`
- publication_or_revision: `2025-11-25 basic + sampling; 2025-06-18 architecture`
- accessed_on: `2026-04-17`
- applicable_topics: `03 agent-native-infrastructure; 04 security-and-governance`

## Why This Source Matters

MCP 是“agent 如何接外部工具与数据”这件事的事实标准之一。对 Topic 03，它是 runtime / tool interface 的重要基准；对 Topic 04，它又是身份、授权、隔离与 consent 的关键控制面。

## Key Facts Captured

- MCP 使用 `JSON-RPC 2.0`，定义了 stateful client-host-server 交互协议。
- Architecture 明确规定：
  - `host` 负责创建 client、控制权限与生命周期、执行安全策略和用户授权决定。
  - `client` 与具体 server 保持隔离连接并维持边界。
  - `server` 暴露 resources、tools、prompts，并必须遵守安全约束。
- Basic overview 明确包含 `authorization` 作为 HTTP transport 的框架层。
- Sampling 规范指出 server 可以发起 agentic sampling，但出于 trust & safety，应该始终保留 `human in the loop` 拒绝权。
- MCP 把工具能力、上下文能力和授权能力统一到一个协议栈里，这使它既是集成协议，也是安全边界入口。

## Research Use

- Topic 03：支撑 Agent OS 最小 runtime 组件定义，尤其是 tool protocol、capability negotiation、stateful sessions。
- Topic 04：支撑对 host-enforced boundary、authorization、consent、tool-enabled sampling 的治理研究。
- Wave 2：可作为“平台便利性与安全边界张力”的具体实例。

## Caveats

- MCP 是协议，不是完整 Agent OS。
- 它说明“接口与边界如何标准化”，但不自动提供 blast-radius 计算、组织治理或 quality verification。
