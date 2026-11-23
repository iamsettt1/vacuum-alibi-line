#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes a single deadpan excuse from a robot vacuum for missing a spot
to /output/entry.txt. Deterministic: the line is a fixed constant, so
every run produces byte-identical output.
"""

import os

LINE = (
    "I did not miss that spot. My lidar classified the crumb as "
    "load-bearing, and I refuse to be the robot that collapses this house."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters, a single line, not blank.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
