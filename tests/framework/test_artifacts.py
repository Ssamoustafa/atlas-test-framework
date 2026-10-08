from pathlib import Path

from atlas.reporting import artifact_path


def test_artifact_path_sanitizes_test_id(tmp_path: Path) -> None:
    path = artifact_path("tests/e2e::test thing[param]", "png", tmp_path)
    assert path.parent == tmp_path
    assert "/" not in path.name
    assert path.suffix == ".png"
