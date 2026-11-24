#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse - make.fun
u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.

One original line: the excuse a robot vacuum gives for missing a spot,
written to /output/entry.txt. Deterministic: the same bytes on every run,
no network, no randomness, no input files.
"""

import os
import sys

EXCUSE = (
    "I skipped that corner because my cliff sensor saw the stairs "
    "and filed for early retirement."
)


def main() -> int:
    # Runtime gate, mirroring the house gate: 1-140 chars, not only whitespace.
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"excuse is {len(text)} chars, outside the 1-140 gate")
    if not text:
        raise SystemExit("excuse is only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back gate: the bytes on disk must be exactly the line above.
    with open(path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit("entry.txt on disk does not match the excuse")
    return 0


if __name__ == "__main__":
    sys.exit(main())
