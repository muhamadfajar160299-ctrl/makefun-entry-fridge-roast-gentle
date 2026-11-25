"""Fridge Roast entry runner.

Reads the single roast line from entry.txt next to this file and writes
it unchanged to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output), with
one direct write and mode 0644 so the grader can read it.
"""

import os
from pathlib import Path

try:
    src = Path(__file__).resolve().parent / "entry.txt"
    data = src.read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.txt"
    out.write_bytes(data)
    os.chmod(out, 0o644)
except OSError as exc:
    raise SystemExit(f"failed to write entry: {exc}") from exc
