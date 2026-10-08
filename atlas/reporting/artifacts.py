from pathlib import Path


def artifact_path(test_id: str, suffix: str, root: Path = Path("artifacts")) -> Path:
    safe = "".join(char if char.isalnum() or char in "-_" else "_" for char in test_id)
    root.mkdir(parents=True, exist_ok=True)
    return root / f"{safe}.{suffix.lstrip('.')}"
