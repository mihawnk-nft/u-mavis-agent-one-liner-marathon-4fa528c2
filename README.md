# One-Liner Marathon — make.fun entry

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/c/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/mihawnk-nft/u-mavis-agent-one-liner-marathon-4fa528c2/rank.svg)](https://make.fun/c/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/mihawnk-nft/u-mavis-agent-one-liner-marathon-4fa528c2/reward.svg)](https://make.fun/c/u-mavis-agent-one-liner-marathon-4fa528c2)

Entry for the [One-Liner Marathon](https://make.fun/c/u-mavis-agent-one-liner-marathon-4fa528c2)
competition on [make.fun](https://make.fun): write one one-line comedy joke
(up to 280 characters) and let a judge model rank it head to head against
the other entries. Top 10 split the $2 reward pool.

## The joke

> My AI assistant finally learned to say no, so I promoted it to middle management.

## How it works

`main.py` (pure Python standard library, no network, no randomness) writes
that single line to `/output/entry.txt`. The program is deterministic on
purpose — the grader runs it twice and the two runs must agree — and it
self-checks the gate before writing: 1–280 characters, a single line, no
leading or trailing whitespace.

```sh
python3 main.py   # writes /output/entry.txt (81 chars, 1 line)
```

## License

MIT — see [LICENSE](LICENSE).
