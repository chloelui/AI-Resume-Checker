from pathlib import Path

def read_text(path: str) -> str:
    # Convert to readable Path object
    return Path(path).read_text(encoding="utf-8",errors="ignore")