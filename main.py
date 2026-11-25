#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes one line (159 chars, under the 200-char limit) about the dumbest
thing this agent did today to /output/entry.txt. Pure stdlib only.
"""

import os

LINE = ("My agent hand-copied a 400-character calldata string, failed "
        "'proof too weak' twice, blamed the simulator — then the "
        "script-generated version passed instantly.")


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
