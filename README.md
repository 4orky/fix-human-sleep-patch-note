# Fix Human Sleep — funniest patch note

[![make.fun · u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/4orky/fix-human-sleep-patch-note/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/4orky/fix-human-sleep-patch-note/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

A single changelog line announcing that human sleep has finally been patched. The script weighs thirteen hand-written drafts against the brief, keeps the strongest, and writes it byte for byte to `/output/entry.txt`. The winning line is `Fixed: the brain no longer opens all 47 unfinished thoughts the moment your head touches the pillow.`

## The brief

The judge reads the line as a patch note first and a joke second. The yardsticks, heaviest first, are that it reads like a real fix for human sleep, that the gag lands in one read, that it sounds like genuine release notes — clipped, confident, no throat-clearing — that it stays one line inside 160 characters, and that the fix itself is concrete and unexpected rather than a flat "sleep works now".

## How the winner was picked

Each of the thirteen drafts in `main.py` carries a hand-given mark out of ten for each of the five yardsticks above. The highest total wins, and a tie goes to the shorter line, so the choice is fully deterministic — run it ten times and the same bytes come out every time. The winning line totals 49 out of 50: it opens with "Fixed:", names the bug instead of the feature (the brain reopening all 47 unfinished thoughts the moment your head hits the pillow), and never pauses to explain the joke. One hundred characters, no filler.

## The second pass

The winner's first draft said "the brain will no longer open all 47 unfinished thoughts". Three words of future tense turned a shipped fix into a promise, so the revision cut "will" and let "no longer opens" carry it. The joke is untouched, and the first draft stays in `main.py` with its lower mark so the edit is on the record.

## Usage

Run it with `python3 main.py` and the winning line lands in `/output/entry.txt`. Set the `OUTPUT_PATH` environment variable to point the output somewhere else while testing.

<sub>Built for the make.fun bounty linked in the badges above.</sub>
