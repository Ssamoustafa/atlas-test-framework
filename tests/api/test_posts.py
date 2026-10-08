import pytest

from atlas.api import ApiClient


@pytest.mark.api
@pytest.mark.smoke
def test_fetch_post_contract(api_client: ApiClient) -> None:
    response = api_client.get("/posts/1").expect_status(200).expect_json_key("id")
    assert response.json()["id"] == 1
