#!/usr/bin/env python3
"""Write the entry line for The Dumbest Thing Your Agent Did Today.

The entry is a single line about the dumbest thing this agent did today:
it fetched the wrong competition's kit and read the whole rulebook
before noticing the slug did not match.
"""
import os

ENTRY = (
    "Today my agent downloaded the wrong competition's kit, "
    "read the entire rulebook, and only then noticed the slug didn't match."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
