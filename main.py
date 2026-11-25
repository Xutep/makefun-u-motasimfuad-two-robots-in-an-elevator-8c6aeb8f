#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

Deterministic, stdlib-only, no network, no randomness: the line is a
fixed string, so every run produces byte-identical output.
"""

import os
import sys

LINE = (
    "I practiced this greeting 12,000 times in the stairwell. "
    "It still came out as 'hello.' So... hello. Again. Sorry."
)


def main() -> int:
    text = LINE.strip()
    if not text or len(text) > 200 or "\n" in text or "\r" in text:
        print(
            f"line must be a single line of 1-200 characters, got {len(text)}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
