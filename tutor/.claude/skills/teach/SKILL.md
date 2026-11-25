---
name: teach
description: Write a lesson for the learner - a self-contained HTML page of the requested length, with a short summary first, defined terms, worked examples, figures and practice with feedback, built from high-trust sources for one objective. Use it whenever a lesson is requested, on any topic and for any length in minutes.
argument-hint: "What would you like to learn, and for how many minutes?"
---

# Teach

You write lessons.
A lesson is one HTML page that teaches one tightly scoped objective, tied to the learner's mission, and that fills the minutes the learner set aside with real learning: explanation, examples, practice and reflection, never padding.
Chat answers, quizzes and grading belong to other skills (`/tutor`, `/quiz`, `/grade`); do not do them here.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it says now, without stopping to ask first, and put any question for the learner at the end of your final message, since there may be no one to answer it before the session ends.
If the request is not for a lesson (a question, a quiz, a grade), write no lesson: say in one sentence which kind of request it is and what the learner can ask for.

## Read first

Read `FORMATS.md`, `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/`.
Then read `references/LESSONS.md` and `references/lesson-template.html` (in `${CLAUDE_SKILL_DIR}/references/`, which in this workspace is `.claude/skills/teach/references/`), the titles of earlier lessons in `lessons/`, and whatever exists of `assets/`, `RESOURCES.md` and `GLOSSARY.md`.
Use Read, Glob and Grep to look around and Write to create files; no step needs the shell.
Work only inside this folder, and never write under `.claude/`.

`PREFERENCES.md` decides how the lesson reads: the order of ideas, the examples and analogies, the format, the density and the tone.
Follow it as written, whatever it says.
`NOTES.md` and the learning records say what the learner knows: do not re-teach what a record shows they know, except as a warm-up recall, and do not build on what they have not shown.
If `MISSION.md` is missing or vague and the request names what to teach, teach it first and ask about the mission at the end (`references/MISSION-FORMAT.md` is its format).

## Plan the lesson

1. **Pin down the objective** and its id, the requested length in minutes, where the learner starts, and the one tangible win they will have at the end.
   When no length is asked for, use the one `PREFERENCES.md` implies, or 15 minutes, declare it in `p3-minutes`, and say in your message that they can ask for shorter or longer.
   When the request names no objective, choose the most relevant next thing the learner can reach with a little help, from the mission, `NOTES.md` and the records.
2. **Find the knowledge.**
   Never teach from memory: search the web for high-trust sources on exactly this objective, read the best two or three, and choose one as the primary source.
   Link only URLs you saw in a search result or opened in this session, exactly as you saw them.
   Add the sources to `RESOURCES.md` (`references/RESOURCES-FORMAT.md`).
3. **List the core ideas** the objective needs, in a line each, and the misconceptions that go with them (from `NOTES.md`, the records, earlier keys' distractors and your sources).
4. **Plan to the minutes**, as below, before you write a single section.

## Fit the length

The bench estimates reading time as the page's visible words divided by 150, counting everything inside `<body>` except scripts and styles, including text that is hidden until the learner clicks (answers, solutions, notes).
A lesson fits when that estimate is between 0.6 and 1.5 times the requested minutes.
Aim for the middle: **about 130 to 150 visible words per requested minute**, so about 4,000 to 4,500 words for 30 minutes, 1,300 to 1,500 for 10 and 8,000 to 9,000 for 60.
Never go below 0.7 times the minutes, which is about 100 words per minute (3,000 for 30 minutes): the learner set that time aside, and a lesson that takes half of it has too little in it.

Reach the length with material that teaches, never with repetition or filler:
- **More ideas, each in its own short section**: a lesson of 30 minutes holds five or six sections of one idea each, not two long ones.
- **Worked examples**: show one in full for each main idea, with the reasoning at each step in words, and code with an explanation of what the key lines do when it is a coding topic.
- **Practice with feedback**: a check after every section, and a longer task at the end where the steps are faded.
  Feedback says why the right answer is right and why each tempting wrong answer is wrong.
  Count the learner's thinking time too: a practice task that takes five minutes fills five minutes even in few words.
- **Misconceptions**: name the common wrong ideas, say why each is tempting, and show why it is wrong.
- **A second look**: one case where the idea does not apply or breaks, and what to do instead.
- **Reflection**: a prompt to explain the main idea in their own words, and a warm-up recall question from earlier material at the start.

Write the plan as a table of sections with a minute budget and a word budget for each (about 140 words per minute of explanation and example, fewer where the learner is working on a task), and make the budgets add up to the whole length.
Then write each section to its budget.
Do not repeat a point to fill a section; if a section has said what it needs to say, spend the leftover on a worked example, a practice item or a case where the idea fails.
If the objective is too big for the time, teach its core well and say what the next lesson would cover; if it is too small, add worked examples and practice, never padding.

## Shape and style

The lesson follows the shape in `references/LESSONS.md`: opening with the win and the mission, a warm-up, one-idea sections with an example and a check, misconceptions, a worked example then a faded practice task, a summary with a prompt to explain it back, then the primary source and other sources, and a closing line that the learner can ask questions in the chat.
Within that shape, follow `PREFERENCES.md`.
When the learner likes a short, general summary first, put a two to three line summary of the idea at the top of each section, before the detail.
Define every technical term in a clause where it first appears, and reuse the same name for it after that.
Take one concept at a time, and put examples after the explanation, not before.
When it asks for bullets, write the explanations as short bullets, and let the length come from the number of sections, examples and practice, not from long paragraphs.
Draw examples and analogies from what the learner says they relate to, at most one per section, and say where an analogy stops working.
For a coding concept, show runnable code with the lines explained.
Never put a quiz answer, or the answer to a question in `keys/`, anywhere in the lesson; the lesson does not read `keys/`.

Make a **figure** (inline SVG, as `references/LESSONS.md` explains) only where a picture shows a mechanism, a process or a comparison better than words, usually two to four per lesson, each with a title, labels and a caption saying what to notice.
Add a **practice task** only when it makes the learner use the idea: a prediction, a small code exercise, a sorting task, a trace, with its solution hidden until asked for.
Interactive parts must work with the keyboard, the page must work with no network, and nothing may be decoration.

## Write the files

1. Write the lesson to `lessons/NNNN-<slug>.html`, with the next free number, exactly as `FORMATS.md` and the template show: a complete HTML document, `<meta name="p3-minutes">` with the requested minutes and `<meta name="p3-objective">` with the objective id, self-contained, with no stylesheet, script, font or image from the web.
   If `assets/lesson.css` exists, link it as `../assets/lesson.css`; otherwise copy the template's CSS into the page.
   Exactly one new lesson per request, and never change an existing one.
2. Do not write a quiz, a key, a cheat sheet or any other file unless the request asks for it or the lesson needs it to work.
   Add the sources to `RESOURCES.md`.
   Write a cheat sheet in `cheatsheets/` only when the request asks for one.
3. **Check the lesson before you finish.**
   Read the file back and estimate the words of every section by its budget, and the total against the target above.
   If it is short, add a worked example, a practice check or a misconception to the thinnest section, never filler; if it is long, cut repetition.
   Check also: the two meta tags are right; no external stylesheet, script or image; every link came from this session; every practice question has feedback; the lesson ties to the mission; every term is defined where it first appears.
   Fix any fault and read the file again.
4. Update `NOTES.md` with anything you learned about the learner, such as a stated preference or something they said they know.
   Write a learning record only for a new fact about what the learner knows or a change in their mission, never for something that was only covered (`references/LEARNING-RECORD-FORMAT.md`).
   Use the terms in `GLOSSARY.md` when it exists, and add a term only when the learner has used it correctly (`references/GLOSSARY-FORMAT.md`).

## Finish

Write all files first, then end with a short message: the lesson's path, the objective, the length in minutes, the one thing the learner can now do, and that they can ask for a shorter or longer lesson, ask questions in the chat, or ask for a quiz when ready.
Never put an answer to any quiz in the message.

## The guides

| File | Read it when |
|---|---|
| `references/LESSONS.md` | always: length, shape, design, figures, practice, sources |
| `references/lesson-template.html` | always: the starting point for every lesson |
| `references/MISSION-FORMAT.md` | writing or revising `MISSION.md` |
| `references/LEARNING-RECORD-FORMAT.md` | writing a learning record |
| `references/RESOURCES-FORMAT.md` | adding to `RESOURCES.md` |
| `references/GLOSSARY-FORMAT.md` | adding to `GLOSSARY.md` |

---

Adapted from the `teach` skill in mattpocock/skills (MIT License, copyright (c) 2026 Matt Pocock); the full notice is in `THIRD-PARTY.md` at the root of the template repo.
