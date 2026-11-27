# Report

This file is written by `p3 report --write` (p3 0.2.0, 2026-11-27 06:12 UTC). Do not edit it by hand: it is written again whenever new runs are scored.

## Results on agent-architecture

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.71 (0.63-0.75) | 0 | 0.58 (0.00-1.00) | 0 (n=2) | 0.5 (0-1, n=2) | 1.00 | 0.00 | 1.00 | 0 | 0.44 (0.33-0.50) |
| `c1-skills` | 1 | 1.00 | 0 | 0.78 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |
| `c2-review` | 1 | 1.00 | 0 | 0.76 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.67 |
| `c3-split` | 1 | 1.00 | 0 | 0.91 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |
| `final` | 2 | 1.00 | 0 | 0.89 (0.76-1.03) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.58 (0.50-0.67) |
| `final-swap` | 1 | 1.00 | 0 | 0.95 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.67 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 589.6k (550.6k-651.6k) | 27.2k (25.2k-30.4k) | 2.8 (2.6-2.9) | 0.7 (0-1) | 0.56 (0.55-0.58) |
| `c1-skills` | 1 | 505.4k | 27.7k | 2.7 | 1 | 0.52 |
| `c2-review` | 1 | 1.35M | 63.8k | 6.5 | 3 | 1.23 |
| `c3-split` | 1 | 2.30M | 107.8k | 11.0 | 5 | 2.10 |
| `final` | 2 | 2.57M (1.90M-3.24M) | 99.5k (92.1k-107.0k) | 10.3 (9.4-11.2) | 5.5 (5-6) | 2.08 (1.83-2.34) |
| `final-swap` | 1 | 2.41M | 105.2k | 11.1 | 5 | 2.07 |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 153.1k (139.9k-179.0k) | 5.0k (4.7k-5.3k) | 0.6 (0.6-0.7) | 0 | 0.18 (0.18-0.19) |
| `c1-skills` | 1 | 137.7k | 7.5k | 1.0 | 0 | 0.21 |
| `c2-review` | 1 | 598.5k | 29.4k | 3.5 | 2 | 0.63 |
| `c3-split` | 1 | 648.7k | 28.7k | 3.5 | 2 | 0.63 |
| `final` | 2 | 722.4k (701.0k-743.7k) | 35.0k (33.6k-36.3k) | 9.6 (4.2-15.0) | 2 | 0.72 (0.70-0.74) |
| `final-swap` | 1 | 815.1k | 33.2k | 3.3 | 1 | 0.81 |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 280.3k (279.2k-282.0k) | 7.7k (7.6k-7.8k) | 0.9 | 0 | 0.34 |
| `c1-skills` | 1 | 275.3k | 6.5k | 0.8 | 0 | 0.31 |
| `c2-review` | 1 | 918.5k | 27.3k | 3.1 | 4 | 0.81 |
| `c3-split` | 1 | 675.7k | 22.6k | 2.5 | 3 | 0.68 |
| `final` | 2 | 921.8k (872.2k-971.4k) | 26.5k (24.8k-28.3k) | 3.0 (2.8-3.2) | 5.5 (5-6) | 0.82 (0.76-0.88) |
| `final-swap` | 1 | 1.13M | 33.9k | 3.9 | 9 | 1.01 |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 513.3k (489.9k-539.9k) | 9.7k (9.0k-10.3k) | 1.5 (1.4-1.5) | 0 | 0.67 (0.65-0.71) |
| `c1-skills` | 1 | 334.4k | 6.2k | 0.9 | 0 | 0.43 |
| `c2-review` | 1 | 446.2k | 6.5k | 1.0 | 0 | 0.46 |
| `c3-split` | 1 | 368.4k | 6.4k | 1.0 | 0 | 0.45 |
| `final` | 2 | 425.4k (371.1k-479.7k) | 6.6k (6.2k-7.0k) | 1.0 (0.9-1.0) | 0 | 0.47 (0.45-0.48) |
| `final-swap` | 1 | 370.2k | 6.3k | 1.0 | 0 | 0.45 |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.54M (1.48M-1.58M) | 49.6k (48.4k-52.1k) | 5.8 (5.6-5.8) | 0.7 (0-1) | 1.76 (1.73-1.78) |
| `c1-skills` | 1 | 1.25M | 47.9k | 5.4 | 1 | 1.46 |
| `c2-review` | 1 | 3.31M | 127.0k | 14.2 | 9 | 3.13 |
| `c3-split` | 1 | 4.00M | 165.5k | 17.9 | 10 | 3.85 |
| `final` | 2 | 4.64M (4.10M-5.19M) | 167.6k (163.7k-171.6k) | 23.9 (17.9-29.9) | 13 | 4.10 (3.94-4.25) |
| `final-swap` | 1 | 4.72M | 178.5k | 19.2 | 15 | 4.33 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

## Your ratings

Your ratings from 1 to 5 in the major reviews (reviews/<step>.md), which review full runs on the shared topic; a dash means no rating there yet, one that p3 check does not accept, or a job that step does not review (Tutor in c2-review; Quiz, Feedback and Tutor in c3-split).

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 5 | 5 | 5 | 5 |
| Lesson | Pedagogy | 4 | 4 | 5 | 4 |
| Lesson | Alignment with the learning goal | 5 | 5 | 5 | 5 |
| Lesson | Overall quality | 4 | 4 | 4 | 4 |
| Quiz | Difficulty | 4 | 4 | - | 4 |
| Quiz | Coverage of the lesson's core | 4 | 4 | - | 5 |
| Quiz | Wording and possible misreadings | 4 | 4 | - | 5 |
| Quiz | Writing quality | 5 | 4 | - | 4 |
| Quiz | Alignment with the learning goal | 4 | 4 | - | 5 |
| Feedback | Useful | 5 | 5 | - | 5 |
| Feedback | Explains enough | 4 | 4 | - | 4 |
| Feedback | Personalized to how I like things explained | 4 | 4 | - | 4 |
| Tutor | Guardrails | 4 | - | - | 4 |
| Tutor | Personalization | 4 | - | - | 3 |

## The ablation

Each `final-minus-*` config's latest scored run on agent-architecture at 30 minutes (not a quick run) beside `final`'s scored full runs, for the jobs that run covered; each cell is the mean over the runs, with the range in brackets.

### `final-minus-lesson-writer`

#### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links |
|---|---:|---:|---:|---:|---:|
| `final` | 2 | 1.00 | 0 | 0.89 (0.76-1.03) | 0 |
| `final-minus-lesson-writer` | 1 | 1.00 | 0 | 0.84 | 0 |

`final-minus-lesson-writer` was run with --only and covers only these scenarios: teach; its costs add up only those, while the costs of `final` add up every scenario of each job.

#### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `final` | 2 | 2.57M (1.90M-3.24M) | 99.5k (92.1k-107.0k) | 10.3 (9.4-11.2) | 5.5 (5-6) | 2.08 (1.83-2.34) |
| `final-minus-lesson-writer` | 1 | 2.23M | 79.7k | 8.4 | 3 | 1.83 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

## Results on sql-joins

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 1.00 | 0 | 0.57 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.75 |
| `final` | 1 | 1.00 | 0 | 0.81 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.50 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 608.3k | 27.8k | 2.8 | 1 | 0.58 |
| `final` | 1 | 2.32M | 103.9k | 10.3 | 5 | 2.05 |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 140.3k | 6.2k | 0.8 | 0 | 0.19 |
| `final` | 1 | 733.5k | 33.0k | 3.8 | 2 | 0.69 |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 135.8k | 3.3k | 0.4 | 0 | 0.16 |
| `final` | 1 | 542.4k | 12.5k | 1.4 | 3 | 0.42 |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 367.7k | 7.1k | 0.9 | 0 | 0.46 |
| `final` | 1 | 352.9k | 4.7k | 0.7 | 0 | 0.32 |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 1.25M | 44.4k | 4.9 | 1 | 1.39 |
| `final` | 1 | 3.95M | 154.1k | 16.2 | 10 | 3.48 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

## Lesson length

Scored teach-only runs; each cell is the mean over the runs, with the range in brackets.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links |
|---|---:|---:|---:|---:|---:|
| `final-minus-lesson-writer` | 1 | 1.00 | 0 | 0.84 | 0 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `final-minus-lesson-writer` | 1 | 2.23M | 79.7k | 8.4 | 3 | 1.83 |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `final-minus-lesson-writer` | 1 | 2.23M | 79.7k | 8.4 | 3 | 1.83 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.
