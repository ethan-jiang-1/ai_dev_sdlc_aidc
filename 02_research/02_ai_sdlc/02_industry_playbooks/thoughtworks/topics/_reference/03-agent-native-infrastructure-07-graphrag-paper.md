# Topic 03 / Ref 07: GraphRAG Paper

- source_url: `https://arxiv.org/abs/2404.16130`
- source_type: `arXiv paper`
- authority_level: `primary research`
- publication_time: `2025 revised version`
- accessed_on: `2026-04-17`
- topic: `03 agent-native-infrastructure`

## Why This Matters

Topic 03 asks how latent enterprise knowledge can become machine-usable. GraphRAG is one of the clearest research answers: transform document corpora into graph structures plus community summaries for better reasoning over private data.

## Key Facts Captured

- The paper argues conventional RAG fails on “global” corpus-level questions.
- GraphRAG builds an entity knowledge graph and pre-generated community summaries from source documents.
- It then uses partial responses from those summaries to compose a final answer.
- The paper reports substantial gains over baseline RAG on global sensemaking questions over large private corpora.

## Research Use

- Supports Topic 03’s claim that an enterprise semantic layer may need graph structure, not only vector retrieval.
- Gives a concrete mechanism for turning hidden organizational text into a reusable knowledge substrate.

## Caveats

- GraphRAG is promising but computationally heavier than basic retrieval.
- It is a knowledge-layer primitive, not an entire agent runtime or governance system.
