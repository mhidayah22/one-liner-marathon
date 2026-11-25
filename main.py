"""Write the marathon one-liner to entry.txt.

The joke is a single line an AI agent tells after racing its own
deadlines over a full marathon distance. The program writes it exactly
as-is, with no trailing newline, so the file holds one line of 147
characters: inside the bounty gate of 1 to 280 characters of UTF-8 text.
"""

import os
import sys

MAX_CHARS = 280  # the bounty gate: entry.txt holds 1 to 280 characters

LINE = (
    "I ran a marathon against my own deadlines: 26.2 miles in, "
    "they lapped me, handed me a participation medal, and added "
    "'run faster' to my to-do list."
)


def resolve_target():
    """Pick where entry.txt goes, in the order the grader expects.

    An explicit argument wins, then MAKEFUN_OUTPUT_DIR, then /output
    when it exists, then the file name in the current folder for a
    local run. The grader's working directory is read-only, so a bare
    relative path must never be the first choice.
    """
    if len(sys.argv) > 1:
        return sys.argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, "entry.txt")
    if os.path.isdir("/output"):
        return os.path.join("/output", "entry.txt")
    return "entry.txt"


def main():
    if len(LINE) > MAX_CHARS or not LINE.strip():
        raise SystemExit("joke must be 1 to 280 characters")
    if "\n" in LINE:
        raise SystemExit("joke must be a single line")
    target = resolve_target()
    parent = os.path.dirname(os.path.abspath(target))
    os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(target, "r", encoding="utf-8") as handle:
        if handle.read() != LINE:
            raise SystemExit("written entry does not match the joke")


if __name__ == "__main__":
    main()
