# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source for context, context rot, the attention budget, compaction, structured note-taking, just-in-time retrieval and sub-agents. Use for: deciding what an agent keeps in context and what it saves outside it.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official definition of the context window, what counts toward it, context rot, compaction and context editing. Use for: what fills the window and how it relates to cost.
- [Docs: Memory tool (Claude Platform, Spanish version)](https://platform.claude.com/docs/es/agents-and-tools/tool-use/memory-tool)
  Official description of a file-based memory the application stores and the model reads and writes through tool calls. Use for: how notes persist between sessions, and path-safety rules.
- [Post: "LLM Powered Autonomous Agents" by Lilian Weng](https://lilianweng.github.io/posts/2023-06-23-agent)
  Classic overview of agent components, including short-term and long-term memory. Seen in search results only; use for: background vocabulary.

## Wisdom (Communities)

- None added yet. Gap: a moderated community for people building retrieval and agent projects; to be found with the learner (their university's CS or data science club may serve).

## Gaps

- A high-trust source on retrieval (chunking, embeddings) written for beginners; not yet read.
