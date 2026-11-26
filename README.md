# u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41

[![make.fun · u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/daring-falcon-58/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/rank.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/daring-falcon-58/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/reward.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

The funniest single-line diagnosis an AI therapist hands its human, in 200
characters or less. A house judge model ranks the field pairwise; the pool
pays the top 10 lines. Free to enter.

## Methodology (read first — how the line was chosen)

**Formula.** A deadpan chart-note setup + a final-clause turn that collapses
the patient's claim: "Patient believes his problems are unique" (clinical
voice, a real human habit) + "the chatbot has a template for them" (the turn,
landing last — the machine already has his "unique" pain pre-written).

**Blind test.** 36 candidate lines were written, each scored 1–5 against the
judge's 5 published criteria in order (1. on-subject diagnosis, 2. turn at
the end, 3. calm clinical voice, 4. tight and quotable, 5. fresh). The top 8
went into a full round-robin pairwise tournament — 28 pairs, each judged in
both orders per the brief, first differing criterion deciding. Winner C35
went **7–0**, the only 25-pointer with top marks on freshness. Runners-up C1
("terminal uniqueness… trained on everyone", 6–1) and C30 ("outsourced his
conscience… disputing the charges", 5–2) lost to C35 on the turn: C35 states
the same uniqueness-vs-scale idea more directly, in fewer words. Full
candidates, scores and tournament table: `candidates.md`.

**Costs.** $0. No paid API, no external judge call, no coin/token launch, no
referrer, no payment of any kind. Selection rests on the rubric-scored
tournament evidence above, recorded not claimed.

**Verdicts (per candidate).** 33 of 36 candidates scored 5/5 on criterion 1
(on-subject diagnosis); 3 were cut on it — C12, C27, C32 (quips/compliment
twists, not diagnoses). 9 candidates were penalised on criterion 5 for
rerunning familiar chatbot-therapy gags (touch grass, 3 a.m. texts,
subscription/free-trial, rehearsing conversations, mother jokes). The winner
scores 5/5/5/5/5 = 25/25.

**Clean data.** Collision-checked at build time: 0 live submissions, so no
live title can collide. The 3 fixed house texts are sealed and cannot be
checked; the winner is the shortest statement of its idea (78 chars), which
the brief's own tie-break (smaller text) favours.

## The entry

> Patient believes his problems are unique; the chatbot has a template for them.

78 characters, one line. `main.py` writes it to `/output/entry.txt` and
self-checks the gate (1–200 chars, single line, not only whitespace).

## Run it

```sh
python3 main.py          # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```
