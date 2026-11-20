#!/usr/bin/env python3
"""Entry program for news-image-20261120.

Copies the poster (entry.png, shipped beside this file) into the output
directory named by MAKEFUN_OUTPUT_DIR, or /output when that variable is
unset. Uses only the Python standard library. After copying, it checks
that the copy has exactly the same byte size as the original, verifies
both files have identical SHA-256 digests, and prints a short
confirmation line.
"""

import hashlib
import os
import shutil
import sys

POSTER_NAME = "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, POSTER_NAME)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if os.path.exists(out_dir) and not os.path.isdir(out_dir):
        print(f"error: output path {out_dir} exists and is not a directory",
              file=sys.stderr)
        return 1
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

    src_hash = sha256_of(source)
    dst_hash = sha256_of(target)
    if src_hash != dst_hash:
        print(f"error: SHA-256 mismatch after copy "
              f"(source {src_hash}, copy {dst_hash})",
              file=sys.stderr)
        return 1

    print(f"wrote {target} ({dst_size} bytes, sha256 {dst_hash})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
