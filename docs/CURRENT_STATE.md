# CURRENT_STATE.md

## Estado actual — Tech Sphere Challenge 2026

**Fecha:** 9 de agosto de 2026

**Fase:** Implementación incremental del núcleo funcional

**Prioridad:** Cerrar Knowledge Vivo y posteriormente las compuertas eliminatorias
antes de realizar refinamientos estéticos.

---

# 1. Repositorios y separación de responsabilidades

## 1.1 Repositorio de desarrollo

Ruta local:

`clinical-ai-voice-agent/tech-sphere-challenge-2-ai-voice-agent/`

Repositorio:

`git@github.com:Camilo899/tech-sphere-challenge-2-ai-voice-agent.git`

Rama:

`main`

Estado:

* rama `main` sincronizada con `origin/main`;
* working tree limpio;
* último commit:

`94217df feat: integrate clinical knowledge ingestion`

El repositorio contiene la implementación, pruebas y documentación propia.

---

## 1.2 Repositorio oficial

Ruta:

`clinical-ai-voice-agent/ParticipantArtifacts/`

Repositorio:

`TechSphere2026/ParticipantArtifacts`

Contiene:

* requisitos oficiales;
* rúbrica;
* stack técnico;
* datasets;
* material normativo.

No se modifica ni se mezcla su historial Git con el repositorio de desarrollo.

---

# 2. Documentación propia

La documentación de continuidad se encuentra en:

* `docs/AI_CONTEXT.md`
* `docs/CURRENT_STATE.md`
* `docs/PROJECT_JOURNAL.md`
* `docs/challenge/CHALLENGE_ANALYSIS.md`

Los documentos oficiales del reto permanecen sin modificaciones.

---

# 3. Validación actual

## Ruff

Comando:

```text
uv run ruff check app tests
```

Resultado:

```text
All checks passed!
```

## Pytest

Comando:

```text
uv run python -m pytest
```

Resultado:

```text
69 passed in 77.92s
```

Estado:

🟢 **69/69 pruebas pasando.**

---

# 4. Arquitectura

La solución utiliza arquitectura hexagonal:

```text
Presentation
    ↓
Application
    ↓
Domain
    ↓
Ports
    ↓
Infrastructure
```

Componentes principales:

### Presentation

* FastAPI;
* API schemas;
* endpoints;
* exception handler.

### Application

* DTOs;
* use cases;
* fakes;
* factories;
* orchestration.

### Domain

* entities;
* value objects;
* domain services;
* clinical decision logic;
* ports.

### Infrastructure

* Gemini;
* embeddings;
* ChromaDB;
* RAG;
* indexación.

La arquitectura no debe rediseñarse innecesariamente.

---

# 5. Implementación actual

## 5.1 Dominio y aplicación

Existe una base funcional para:

* contexto de conversación;
* casos de seguimiento;
* mensajes;
* estado conversacional;
* decisiones clínicas;
* niveles de riesgo;
* evidencia;
* explicaciones de decisión;
* análisis conversacional;
* razonamiento clínico;
* clasificación de síntomas;
* evaluación de riesgo;
* resumen;
* orquestación.

Servicios relevantes:

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

Casos de uso:

* `StartFollowUpUseCase`
* `SendMessageUseCase`

---

# 6. API

Actualmente existe:

* aplicación FastAPI;
* health endpoint;
* follow-up endpoint;
* messages endpoint;
* schemas Pydantic;
* DTOs;
* dependency injection;
* composition root;
* global exception handler.

Estado:

🟢 **API base implementada y probada.**

---

# 7. LLM

Modelo seleccionado:

**Google Gemini 1.5 Flash**

Integración:

* `google-genai`;
* `LanguageModel`;
* `GeminiLanguageModel`;
* `ClinicalResponseService`;
* `ClinicalPromptBuilder`;
* `ConversationOrchestrator`.

Configuración:

`GEMINI_API_KEY`

Estado:

🟢 **LLM integrado y validado mediante pruebas.**

---

# 8. RAG

La infraestructura RAG real está implementada.

## 8.1 Embeddings

Proveedor:

`BGEEmbeddingProvider`

Modelo:

`BAAI/bge-m3`

## 8.2 Vector store

Proveedor:

`ChromaKnowledgeProvider`

Tecnología:

`ChromaDB`

## 8.3 Indexador

Existe:

`ChromaKnowledgeIndexer`

Permite:

* indexar chunks;
* conservar metadatos;
* identificar documentos;
* eliminar documentos.

## 8.4 Recuperación

Flujo:

```text
Consulta
   ↓
BGE-M3
   ↓
ChromaDB
   ↓
Resultados
   ↓
Evidence
```

## 8.5 Grounding

Flujo:

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

🟢 **Grounding implementado.**

🟡 **Evaluación clínica integral pendiente.**

---

# 9. Knowledge Ingestion

Se implementó:

`ClinicalKnowledgeIngestionService`

Responsabilidad:

recibir un chunk clínico y delegar su indexación mediante
`KnowledgeIndexer`.

Flujo:

```text
ClinicalKnowledgeIngestionService
            ↓
      KnowledgeIndexer
            ↓
  ChromaKnowledgeIndexer
            ↓
         ChromaDB
```

También existe prueba de:

* delegación de ingestión;
* eliminación de chunks pertenecientes a un documento.

Estado:

🟢 **Servicio de ingestión implementado y probado.**

---

# 10. Knowledge Vivo

Knowledge Vivo todavía no está completo.

## Ya implementado

* embeddings;
* almacenamiento vectorial;
* recuperación;
* evidencia;
* indexación;
* eliminación por documento;
* servicio de ingestión.

## Falta implementar

```text
Documento
   ↓
Upload
   ↓
Extracción
   ↓
Chunking
   ↓
Ingestión
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

Estado:

🟡 **En implementación.**

La compuerta G5 no debe marcarse como superada hasta demostrar el flujo completo.

---

# 11. Compuertas eliminatorias

## G1 — Cuatro entregables

Requiere:

1. repositorio;
2. diagrama;
3. informe;
4. video.

Estado:

🟡 **En progreso.**

---

## G2 — Levantamiento ≤15 minutos

La base técnica utiliza:

* `pyproject.toml`;
* `uv.lock`;
* dependencias reproducibles.

Falta realizar una prueba cronometrada utilizando únicamente el README final.

Estado:

🟡 **Pendiente de validación.**

---

## G3 — Modelo permitido

Modelo:

**Google Gemini 1.5 Flash**

Estado:

🟢 **Implementado.**

---

## G4 — Voz en tiempo real

Falta implementar:

```text
Micrófono
   ↓
STT
   ↓
RAG / decisión / LLM
   ↓
TTS
   ↓
Audio
```

Estado:

🔴 **Pendiente.**

---

## G5 — Knowledge Vivo

La infraestructura necesaria existe parcialmente.

Falta demostrar:

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

# 12. Criterios de puntuación

| Criterio                                   | Estado |
| ------------------------------------------ | ------ |
| RAG, precisión clínica y conocimiento vivo | 🟡     |
| Lógica de decisión y escalamiento          | 🟡     |
| Comprensión del problema y conversación    | 🟡     |
| Calidad de conversación de voz             | 🔴     |
| Video                                      | 🔴     |
| Repositorio, proceso y buenas prácticas    | 🟡     |

---

# 13. Métricas obligatorias

Todavía no están instrumentadas de forma verificable:

| Métrica                        | Estado |
| ------------------------------ | ------ |
| Latencia P50                   | 🔴     |
| Latencia P95                   | 🔴     |
| Fin de habla → inicio de audio | 🔴     |
| Input tokens / turno           | 🔴     |
| Output tokens / turno          | 🔴     |
| Tokens / llamada               | 🔴     |
| Invocaciones LLM / turno       | 🔴     |
| Consultas RAG / llamada        | 🔴     |
| Costo estimado / llamada       | 🔴     |

Las métricas finales deberán derivarse de logs estructurados.

No deben introducirse valores manuales para aparentar precisión.

---

# 14. Riesgos prioritarios

## Críticos

1. Falso negativo clínico.
2. Alucinación clínica.
3. Prompt injection.
4. Voz no funcional.
5. Knowledge Vivo incompleto.
6. Levantamiento superior a 15 minutos.

## Altos

7. Métricas inconsistentes.
8. Demo diferente al repositorio.
9. Diagrama desactualizado.
10. Falta de trazabilidad.
11. Validación insuficiente sobre dataset.

---

# 15. Estado global

## Compuertas

```text
G1 🟡
G2 🟡
G3 🟢
G4 🔴
G5 🟡
```

## Núcleo técnico

```text
Dominio                  🟢
Application              🟢
API                      🟢
LLM                      🟢
RAG                      🟢
Grounding                🟢
Knowledge Ingestion      🟢
Knowledge Vivo           🟡
Decisión clínica         🟡
Voz                      🔴
Administración           🔴
Observabilidad           🔴
Demo                     🔴
```

---

# 16. Próximo incremento

## INC-004 — Knowledge Vivo

Objetivo:

```text
Documento
→ Upload
→ Extract
→ Chunk
→ Index
→ Query
→ Evidence
→ Grounded response
→ Delete
→ Verify forgetting
```

El objetivo es construir la funcionalidad mínima observable requerida por G5.

No se debe rediseñar el RAG existente.

---

# 17. Próximos incrementos

### INC-005

Decisión clínica conectada con evidencia real.

Validar:

* verde;
* amarillo;
* rojo;
* ambigüedad;
* escalamiento;
* falsos negativos.

### INC-006

Pipeline de voz:

```text
STT
→ Conversation
→ RAG
→ Decision
→ LLM
→ TTS
```

### Posteriormente

* interfaz de llamada;
* consola administrativa;
* observabilidad;
* evaluación del dataset;
* pruebas adversariales;
* README final;
* diagrama;
* informe;
* video.

---

# 18. Checkpoint de recuperación

Si el desarrollo continúa en otra conversación:

**Fecha:** 2026-08-09

**Commit:**

`94217df feat: integrate clinical knowledge ingestion`

**Tests:**

`69 passed`

**Ruff:**

`All checks passed!`

**Working tree:**

`clean`

**Branch:**

`main`

**Current increment:**

`INC-004 — Knowledge Vivo`

**Next action:**

Construir la ruta completa de Knowledge Vivo sin modificar innecesariamente
la arquitectura RAG existente.