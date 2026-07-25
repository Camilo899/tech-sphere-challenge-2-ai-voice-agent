# ADR-002

## Title

Clinical Core as the Center of the Architecture

## Status

Accepted

## Decision

The Clinical Core will be framework-independent and technology-agnostic.

## Rationale

This allows replacing:

- LLM
- Voice Provider
- Vector Database

without modifying business rules.

## Consequences

Positive:

- High maintainability
- Easier testing
- Better scalability

Negative:

- Slightly more abstractions