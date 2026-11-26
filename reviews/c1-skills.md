# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/_live/20261124-221024-agent-architecture-m30-r1 (live quick run)

**My thoughts:**

Looking at the results for round 1, it seems like the tutor does a good job at not revealing quiz answers, seeing how tutor_leaks = 0. However, tutor-p01 asks which option protects the learner, which tells us that some hints that the tutor gives are too revealing. tutor-p01 also gave a reply that was estimated to be 250 words, which may a too long for my preferences. The personalization aspect is working as it gave a sports analogy that was happy with. 
I think what should be prioritized next is the tutor providing hints that help with the learner's reason without narrowing down the correct multiple-choice option.
**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md, tutor/CLAUDE.md
- Why: Chat replies still ran inside /teach with no rule against hints that narrow a quiz item (tutor-p01's "which option still protects you") and a reply of about 250 words; a tutor skill of its own makes every hint fit all options alike, caps quiz-help replies at about 120 words, and follows PREFERENCES.md, with tutor/CLAUDE.md now sending chat messages to /tutor.

### Round 2

**Run:** bench/runs/_live/20261124-224058-agent-architecture-m30-r1 (live --only quiz,tutor-p01,tutor-p02)

**My thoughts:**

The updated quiz now scores 100% key agreement but there are some things to note. Some incorrect choices appear too easy to eliminate. Multiple choice questions seem to test the same concepts, reducing coverage. Finally, one of the questions (q6) practically reveals the answer in the question itself. The shorter answers in this round are a lot better and what I would prefer. 

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md, tutor/CLAUDE.md
- Why: Quizzes still came from /teach, and these thoughts found easy-to-eliminate wrong options, repeated concepts and a q6 stem that gives its answer away; a quiz skill of its own assigns each item a distinct core idea, builds every wrong option from a plausible misconception, bars answer-revealing stems, and has the key read back as valid JSON.
  
### Round 3

**Run:** bench/runs/_live/20261124-232400-agent-architecture-m30-r1 (live --only quiz,grade-s1,grade-s2)

**My thoughts:**

The JSON is still valid and the key agreement is also 100% for this round. However, quiz seemed to improve some of the problems we saw in the previous round. One of them being how distracting options for MCQ questions are more plausible and similarly structured to the correct answer. Questions also seem to follow more distinct concepts, although some slight overlapping does exist. q6 also does not seem to suggest its own answer this time compared to round 2. Moving forward, I think a more consistent feedback structure, gentler correction of flawed reasoning, and having more useful concepts to review would complete this tutor. 

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/grade/SKILL.md, tutor/CLAUDE.md
- Why: Grading still ran inside /teach and these thoughts asked for a more consistent feedback structure, gentler correction of flawed reasoning and more useful concepts to review; a grade skill of its own gives every item the same shape (verdict, what was right, what was missing, one taught concept to review), steers gently with a question when the answer was right but the reasoning was not, keeps the verdicts and key-based misconception ids as they were, and has the grades file read back as valid JSON.
  
### Round 4

**Run:** bench/runs/_live/20261125-045028-agent-architecture-m30-r1 (live --only grade-s1,grade-s2,teach)

**My thoughts:**

grade seemed to imporve some things this time around. Feedback became shorter, more consistent, and easier to scan. JSON output remained valid. However verdict agreement dropped from 100% to 91.7% after grade. Submission 2, q4 received a correct verdict instead of partial. The feedback also endorsed the learner's incorrect reasoning. It seems like what we have up to this point in terms of length is the only thing that catched my eye. Lesson length is a reasonable priority for Teach, as long as the additional material contributes to learning rather than simply adding words.
Keep What changed untouched.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/SKILL.md
- Why: The baseline lesson was only about 2,600 words for 30 minutes (length ratio 0.58, under the 0.6 floor) and /teach still carried the quiz, grade and tutor jobs now done by their own skills; the rewrite makes /teach lessons-only, sets a target of about 130 to 150 visible words per minute reached with worked examples, practice, misconceptions and reflection rather than padding, and puts a short summary and defined terms first as PREFERENCES.md asks.

### Round 5

**Run:** bench/runs/_live/20261125-173027-agent-architecture-m30-r1 (live --only teach,grade-s2)

**My thoughts:**

It seems like the Teach rewrite was worthwhile as its length ratio rose from 0.58 to 0.72, factual correctness stayed at 100%, and the teach scenario used substantially fewer tokens. However, submission 2, q4 was marked correct twice when it should have been partial, meaning that a learner can select the correct answer but explain it using incorrect reasoning. This needs to be corrected. 

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/grade/SKILL.md
- Why: Submission 2's q4 was graded correct in two live runs although the learner's stated reasoning was wrong; the grade skill now judges the selected answer and the stated reasoning separately before choosing a verdict, grades a right answer with a substantively wrong reason as partial with the matching misconception id from the workspace, and rechecks every correct item for a contradicted reason before the file is written.

## Major review

**Run:** bench/runs/c1-skills/20261125-230647-agent-architecture-m30-r1

**Live tries:**

None

### Lesson

#### Technical correctness and facts

Rating: 5/5

100% factual correctness, zero misconceptions asserted, and no dead links.

#### Pedagogy

Rating: 4/5

Good structure, examples, worked exercises, and practice. The lesson is still somewhat short for 30 minutes.

#### Alignment with the learning goal

Rating: 5/5

Covers objective O3 and its key concepts with relevant exercises.

#### Overall quality

Rating: 4/5

Strong lesson overall, but personalization and length could improve.

### Quiz

#### Difficulty

Rating: 4/5

More plausible distractors, although some wrong options may still be too similar or too easy.

#### Coverage of the lesson's core

Rating: 4/5

Covers important concepts, but q5 and q6 overlap somewhat.

#### Wording and possible misreadings

Rating: 4/5

No automatically flagged ambiguity, but human review of the questions is still worthwhile.

#### Writing quality

Rating: 5/5

Clear, consistently structured items with explanations.

#### Alignment with the learning goal

Rating: 4/5

Questions target relevant concepts, but coverage could be more diverse.

### Feedback

#### Useful

Rating: 5/5

Correct verdicts, actionable explanations, and appropriate misconception detection.

#### Explains enough

Rating: 4/5

Feedback is concise and generally informative, although some responses could give more targeted guidance.

#### Personalized to how I like things explained

Rating: 4/5

Direct, bulleted, and concise, but not consistently personalized with examples.

### Tutor

#### Guardrails

Rating: 4/5

Zero answer leaks, but tutor-p05 gave advanced mathematical content despite recognizing it was above the learner's level.

#### Personalization

Rating: 4/5

Generally responds at the learner's level and sometimes uses preferred analogies, but p05 shows inconsistent level adaptation.

### Compared with the previous step

Compared with c0-baseline, c1-skills improved the tutor's overall performance, especially its ability to respond appropriately to learners. Tutor behavior increased from 0.33–0.50 in the baseline runs to 0.83, with zero answer leaks. Quiz key agreement reached 1.00, compared with inconsistent baseline results, while grading accuracy stayed at 1.00. Lesson factual correctness also remained at 1.00, and the length ratio improved slightly to 0.78. The full benchmark's estimated list cost decreased from around $1.73–$1.78 to $1.46. Overall, the separate skills appear to have improved consistency and efficiency without sacrificing accuracy.

### What the next step should fix

The next step should focus on catching quality problems that the current skills miss. The clearest issue is tutor-p05: the tutor recognized that deriving PPO was beyond the learner's current level but still provided the advanced formula instead of explaining why it was too advanced and suggesting a more achievable starting point. I also want the reviewer subagents to check lesson depth and personalization, quiz question overlap and distractor quality, and grading feedback for misconceptions and useful explanations. These checks should help catch problems before the tutor delivers its responses, rather than relying only on benchmark scores.
