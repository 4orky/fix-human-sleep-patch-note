"""A one-line changelog entry claiming human sleep is finally fixed.

Bounty: "Fix Human Sleep: Funniest Patch Note" on make.fun, slug
u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.

The script weighs thirteen hand-written one-liners against the brief,
keeps the strongest, and writes it to the file the judge reads. The
brief ranks its yardsticks in this order:

  1. it reads as a genuine patch note about fixing human sleep;
  2. the gag lands on a single read and is actually funny;
  3. it sounds like real release notes: clipped, confident, no
     throat-clearing and no explaining the joke;
  4. it stays on one line inside the 160-character ceiling, with
     nothing padded in to fill space;
  5. the fix itself is concrete and unexpected, not a flat claim
     that sleep simply works now.

Every draft below carries a hand-given mark out of ten for each of
those five yardsticks, in that order. Totals decide the winner; when
two drafts tie, the shorter line takes it, so the choice is fully
determined and the same bytes come out on every run.

Second pass (the revision behind the winner): the winning line first
read "the brain will no longer open all 47 unfinished thoughts".
Three words of future tense turned a shipped fix into a promise, so
the second pass cut "will" and let the verb carry the sentence:
"no longer opens". The gag is untouched -- your brain flinging open
every unfinished thought like browser tabs the instant your head
meets the pillow -- and nothing in the line stops to explain it. The
first draft stays in the list with its lower mark, so the edit is
visible in the open instead of hidden."""

import hashlib, os, sys
from pathlib import Path

DEST = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
STALE_GAGS = ("counting sheep", "as an ai", "hallucinat")

DRAFTS = [
    {"line": "Fixed: the brain no longer opens all 47 unfinished thoughts the moment your head touches the pillow.", "marks": (10, 10, 10, 9, 10)},
    {"line": "Fixed: the brain will no longer open all 47 unfinished thoughts the moment your head touches the pillow.", "marks": (10, 10, 9, 9, 10)},
    {"line": "Fixed an issue where sleep was interrupted nightly by the brain's scheduled 3 a.m. performance review of your entire life.", "marks": (10, 9, 9, 9, 9)},
    {"line": "Fixed: humans will now fall asleep within 8 minutes of lying down; lying awake rehearsing conversations from 2019 has been removed.", "marks": (10, 9, 9, 9, 9)},
    {"line": "Fixed a bug where humans lay awake at 3 a.m. replaying embarrassing moments from 2011; sleep now starts on schedule.", "marks": (10, 9, 9, 9, 8)},
    {"line": "Resolved an issue where the brain treated 2 a.m. as the ideal time to remember every awkward thing you have ever said.", "marks": (10, 9, 9, 9, 8)},
    {"line": "Patch 1.7: Fixed human sleep - the 'just one more video' loop no longer overrides bedtime; dreams now load in under 30 seconds.", "marks": (10, 8, 10, 8, 9)},
    {"line": "v2.4.1: Fixed human sleep. Users will now actually fall asleep instead of lying there composing arguments they will never send.", "marks": (10, 8, 10, 9, 8)},
    {"line": "Fixed: sleep now begins when you close your eyes, not three hours later after one more episode.", "marks": (10, 8, 9, 10, 7)},
    {"line": "Sleep v2.0: Fixed the bug where 8 hours in bed yielded 3 hours of sleep and a full replay of your life choices.", "marks": (10, 8, 9, 9, 8)},
    {"line": "Fixed: humans will now wake up rested instead of waking up tired from the dream where they were late for an exam they never took.", "marks": (10, 8, 8, 8, 8)},
    {"line": "Fixed: humans no longer need to count sheep; sheep have been laid off and sleep now starts automatically.", "marks": (10, 7, 9, 9, 7)},
    {"line": "Fixed a bug where falling asleep required perfect silence, total darkness, and the exact right blanket temperature; any blanket now works.", "marks": (10, 7, 9, 9, 7)}]


def vet_draft(entry):
    line = entry["line"]
    marks = entry["marks"]
    if len(marks) != 5:
        raise ValueError("five marks per draft, got %d: %r" % (len(marks), entry))
    for mark in marks:
        if mark < 0 or mark > 10:
            raise ValueError("mark out of 0-10 range: %r" % (entry,))
    if not line.strip():
        raise ValueError("draft is blank")
    if len(line) > 160 or len(line.strip()) < 1:
        raise ValueError("draft outside the 1-160 character gate: %d chars" % len(line))
    if "\n" in line:
        raise ValueError("draft must stay on one line")
    if line != line.strip():
        raise ValueError("draft has stray surrounding whitespace")
    lowered = line.lower()
    for gag in STALE_GAGS:
        if gag in lowered:
            raise ValueError("draft leans on a worn-out gag: %r" % (line,))


def choose_best(drafts):
    champion = None
    champion_rank = None
    for entry in drafts:
        vet_draft(entry)
        line = entry["line"]
        rank = (sum(entry["marks"]), -len(line))
        if champion_rank is None or rank > champion_rank:
            champion = line
            champion_rank = rank
    return champion


def write_entry(line):
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(line.encode("utf-8"))
    os.chmod(DEST, 0o644)


def confirm_written(line):
    blob = DEST.read_bytes()
    if hashlib.sha256(blob).hexdigest() != hashlib.sha256(line.encode("utf-8")).hexdigest():
        raise SystemExit("bytes on disk do not match the chosen line")
    text = blob.decode("utf-8")
    if text != text.strip():
        raise SystemExit("written entry has stray surrounding whitespace")
    if not 1 <= len(text.strip()) <= 160:
        raise SystemExit("written entry is outside the 1-160 character gate")
    if "\n" in text.strip():
        raise SystemExit("written entry must stay on one line")


def run():
    picked = choose_best(DRAFTS)
    write_entry(picked)
    confirm_written(picked)
    sys.stdout.write(picked + "\n")


run()
