# Decision log

The decisions you made on the ladder, in your own words.
About one to two pages in total: each answer is two to four sentences with one number or one quote in it.

This file is the write-up of the project since version 0.2.
It replaces `EVAL.md`, which you no longer need to write.
If you already wrote a section of `EVAL.md` that answers a prompt here, keep it and point to it, such as "See EVAL.md, section 3", with one sentence that gives the answer.

The numbers come from `REPORT.md`, which `uv run p3 report --write` writes from your scored runs, so you never copy a table by hand.
Your ratings come from your major reviews in `reviews/`.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one, and "it did not pay off" is a full answer when you measured it.

Answer prompts 1 to 3 as you finish each step, while the decision is still fresh, and the rest once `final` has its runs.
Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p3 check` reports a marker as work still to do, and `uv run p3 check --final` fails while any marker is left.

Please do not let an agent write these for you.
They are about what you chose and what you saw, and the Builder and the Guide never write them.

---

## 1. Step 1: the skill change that mattered most

Of everything you changed while building `c1-skills`, which one change to a skill made the biggest difference, and how do you know?
Name the round, and give the evidence: a rating that moved, a check in `REPORT.md` that moved, or a quote from an output before and after.

I think the biggest improvement came from Round 1, when I added the dedicated tutor skill. Tutor behavior improved from 0.50 to 1.00 in the focused test, and the responses became shorter and less revealing. Instead of giving hints that narrowed down quiz answers, the tutor helped learners work through the options themselves.

## 2. Step 2: which review loop earned its cost

In `c2-review` you put reviewers on teach, quiz and grade.
Which loop earned its cost and which did not?
For each of the two, give what it cost in tokens against `c1-skills` and one thing its reviewer caught, or say that it caught nothing.

I think the Grade reviewer was the most worthwhile because it caught vague feedback and missing explanations while keeping grading accuracy at 100%. It increased token usage from about 135k to 468k, but the feedback became more useful. The Teach reviewer was less worthwhile because tokens increased from 505k to 1.35M while the lesson length ratio slightly decreased from 0.776 to 0.760. Although it caught unclear terminology and dense explanations, the improvement didn't justify the extra cost for me.

## 3. Step 3: whether splitting the teach job paid

`c3-split` splits the teach job across subagents.
Did the lesson get better by your own ratings, and what did the split cost against `c2-review`?
Say in one sentence whether you would pay that price again.

Splitting Teach improved length from 0.760 to 0.908, but increased Teach runtime from 6.5 to 11.0 minutes and tokens from 1.35M to 2.30M. From this, we can reasonably say that the split improved lesson quality enough to be useful, but the extra cost makes it important to choose components carefully in Final. It can also be noted that the planner alone had already achieved a 1.02 length ratio in the focused run.

## 4. `final`: what you kept, what you dropped, and a change that did not pay

Which components did `final` keep and which did it drop, and what rule did you use to decide?
Then name one change anywhere on the ladder that did not pay off: what you expected, what you measured, and what you did about it.

For my final configuration, I decided to keep all four skills (teach, quiz, grade, and tutor), along with the six subagents and the answer-key protection hook. I didn't remove any components because the existing workflows were producing accurate results, and I wanted to preserve the improvements while meeting the security requirements. My rule was to keep components that improved lesson quality, caught meaningful mistakes, or were necessary for protecting answer keys.
One change that did not clearly pay off was adding the quiz-reviewer. I expected it to improve question clarity and answer-key accuracy, but quiz key agreement was already 1.00 before adding it and stayed at 1.00 afterward. The reviewer increased token usage and runtime without a measurable improvement in that score. I kept it in Final because it could still catch individual mistakes, but I would consider removing it in a future cost-optimized version.

## 5. The ablation

Which component did you remove, and what did you predict would happen to quality and to cost before you ran it?
Then the result, with the numbers of the ablation's run beside `final`'s, and what one run lets you claim and what it does not.

For my ablation, I chose to remove the lesson-writer subagent while keeping the lesson-planner and lesson-reviewer. I predict that the lesson will remain factually correct, but its explanations, examples, and practice questions may become less consistent because the main agent will have to handle the writing itself.I expect the ablation to be slightly cheaper and faster because it removes one subagent call. However, the main agent might use some of those saved resources to write and revise the lesson, so the cost reduction may be modest.

The ablation partly supported my prediction. Without the `lesson-writer`, factual correctness remained 1.00, with no detected misconceptions or dead links. The lesson length ratio was 0.84, compared with 0.76 and 1.03 in the two Final runs. However, the ablation had fewer practice and answer blocks (6 compared with 10 and 13), suggesting that the dedicated writer may help produce more complete learning activities.
The ablation ran in 8.4 minutes, compared with 9.4 and 11.2 minutes for Final. Its estimated cost was $1.83, compared with $1.83 and $2.34, so it was faster but not consistently cheaper. Since this was only one ablation run and the two Final runs already varied substantially, I cannot confidently attribute the differences to removing the writer. I would keep the writer in Final for now, but the evidence for its added value is limited.

## 6. Your blind picks against your open reviews

You reviewed `final` openly, knowing you built it, and then compared it with `c0-baseline` blind.
Give the blind tally for each job, and say where it agreed with your open reviews and where it did not.
Where they disagreed, say what you think happened.

TODO: your answer to prompt 6.

---

## 7. The test topic

You tuned the tutor on the shared topic only.
On your test topic, did `final` still beat `c0-baseline`, and was the gain smaller, the same, or larger than on the shared topic?
Give one number or one quote from each config's output on it.

TODO: your answer to prompt 7.

---

## 8. The judge check

The bench's judge scored your lessons' facts and your tutor's replies.
Label ten of the items it judged yourself, before you look at its verdicts.
On how many of the ten did you agree with it, and what was one disagreement about?

TODO: your answer to prompt 8.

---

## 9. The stretch

What you tried, what it showed, and the one number that says so.
For the length study, give the outcome your `PREREG.md` rule points to.
If you did not take a stretch, write "No stretch."

TODO: your answer to prompt 9.
