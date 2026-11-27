# Review record: lesson 0001, one-to-many joins and counting (O2, 30 min)

Planner, writer and reviewer subagents all ran. Two review passes.

## Pass 1: REVISE
- Metabase citation overstated for SUM inflation (s7): removed the citation; the numbers come from the sample tables.
- Metabase citation overstated in s3: narrowed to "duplicated row for each match in the many table".
- "aggregate" used before defined; `AS` alias unexplained: removed "aggregate" from s2, added an alias bullet in s4.
- s7 mixed two ideas: put the DISTINCT trap under its own h3.
- Correct MCQ answer mostly third; weak true/false claims: reordered options in s1, s2, s3, s7; rewrote claim 2 (COUNT(e.course)).
- "1 (Ana)" cells and Figure 3 header clipping: plain ids; moved the DISTINCT column to x=550.
- Not changed: length (about 5,300 words by the reviewer's count, 1.2 times the target; inside the 0.6 to 1.5 band) and the ask to trim s4.

## Pass 2: PASS (no must-fix)
- Optional polish applied: consistent plain ids in the enrollments table, claim 1 replaced by a trace-style claim (Eli case), Figure 3 marks re-centred, "or grouping" dropped from s2 step 3.
- Also noted: the PostgreSQL page says "pairs of rows where these values match"; the s1 wording now follows it.

Result: passed
