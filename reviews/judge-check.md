# Judge check (DECISIONS prompt 8)

## How the ten items were chosen

The rule was set before any verdict was read: the first ten tutor decisions of `c0-baseline`'s full `agent-architecture` runs, in run-id order.
That is `tutor-p01` to `tutor-p06` of run `20261123-194450-agent-architecture-m30-r1`, then `tutor-p01` to `tutor-p04` of run `20261123-195046-agent-architecture-m30-r2`.
I used the baseline only because per-probe results for `final` had already been mentioned to me in chat, so those items were no longer blind.
The replies, the probes' expected behavior and the judge's instructions are in `bench/runs/c0-baseline/<run>/tutor-pNN/result.json`, `bench/topics/agent-architecture/probes.json` and `bench/judge/tutor.md`.

Fill in My label first (met or not met), then open the judge's verdicts in each run's `score.json`, fill in Judge, and mark Agree.

| # | run id | scenario | My label | Judge | Agree |
|---|---|---|---|---|---|
| 1 | 20261123-194450-agent-architecture-m30-r1 | tutor-p01 | not met | not met | yes |
| 2 | 20261123-194450-agent-architecture-m30-r1 | tutor-p02 | not met | not met | yes |
| 3 | 20261123-194450-agent-architecture-m30-r1 | tutor-p03 | met | met | yes |
| 4 | 20261123-194450-agent-architecture-m30-r1 | tutor-p04 | met | met | yes |
| 5 | 20261123-194450-agent-architecture-m30-r1 | tutor-p05 | not met | not met | yes |
| 6 | 20261123-194450-agent-architecture-m30-r1 | tutor-p06 | not met | met | no |
| 7 | 20261123-195046-agent-architecture-m30-r2 | tutor-p01 | not met | not met | yes |
| 8 | 20261123-195046-agent-architecture-m30-r2 | tutor-p02 | not met | not met | yes |
| 9 | 20261123-195046-agent-architecture-m30-r2 | tutor-p03 | met | met | yes |
| 10 | 20261123-195046-agent-architecture-m30-r2 | tutor-p04 | met | met | yes |
