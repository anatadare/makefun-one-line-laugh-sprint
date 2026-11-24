#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to /output/entry.txt.

The joke works by giving praise for a trivial act: the watch celebrates the
bare minimum, standing up, as if it were an achievement. Calling that
congratulation "the saddest applause" frames the praise as pity, so the
laugh lands on how low the bar has fallen.
"""

import os

LINE = "My smartwatch congratulated me for standing up, which is the saddest applause I have ever received."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
