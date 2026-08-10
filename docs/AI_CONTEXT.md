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

Git:

`git@github.com:Camilo899/tech-sphere-challenge-2-ai-voice-agent.git`

Este repositorio contiene:

* implementación;
* pruebas;
* documentación propia;
* evolución Git;
* artefactos de entrega.

### Official challenge repository

`ParticipantArtifacts`

Git:

`TechSphere2026/ParticipantArtifacts`

Este repositorio contiene:

* requisitos oficiales;
* rúbrica;
* stack permitido;
* datasets;
* material normativo del reto.

El repositorio oficial **no se modifica** y su historial Git no se mezcla con el
repositorio de desarrollo.

---

## Official sources

Los siguientes documentos son normativos:

* `ParticipantArtifacts/README.md`
* `ParticipantArtifacts/docs/rubrica-evaluacion.md`
* `ParticipantArtifacts/docs/stack-tecnico.md`

No modificar estos documentos.

La interpretación operativa del reto se mantiene en:

* `docs/AI_CONTEXT.md`
* `docs/CURRENT_STATE.md`
* `docs/PROJECT_JOURNAL.md`
* `docs/challenge/CHALLENGE_ANALYSIS.md`

---

## Current Git state

Branch:

`main`

Remote:

`origin/main`

Working tree:

`clean`

Latest commit:

`94217df feat: integrate clinical knowledge ingestion`

Recent relevant commits:

```text
94217df feat: integrate clinical knowledge ingestion
9ddeb16 test: isolate RAG factory integration tests
8bc9dcf feat: integrate knowledge indexer into RAG stack
5560c63 feat: implement Chroma knowledge indexer
```

El repositorio está sincronizado con `origin/main`.

---

## Current validation

Lint:

```text
uv run ruff check app tests
All checks passed!
```

Tests:

```text
uv run python -m pytest
69 passed
```

Última ejecución conocida:

```text
69 passed in 77.92s
```

No existe actualmente una falla conocida de Ruff o Pytest en el checkpoint.

---

## Architecture

La solución utiliza arquitectura hexagonal.

```text
Presentation
    │
    ├── FastAPI
    ├── API Schemas
    └── Voice Interface
    │
    ▼
Application
    │
    ├── DTOs
    ├── Use Cases
    ├── Ports
    └── Orchestration
    │
    ▼
Domain
    │
    ├── Entities
    ├── Value Objects
    ├── Domain Services
    └── Clinical Decision Logic
    │
    ▼
Infrastructure
    │
    ├── Repository Implementations
    ├── LLM Adapter
    ├── RAG / Vector Store
    ├── Document Processing
    ├── STT Adapter
    ├── TTS Adapter
    └── Observability
```

La infraestructura concreta no debe introducirse directamente en el dominio.

---

## Technology

* Python 3.12
* FastAPI
* Pydantic
* Pytest
* Ruff
* MyPy
* uv
* Google Gemini 1.5 Flash
* BGE-M3
* ChromaDB

---

## Allowed LLM

El reto permite únicamente los modelos definidos por el stack oficial.

El modelo seleccionado es:

**Google Gemini 1.5 Flash**

La integración se realiza mediante:

* `google-genai`;
* puerto `LanguageModel`;
* `GeminiLanguageModel`;
* `GEMINI_API_KEY`;
* `ClinicalResponseService`;
* `ClinicalPromptBuilder`;
* `ConversationOrchestrator`.

El dominio permanece desacoplado del proveedor concreto.

---

## Implemented domain/application

Actualmente existe una base funcional para:

* `ConversationContext`
* `FollowUpCase`
* `ClinicalDecision`
* `RiskLevel`
* `ConversationState`
* `ConversationMessage`
* `Evidence`
* `DecisionExplanation`
* `ConversationOrchestrator`
* `ClinicalKnowledgeService`
* `ClinicalQueryBuilder`
* `ClinicalPromptBuilder`
* `ClinicalResponseService`
* `ClinicalReasoner`
* `DecisionEngine`
* `RiskAssessmentService`
* `SymptomClassifier`
* `ConversationAnalysisService`
* `SummaryGenerationService`
* `StartFollowUpUseCase`
* `SendMessageUseCase`

También existen:

* DTOs;
* ports;
* fakes;
* dependency injection;
* composition root;
* FastAPI;
* schemas Pydantic;
* exception handler global.

---

## Implemented API

Actualmente existe:

* health endpoint;
* follow-up endpoint;
* messages endpoint;
* request/response schemas;
* application DTOs;
* dependency injection;
* global exception handling.

---

## Implemented LLM

Existe:

`app/infrastructure/llm/gemini_language_model.py`

El adaptador implementa:

`LanguageModel`

y utiliza:

`google-genai`

La configuración se realiza mediante:

`GEMINI_API_KEY`

Estado:

🟢 **LLM real integrado y probado.**

---

## Implemented RAG

La infraestructura RAG real está implementada.

### Embeddings

Proveedor:

`BGEEmbeddingProvider`

Modelo:

`BAAI/bge-m3`

### Vector store

Proveedor:

`ChromaKnowledgeProvider`

Almacenamiento:

`ChromaDB`

### Indexación

Existe:

`ChromaKnowledgeIndexer`

Soporta:

* indexación de chunks;
* metadatos;
* identificación por documento;
* eliminación por documento.

### Recuperación

Existe:

```text
Consulta
   ↓
BGE-M3
   ↓
ChromaDB
   ↓
Resultados recuperados
   ↓
Evidence
```

### Grounding

La evidencia recuperada se incorpora al flujo clínico:

```text
KnowledgeProvider
       ↓
ClinicalKnowledgeService
       ↓
Evidence
       ↓
ClinicalPromptBuilder
       ↓
Gemini
```

Estado:

🟢 **RAG base implementado y validado.**

🟢 **Recuperación de evidencia integrada.**

🟡 **Validación clínica integral pendiente.**

---

## Knowledge Ingestion

Se implementó:

`ClinicalKnowledgeIngestionService`

Ubicación:

`app/domain/services/clinical_knowledge_ingestion_service.py`

El servicio recibe:

* `document_name`;
* `section`;
* `chunk_id`;
* `text`.

y delega la indexación mediante:

`KnowledgeIndexer`

Flujo actual:

```text
ClinicalKnowledgeIngestionService
            ↓
      KnowledgeIndexer
            ↓
  ChromaKnowledgeIndexer
            ↓
         ChromaDB
```

Existe prueba automatizada de la delegación.

También existe prueba de eliminación específica de documentos.

---

## Knowledge Vivo

Knowledge Vivo **todavía no está terminado**.

Actualmente existe la infraestructura para:

* indexación;
* recuperación;
* eliminación;
* ingestión de chunks;
* generación de embeddings;
* almacenamiento vectorial.

Falta construir y demostrar:

```text
Documento
   ↓
Upload
   ↓
Extracción
   ↓
Chunking
   ↓
ClinicalKnowledgeIngestionService
   ↓
Indexación
   ↓
Consulta
   ↓
Evidence
   ↓
Respuesta fundamentada
   ↓
Delete
   ↓
Verificación de olvido
```

No marcar G5 como completada hasta demostrar el flujo completo de extremo a extremo.

---

## Elimination gates

### G1 — Cuatro entregables

Requiere:

1. Repositorio.
2. Diagrama.
3. Informe.
4. Video.

Estado:

🟡 **En progreso.**

### G2 — Levantamiento ≤15 minutos

La arquitectura utiliza:

* `pyproject.toml`;
* `uv.lock`;
* dependencias declaradas.

Falta validar el procedimiento completo siguiendo exclusivamente el README.

Estado:

🟡 **Pendiente de validación final.**

### G3 — Modelo permitido

Modelo:

**Google Gemini 1.5 Flash**

Estado:

🟢 **Implementado.**

### G4 — Voz en tiempo real

Falta implementar:

```text
Micrófono
   ↓
STT
   ↓
Conversación
   ↓
RAG
   ↓
Decisión
   ↓
LLM
   ↓
TTS
   ↓
Audio
```

Estado:

🔴 **Pendiente.**

### G5 — Knowledge Vivo

Existe una base real de indexación, recuperación y eliminación.

Falta la ruta observable:

```text
upload
→ process
→ query
→ delete
→ verify forgetting
```

Estado:

🟡 **En implementación.**

---

## Main scoring areas

| Criterio                                   | Estado |
| ------------------------------------------ | ------ |
| RAG, precisión clínica y conocimiento vivo | 🟡     |
| Lógica de decisión y escalamiento          | 🟡     |
| Comprensión del problema y conversación    | 🟡     |
| Calidad de conversación de voz             | 🔴     |
| Video                                      | 🔴     |
| Repositorio, proceso y buenas prácticas    | 🟡     |

---

## Not implemented yet

### Knowledge Vivo

* upload de documentos;
* extracción;
* chunking documental;
* pipeline completo de ingestión;
* endpoint administrativo;
* verificación end-to-end de olvido.

### Voz

* STT;
* TTS;
* pipeline de voz en tiempo real;
* interrupciones;
* manejo de silencios;
* interfaz de llamada.

### Administración

* consola de administración;
* listado de documentos;
* estado de procesamiento;
* eliminación desde interfaz.

### Observabilidad

* latencia P50;
* latencia P95;
* fin de habla → inicio de audio;
* input tokens por turno;
* output tokens por turno;
* tokens por llamada;
* invocaciones LLM por turno;
* consultas RAG por llamada;
* costo estimado por llamada.

### Evaluación

* evaluación completa sobre dataset;
* validación sistemática de verde/amarillo/rojo;
* falsos negativos;
* casos ambiguos;
* prompt injection;
* solicitudes fuera de misión;
* regionalismos colombianos;
* pacientes hostiles o asustados.

### Entregables

* README final ≤15 minutos;
* diagrama final;
* informe;
* video;
* evidencia final de evaluación.

---

## Current priority

### INC-004 — Knowledge Vivo

Objetivo:

```text
Upload
→ Extract
→ Chunk
→ Index
→ Query
→ Evidence
→ Grounded response
→ Delete
→ Verify forgetting
```

No rediseñar el RAG existente.

Extender los puertos y adaptadores actuales.

---

## Next increments

### INC-004

Completar Knowledge Vivo.

### INC-005

Conectar decisión clínica con evidencia real y validar los escenarios del dataset.

### INC-006

Implementar:

```text
STT
→ Conversation
→ RAG
→ Decision
→ LLM
→ TTS
```

### Posteriormente

* interfaz mínima de llamada;
* consola administrativa;
* observabilidad;
* evaluación del dataset;
* pruebas adversariales;
* README reproducible;
* diagrama;
* informe;
* video.

---

## Working rules

Antes de cada incremento:

1. Identificar el requisito oficial.
2. Identificar la compuerta o criterio afectado.
3. Identificar ubicación de implementación.
4. Definir prueba.
5. Definir evidencia.
6. Implementar el incremento mínimo.
7. Ejecutar Ruff.
8. Ejecutar Pytest.
9. Actualizar documentación.
10. Crear commit.
11. Hacer push.
12. Continuar.

No implementar funcionalidades estéticas antes de cerrar las compuertas eliminatorias.

No considerar completado un requisito por la existencia de:

* interfaces;
* ports;
* fakes;
* schemas;
* placeholders.

Un requisito se considera implementado cuando existe comportamiento observable,
pruebas y evidencia suficiente.

---

## Recovery checkpoint

Si el proyecto continúa en una nueva conversación, utilizar este punto como
contexto inicial:

**Commit:**

`94217df feat: integrate clinical knowledge ingestion`

**Tests:**

`69 passed`

**Lint:**

`All checks passed!`

**Working tree:**

`clean`

**Branch:**

`main`

**Current increment:**

`INC-004 — Knowledge Vivo`

**Immediate objective:**

```text
Document upload
→ extraction
→ chunking
→ ingestion
→ indexing
→ query
→ delete
→ forgetting verification
```

No reiniciar la arquitectura.

No reemplazar el RAG actual.

Continuar incrementalmente sobre los ports, servicios y adaptadores existentes.