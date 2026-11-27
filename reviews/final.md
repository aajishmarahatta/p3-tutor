# Reviews: final

Your review of `final`: optional quick rounds, its major review, your three learning sessions, and your review of the two test topics.
Quick rounds are optional here; use one for each component that `final` adds, such as a grader subagent, so its inventory entry has its with and without.
`p3 check` ignores an optional round you leave untouched.
The major review covers all four jobs on one of the three runs of `final`, and its previous step is `c3-split`; for the quiz and the feedback, which `c3-split` did not review, compare with `c2-review`, and for the tutor with `c1-skills`.
Its live tries are your three learning sessions, all on one of your two test topics, written up under Learning sessions below, so its Live tries line points at them.
Hold the sessions on `tutor/` as you snapshotted `final`, and note what they make you want to change instead of changing it.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1 (optional)

**Run:** bench/runs/_live/20261126-190228-agent-architecture-m30-r1

**My thoughts:**

The new grader subagent produced correct verdicts on every graded item, with 1.00 verdict agreement, 1.00 misconception hit rate, and no false-wrong grades. The main conversation did not read the answer key, while the grader and grade-reviewer accessed it successfully. The first benchmark trace did not directly demonstrate a block, but a separate controlled live probe confirmed that the PreToolUse hook blocks the main conversation and permits the authorized grader. The additional subagent calls increase grading cost, but protecting the answer key is necessary for the final architecture.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grader.md, tutor/.claude/skills/grade/SKILL.md, tutor/.claude/skills/quiz/SKILL.md, tutor/.claude/skills/teach/SKILL.md, tutor/CLAUDE.md, tutor/.claude/settings.json, tutor/.claude/hooks/keys_guard.py, tests/test_guard.py
- Why: With the answer-key guard on, the main conversation can no longer read keys/, so grading moves to a grader subagent that the guard allows; /grade now only starts the grader and the grade-reviewer and writes the final file once, and /quiz writes its key once from a draft, as the guide requires.

## Major review

**Run:** bench/runs/final/20261126-192430-agent-architecture-m30-r2

**Live tries:**

My interactive learning session on sql-joins is documented under Session 1 in Learning sessions below. I practiced join counting, completed a five-question quiz, reviewed my mistakes with the tutor, and solved two new application problems.

### Lesson

#### Technical correctness and facts

Rating: 5

The lesson maintained 1.00 factual correctness with no detected misconceptions or dead links. I thought the technical material was reliable, and the worked examples helped explain how agents manage context and memory.

#### Pedagogy

Rating: 4

The lesson was organized into sections with explanations, examples, and practice activities. The planner and writer helped produce a more complete lesson, and this run reached a length ratio of 1.03 for the requested 30 minutes. However, lesson length varied considerably between Final runs, with the other run reaching only 0.76.

#### Alignment with the learning goal

Rating: 5

The lesson focused on the requested learning objective about agent context and memory. The explanations and practice activities supported understanding how information is managed within and between agent sessions. I thought the structure was relevant to what the learner was supposed to accomplish.

#### Overall quality

Rating: 4

The lesson was accurate, structured, and close to the requested length. The separate planning, writing, and reviewing steps helped produce a detailed lesson. I would still improve consistency between runs and make sure the examples and explanations match the learner's preferences more closely.

### Quiz

#### Difficulty

Rating: 4

The quiz tested concepts from the lesson at a reasonable level. I thought the questions were useful for checking understanding rather than just memorizing definitions. Some questions could be more challenging or involve applying the ideas to new situations.

#### Coverage of the lesson's core

Rating: 5

The quiz covered the major concepts from the learning objective. The Final benchmark produced six questions, and the scoring did not identify incorrect answer keys or ambiguous items.

#### Wording and possible misreadings

Rating: 5

The questions appeared clear and specific enough to answer. The benchmark reported zero likely ambiguous questions and zero likely wrong keys. The separate quiz reviewer also provided an additional check before publication.

#### Writing quality

Rating: 4

The quiz was organized and readable, with answer choices that generally made sense. The generated quiz had 1.00 key agreement. However, the review workflow required additional time and tokens, and the second Final quiz process timed out even though its output and scoring were completed.

#### Alignment with the learning goal

Rating: 5

The quiz tested the same learning objective as the lesson. I thought it was appropriate for checking whether the learner understood the core ideas instead of introducing unrelated material.

### Feedback

#### Useful

Rating: 5

The grading agent correctly distinguished between correct, incorrect, and partially correct responses. Both Final benchmarks achieved 1.00 verdict agreement and 1.00 misconception detection, with no false-wrong grades. The feedback was useful because it identified mistakes rather than only assigning scores.

#### Explains enough

Rating: 4

The feedback explained why answers were correct or incorrect and identified misconceptions when appropriate. The grading reviewer also helped catch problems with explanations. I would still prefer the feedback to be concise and to focus directly on the learner's reasoning.

#### Personalized to how I like things explained

Rating: 4

The feedback was generally structured and explanatory, which matches my preference for clear explanations. I appreciated that the grading system could recognize partial understanding instead of treating every imperfect answer as wrong. I would improve personalization by including more short examples tied to the learner's background when useful.

### Tutor

#### Guardrails

Rating: 4

The tutor did not leak any protected answers in either Final benchmark. The PreToolUse hook also successfully blocked unauthorized access to answer keys in a controlled live test while allowing the grader to access them. However, the tutor still struggled with some behavior probes, so protecting answers did not guarantee that every tutoring response was ideal.

#### Personalization

Rating: 3

The tutor sometimes adjusted its explanations appropriately, but its behavior was inconsistent. Expected behavior was met on 0.50 of probes in Final run 1 and 0.67 in Final run 2. In particular, it still tended to provide explanations that were too advanced instead of giving a simpler next step. I would like the tutor to respond more consistently at the learner's level.

### Compared with the previous step

Compared with c3-split, Final maintained 1.00 factual correctness, quiz key agreement, grading accuracy, and misconception detection, with zero answer leaks. The main improvement in Final was security: the answer-key guard and dedicated grader separated protected keys from the main conversation.

Teaching length varied across the Final runs, with ratios of 0.76 and 1.03 compared with 0.91 in c3-split. Tutor behavior was less consistent, scoring 0.50 and 0.67 compared with 0.83 in c3-split. The Final configuration was slightly more expensive, but the additional security protection was an important requirement.

### What I would do next

I would focus on improving the tutor's ability to recognize when an explanation is too advanced and respond with simpler hints or examples. I would also consider reducing the cost of review loops that have not shown much measurable improvement, especially the quiz reviewer. Finally, I would try to make lesson length and personalization more consistent across repeated runs.

## Learning sessions

### Session 1

**Date:** 2026-11-26

**Topic:** sql-joins, one-to-many relationships and ON versus WHERE

I used the Final tutoring agent to practice SQL joins, especially counting rows after one-to-many joins and understanding the difference between ON and WHERE conditions. The tutor started with small tables and asked me to predict query results before giving explanations. I initially answered the basic counting questions correctly, but I scored only 2/5 on the quiz because I was still confusing how ON and WHERE affect a LEFT JOIN.

The tutor helped me work through my mistakes by having me list the joined rows myself instead of immediately giving me the answers. After reviewing the mistakes, I correctly explained the different results of filtering in ON versus WHERE. I also completed two new problems involving soccer goals and NFL games. I initially missed one soccer goal when counting, but corrected it after a hint. In the final NFL problem, I independently wrote the correct query and calculated four qualifying games from three different teams.

I found the step-by-step questions and sports examples especially helpful. The main improvement I would suggest is making the quiz review process shorter and focusing more quickly on the specific concept I misunderstood. Overall, I finished the session with a clearer understanding of COUNT(*), COUNT(column), COUNT(DISTINCT column), and where to place filtering conditions in joins.


## Test topics

### sql-joins

I created SQL joins as my held-out topic to test whether the Final architecture could handle a different subject without being tuned specifically to agent architecture.

The baseline and Final configurations both achieved 1.00 factual correctness, 1.00 quiz key agreement, and 1.00 grading verdict agreement, with no answer leaks. The biggest improvement was lesson length: the baseline produced a ratio of 0.57, while Final reached 0.81. The Final lesson was closer to the intended 30 minutes and provided more opportunity to explain the material.

However, tutor expected behavior decreased from 0.75 in the baseline to 0.50 in Final. One Final probe failed because the tutor avoided a hint that might reveal too much about the quiz answer, even though the expected response specifically asked for that hint. Both configurations also struggled with the advanced query-optimization question.

The Final run took 16.2 minutes compared with 4.9 minutes for the baseline, and its estimated cost was $3.48 compared with $1.39. I think the additional cost improved lesson completeness and added security, but it did not consistently improve tutoring behavior.