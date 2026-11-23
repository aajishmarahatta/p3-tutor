# Agent architecture Resources

## Knowledge

- [Anthropic Engineering: "Effective context engineering for AI agents"](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context, attention budget, compaction, structured note-taking, just-in-time retrieval, sub-agents. Use for: what to keep in the context and how to manage it.
- [Anthropic Engineering: "Contextual Retrieval"](https://www.anthropic.com/engineering/contextual-retrieval)
  Chunking, embeddings, BM25, hybrid search and the contextual-chunk fix, with failure-rate numbers from Anthropic's own tests. Use for: designing manual search.
- [Claude docs: Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side file memory under /memories, its commands and security notes. Use for: saving notes between sessions.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the context limit. Use for: estimating tokens and cost per call.

## Wisdom (Communities)

- Local: the team's own design reviews and instructors.
  Use for: testing where each fact in the assistant should live. No online community has been vetted yet.

## Gaps

- A vetted online community for building agents with small budgets.
