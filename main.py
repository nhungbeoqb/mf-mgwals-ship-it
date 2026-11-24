#!/usr/bin/env python3
"""Ship It Friday (u-mgwals-ship-it-friday-30bd407a).

Writes one line: the funniest git commit message an AI coding agent
would write right before breaking production on a Friday.
Deterministic: the same bytes on every run.
"""
import os
from pathlib import Path

ENTRY = (
    "refactor: replaced the payment gateway with Math.random() "
    "\u2014 every charge is now a surprise. "
    "Deploying Friday 4:59pm, what could go wrong?"
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
