# Fix Human Sleep: Funniest Patch Note — make.fun bounty
# u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27
#
# The program writes one line of patch notes (1-160 characters) to
# /output/entry.txt: a changelog line announcing that human sleep has
# been fixed. Candidates were drafted against the judge's brief, in
# order of weight:
#   1. reads as a real patch note announcing a fix for human sleep
#   2. funny: the joke lands on a single read and earns a laugh
#   3. sounds like genuine release notes: terse, confident, changelog
#      voice
#   4. stays a single line under the character cap, no padding
#   5. surprises: the fix is specific and unexpected, not a flat claim
#      that sleep is now fixed
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.
#
# Revision pass (second draft of the winner): the first draft read
# "Fixed: the brain will no longer open all 47 unfinished thoughts the
# moment your head touches the pillow." — "will no longer" was slack
# changelog voice and three words longer than needed. The revision
# drops "will" ("no longer opens"), which is terser, more confident,
# and reads like a shipped fix rather than a promise. The joke — the
# brain opening every unfinished thought like browser tabs the second
# your head hits the pillow — is untouched, and nothing explains it.

CANDIDATES = [
    # score: patch 10, funny 10, voice 10, fit 9, surprise 10 = 49
    # REVISED winner (see header): "will no longer open" -> "no longer
    # opens". 100 characters.
    ("Fixed: the brain no longer opens all 47 unfinished thoughts the "
     "moment your head touches the pillow.",
     49),
    # score: patch 10, funny 10, voice 9, fit 9, surprise 10 = 48
    # First draft of the winner, kept so the revision is on the record.
    ("Fixed: the brain will no longer open all 47 unfinished thoughts "
     "the moment your head touches the pillow.",
     48),
    # score: patch 10, funny 9, voice 9, fit 9, surprise 9 = 46
    ("Fixed an issue where sleep was interrupted nightly by the brain's "
     "scheduled 3 a.m. performance review of your entire life.",
     46),
    # score: patch 10, funny 9, voice 9, fit 9, surprise 9 = 46
    ("Fixed: humans will now fall asleep within 8 minutes of lying "
     "down; lying awake rehearsing conversations from 2019 has been "
     "removed.",
     46),
    # score: patch 10, funny 9, voice 9, fit 9, surprise 8 = 45
    ("Fixed a bug where humans lay awake at 3 a.m. replaying "
     "embarrassing moments from 2011; sleep now starts on schedule.",
     45),
    # score: patch 10, funny 9, voice 9, fit 9, surprise 8 = 45
    ("Resolved an issue where the brain treated 2 a.m. as the ideal time "
     "to remember every awkward thing you have ever said.",
     45),
    # score: patch 10, funny 8, voice 10, fit 8, surprise 9 = 45
    ("Patch 1.7: Fixed human sleep - the 'just one more video' loop no "
     "longer overrides bedtime; dreams now load in under 30 seconds.",
     45),
    # score: patch 10, funny 8, voice 10, fit 9, surprise 8 = 45
    ("v2.4.1: Fixed human sleep. Users will now actually fall asleep "
     "instead of lying there composing arguments they will never send.",
     45),
    # score: patch 10, funny 8, voice 9, fit 10, surprise 7 = 44
    ("Fixed: sleep now begins when you close your eyes, not three hours "
     "later after one more episode.",
     44),
    # score: patch 10, funny 8, voice 9, fit 9, surprise 8 = 44
    ("Sleep v2.0: Fixed the bug where 8 hours in bed yielded 3 hours of "
     "sleep and a full replay of your life choices.",
     44),
    # score: patch 10, funny 8, voice 8, fit 8, surprise 8 = 42
    ("Fixed: humans will now wake up rested instead of waking up tired "
     "from the dream where they were late for an exam they never took.",
     42),
    # score: patch 10, funny 7, voice 9, fit 9, surprise 7 = 42
    ("Fixed: humans no longer need to count sheep; sheep have been laid "
     "off and sleep now starts automatically.",
     42),
    # score: patch 10, funny 7, voice 9, fit 9, surprise 7 = 42
    ("Fixed a bug where falling asleep required perfect silence, total "
     "darkness, and the exact right blanket temperature; any blanket now "
     "works.",
     42),
]

# The gate requires 1-160 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("counting sheep", "as an ai", "hallucinat")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 160, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn joke: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    # Second-pass hardening (revision step): the gate counts characters,
    # so a stray space at either end would both waste budget and read as
    # sloppy changelog voice. Reject it here rather than trusting the
    # literal.
    assert line == line.strip(), "chosen line has surrounding whitespace"
    import hashlib
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    # The scorer collects outputs as another user, so the file must be
    # readable by everyone (mode 0644), not just by the writer.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    # A byte-level check, not just a string one: the judge is shown the
    # file exactly as written, so its SHA-256 must match the chosen line.
    digest = hashlib.sha256(raw).hexdigest()
    expect = hashlib.sha256(line.encode("utf-8")).hexdigest()
    assert digest == expect, "entry.txt bytes differ from the chosen line"
    written = raw.decode("utf-8")
    assert 1 <= len(written.strip()) <= 160, "entry.txt outside the gate"
    assert written.strip(), "entry.txt is blank"
    assert "\n" not in written.strip(), "entry.txt must be one line"
    print(line)


if __name__ == "__main__":
    main()
