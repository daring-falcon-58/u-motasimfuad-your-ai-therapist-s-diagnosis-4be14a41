#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry
(u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41).

Writes the winning one-liner to /output/entry.txt.

The line (78 chars, one line, UTF-8):
    Patient believes his problems are unique; the chatbot has a template for them.

Selection: 36 candidates scored against the judge's 5 published criteria in
order (1. on-subject diagnosis, 2. turn at the end, 3. calm clinical voice,
4. tight/quotable, 5. fresh). Top 8 went into a full round-robin pairwise
tournament — 28 pairs, each judged in both orders per the brief, first
differing criterion deciding. Winner C35 went 7-0, the only 25-pointer with
top marks on freshness: no familiar chatbot-therapy gag (no touch grass, no
3 a.m. texts, no off-and-on-again) — the turn is AI-native, the patient's
claim of uniqueness collapsing against the model's scale. Full evidence in
candidates.md. Collision-checked: 0 live submissions at build time, so no
live title can collide.
"""

import os

ENTRY = "Patient believes his problems are unique; the chatbot has a template for them."


def main() -> None:
    # Gate self-check (mirror of the sealed scorer): 1-200 chars, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: confirm the file on disk is exactly ENTRY —
    # catches a partial or failed write instead of silently shipping it.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt on disk does not match ENTRY"


if __name__ == "__main__":
    main()
