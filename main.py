#!/usr/bin/env python3
"""Cat Reviews Its Human — one funny single-line one-star review.

The entry is fixed text: a house cat's deadpan one-star review of its
human, built around concrete, recognisable details (9 to 5, warm
keyboard, sunny spot on the desk) with the sting in the last words.
"""

import os

ENTRY = (
    "One star. He works 9 to 5 on the warm keyboard and calls the sunny "
    "spot on his desk his office. It has always been my bed."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
