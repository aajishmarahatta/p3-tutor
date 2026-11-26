# Reviews: c2-review

Your quick rounds while you build the review loops on teach, quiz and grade, and then the major review of `c2-review`.
Add one reviewer subagent per round, so the run before it shows the output without it and the run after it shows the output with it.
The major review covers the lesson, the quiz and the feedback, and its previous step is `c1-skills`.
Say in it whether the problems your `c1-skills` review found are gone.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c1-skills/20261125-230647-agent-architecture-m30-r1

**My thoughts:**

Using the existing c1-skills full benchmark for Round 1, quiz key agreement was 1.00, with no automatically detected ambiguous items or wrong keys. Some items still tested similar concepts, particularly q5 and q6. Some incorrect options mapped to the same misconception ID. Automated scores were strong, but the quiz could still improve in distractor variety and coverage.
We could prioritize better coverage of distinct concepts and stronger distractor quality.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: The c1-skills quiz still had overlapping items (q5 and q6) and wrong options that mapped to the same misconception id, which its own skill did not catch; a quiz-reviewer subagent with a fresh context and a checklist on difficulty, coverage, wording, writing quality and alignment now reads the draft in drafts/, and the quiz skill revises on its findings for at most two passes before writing the final quiz and key once, with a record in review-records/.

### Round 2

**Run:** bench/runs/_live/20261126-020128-agent-architecture-m30-r1

**My thoughts:**

A few notes about this run. The reviewer made the distractors more plausible and addressed reused misconception IDs. q1, q2, and q3 still cover similar ideas.Both review passes ended with REVISE, showing the loop stopped at its cap rather than achieving full approval. Quiz accuracy remained at 100%, but runtime and token usage increased substantially. Grading is already accurate, so the next reviewer should focus on reasoning errors, targeted feedback, and personalization

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grade-reviewer.md, tutor/.claude/skills/grade/SKILL.md
- Why: These thoughts found grading accurate but asked the next reviewer to focus on reasoning errors, targeted feedback and personalization; a grade-reviewer subagent now regrades the submission independently and checks verdicts (a right answer with wrong reasoning must be partial), misconception ids, specific review pointers, and the useful, explains-enough and personalized criteria, and the grade skill drafts in drafts/, revises on its findings for at most two passes, and writes the final grades file once with a record in review-records/.

### Round 3

**Run:** bench/runs/_live/20261126-023431-agent-architecture-m30-r1

**My thoughts:**

Grade improved as the reviewer caught vague feedback, clarified explanations, and finished with PASS while maintaining 100% grading accuracy. It seems like Teach is still short. The length ratio is 0.73, corresponding to approximately 22 minutes of estimated reading time for a 30-minute lesson. Teach sometimes also assumes prior knowledge. The judge flagged unexplained comparisons and dense technical material

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: This round's thoughts found the lesson still short for 30 minutes, with terms and comparisons used before they were explained and statistics without a named source; a lesson-reviewer subagent now reads the draft in four separate sections (facts, pedagogy, alignment, overall quality) with web fact-checking and a length estimate, and the teach skill drafts in drafts/, revises on its findings for at most two passes, and writes the final lesson once with a record in review-records/.

## Major review

**Run:** bench/runs/c2-review/TODO

**Live tries:**

TODO

### Lesson

#### Technical correctness and facts

Rating: TODO

TODO

#### Pedagogy

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

#### Overall quality

Rating: TODO

TODO

### Quiz

#### Difficulty

Rating: TODO

TODO

#### Coverage of the lesson's core

Rating: TODO

TODO

#### Wording and possible misreadings

Rating: TODO

TODO

#### Writing quality

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

### Feedback

#### Useful

Rating: TODO

TODO

#### Explains enough

Rating: TODO

TODO

#### Personalized to how I like things explained

Rating: TODO

TODO

### Compared with the previous step

TODO

### What the next step should fix

TODO
