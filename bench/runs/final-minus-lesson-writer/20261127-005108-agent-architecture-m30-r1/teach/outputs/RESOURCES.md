# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on context as a limited resource: smallest set of high-signal tokens, compaction, clearing tool results, structured note-taking, just-in-time retrieval. Use for: deciding what an agent keeps in context.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What the context window is, how it fills, context rot, caching's effect on cost. Use for: window limits and cost reasoning. Check the live page for current model limits.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side file-based memory across conversations. Use for: designing saved notes between sessions.

## Wisdom (Communities)

No community has been added yet.

## Gaps

- A high-trust, provider-neutral source on retrieval over long documents (chunking, keyword vs embedding search).
