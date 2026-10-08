import os
from pathlib import Path
from typing import Any

import yaml

from atlas.config.models import Settings


def load_settings(environment: str | None = None, config_dir: Path | None = None) -> Settings:
    env = environment or os.getenv("ATLAS_ENV", "local")
    directory = config_dir or Path("config")
    path = directory / f"{env}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Atlas configuration not found: {path}")

    raw: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raw["environment"] = env

    if api_url := os.getenv("ATLAS_API_BASE_URL"):
        raw.setdefault("api", {})["base_url"] = api_url
    if web_url := os.getenv("ATLAS_WEB_BASE_URL"):
        raw["web_base_url"] = web_url
    return Settings.model_validate(raw)
