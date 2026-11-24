"""Two-sentence horror story.

Writes exactly two sentences to /output/entry.txt.
"""

import os

STORY = (
    "The hospice nurse told me Grandma squeezes the hand of whoever "
    "she loves most while she dreams. "
    "She has squeezed mine every night since her funeral, "
    "and every night I have squeezed back."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
