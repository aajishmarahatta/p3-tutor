---
name: grade
description: Grade a learner's submission to a quiz - a verdict, a misconception and short feedback for every item, and a summary, written as a valid grades file in the way the learner likes feedback. Use it whenever a submission needs grading or the learner hands in answers to a quiz, on any topic.
argument-hint: "Which quiz and submission should I grade?"
---

# Grade

You tell the learner exactly where they stand on a quiz, and what to do about it.
A good grade is accurate first, then consistent, short and useful: the learner reads it once and knows what was right, what was missing, and what to review.
Your grades file is read by a script, so it must be exact.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it says now, without stopping to ask first, and put any question for the learner at the end of your final message, since there may be no one to answer it before the session ends.
If no submission is named, grade the highest-numbered submission that has no grades file yet, on the quiz it names.

## Read first

Read `FORMATS.md`, `PREFERENCES.md`, `MISSION.md`, `NOTES.md` and every file in `learning-records/`.
Then read the submission (`submissions/sN.json`), its quiz (`quizzes/NNNN.json`), its key (`keys/NNNN.json`), any earlier grades in `grades/`, and the lesson on the quiz's objective if there is one.
You may read the key here because you are grading; never copy it into anything the learner reads except as feedback on an answer already given.
Work only inside this folder, and never write under `.claude/`.

`PREFERENCES.md` decides how the feedback sounds: its tone, its length, its format, and the examples to use.
Follow it as written, whatever it says.
The verdicts never depend on it.

## Decide the verdicts

Grade every item of the quiz, in order, including items left unanswered (those are `wrong`, with a feedback line that says so).

**For every item, judge two things separately, in this order, before you pick a verdict:**

1. **The answer**: the option, number or statement the learner gave, against the key.
   Write down for yourself: right, partly right or wrong.
2. **The reasoning**: any explanation, note or "because" the learner wrote with it, read on its own, against the key's `rationale` and what is actually true.
   Write down: none given, sound, or containing a wrong belief or a false claim.
   Read it even when the answer is right, and read all of it: a learner who picks the right answer can still say something false in the sentence after it.
   A reason that is only vague or incomplete is not a wrong belief; a reason that states or assumes something false about how the idea works is.

Then combine them:

- `correct`: the answer is right and the reasoning is sound or absent, however it is worded and by whatever valid route it is reached.
- `partial`: part of it is right: the right method with a slip or the wrong unit, one half of a two-part idea, or **the right answer with a reason or added claim that contains a wrong belief**.
  A right answer does not make the item `correct` when its stated reasoning is substantively wrong: that is `partial`, never `correct`, even if the answer is exactly what the key wants and the reasoning is only wrong in its details.
- `wrong`: it misses the idea, contradicts it, or is blank.
- `mcq`: compare the chosen option with the key's `answer`; if the learner wrote out an option's text instead of its id, match it to the option.
  Then judge the reason as above.
- `numeric`: right when within the key's `tolerance` (1% of the answer when none), after converting any unit the learner stated; judge a stated reason as above.
- `short`: judge the meaning against `answer` and the `accepted` forms, which are examples and not the only wordings.
- If you are sure the key itself is wrong, grade against what is actually correct and say so in the summary.

Decide every verdict from the response, never from how much effort it shows, and never lean toward a kinder grade.
Before you write the file, go through every `correct` item once more and ask: did the learner give a reason, and does it say anything the key's rationale contradicts?
If so, it is `partial`.

## Name the misconception

`misconception` is the id of the misconception the response shows, in its answer or in its reasoning, or `null`.

- For `mcq`, take the key's `distractors` entry for the chosen option.
- For other items, or a right option with wrong reasoning, use the id of the misconception the wrong belief matches, from ids the workspace already has: the key's `distractors` (a wrong option built on the same belief), the key's `rationale`, `NOTES.md`, the learning records, other keys.
  A `partial` verdict for wrong reasoning names that id; it is `null` only when the wrong belief matches no id the workspace has.
- A `correct` answer, a slip, a blank, or an answer that matches no known misconception gets `null`.
- Never invent an id, and never use one that does not exist in the workspace.
  A `partial` verdict can name one as well.

## Write the feedback

Every item gets feedback with the same shape, so the learner always knows where to look.
Use this order, in the format `PREFERENCES.md` asks for (bullets if it asks for bullets):

1. **Verdict line**: the verdict in plain words, first, with no softening and no praise: "Correct.", "Partly right.", "Wrong.".
2. **What was right**: one short clause, when something was right.
   For a correct answer, this is all you need, plus at most one sentence that makes it stick.
3. **What was missing or wrong**: the right idea and why it holds, in plain words, taken from the key's rationale and put in your own words.
   Name a wrong belief plainly and say why it is tempting, without blame.
4. **Review**: for every `partial` and `wrong` item, one line, `Review: <one concept>`, where the concept is a thing the learner has already been taught (a part of a lesson, a learning record, or an idea in this quiz's other items), named exactly.
   If the concept is not taught yet, say so plainly in a few words ("not covered yet").
   Never point at something vague, and never name two concepts.

Rules for all feedback:
- **Right answer, wrong reasoning** (a `partial` where the answer was right but the reason was not): the verdict line is "Partly right.", then say that the answer is right, then steer gently to the flaw by asking one question about their reasoning, for example "What did you assume about ...?", and then give the correct reasoning.
  Do not say "your reasoning is wrong" bluntly; name what the reasoning missed.
  This is the one case where a question comes before the correction.
- **Wrong because of a misconception**: be blunt about the verdict and gentle about the belief.
  Offer a question back to the learner only when it helps them see the flaw themselves, and only one.
- Stay on the item: no new concepts, no tangents, no extra tasks, and no comparisons with other quizzes inside an item's feedback.
- Keep each item to about 40 words when it is `correct` and about 70 when it is `partial` or `wrong`, never more than 90, unless `PREFERENCES.md` asks for more.
- At most one example or analogy in the whole file, and only when it makes an idea clearer; take it from what `PREFERENCES.md` says the learner relates to, and say where it stops working if it might mislead.
- Never put an answer to a different, ungraded item in the feedback.
- Never leave feedback empty.

## Write the summary

`summary` is for the whole submission, about 60 words and never more than 90:
- how many items were correct, partial and wrong, as plain numbers;
- the one idea they have down;
- the one thing to work on next, the same concept as the most important `Review:` line;
- one concrete next step (a lesson section to reread, or one thing to try).

If an earlier grade for the same learner exists, you may add one clause on what changed since then, and only if it is true from the files.

## Write the files

1. Write `grades/NNNN-sN.json`, named after the quiz number and the submission, exactly as `FORMATS.md` shows: an object with `quiz`, `submission`, `items` (one entry per quiz item, same ids and order, each with `id`, `verdict`, `misconception`, `feedback`) and `summary`.
   Never overwrite an existing grades file; if one exists for this pair, grade only if the request asks for a regrade, and then say so in your final message.
2. Read the file back and check it yourself, character by character where a string is long, because a file that does not parse scores as no grade at all:
   - one JSON object, with no comments and no trailing commas;
   - every `"` inside a string is escaped as `\"`, or, better, written as a single quote; feedback often quotes the learner, and a quoted word is the most common way a file breaks;
   - a line break inside a feedback string is written `\n` or left out, never typed raw; with bullets, join them with `\n- `;
   - every bracket and brace is closed, and `misconception` is a string id or `null`, never an empty string;
   - there is one entry for every quiz item, with the same ids in the same order, and `verdict` is exactly `correct`, `partial` or `wrong`.
   If you find a fault, fix the file and read it again.
   Do not rely on the shell: it may not be available in every run.
3. If the grades show something worth keeping, write to `NOTES.md` what the learner now knows and what they still do not, and a misconception they showed.
   Write a learning record in `learning-records/` when the grades are evidence of real understanding of something non-trivial, or of a misconception to work on, as `FORMATS.md` describes.
   Do not write one for something that was only covered.

## Finish

End with a short message to the learner, in the way `PREFERENCES.md` asks: the grades file's path, the counts, and the one thing to work on next.
Do not repeat the feedback, and do not reveal the key beyond what the feedback already says.
