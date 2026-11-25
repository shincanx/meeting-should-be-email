#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — make.fun bounty entry.

Writes exactly one joke line (plain text, <= 200 chars) about a meeting
that should have been an email to $MAKEFUN_OUTPUT_DIR/entry.txt,
then prints that line. Fully deterministic, exit 0.
"""
import os

LINE = "We scheduled a meeting to discuss the email, then emailed a recap of the meeting about the email. Attendance: everyone. Attention: no one."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
