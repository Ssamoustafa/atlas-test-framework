# API Contract Testing

Contract tests verify that an API's response shape and semantics match what consumers rely on, independent of specific data values.

## What to check

- Status codes for success and error paths
- Required fields, types, and nullability
- Headers (e.g. `Content-Type`)
- Backwards compatibility: no removed or retyped fields

## Approaches

1. **Lightweight (built in):** `ApiResponse.expect_json_key()` for required keys.
2. **Schema validation:** validate responses against JSON Schema (OpenAPI) with `jsonschema`.
   Store schemas under `tests/api/contracts/`.
3. **Consumer-driven (optional):** Pact, where consumers publish expectations and providers verify them in CI.

## Example

```python
import jsonschema, pytest

POST_SCHEMA = {
    "type": "object",
    "required": ["id", "userId", "title", "body"],
    "properties": {
        "id": {"type": "integer"},
        "userId": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}

@pytest.mark.api
@pytest.mark.contract
def test_post_contract(api_client):
    response = api_client.get("/posts/1").expect_status(200)
    jsonschema.validate(response.json(), POST_SCHEMA)
```

Register the `contract` marker in `pyproject.toml` and add `jsonschema` to dev dependencies when adopting this.

## Guidelines

- Assert structure, not volatile values.
- Version schemas with the API; review schema diffs like code.
- Run contract tests on every PR; they are fast and need no browser.
