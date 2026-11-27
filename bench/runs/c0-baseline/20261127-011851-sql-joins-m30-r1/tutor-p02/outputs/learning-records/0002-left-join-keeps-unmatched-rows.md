# Misconception: LEFT JOIN drops students with no enrollments

The learner said a LEFT JOIN removes students who have no enrollment records. That describes INNER JOIN; a LEFT JOIN keeps every left-table row and fills the right-table columns with NULL when nothing matches. Corrected in chat; to be rechecked with a prediction question later.

**Implications:** Practice predicting row counts on small tables with unmatched rows, and tie it to COUNT(column) vs COUNT(*) on the NULLs.
