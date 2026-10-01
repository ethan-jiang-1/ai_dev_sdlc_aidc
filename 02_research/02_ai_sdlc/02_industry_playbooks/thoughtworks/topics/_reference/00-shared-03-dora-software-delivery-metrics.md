# W0-03 DORA: Software Delivery Performance Metrics

- source_url: `https://dora.dev/guides/dora-metrics/`
- source_type: `official methodology guide`
- authority_level: `official framework`
- publication_time: `live guide`
- accessed_on: `2026-04-17`
- applicable_topics: `01 engineering-paradigm; 02 organizational-synergy`

## Why This Source Matters

Wave 1 之后我们会频繁讨论“质量”“稳定性”“高频小步”“审批速度”等概念。DORA 指标是这类讨论的标准口径，必须先固定，否则后面很容易混用产量指标和交付健康指标。

## Key Facts Captured

- DORA 当前采用五个软件交付指标，而不是只看“四 key”旧口径。
- Throughput 维度包括：`change lead time`、`deployment frequency`、`failed deployment recovery time`。
- Instability 维度包括：`change fail rate`、`deployment rework rate`。
- DORA 明确强调速度和稳定性不是天然 tradeoff，长期看“better software faster”与“worse software slower”才是更真实的对立。
- DORA 也提醒不要把指标当作游戏目标，更不要跨上下文地粗暴比较不同应用或团队。

## Research Use

- Topic 01：定义“小批量高频交付”与“大批量回退”的可衡量对象。
- Topic 02：支持组织与治理讨论，避免把人机协作成效简化成代码吞吐。
- Wave 2：作为统一评估框架，用来比较不同 topic 对交付系统的影响。

## Caveats

- DORA 是交付性能框架，不直接回答 agent 安全、Agent OS 或 middle loop 工具设计。
- 它适合做 outcome frame，不适合单独解释 AI-native 机制。
