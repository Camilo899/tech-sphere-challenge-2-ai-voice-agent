# CURRENT_STATE.md

## Estado actual — Tech Sphere Challenge 2026

**Fecha:** 7 de agosto de 2026
**Fase:** Preparación técnica e implementación incremental
**Prioridad:** Superar primero las compuertas eliminatorias y construir evidencia verificable.

---

## 1. Repositorios y separación de responsabilidades

### 1.1 Repositorio de desarrollo y entrega

Ruta local:

`clinical-ai-voice-agent/tech-sphere-challenge-2-ai-voice-agent/`

Repositorio Git:

`git@github.com:Camilo899/tech-sphere-challenge-2-ai-voice-agent.git`

Rama:

`main`

Estado verificado:

- `main` sincronizada con `origin/main`.
- Último commit: `148b425`
- Working tree con documentación propia aún sin seguimiento.
- No se deben mezclar los historiales del repositorio oficial y el repositorio de desarrollo.

### 1.2 Repositorio oficial del reto

Ruta local:

`clinical-ai-voice-agent/ParticipantArtifacts/`

Repositorio:

`TechSphere2026/ParticipantArtifacts`

Este repositorio contiene el material oficial proporcionado por Tech Sphere.

Su contenido se utiliza como fuente normativa y de datos.

No se incorpora su historial Git al repositorio de desarrollo.

---

## 2. Documentación oficial

Los siguientes archivos son normativos:

- `ParticipantArtifacts/docs/rubrica-evaluacion.md`
- `ParticipantArtifacts/docs/stack-tecnico.md`
- `ParticipantArtifacts/README.md`

### Regla

Los documentos oficiales **NO se modifican**.

Nuestra documentación interpreta y operacionaliza estos documentos, pero no los reemplaza.

---

## 3. Documentación propia

La documentación de continuidad del proyecto se encuentra en:

- `docs/AI_CONTEXT.md`
- `docs/CURRENT_STATE.md`
- `docs/PROJECT_JOURNAL.md`
- `docs/challenge/CHALLENGE_ANALYSIS.md`

Estos documentos sí forman parte del desarrollo del proyecto.

---

## 4. Estado Git actual

Último commit:

`148b425 feat(application): add send message DTOs and API schemas`

Historial reciente relevante:

- `148b425` — Send message DTOs and API schemas
- `d87bf3b` — Global exception handling
- `ef9e9e8` — Health check endpoint
- `605487d` — Follow-up endpoint connected to application use case
- `291c6e2` — Initial FastAPI application and follow-up route
- `0ef1ff7` — Start follow-up API schemas
- `6758e8c` — Start follow-up request/response DTOs
- `271e906` — Decision explanation value object
- `66b71db` — Clinical query builder service
- `bcfead4` — Composition root for conversation orchestrator
- `673d92e` — Clinical knowledge service
- `8bc6ec0` — Knowledge provider port

Pendiente de seguimiento Git:

- `docs/AI_CONTEXT.md`
- `docs/CURRENT_STATE.md`
- `docs/PROJECT_JOURNAL.md`
- `docs/challenge/CHALLENGE_ANALYSIS.md`

---

## 5. Arquitectura actual

La solución utiliza una arquitectura hexagonal con separación entre:

- Presentation
- Application
- Domain
- Infrastructure

Stack base:

- Python 3.12
- FastAPI
- Pydantic
- Pytest
- Ruff
- MyPy
- uv

La arquitectura existente debe extenderse para cumplir el reto.

No se rediseñará innecesariamente la arquitectura.

---

## 6. Implementación existente

Ya existe una primera capa funcional del dominio de conversación postoperatoria.

Componentes implementados incluyen:

- Entidades de dominio.
- Value Objects.
- Servicios de dominio.
- Puertos.
- Servicios de conocimiento clínico.
- Orquestador de conversación.
- `LanguageModel`.
- `GeminiLanguageModel`.
- `ClinicalPromptBuilder`.
- `ClinicalResponseService`.
- Application DTOs.
- Use Cases.
- Composition Root.
- Dependency Injection.
- FastAPI.
- Health endpoint.
- Follow-up endpoint.
- Global exception handler.
- Send message DTOs.
- API schemas.
- `BGEEmbeddingProvider`.
- `ChromaKnowledgeProvider`.
- Factory de infraestructura RAG.
- Indexación de chunks clínicos.
- Recuperación de evidencia mediante búsqueda vectorial.
- Integración de evidencia en `ConversationOrchestrator`.
- Grounding del prompt clínico mediante `ClinicalPromptBuilder`.
- Integración BGE-M3 → ChromaDB validada mediante pruebas.

Existe `StartFollowUpUseCase`, responsable de:

1. Crear el contexto de conversación.
2. Inicializar el estado conversacional.
3. Inicializar la decisión clínica.
4. Persistir el contexto mediante `ConversationRepository`.

Estado inicial:

- `ConversationState.GREETING`
- `ClinicalDecision.CONTINUE`

---

## 7. Estado del reto

La matriz operativa de trazabilidad ya está creada:

`docs/challenge/CHALLENGE_ANALYSIS.md`

Su función es traducir:

`Requisito → Implementación → Prueba → Evidencia → Entregable`

Actualmente las compuertas y criterios están identificados, pero todavía no deben marcarse como superados sin evidencia verificable.

---

## 8. Compuertas eliminatorias

La implementación final debe superar:

### G1 — 4 entregables

1. Repositorio.
2. Diagrama.
3. Informe final.
4. Video.

### G2 — Levantamiento ≤15 minutos

La solución debe poder levantarse siguiendo exclusivamente el README.

### G3 — Modelo permitido

🟢 **IMPLEMENTADO**

El modelo seleccionado es:

**Google Gemini 1.5 Flash**

La integración se realiza mediante:

- SDK `google-genai`;
- puerto `LanguageModel`;
- adaptador `GeminiLanguageModel`;
- variable de entorno `GEMINI_API_KEY`;
- `ClinicalResponseService`;
- `ClinicalPromptBuilder`;
- integración con `ConversationOrchestrator`.

La suite automatizada actual reporta:

`60 passed`

La elección y justificación técnica están registradas en
`docs/PROJECT_JOURNAL.md`.

G3 se considera implementado a nivel técnico. La evidencia final de entrega
todavía deberá incluir configuración, código, README, informe y demostración.


### G4 — Voz en tiempo real

El jurado debe poder:

- iniciar una llamada desde navegador/API;
- hablar mediante micrófono;
- recibir respuesta hablada.

### G5 — Knowledge vivo

Debe ser posible:

1. Subir un documento desde la consola.
2. Procesarlo.
3. Consultarlo mediante el agente.
4. Eliminarlo.
5. Verificar que deja de ser recuperable.

---

## 9. Criterios de puntuación

| Criterio | Puntos |
|---|---:|
| RAG, precisión clínica y conocimiento vivo | 20 |
| Lógica de decisión y escalamiento | 20 |
| Comprensión del problema y conversación | 15 |
| Calidad de conversación de voz | 15 |
| Video | 15 |
| Repositorio, proceso y buenas prácticas | 15 |
| **Total** | **100** |

La prioridad técnica se concentra en los primeros dos criterios porque constituyen el núcleo funcional de la solución.

---

## 10. Métricas obligatorias

El sistema debe instrumentar desde la implementación:

- Latencia P50.
- Latencia P95.
- Latencia desde fin de habla hasta inicio del audio.
- Tokens de entrada por turno.
- Tokens de salida por turno.
- Tokens por llamada.
- Invocaciones al LLM por turno.
- Consultas RAG por llamada.
- Costo estimado por llamada.

Las métricas deberán proceder de logs verificables.

---

## 11. Riesgos prioritarios

### Críticos

1. Falso negativo clínico.
2. Alucinación clínica peligrosa.
3. Prompt injection.
4. Fallo de voz en tiempo real.
5. Fallo del knowledge vivo.
6. Levantamiento superior a 15 minutos.

### Altos

7. Métricas inconsistentes con los logs.
8. Demo diferente al repositorio entregado.
9. Diagrama que no corresponde al código.
10. Falta de trazabilidad de fuentes clínicas.

---

## 12. Principios de desarrollo

Cada incremento debe producir al menos uno de:

- funcionalidad;
- prueba;
- evidencia;
- métrica;
- documentación;
- reducción de riesgo.

No se priorizarán funcionalidades puramente estéticas.

La estética de las superficies no es criterio de puntuación.

---

## 13. Próximo objetivo

El circuito RAG real y el grounding del LLM ya están implementados:

`Consulta → embeddings BGE-M3 → ChromaDB → Evidence → ClinicalPromptBuilder → Gemini`

El siguiente objetivo técnico es implementar Knowledge Vivo sobre esta infraestructura:

`Documento → ingestión → extracción → chunking → embeddings → ChromaDB → consulta → eliminación → verificación de olvido`

Después se integrarán progresivamente:

`Voz → STT → RAG/LLM → TTS`

junto con observabilidad, métricas obligatorias y consola de administración.

El siguiente incremento técnico prioritario es **INC-004 — Knowledge Vivo**.

Cada incremento será validado antes de iniciar el siguiente.