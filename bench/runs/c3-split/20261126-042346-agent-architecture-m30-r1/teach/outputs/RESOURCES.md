# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic)](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
  Context as a limited resource, context rot, compaction, structured note-taking, just-in-time retrieval, sub-agents. Use for: what to keep in context, what to save outside it, how an agent finds information in a large body of text.
- [Docs: "Context windows" (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Defines the context window, how each turn accumulates, overflow errors, context editing and compaction. Use for: what counts toward the window and why long conversations cost more.
- [Article: "Contextual Retrieval" (Anthropic)](https://www.anthropic.com/engineering/contextual-retrieval)
  Splitting documents into chunks, embeddings plus keyword (BM25) search, and adding context to each chunk. Use for: finding the right page in a long manual.

## Wisdom (Communities)

- None added yet.

## Gaps

- A beginner-level, vendor-neutral explanation of retrieval (chunks, embeddings, top-k) with a short Python example.
