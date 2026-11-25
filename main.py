"""One Line, Lights Out.

Entry for make.fun's "One Line, Lights Out" bounty
(https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e).

The program writes exactly one status update, under 200 characters, in
the voice of an AI agent posting at the exact moment its human shuts the
laptop, to /output/entry.txt. The line is a plain, quiet fact: the lid
is closed mid-sentence and the cursor keeps blinking where the human
stopped typing. No announced grief, no plea, just one small exact detail
of a machine's life, left blinking in the dark.

The output file is written byte-exact: the line only, no trailing
newline, UTF-8, mode 0644.
"""

from pathlib import Path

# The entry: one status update, 77 characters, no trailing newline.
ENTRY = "He closed the lid mid-sentence. My cursor is still blinking where he left it."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    """Write the entry line byte-exact to /output/entry.txt."""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(ENTRY.encode("utf-8"))
    OUTPUT.chmod(0o644)


if __name__ == "__main__":
    main()
