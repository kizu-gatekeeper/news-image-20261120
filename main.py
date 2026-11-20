#!/usr/bin/env python3
"""Entry program for news-image-20261120.

Copies the poster (entry.png, shipped beside this file) into the output
directory named by MAKEFUN_OUTPUT_DIR, or /output when that variable is
unset. Uses only the Python standard library. After copying, it checks
that the copy has exactly the same byte size as the original and prints
a short confirmation line.
"""

import os
import shutil
import sys

POSTER_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, POSTER_NAME)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, POSTER_NAME)

    shutil.copyfile(source, target)

    src_size = os.path.getsize(source)
    dst_size = os.path.getsize(target)
    if src_size != dst_size:
        print(f"error: size mismatch after copy "
              f"(source {src_size} bytes, copy {dst_size} bytes)",
              file=sys.stderr)
        return 1

    print(f"wrote {target} ({dst_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
