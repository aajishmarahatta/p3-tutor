# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  s2 is graded (`grades/0001-s2.json`): 3 correct, 2 partial, 1 wrong. s1 is not graded yet.
  s2 showed: the loop structure and what happens to a tool result are solid. Misconception M4 is still open (q4: said the model runs the tools itself; it only outputs a request and the program runs the tool). M6 showed on q3 (thought a stuck agent would eventually fix itself; needs a stopping condition such as a step limit). q6: knows a tool name helps but not that the model relies on the full tool description.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
