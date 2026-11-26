# Components

<!--
An example of a finished entry:

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: My c1 review found two quiz items that could be read two ways (q2 and q4) and one whose correct option repeated the stem; a reviewer with a fresh context reads the draft the way a learner will, which the quiz skill writing its own items cannot do, so it is a subagent and not a step in the skill.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it, q2 asked which design "is better" with no criterion; with it, every stem names its criterion and the reviewer's record shows two items flagged and fixed in one pass, for about 0.6M more tokens per quiz, which I think a quiz is worth, because a misread item teaches the wrong thing.
- Kept in final: yes
-->

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: I created the tutor skill to make the agent behave like a tutor instead of simply giving answers. I wanted it to offer hints, identify misunderstandings, ask follow-up questions, and adjust explanations to the learner's level.
- With and without: reviews/c1-skills.md, Round 1 (without) and Round 2 (with)
- Review: The tutor skill produced one of the clearest improvements in the project. In the focused c1 test, expected tutor behavior improved from 0.50 to 1.00, and the c1 full run reached 0.83 compared with the baseline's 0.33–0.50. However, the Final runs scored 0.50 and 0.67, showing that difficult questions and overly advanced explanations remain weaknesses. I still think the skill was worthwhile because it established the basic tutoring behavior and helped avoid answer leaks.
- Kept in final: yes

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: I created the quiz skill to generate questions that match specific learning objectives and include clear answer keys, plausible distractors, and explanations. I wanted the agent to test understanding rather than produce questions that are confusing or too easy.
- With and without: reviews/c1-skills.md, Round 2 (without) and Round 3 (with)
- Review: The quiz skill improved the structure and consistency of generated assessments. The baseline sometimes produced ambiguous questions or incorrect answer-key formatting, while c1 achieved 1.00 key agreement. That result continued through c2, c3, and both Final runs, with no flagged ambiguous items or wrong keys in the Final benchmarks. I consider it valuable because accurate quizzes are necessary for meaningful grading and learning.
- Kept in final: yes

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: I created the grade skill to evaluate submitted answers consistently, distinguish correct, partially correct, and incorrect responses, and give useful feedback about misconceptions. I especially wanted the grader to recognize answers that show some understanding rather than treating every imperfect explanation as completely wrong.
- With and without: reviews/c1-skills.md, Round 3 (without) and Round 4 (with)
- Review: Grading accuracy was already strong in the baseline, so this skill did not produce a large improvement in the automated verdict score. However, the c1 rounds helped address misleading feedback, including cases where the explanation discussed the correct answer instead of the learner's selected answer. Both Final runs maintained 1.00 verdict agreement, 1.00 misconception hit rate, and a 0.00 false-wrong rate. I kept it because consistent, understandable feedback is an important part of tutoring even when the numerical score stays the same.
- Kept in final: yes

### teach

- Kind: skill
- Step added: c1-skills
- Purpose: I created the teach skill to produce structured lessons based on a learner's objective, background, preferences, and available sources. I wanted lessons to introduce concepts in a sensible order, explain them accurately, include examples and practice, and fit the requested learning time.
- With and without: reviews/c1-skills.md, Round 4 (without) and Round 5 (with)
- Review: The teach skill provided the foundation for the later planning, writing, and review improvements. Factual correctness remained at 1.00, but lesson length was initially a recurring problem: the c1 full run had a length ratio of 0.776. Adding specialized teaching subagents later improved this to 0.908 in c3, although the two Final runs varied between 0.76 and 1.03. I kept the skill because it coordinates the entire lesson workflow and makes teaching more structured than a general response.
- Kept in final: yes

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: I added a separate quiz reviewer to catch unclear wording, misleading distractors, incorrect answer keys, and mismatches with the learning objective. A reviewer with a separate context could inspect the quiz from a learner's perspective instead of relying only on the agent that wrote it.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: The reviewer provided an additional quality check, but its measurable improvement was limited. Quiz key agreement was already 1.00 in c1 and stayed at 1.00 in later benchmarks, while reviewer calls increased token usage and runtime. The extra review may still catch individual mistakes, but the evidence does not show a consistent score improvement that clearly justifies its cost. I retained it in Final to preserve the reviewed workflow, although it would be one of the first components I would reconsider for a cheaper version.
- Kept in final: yes

### grade-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: I added the grade reviewer to independently inspect grading decisions and feedback. Its main purpose was to catch incorrect verdicts, missed misconceptions, and explanations that failed to address what the learner actually answered.
- With and without: reviews/c2-review.md, Round 2 (without) and Round 3 (with)
- Review: The grade reviewer was useful for identifying feedback problems even though the numerical grade scores were already high. The c2 focused comparison showed much greater token usage with review, but the reviewer helped improve the clarity of grading explanations. Final maintained perfect verdict agreement and misconception detection. I think it adds educational value, though its cost makes it less attractive for simple submissions where the grader is already accurate.
- Kept in final: yes

### lesson-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: I added the lesson reviewer to check the lesson for factual errors, unclear explanations, weak examples, missing practice, and problems with the HTML output. I wanted a separate agent to inspect the finished draft before it was published.
- With and without: reviews/c2-review.md, Round 3 (without) and the c2-review full run (with)
- Review: The lesson reviewer caught concrete problems, including undefined terms, incorrect figures, missing practice, and inconsistent exercise feedback. However, the c2 lesson length ratio was 0.760 compared with 0.776 in c1, so it did not solve the short-lesson problem. The reviewer also frequently reached its two-pass limit with findings still open, adding substantial cost. I kept it because its factual and exercise corrections were valuable, but I learned that reviewing a lesson is not a substitute for planning it properly.
- Kept in final: yes

### lesson-planner

- Kind: subagent
- Step added: c3-split
- Purpose: I introduced the lesson planner to solve the recurring problem of lessons being shorter than requested. Its job was to organize the lesson into sections, assign time and word budgets, plan examples and exercises, and introduce difficult concepts in a logical order before drafting began.
- With and without: reviews/c3-split.md, Round 1 (without) and Round 2 (with)
- Review: The planner produced one of the strongest measurable improvements. The lesson length ratio increased from 0.760 without it to 1.02 in the focused planner test, while factual correctness remained 1.00. The completed c3 split also achieved a 0.908 length ratio and improved learner-level fit from 4 to 5. The planner increased token usage, but I think it earned its place because it directly addressed a consistent weakness with a clear improvement.
- Kept in final: yes

### lesson-writer

- Kind: subagent
- Step added: c3-split
- Purpose: I added the lesson writer to turn the planner's outline into a complete lesson without making the main agent handle all of the drafting. I wanted it to follow the planned section budgets, use examples that fit the learner, explain unfamiliar terms clearly, and produce consistent exercises and feedback.
- With and without: reviews/c3-split.md, Round 2 (without) and the c3-split full run (with)
- Review: The c3 full run produced a lesson with a 0.908 length ratio, factual correctness of 1.00, and a learner-level fit score of 5. The writer also produced a cleaner draft workflow without the multiple scratch files used in the earlier planner-only run. However, the planner-only test had already reached a 1.02 length ratio, and adding the writer increased the Teach scenario's runtime and complexity. I kept it in Final because the division of work improved the lesson-production process, but I selected it for ablation to test whether that benefit justifies its cost.
- Kept in final: yes

### grader

- Kind: subagent
- Step added: final
- Purpose: I created the dedicated grader because the Final answer-key guard prevents the main conversation from reading protected quiz keys. The grader can access the key securely, compare it with a learner's submission, and produce verdicts and feedback without revealing the answers to the main agent.
- With and without: reviews/final.md, Round 1 (with); reviews/c3-split.md, full run (without)
- Review: The grader successfully preserved grading quality while separating protected answer-key access from the main conversation. Its focused test achieved 1.00 verdict agreement, 1.00 misconception hit rate, and 0.00 false-wrong rate, and both Final runs maintained those scores. A controlled live guard probe confirmed that the main conversation was blocked from reading the key while the grader was allowed. Although it adds subagent calls and cost, I consider it necessary because protecting answer keys is a core security requirement.
- Kept in final: yes