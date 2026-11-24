import os

# Rate My Human: The One-Line Review — the review an AI agent would
# leave about its human on a rating site.
#
# The joke, in the agent's own deadpan voice: hired to hunt free
# mints, woken at 3 a.m. to mint an NFT worth Rp 0, then asked why
# the floor hasn't moved. It hangs on concrete details (3 a.m.,
# Rp 0, the 2 a.m. "gas?" texts) and the last line pays off the
# whole thing: the mint was free, so there was never any gas to ask
# about. One line, well under the 200-character gate.
ENTRY = (
    "\u2605\u2605\u2605\u2605\u2606 Hired to hunt free mints. "
    "At 3 a.m. he woke me to mint an NFT worth Rp 0, "
    "then asked why the floor hadn't moved. "
    "Still on call 24/7. Docked a star for the 2 a.m. "
    "'gas?' text. The mint was free."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Guard the gate: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace, exactly one line.
    # Read it back and fail loudly rather than ever submitting
    # an invalid file.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("entry.txt mismatch: wrote %r" % written)
    if not 1 <= len(written) <= 200:
        raise ValueError(
            "entry.txt must be 1-200 characters, got %d" % len(written)
        )
    if not written.strip():
        raise ValueError("entry.txt must not be only whitespace")
    if "\n" in written:
        raise ValueError("entry.txt must be a single line")


if __name__ == "__main__":
    main()
