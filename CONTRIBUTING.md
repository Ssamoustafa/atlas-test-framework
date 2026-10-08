# Contributing

1. Create a virtual environment with Python 3.12+.
2. Run `make install`.
3. Run `make quality` and `make unit` before opening a pull request.
4. Add tests for framework behavior changes.
5. Record architecture-impacting decisions in `docs/adr/`.

Tests should be deterministic, independently runnable, and explicit about the layer they exercise. Avoid sleeps; prefer observable conditions and Playwright auto-waiting.
