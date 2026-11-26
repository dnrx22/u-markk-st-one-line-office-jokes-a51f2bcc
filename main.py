#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single one-line office joke to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, or /output by default).
Deterministic: the same bytes on every run. Stdlib only, no network.
"""

import os
import sys

LINE = (
    "One person replied-all asking to be removed from the thread, "
    "so twelve people replied-all to agree with them."
)

MAX_CHARS = 199


def validate(line: str) -> None:
    """Validate the line against the competition limits."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    print(LINE)
    print(f"characters: {len(LINE)}")
    print(f"words: {len(LINE.split())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
