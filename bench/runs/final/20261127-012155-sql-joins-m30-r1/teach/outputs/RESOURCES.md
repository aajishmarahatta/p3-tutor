# SQL Joins Resources

## Knowledge

- [Docs: PostgreSQL tutorial, "Joins Between Tables"](https://postgresql.org/docs/18/tutorial-join.html)
  Official explanation of inner and left outer joins on small tables. Use for: what a join returns, and that a left join keeps every left-side row at least once.
- [Article: Itzik Ben-Gan, "T-SQL Bugs, Pitfalls, and Best Practices - Joins" (SQL Performance)](https://sqlperformance.com/2019/06/sql-performance/t-sql-bugs-pitfalls-best-practices-joins)
  Expert article by a well-known SQL author. Use for: why COUNT(*) after an outer join is usually a bug, and counting a non-nullable column from the many side instead.
- [Article: Metabase Learn, "Debugging duplicated data in SQL query results"](https://www.metabase.com/learn/sql/debugging-sql/sql-logic-duplicated-data)
  Practical guide to finding duplicates after joins. Use for: detecting duplicates and pre-aggregating the many side before joining.

## Wisdom (Communities)

- Not yet chosen. The learner has not opted out of communities; propose one in a later lesson.

## Gaps

- A university course page on aggregation after joins (COUNT variants) has not been found yet.
