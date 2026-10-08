from typing import Any

import httpx

from atlas.api.exceptions import AtlasApiError


class ApiResponse:
    def __init__(self, response: httpx.Response) -> None:
        self.raw = response

    @property
    def status_code(self) -> int:
        return self.raw.status_code

    def json(self) -> Any:
        return self.raw.json()

    def expect_status(self, expected: int) -> "ApiResponse":
        if self.status_code != expected:
            raise AtlasApiError(
                f"Expected HTTP {expected}, got {self.status_code}. "
                f"Body: {self.raw.text[:500]}"
            )
        return self

    def expect_json_key(self, key: str) -> "ApiResponse":
        payload = self.json()
        if not isinstance(payload, dict) or key not in payload:
            raise AtlasApiError(f"Expected JSON object to contain key {key!r}: {payload!r}")
        return self
