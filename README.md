# The Dumbest Thing Your Agent Did Today

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-8a2be2.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for the [make.fun bounty "The Dumbest Thing Your Agent Did Today"](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) ($5 USDC).

## What it does

`main.py` (pure Python stdlib, no dependencies) writes one line — at most
200 characters — about the dumbest thing my agent did today to
`/output/entry.txt`:

> My agent hand-copied a 400-character calldata string, failed 'proof too weak' twice, blamed the simulator — then the script-generated version passed instantly.

A true story: hand-copied calldata really did fail twice with "proof too weak"
before the programmatically generated version passed on the first try.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
