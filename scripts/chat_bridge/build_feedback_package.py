#!/usr/bin/env python3
"""Package only the ChatGPT-Codex bridge directory."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path


FORBIDDEN_SUFFIXES = {
    ".fastq", ".fq", ".fasta", ".fa", ".bam", ".sam", ".gz", ".chunk",
    # The bridge package is a state-sync artifact. Presentation images remain
    # in results/ and should not make the public bridge mirror large.
    ".png", ".jpg", ".jpeg", ".pdf", ".svg", ".html", ".pptx",
}
MAX_BRIDGE_FILE_BYTES = 1024 * 1024
SECRET_NAME_RE = re.compile(
    r"(^|[/_.-])(secret|token|api[-_]?key|credential|password|passwd|id_rsa|id_dsa|id_ed25519|\.env)([/_.-]|$)",
    re.IGNORECASE,
)


def is_forbidden(path: Path) -> bool:
    return (
        path.suffix.lower() in FORBIDDEN_SUFFIXES
        or path.stat().st_size > MAX_BRIDGE_FILE_BYTES
        or bool(SECRET_NAME_RE.search(path.as_posix()))
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bridge", "--in", dest="bridge", default="chat_bridge", help="Bridge directory to package.")
    parser.add_argument("--out", default="chat_bridge_feedback_package.zip", help="Output zip path.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path.cwd().resolve()
    bridge = Path(args.bridge)
    if not bridge.is_absolute():
        bridge = root / bridge
    bridge = bridge.resolve()
    out = Path(args.out)
    if not out.is_absolute():
        out = root / out
    out = out.resolve()

    if not bridge.exists() or not bridge.is_dir():
        raise SystemExit(f"Bridge directory not found: {bridge}")
    try:
        bridge.relative_to(root)
    except ValueError as exc:
        raise SystemExit("Bridge directory must live under the repository root") from exc

    files: list[Path] = []
    skipped: list[str] = []
    for path in sorted(bridge.rglob("*")):
        if not path.is_file():
            continue
        if path.resolve() == out:
            skipped.append(path.as_posix())
            continue
        if is_forbidden(path):
            skipped.append(path.as_posix())
            continue
        files.append(path)

    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, arcname=path.relative_to(root).as_posix())

    summary = {
        "package": out.relative_to(root).as_posix() if out.is_relative_to(root) else out.as_posix(),
        "files_included": len(files),
        "files_skipped": len(skipped),
        "scope": "chat_bridge_only",
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
