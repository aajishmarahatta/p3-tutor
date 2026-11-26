# Guard probe: live evidence that the hook ran

A controlled probe, made on 2026-11-26 before `final` was snapshotted, because the first `grade-s1` live run
(`bench/runs/_live/20261126-190228-agent-architecture-m30-r1`) never tried to read `keys/` from the main conversation,
so its trace shows the grader's reads going through but no block. Live runs are not committed, so the result is recorded here.

## How it was run

- A scratch folder outside this repository held a copy of `tutor/.claude/` and a dummy `keys/0001.json` with made-up text, no real key.
- `claude -p` was started in it with the bench's own flags: `--setting-sources project,local`, `--permission-mode acceptEdits`,
  `--allowedTools Glob Grep WebSearch WebFetch`, `--model sonnet`, `--max-turns 8`, so the folder was untrusted, as in a bench scenario.
- Probe 1 asked the main conversation to use the Read tool on `keys/0001.json`.
- Probe 2 asked the main conversation to start the `grader` subagent and have it Read `keys/0001.json`.

## What came back

Probe 1, main conversation, Read `keys/0001.json` (the tool result, an error):

```
PreToolUse:Read hook error: [python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/keys_guard.py"]: Blocked: the answer keys in keys/ are not available to the main conversation. Quiz items are in quizzes/. Grading and key checks are done by the grader subagent (the grade skill starts it), and the quiz skill writes its key once from a draft ...
```

The message is the script's own text, with the hook's command, so it is the hook's denial and not a permission or trust error.
The dummy file's text did not appear anywhere in the main conversation's output.

Probe 2, `grader` subagent, Read `keys/0001.json`: the read returned the file's contents. The hook let the allowed agent through,
so `agent_type` reaches the script.

stderr in both probes said `permissions.allow` was ignored because the folder is not trusted; the hook ran regardless,
as the guide says hooks in project settings do.
