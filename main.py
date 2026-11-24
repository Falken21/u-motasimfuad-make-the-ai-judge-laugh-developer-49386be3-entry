#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to /output/entry.txt
with no trailing newline.
"""

import os

def build_excuse() -> str:
    """Return the entry line: the oldest excuse in the book, taken literally."""
    return (
        "It works on my machine, so I shipped my machine to the data center "
        "\u2014 production is now just my laptop in a rack, and honestly, "
        "it's never run better."
    )


def write_entry(out_dir: str) -> str:
    """Write the excuse to <out_dir>/entry.txt with no trailing newline."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(build_excuse())
    return out_path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
