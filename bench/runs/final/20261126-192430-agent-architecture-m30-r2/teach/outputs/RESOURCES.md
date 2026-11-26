# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context, context rot, attention budget, just-in-time vs pre-loaded retrieval, compaction, structured note-taking, sub-agents. Use for: what to keep in context, how an agent finds information, notes as memory.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What the context window is, what counts toward it, how turns accumulate, what happens at the limit. Use for: tokens, window size, cost of long conversations.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  File-based memory that persists between sessions, run client-side by the application. Use for: designing what the assistant saves between visits.
- [Article: "Building effective agents" (Anthropic Engineering)](https://anthropic.com/engineering/building-effective-agents)
  The augmented LLM (model plus retrieval, tools, memory) as the building block of agents; advice to start simple. Use for: workflows vs agents, the big picture. Note: the page says some tooling in it is dated.

## Wisdom (Communities)

- None added yet. The learner has not said whether they want communities.

## Gaps

- A high-trust source on retrieval over long manuals (chunking, embeddings) for the makerspace use case; a later lesson on retrieval will need one.
