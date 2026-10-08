# ADR 003: Page and component objects

**Status:** Accepted

## Context
Large page objects often become god objects, while raw selectors duplicated in tests create maintenance cost.

## Decision
Model navigation-level behavior with page objects and reusable UI regions with component objects. Keep assertions close to test intent unless they express reusable component invariants.

## Consequences
Selectors and interaction mechanics are centralized without hiding every assertion behind opaque helper methods.
