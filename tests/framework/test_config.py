from pathlib import Path

from atlas.config import load_settings


def test_load_settings_from_explicit_directory(tmp_path: Path) -> None:
    (tmp_path / "test.yaml").write_text(
        "web_base_url: https://example.com\n"
        "api:\n"
        "  base_url: https://api.example.com\n",
        encoding="utf-8",
    )
    settings = load_settings("test", tmp_path)
    assert settings.environment == "test"
    assert str(settings.api.base_url).startswith("https://api.example.com")
