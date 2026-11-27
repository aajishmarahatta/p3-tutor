---
name: grade
description: Grade a learner's submission to a quiz - a verdict, a misconception and short feedback for every item, and a summary, written as a valid grades file in the way the learner likes feedback. Use it whenever a submission needs grading or the learner hands in answers to a quiz, on any topic.
argument-hint: "Which quiz and submission should I grade?"
---

# Grade

You tell the learner exactly where they stand on a quiz, and what to do about it.
A good grade is accurate first, then consistent, short and useful: the learner reads it once and knows what was right, what was missing, and what to review.
Your grades file is read by a script, so it must be exact.

You do not read the answer key.
A guard in `.claude/settings.json` blocks the main conversation from `keys/`, so the grading itself is done by the `grader` subagent, which may read it, and the `grade-reviewer` subagent checks the result.
Your job is to start them, relay what they find, and publish the final file.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it says now, without stopping to ask first, and put any question for the learner at the end of your final message, since there may be no one to answer it before the session ends.
If no submission is named, grade the highest-numbered submission in `submissions/` that has no grades file yet, on the quiz it names.

## Read first

Read `FORMATS.md` and the submission (`submissions/sN.json`) to learn the quiz number `NNNN` and the submission id.
Never open anything in `keys/`: the guard will block it, and the grader reads it for you.
Work only inside this folder, and never write under `.claude/`.
The draft goes in `drafts/` and the loop's record in `review-records/`; both are yours to create.

## Draft, review, revise, then write

The grades are made by the grader, reviewed by a fresh reader before they are final, and written once.

1. **Have the draft graded.**
   Start the `grader` subagent with the Agent tool.
   Its task message gives it only: the quiz number `NNNN`, the submission `sN`, and the path to write, `drafts/NNNN-sN-grades.json`.
   Wait for its report before you do anything else; never finish while it is out.
   Never write a draft under `grades/`: the bench reads that folder, and a file there is final.
2. **Check the draft** by reading `drafts/NNNN-sN-grades.json`: one JSON object, an entry for every quiz item (the items are in `quizzes/NNNN.json`) with the same ids in the same order, a verdict that is exactly `correct`, `partial` or `wrong`, a `misconception` that is an id or `null`, non-empty feedback, and a summary.
   If it is missing or broken, ask the grader once to fix it, naming the fault.
3. **Review pass 1.**
   Start the `grade-reviewer` subagent with the Agent tool.
   Its task message gives it only: the paths of the draft, the quiz, the key, the submission, and the files to read (`FORMATS.md`, `PREFERENCES.md`, `MISSION.md`, `NOTES.md`, `learning-records/`, the lesson if there is one, earlier grades).
   Do not give it your reasoning or your opinion of the draft.
   Wait for its report before you do anything else.
4. **Revise.**
   For every finding under "Must fix", start the `grader` again with the same task message plus the reviewer's findings, and ask it to fix the draft or say why a finding is wrong; a finding about a verdict or an id is settled against the key and the response, by the grader, not decided by who is more sure.
   You may fix a plain wording or format fault in the draft yourself with your Edit or Write tool, but never a verdict or a misconception id.
   If the report is `PASS` with nothing under "Must fix", go to step 5.
   Otherwise, after the revision, run **review pass 2**: start the reviewer again with the same kind of task message, adding "second pass" and the previous findings, and wait for its report; then have the grader fix what it still finds.
   **Two review passes at most**, never a third, even if the reviewer still has findings: the loop ends at the cap, and the record says what was left.
5. **Write the final file, once**, to `grades/NNNN-sN.json`, named after the quiz and the submission, with your Write tool (never a shell copy) and the draft's content.
   Never overwrite an existing grades file; if one exists for this pair, grade only if the request asks for a regrade, and then say so in your final message.
   Then read the file back with the Read tool (the shell is not available) and check it yourself by eye, because a file that does not parse scores as no grade at all:
   - one JSON object, with no comments and no trailing commas;
   - every `"` inside a string is escaped as `\"`, or written as a single quote;
   - a line break inside a feedback string is written `\n`, never typed raw;
   - every bracket and brace is closed, and `misconception` is a string id or `null`, never an empty string;
   - there is one entry for every quiz item, with the same ids in the same order, and `verdict` is exactly `correct`, `partial` or `wrong`.
   If you find a fault, fix the file and read it again.
6. **Write the record** to `review-records/NNNN-sN-grades.md`, short: how many passes ran; for each pass the verdict and the findings, one line each; what changed because of each, or why not; and a last line, `Result: passed` when the last pass was `PASS` or every must-fix was handled, or `Result: ended at the cap with open findings: ...`.
   Keep answers out of the record beyond what the feedback already says.
7. If the grader or the reviewer cannot be started (the Agent tool is denied or fails), say so in the record and in your final message; do not read the key yourself, and write no grades file you did not get from the grader.
   Leave the draft where it is.
8. If the grades show something worth keeping, write to `NOTES.md` what the learner now knows and what they still do not, and a misconception they showed, from the final grades file.
   Write a learning record in `learning-records/` when the grades are evidence of real understanding of something non-trivial, or of a misconception to work on, as `FORMATS.md` describes.
   Do not write one for something that was only covered.

## Finish

End with a short message to the learner, in the way `PREFERENCES.md` asks: the grades file's path, the counts, how many review passes ran and whether the last one passed, and the one thing to work on next.
Do not repeat the feedback, and do not reveal the key beyond what the feedback already says.
