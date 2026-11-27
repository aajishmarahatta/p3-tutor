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

My blind comparisons produced the following results:

- Teach: Final won 2, Baseline won 0.
- Quiz: Final won 0, Baseline won 1, with 1 tie.
- Grade: Final won 8, Baseline won 16.
- Tutor: Final won 10, Baseline won 2.

My teaching preferences agreed with my open review because I preferred Final's more organized and interactive lessons. The Final tutor also performed well in my blind preferences, even though its automatic behavior scores were not consistently better.
The biggest disagreement was grading. I rated Final's grading quality positively in my open review, but I preferred Baseline in 16 of the 24 blind comparisons. I think this happened because both systems produced correct grading verdicts, while I personally preferred the paragraph-style explanations over the bullet-point formatting in some Final responses.
The quiz results were mixed, with one Baseline win and one tie. This suggests that additional reviewer agents did not necessarily make the quiz more appealing to me, even though Final achieved better answer-key agreement.
Overall, the blind comparisons showed that Final's architecture improved some aspects of my learning experience, but the added complexity did not automatically improve every output.

## 7. The test topic

You tuned the tutor on the shared topic only.
On your test topic, did `final` still beat `c0-baseline`, and was the gain smaller, the same, or larger than on the shared topic?
Give one number or one quote from each config's output on it.

On my held-out sql-joins topic, Final improved lesson completeness but did not consistently outperform the Baseline in every category.
The Baseline lesson had a length ratio of 0.57, while Final reached 0.81. Both configurations maintained 1.00 factual correctness, 1.00 quiz key agreement, and 1.00 grading verdict agreement.
However, Baseline met 0.75 of the expected tutor behaviors while Final met only 0.50. Final was also substantially more expensive, with an estimated list cost of $3.48 compared with $1.39.
On the shared agent-architecture topic, Final's average lesson length ratio was 0.89 compared with 0.75 for Baseline, an improvement of 0.14. On sql-joins, the improvement was 0.24. Therefore, the lesson-length gain was larger on my held-out topic, although tutoring behavior actually became worse.
This suggests the architecture generalized well for producing longer, factually correct lessons, but its tutoring improvements did not generalize consistently.

For example, on my held-out SQL joins topic, the Baseline lesson had a length ratio of 0.574 and contained 2,585 words, while the Final lesson had a length ratio of 0.807 and contained 3,632 words. Both achieved 1.00 factual correctness. This shows that Final generated a substantially more complete lesson without sacrificing factual accuracy, although it did not consistently improve tutor behavior.

## 8. The judge check

The bench's judge scored your lessons' facts and your tutor's replies.
Label ten of the items it judged yourself, before you look at its verdicts.
On how many of the ten did you agree with it, and what was one disagreement about?

I independently labeled ten tutor responses from the first two c0-baseline benchmark runs on agent-architecture, following a selection rule chosen before inspecting their individual judge verdicts. I selected six probes from the first run and four from the second because I had already seen some of Final's individual probe results.

My labels agreed with the automated judge on 9 out of 10 responses (90%). The only disagreement was tutor-p06 in the first run, which explained tool calling using a manager-and-runner analogy. I marked it "not met" because the response was about 356 words, exceeding the expected limit of about 250 words. The judge marked it "met" because it considered the length limit approximate and thought the otherwise accurate analogy satisfied the requirements.
This suggests the judge was generally consistent with my assessment, although it was more lenient about length than I was. This check supports confidence in the tutor-behavior scores, but it does not independently validate the lesson-fact scores.

## 9. The stretch

What you tried, what it showed, and the one number that says so.
For the length study, give the outcome your `PREREG.md` rule points to.
If you did not take a stretch, write "No stretch."

I completed the 498E personalization-swap stretch by creating a fictional learner profile that prefers restaurant examples, big-picture explanations, concise lessons, and direct feedback. I snapshotted it as configs/final-swap/ and ran one benchmark on agent-architecture. The lesson switched from a soccer-coach analogy to a cook-and-order-ticket analogy, the number of questions decreased from 24 to 13, and the grading feedback became shorter and more direct. However, the quiz did not adopt restaurant examples, and the lesson was only about 9% shorter. The swap preserved correctness: factual accuracy, quiz key agreement, and grading verdict agreement all remained at 1.00, while the length ratio of 0.95 stayed within Final's original range of 0.76–1.03.
