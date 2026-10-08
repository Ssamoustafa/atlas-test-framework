# API Testing

Atlas API tests use `atlas.api.ApiClient` (a thin `httpx` wrapper) and `ApiResponse` for fluent checks.

## Layout

- `atlas/api/client.py` — HTTP adapter (`get`, `post`, `delete`)
- `atlas/api/response.py` — `expect_status`, `expect_json_key`
- `tests/api/` — API suites, marked `@pytest.mark.api`
- `api_client` fixture — built from the active environment config (`base_url`)

## Writing a test

```python
@pytest.mark.api
def test_fetch_post(api_client):
    response = api_client.get("/posts/1").expect_status(200).expect_json_key("id")
    assert response.json()["id"] == 1
```

## Guidelines

- One behaviour per test; keep tests independent and data-deterministic (use `atlas.factories`).
- Assert status, then body shape, then key values.
- Put domain logic in domain clients that compose `ApiClient`, not in tests.
- Never hardcode URLs; select the environment via config (`config/*.yaml`).
- No retries to hide failures (see ADR 004).

## Running

```bash
pytest -m api
pytest -m "api and smoke"
```
