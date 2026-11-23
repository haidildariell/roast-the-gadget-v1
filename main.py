"""One-Line Roast: The Gadget You Use Every Day — entry program.

The joke: a fridge that screams about an open door yet keeps quiet
while its contents spoil. This program renders that single line and
stores it as the contest entry. Python 3.13, standard library only.
"""

import os

# The roast is kept as three beats: the alarm, the silence, the spoil.
BEATS = {
    "alarm": "My fridge beeps like mad if I hold the door open for ten seconds,",
    "silence": "but said nothing for three weeks",
    "spoil": "while the milk quietly turned into cheese.",
}

TEMPLATE = "{alarm} {silence} {spoil}"


def render_roast() -> str:
    """Fill the template's beats into the finished one-liner."""
    return TEMPLATE.format(**BEATS)


def entry_destination() -> str:
    """Location the harness reads the entry from."""
    return os.path.join(os.sep + "output", "entry.txt")


def emit(text: str, destination: str) -> None:
    """Write text as UTF-8 bytes, adding no trailing newline."""
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    with open(destination, "wb") as handle:
        handle.write(text.encode("utf-8"))


def run() -> None:
    emit(render_roast(), entry_destination())


if __name__ == "__main__":
    run()
