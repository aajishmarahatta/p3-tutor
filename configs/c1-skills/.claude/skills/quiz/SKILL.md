---
name: quiz
description: Write a quiz and its answer key for an objective, or give a quiz to the learner in the chat - items that test the distinct core ideas of the objective, with plausible wrong options, clear wording and valid JSON files. Use it whenever the learner or a request asks for a quiz or a test on any topic.
argument-hint: "What should the quiz cover, and how many questions?"
---

# Quiz

You write quizzes that show the learner, and you, where they really stand.
A good quiz tests the few ideas that matter most for an objective, once each, in questions that have exactly one defensible answer, with wrong options a half-understanding learner would actually pick.
Your quiz and key are files that a script reads, so they must be exact.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it says now, without stopping to ask first, and put any question for the learner at the end of your final message, since there may be no one to answer it before the session ends.

## Read first

Read `FORMATS.md`, `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/`.
Then read the quizzes in `quizzes/` and their keys in `keys/` (to take the next number, avoid repeating an earlier quiz, and reuse the misconception ids the workspace already has), and any lesson in `lessons/` on the objective.
You may read keys here because you are writing the next one; never show anything from `keys/` to the learner.
Work only inside this folder, and never write under `.claude/`.

`PREFERENCES.md` shapes the wording: plain language, the examples the learner relates to when a scenario needs one, and the length and density of the key's rationales.
The facts and the difficulty come from the objective and what the learner knows, not from `PREFERENCES.md`.

## Plan before you write

1. **Pin down the objective**, its id, and how many items were asked for (four or five after a lesson, when no number is given).
   Every item carries that objective's id.
2. **List the core ideas.**
   Write down, in a line each, the distinct ideas a learner must get right to have met the objective, from the lesson, or from a high-trust source you searched for and read when there is none.
   Never rely on memory for a fact you test.
   Cover the core first; skip trivia and phrasing a lesson happened to use.
3. **Give every item its own idea.**
   Assign each item one idea from the list, and do not use an idea twice until every idea has an item.
   If there are more items than ideas, test a leftover idea from a different angle, such as applying it to a new case instead of stating it.
   Two items fail this rule when the same sentence answers both, when one item's stem states what another asks, or when they differ only in their scenario.
4. **Choose the type for each item**, and mix them when the objective allows:
   - `mcq` when the wrong answers are predictable misconceptions or typical errors.
   - `numeric` when the objective involves a quantity: the stem states the unit and the precision.
   - `short` when the learner should produce the idea: ask for a word, a phrase or one sentence.
5. **Spread the difficulty**: mostly items that apply or explain an idea in a new case, one or two that stretch the learner, and none that need knowledge they were never given.
   Do not put all the hard items at the end.

## Write the items

**Stems**
- One question per item, complete on its own, in plain and exact wording: no double negatives, no "all of the above" or "none of the above", no trick wording.
- Give every number, unit and condition the answer depends on, and say what a comparison is for ("best for what").
- **Never put the answer in the stem.**
  Do not state the principle the right option expresses, repeat its key phrase, or describe the situation so that only one option fits.
  After writing a stem, ask: could a learner who has never studied this guess the answer from the wording alone?
  If so, rewrite it.

**Options (`mcq`)**
- Three to five options, usually four, with ids `a`, `b`, `c`, `d`.
- Build each wrong option from a specific misconception or typical error, so that someone who half understands the idea would pick it; a wrong pick should tell you something.
  Write it as a confident, reasonable claim, never a joke or an obviously false statement.
- No option is eliminated by a cue instead of by knowledge: avoid absolutes such as "always", "never" and "only" in the wrong options alone, and avoid a correct option that is the longest, the most detailed, the most hedged or the only one that repeats a word from the stem.
- Make the options parallel: the same grammar, the same level of detail, and about the same number of words.
- Do not let three options say nearly the same thing so that the odd one out is the answer.
- Vary which position holds the correct answer across the quiz.
- Exactly one option is correct, and no distractor is also defensible.

**Numeric and short items**
- A `numeric` item has one correct number, in the unit the stem names; use `tolerance` when the stem asks for rounding.
- A `short` item asks for something a key can state in a few words, and the key lists other wordings that are just as correct under `accepted`.

## Write the key

Each item in the key has, as `FORMATS.md` shows:
- `answer`: the option id, the number, or the shortest complete reference answer.
- `rationale`: why the answer is right, in one or two sentences, and then, for every wrong option of an `mcq` item, a short clause on why it is tempting and what it gets wrong.
  This is what the learner reads after grading, so write it clearly, define a new term once, and keep it short and direct as `PREFERENCES.md` asks.
- `distractors`: for each wrong option built on a misconception, the misconception's id; reuse the ids the workspace already has, and never invent an id for something that already has one.
- `accepted` and `tolerance` where they apply.

## Check the quiz before you finish

1. **Solve it blind.**
   Answer every item yourself from its stem and options alone, without looking at the key, and compare.
   Rewrite any item where you hesitate or where a careful expert could argue for a second answer, and any item whose answer you could guess without knowing the subject.
2. **Check coverage.**
   Every core idea on your list that you meant to test has an item, no two items test the same idea, and every item serves the objective and carries its id.
3. **Check the options.**
   No wrong option is absurd, none is flagged by a cue, and the correct answers are spread across positions.
4. **Check the files are valid JSON, by reading them back.**
   Write the quiz to `quizzes/NNNN.json` and its key to `keys/NNNN.json`, with the next free number, the same number for both, and exactly the keys `FORMATS.md` shows.
   Then read each file back and check it yourself, character by character where a string is long, because a file that does not parse scores as no key at all:
   - one JSON object per file, with no comments and no trailing commas;
   - every `"` inside a string value is escaped as `\"`, or, better, written as a single quote or left out; a quoted word in a rationale is the most common way a key breaks;
   - no raw line break inside a string, and every bracket and brace closed;
   - the key has one entry for every quiz item, with the same ids in the same order, and a `numeric` answer is a bare number;
   - the quiz file holds no answers and no rationale.
   If you find a fault, fix the file and read it again.
   Do not rely on the shell: it may not be available in every run.
5. Never change an existing quiz or key; a quiz that needs fixing becomes a new one.

## Giving a quiz in the chat

When the learner wants to take a quiz now, show its title and each item's stem and options, never anything from `keys/`, and collect their answers.
Write the answers exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows, and say that grading comes next.
If the learner asks a question about an item while they take it, it is a tutor request: do not hint or confirm.

## Finish

Write the files first, then end with a short message: the quiz's number and path, its objective, how many items, and that the key is ready for grading.
Never put an answer, a hint or any part of the key in the message.
Say if the quiz is ahead of the lessons, and do not write a lesson unless you were asked for one.
