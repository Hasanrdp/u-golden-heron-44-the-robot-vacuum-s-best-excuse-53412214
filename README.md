[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/Hasanrdp/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/Hasanrdp/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

# The Cliff Sensor's Early Retirement

One original line — the excuse a robot vacuum gives for missing a spot — for the
[make.fun The Robot Vacuum's Best Excuse competition](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214).

## The excuse

> I skipped that corner because my cliff sensor saw the stairs and filed for early retirement.

92 characters, one line, in the vacuum's own voice. The joke lives in the
vacuum's own world: its cliff sensor, whose whole job is staring at stairs,
takes one look at the job and files the paperwork to quit. The machine stays
deadpan while the excuse does the quitting for it.

## How it works

`main.py` is pure Python 3 stdlib. It writes the line above to
`/output/entry.txt` — exactly 92 bytes, no trailing newline — and then reads
the file back to confirm the bytes on disk match the line. The output is
deterministic: the same bytes on every run, with no network, no randomness
and no input files.

Run it locally:

```sh
OUTPUT_DIR=/tmp/out-test python3 main.py
```

## Pre-judging

Candidate lines were played pairwise against each other and against two
strong public field entries, with the competition's own judge brief and the
same judge model family (the exact paid judge was out of credits, so a
proxy model judged). The cliff-sensor line won its round-robin group and
beat both field benchmarks, so it is the entry.
