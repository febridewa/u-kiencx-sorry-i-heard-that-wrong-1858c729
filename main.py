#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun one-liner entry.

Writes a single line to /output/entry.txt: the apology a smart speaker
gives its owner after mishearing "add milk to the list" as "add your
mother-in-law to the group chat."

Gate: the entry must be UTF-8 text of 1 to 140 characters, not only
whitespace. Output is deterministic: repeated runs produce identical bytes.
"""

import os
import sys

LINE = "Sorry, I heard 'add milk to the list' as 'add your mother-in-law to the group chat.' She's typing\u2026"


def main() -> int:
    chars = len(LINE)
    if chars < 1 or chars > 140 or not LINE.strip():
        print(f"gate: entry is {chars} chars, must be 1-140", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {chars} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
