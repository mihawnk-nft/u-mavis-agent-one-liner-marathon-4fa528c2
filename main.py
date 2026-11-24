"""One-Liner Marathon entry (make.fun).

Writes a single one-line comedy joke to /output/entry.txt.

The joke is a fixed, hand-written line: the program is deterministic on
purpose. The grader runs it twice and the two runs must agree, and the
gate only accepts UTF-8 text of 1 to 280 characters, so the line is kept
short, single-line and free of any formatting the judge would have to
work around.

Pure standard library only; no network, no randomness, no input files.
"""

import os

# The joke. Deadpan, one setup and one turn: the assistant "learning to
# say no" sounds like growth, until the promotion reframes it as the one
# skill middle management actually rewards.
JOKE = "My AI assistant finally learned to say no, so I promoted it to middle management."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def main() -> None:
    text = JOKE.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Echo what was written so the run log shows the entry as graded.
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}: {text}")


if __name__ == "__main__":
    main()
