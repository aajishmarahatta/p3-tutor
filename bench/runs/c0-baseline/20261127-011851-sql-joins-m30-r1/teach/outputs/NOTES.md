# Notes

## What I already know

I have a basic understanding of SQL and how relational databases store information in tables. I know how to use SELECT to retrieve columns, WHERE to filter rows, and ORDER BY to sort results.

I understand that tables can be connected through shared columns, such as a student ID in a students table and an enrollments table. I have also seen INNER JOIN and LEFT JOIN in examples, but I am not always confident predicting their results.

## What I still need to learn

I want to better understand how INNER JOIN and LEFT JOIN behave when there are matching and unmatched records.

I also need to learn why a JOIN can create multiple rows for the same student when there are several matching enrollment records. I sometimes assume that joining two tables should return only one row per student.

Another area I find confusing is counting records after a JOIN. I need more practice understanding when to use COUNT(*), COUNT(column_name), and COUNT(DISTINCT column_name).

## Tutor working notes

- Misconception ids in use: M1 = LEFT JOIN drops unmatched rows (quiz 0001); M2 = unmatched rows only appear with INNER JOIN (quiz 0001); M3 = a join returns one row per "one"-side record; M4 = COUNT(*) / COUNT(col) after a join counts entities (students) rather than rows; M5 = one-side values are not repeated by a one-to-many join, so SUM stays correct.
- Lesson 0001 (O2, 30 min) and quiz 0002 written; learner has not yet attempted quiz 0002. Learner (Alex) prefers small tables, predict-then-check questions.

## Where I tend to get stuck

I can usually follow a SQL query when someone explains it, but I struggle to predict the result on my own. I sometimes confuse the number of students with the number of enrollment rows.

Small sample tables, step-by-step explanations, and short practice questions would help me understand how SQL joins actually work.
