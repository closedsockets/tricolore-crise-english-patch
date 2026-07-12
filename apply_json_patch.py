#!/usr/bin/env python3
"""Apply a Tricolore Crise JSON binary patch to a clean track03.bin."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


def sha1_file(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def apply_patch(patch_path: Path, source: Path, output: Path) -> None:
    patch = json.loads(patch_path.read_text(encoding="utf-8"))
    expected_source = patch["source_sha1"].lower()
    actual_source = sha1_file(source).lower()
    if actual_source != expected_source:
        raise ValueError(
            f"wrong source file: expected SHA-1 {expected_source}, got {actual_source}"
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output)
    with output.open("r+b") as fh:
        for change in patch["changes"]:
            offset = int(change["offset"])
            old = bytes.fromhex(change["old_hex"])
            new = bytes.fromhex(change["new_hex"])
            fh.seek(offset)
            if fh.read(len(old)) != old:
                raise ValueError(f"source bytes differ at offset {offset}")
            fh.seek(offset)
            fh.write(new)

    expected_output = patch["patched_sha1"].lower()
    actual_output = sha1_file(output).lower()
    if actual_output != expected_output:
        raise ValueError(
            f"output verification failed: expected {expected_output}, got {actual_output}"
        )
    print(f"Created: {output}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--patch", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    apply_patch(args.patch, args.source, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
