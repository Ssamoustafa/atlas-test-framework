# ADR 001: Playwright for browser automation

**Status:** Accepted

## Context
The framework needs reliable browser automation, useful diagnostics, parallel-friendly isolation and modern locator semantics.

## Decision
Use Playwright's synchronous Python API behind page/component abstractions.

## Consequences
We gain browser contexts, tracing, auto-waiting and strong locator APIs. The framework remains coupled to Playwright at the adapter layer, so tests should avoid direct Playwright calls except for assertions and truly page-specific interactions.
