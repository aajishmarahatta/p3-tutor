# Review record: 0001-context-and-memory-in-an-agent (O3, 30 minutes)

Two review passes ran. The plan came from the lesson-planner, the draft from the lesson-writer.

## Pass 1: REVISE
- Section 8 pasted-manual figure was 41,560 and should be 41,260; the example ignored history growth. Fixed: 41,260, totals recomputed, growth stated as ignored.
- No prompt-caching caveat on cost claims. Added a caveat in Section 2 and Section 8, cited to the Context windows docs I read. I did not link the prompt-caching page, which I never opened.
- `load_status` solution contradicted its own advice. Rewrote the task, then fixed the solution.
- Section 3 history order was inconsistent. Reordered, and rewrote the solution.
- BM25 described as a shared-word count, and "contextual embeddings" and "contextual BM25" undefined. Reworded; the toy `score` is labelled a simplified stand-in.
- Warm-up could be answered by reading the page. Rewrote it as genuine recall.
- Misconceptions lacked why each is tempting. Added.
- Section 2 code did not reproduce Figure 2. Rewrote it with the exact output in a comment. Noted the message format in Section 3.
- Just-in-time aside had no example. Added one.

## Pass 2: REVISE
- Section 7 statistic lacked baselines, who writes the prefix, and the test sets. Added all three.
- `load_status` task and solution disagreed. Task now says "student not in file", with the missing-file case as a bonus and a full try/except solution.
- Warm-up used "token" before Section 1 defines it. Reworded.
- BM25 line overstated the source ("rare words"). Reworded to TF-IDF favoring distinctive words.
- `compact` used an assistant role for the summary. Changed to user and marked as a sketch.
- Not changed (optional): a second synonym-trap check in Section 5; the Section 1 sort items lean "in the window".

Reading time was estimated at about 5,000 visible words (33 minutes), within the bench's band.

Result: passed (all must-fix items from pass 2 were handled).
