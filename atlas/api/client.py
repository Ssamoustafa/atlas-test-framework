from collections.abc import Mapping
from typing import Any

import httpx

from atlas.api.response import ApiResponse


class ApiClient:
    """Thin HTTP adapter. Domain-specific clients should compose this class."""

    def __init__(self, base_url: str, timeout: float = 10.0) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    def close(self) -> None:
        self._client.close()

    def get(self, path: str, *, params: Mapping[str, Any] | None = None) -> ApiResponse:
        return ApiResponse(self._client.get(path, params=params))

    def post(self, path: str, *, json: Any = None) -> ApiResponse:
        return ApiResponse(self._client.post(path, json=json))

    def delete(self, path: str) -> ApiResponse:
        return ApiResponse(self._client.delete(path))

    def __enter__(self) -> "ApiClient":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
