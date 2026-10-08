# ADR 002: Browser context per test

**Status:** Accepted

## Context
Shared state is a common source of order-dependent and flaky E2E suites.

## Decision
Create a fresh Playwright browser context for every UI test while sharing the browser process at session scope. Generate unique test data through factories.

## Consequences
Tests remain independent while avoiding the startup cost of launching a browser process for every test. Authentication reuse, when added, should use explicit storage-state fixtures rather than shared mutable sessions.
