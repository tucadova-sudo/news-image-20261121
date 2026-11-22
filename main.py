#!/usr/bin/env python3
"""news-image-20261121 entry: copy the front-page image to the output dir.

The image (entry.png, 1024x1024) sums up Saturday 21 November 2026's world
news: Mexico captures cartel boss 'El Chapo Isidro', the Kryvyi Rih strike,
COP31 overtime, the AI stock sell-off, the Rohingya genocide ruling, and the
day's briefs. Standard library only; the copy is byte-identical every run.
"""
import os
import shutil

ENTRY = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY)
    if not os.path.isfile(src):
        raise SystemExit("missing entry image: " + ENTRY)
    shutil.copyfile(src, os.path.join(out_dir, ENTRY))


if __name__ == "__main__":
    main()
