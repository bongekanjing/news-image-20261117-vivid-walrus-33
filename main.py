"""news-image-20261117 — The Day in One Page, Tuesday 17 November 2026.

The image was designed as an HTML/CSS/SVG broadsheet page and rendered to
entry.png at 1024x1024 by headless Chromium during the build. This program is
the entry's runtime: it validates the stored PNG against the competition
guardrails and copies it to /output/entry.png.

Standard library only, no network, no clock, no randomness: two runs write the
same bytes.
"""

import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")

MAX_BYTES = 1024 * 1024
MAX_SIDE = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_ihdr(blob: bytes) -> tuple[int, int]:
    """Return (width, height) from a PNG's IHDR chunk."""
    if len(blob) < 24 or blob[:8] != PNG_SIGNATURE:
        raise ValueError("entry.png is not a PNG")
    if blob[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR as its first chunk")
    return struct.unpack(">II", blob[16:24])


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    with open(SOURCE, "rb") as handle:
        blob = handle.read()

    width, height = read_ihdr(blob)
    if (width, height) != (MAX_SIDE, MAX_SIDE):
        raise ValueError(f"entry.png is {width}x{height}, expected 1024x1024")
    if len(blob) > MAX_BYTES:
        raise ValueError(f"entry.png is {len(blob)} bytes, over the 1 MiB cap")

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as handle:
        handle.write(blob)
    return 0


if __name__ == "__main__":
    sys.exit(main())
