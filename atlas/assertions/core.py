from typing import TypeVar

T = TypeVar("T")


def assert_that(actual: T, expected: T, message: str | None = None) -> None:
    if actual != expected:
        detail = message or f"Expected {expected!r}, got {actual!r}"
        raise AssertionError(detail)


def assert_contains(container: object, member: object) -> None:
    try:
        contains = member in container  # type: ignore[operator]
    except TypeError as exc:
        raise AssertionError(f"Object {container!r} does not support membership checks") from exc
    if not contains:
        raise AssertionError(f"Expected {container!r} to contain {member!r}")
