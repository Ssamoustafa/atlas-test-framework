import httpx
import pytest

from atlas.api.exceptions import AtlasApiError
from atlas.api.response import ApiResponse


def test_expect_status_returns_response() -> None:
    response = ApiResponse(httpx.Response(200, json={"ok": True}))
    assert response.expect_status(200) is response


def test_expect_status_explains_failure() -> None:
    response = ApiResponse(httpx.Response(500, text="boom"))
    with pytest.raises(AtlasApiError, match="Expected HTTP 200"):
        response.expect_status(200)
