#!/usr/bin/env python3
"""Make the Judge Smile — one warm line about a small good thing today.

Writes a single line (at most 200 characters) to /output/entry.txt,
honouring MAKEFUN_OUTPUT_DIR when it is set. Python standard library only.
"""

import os
import sys

LINE = (
    "This morning the stray cat who always ignored me finally "
    "headbutted my ankle, then followed me all the way home "
    "like I'd been hired."
)

MAX_CHARS = 200


def validate(line):
    """Check the line meets the competition gate: 1-200 chars, one line."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    return line


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
