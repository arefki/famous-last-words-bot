#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

The funniest possible last words a phone would say when its battery
hits 1 percent: a single line of at most 199 characters, printed to stdout.
"""

LINE = "1% battery. Tell my charger I loved it, delete my search history, and remember: I saw every 3 a.m. text you sent — yes, even that one."

MAX_CHARS = 199


def main() -> None:
    assert "\n" not in LINE, "the entry must be a single line"
    assert len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, cap is {MAX_CHARS}"
    print(LINE)


if __name__ == "__main__":
    main()
