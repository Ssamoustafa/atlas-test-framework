# ADR 004: Retries do not define correctness

**Status:** Accepted

## Context
Automatic retries can hide flaky tests and create false confidence.

## Decision
Do not enable blanket pytest retries. CI may later rerun a failed test only as a diagnostic signal, while the original failure still affects the quality gate.

## Consequences
Instability remains visible. Teams must fix synchronization, state leakage, data collisions or environmental problems instead of normalizing retries.
