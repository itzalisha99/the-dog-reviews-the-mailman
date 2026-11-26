"""The Dog Reviews the Mailman — one funny one-line dog review.

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Gate: UTF-8 text of 1 to 200 characters, not only white space.
"""

import os

LINE = "One star. He delivers to my house every day and still acts surprised to see me. I live here. I have always lived here."


def validate(text):
    """Mirror the bounty gate: 1-200 chars, UTF-8, not blank-only."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    text.encode("utf-8")
    return True


def output_path():
    """Resolve the entry path, honouring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    if not validate(LINE):
        raise SystemExit("gate failed: entry is not 1-200 non-blank chars")
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify the bytes on disk are exactly the entry.
    with open(path, "rb") as f:
        on_disk = f.read()
    if on_disk != LINE.encode("utf-8"):
        raise SystemExit("verify failed: entry.txt on disk does not match LINE")
    if not validate(on_disk.decode("utf-8")):
        raise SystemExit("verify failed: entry on disk fails the gate")
    print(f"wrote {path} ({len(LINE)} chars, verified)")


if __name__ == "__main__":
    main()
