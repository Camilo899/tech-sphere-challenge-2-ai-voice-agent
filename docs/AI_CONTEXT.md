# AI_CONTEXT.md

## Project

Clinical AI Voice Agent — Tech Sphere Challenge 2026.

Agente de voz para seguimiento postoperatorio de pacientes colombianos.

El sistema debe conversar en español, recuperar conocimiento clínico mediante RAG,
evaluar criticidad, escalar cuando corresponda, registrar trazabilidad y producir un
resumen estructurado de la llamada.

---

## Repositories

### Development / delivery repository

`tech-sphere-challenge-2-ai-voice-agent`

GitHub:

`Camilo899/tech-sphere-challenge-2-ai-voice-agent`

### Official challenge repository

`ParticipantArtifacts`

Repositorio oficial:

`TechSphere2026/ParticipantArtifacts`

El repositorio oficial es una fuente normativa y de datos.

No se modifica ni se mezcla su historial Git con el repositorio de desarrollo.

---

## Official sources

Los siguientes documentos determinan los requisitos:

- `ParticipantArtifacts/README.md`
- `ParticipantArtifacts/docs/rubrica-evaluacion.md`
- `ParticipantArtifacts/docs/stack-tecnico.md`

No modificar los documentos oficiales.

---

## Architecture

Hexagonal Architecture.

Presentation
│
├── FastAPI
├── API Schemas
└── Voice Interface

Application
│
├── DTOs
├── Use Cases
├── Ports
└── Orchestration

Domain
│
├── Entities
├── Value Objects
├── Domain Services
└── Clinical Decision Logic

Infrastructure
│
├── Repository Implementations
├── LLM Adapter
├── STT Adapter
├── TTS Adapter
├── RAG / Vector Store
├── Document Processing
└── Observability

---

## Current technology

- Python 3.12
- FastAPI
- Pydantic
- Pytest
- Ruff
- MyPy
- uv

---

## Allowed LLMs

The LLM used for reasoning MUST be one of the models explicitly allowed by the official
challenge stack:

- Google Gemini 1.5 Flash
- Llama 3.1 70B via Groq
- Llama 3.2 1B/3B
- Phi-3.5 Mini 3.8B

No other reasoning model is permitted.

The final selected model must be declared and justified in the final report.

---

## Challenge functional requirements

The implementation must provide:

1. Real-time voice conversation.
2. Spanish interaction with Colombian patients.
3. Clinical RAG.
4. Source traceability.
5. Explicit handling of unknown information.
6. Dynamic knowledge upload.
7. Dynamic knowledge deletion.
8. Clinical criticality classification.
9. Safe escalation.
10. Structured alert persistence.
11. Structured call summary.
12. Administration console.
13. Call interface.
14. Observability and required metrics.

---

## Development principles

- Hexagonal Architecture.
- SOLID.
- Clean Code.
- Lightweight DDD.
- Small incremental changes.
- One logical feature per commit.
- Tests before progression whenever practical.
- Do not modify official challenge documents.

---

## Validation

Before advancing an increment:

`uv run pytest`

`uv run ruff check .`

`uv run python -m mypy app`

No known validation failure should be left unresolved before the next increment.

---

## Priority hierarchy

1. Elimination gates.
2. Clinical safety.
3. RAG correctness and traceability.
4. Decision and escalation.
5. Voice interaction.
6. Knowledge live.
7. Observability.
8. Reproducibility.
9. Documentation.
10. UI refinement.

Visual aesthetics are not a scoring priority.

---

## Working rule

Before implementing a feature:

1. Identify the requirement.
2. Identify the gate or scoring criterion affected.
3. Identify the implementation location.
4. Define the test.
5. Define the evidence.
6. Implement the smallest useful increment.
7. Validate.
8. Record the decision.
9. Commit.

Never implement functionality only because it appears technically interesting.