# W1-03 Agent-Native Infrastructure Evidence Summary

## Current Thesis

Topic 03 is no longer just “we need better agent platforms.” The current evidence package supports a stronger thesis:

- Agent-native infrastructure is a stack, not a single runtime.
- The stack needs at least five layers: orchestration, context/memory management, protocol interoperability, knowledge substrate, and observability.
- Long-horizon agent reliability depends on externalized state, stable interfaces, resumability, and durable artifacts.
- Knowledge graphs and semantic layers matter because vector retrieval alone is too weak for many global reasoning tasks over private enterprise data.

## Evidence Clusters

### 1. Orchestration is a first-class runtime problem

- Anthropic’s production research system uses an orchestrator-worker design with delegation, memory, artifacts, and resumability.
- AutoGen formalizes multi-agent conversation and programmable interaction behaviors.
- A2A shows that agents increasingly need a dedicated inter-agent protocol rather than pretending every remote capability is just a tool.

### 2. Memory is an operating-system-like concern

- Anthropic’s runtime articles show plans, artifacts, and file systems being used as external memory.
- MemGPT explicitly frames memory as hierarchical virtual context management.
- This supports the idea that agent memory is a systems problem, not just a bigger context-window problem.

### 3. Knowledge substrate must become structured

- GraphRAG paper and Microsoft’s practical explanation both show why baseline RAG fails on global or “connect-the-dots” enterprise questions.
- Entity graphs plus community summaries give a more reusable substrate for organization-specific reasoning.

### 4. Observability is part of the stack

- OpenTelemetry now treats GenAI operations and agent spans as explicit semantic-convention targets.
- MCP-specific semantic conventions add prompt, tool, RPC, and request identifiers into the instrumentation surface.

### 5. Work-ledger primitives are emerging, but remain fragmented

- Temporal shows one durable pattern: append-oriented event history plus replay to reconstruct execution state after failure.
- LangGraph shows a checkpoint-oriented pattern: thread identity, step checkpoints, intermediate writes, and retrieval by checkpoint boundary.
- OpenAI Agents SDK surfaces complementary runtime primitives: resumable state, history, ownership boundary, interruptions, and traces.
- Inngest shows a step-state pattern: unique step identity, persisted outputs, memoization, retries, and resume-from-failure.
- Together these sources suggest the `work ledger` is not a fantasy, but current public implementations still split its fields across execution history, checkpoint state, and observability systems instead of one unified enterprise ledger.

## What Is Confirmed

- A real Agent OS requires externalized state and memory.
- Protocol design matters at both tool and agent-to-agent levels.
- Knowledge graphs are a serious candidate for enterprise semantic grounding.
- Observability is becoming standardized enough to be treated as infrastructure, not an afterthought.
- A plausible near-term `work ledger` schema now looks more concrete: run or thread identity, ordered execution history, checkpoints or intermediate writes, step outputs, interruption boundary, specialist ownership, and traces.

## What Is Still Missing

- Direct evidence for a production-grade “work ledger” that combines authorization, budget, capability entitlement, and audit history in one design.
- More concrete examples of enterprise ontology extraction from legacy tickets, postmortems, and operational logs.
- More direct comparison between graph-based knowledge layers and simpler retrieval approaches at enterprise scale.

## Source Set

- `_reference/03-agent-native-infrastructure-01-anthropic-multi-agent-research-system.md`
- `_reference/03-agent-native-infrastructure-02-anthropic-managed-agents.md`
- `_reference/03-agent-native-infrastructure-03-anthropic-agent-sdk.md`
- `_reference/03-agent-native-infrastructure-04-a2a-protocol.md`
- `_reference/03-agent-native-infrastructure-05-autogen-multi-agent-framework.md`
- `_reference/03-agent-native-infrastructure-06-memgpt-virtual-context-management.md`
- `_reference/03-agent-native-infrastructure-07-graphrag-paper.md`
- `_reference/03-agent-native-infrastructure-08-graphrag-microsoft-blog.md`
- `_reference/03-agent-native-infrastructure-09-opentelemetry-genai-semconv.md`
- `_reference/03-agent-native-infrastructure-10-opentelemetry-mcp-semconv.md`
- `_reference/03-agent-native-infrastructure-11-temporal-event-history.md`
- `_reference/03-agent-native-infrastructure-12-langgraph-persistence-checkpoints.md`
- `_reference/03-agent-native-infrastructure-13-openai-agents-results-state.md`
- `_reference/03-agent-native-infrastructure-14-openai-agents-tracing-observability.md`
- `_reference/03-agent-native-infrastructure-15-inngest-durable-execution.md`
