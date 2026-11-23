"""One-Line Roast: The Gadget You Use Every Day — entry program.

Writes a single roast line about a fridge to /output/entry.txt.
The fridge polices the door with an alarm, yet stays silent while
food quietly spoils inside it. Python 3.13, standard library only.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The roast: one line, 141 characters, punch lands on the last word.
ROAST_PARTS = [
    "My fridge beeps like mad if I hold the door open for ten seconds,",
    "but said nothing for three weeks",
    "while the milk quietly turned into cheese.",
]


def build_line() -> str:
    """Join the roast fragments into the single entry line."""
    return " ".join(ROAST_PARTS)


def main() -> None:
    line = build_line()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
