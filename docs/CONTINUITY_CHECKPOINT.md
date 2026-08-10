# CONTINUITY_CHECKPOINT.md

## Clinical AI Voice Agent — Tech Sphere Challenge 2026

> Documento operativo para continuar el desarrollo en otro chat sin depender del historial completo de la conversación.

**Actualizado:** 2026-08-10
**Repositorio:** `tech-sphere-challenge-2-ai-voice-agent`
**Rama:** `main`
**Estado Git:** working tree limpio; `main` sincronizada con `origin/main`.

## 1. Regla de continuidad

Antes de continuar una tarea importante:

1. Leer este archivo.
2. Leer `docs/CURRENT_STATE.md`.
3. Leer las últimas entradas de `docs/PROJECT_JOURNAL.md`.
4. Consultar `docs/challenge/CHALLENGE_ANALYSIS.md` para decidir prioridades.
5. Ejecutar `git status` y `git log -1 --oneline`.
6. No asumir que el estado del chat coincide con el estado del repositorio.

El repositorio y estos documentos son la fuente operativa de continuidad; el historial del chat es contexto auxiliar.

## 2. Última validación conocida

### Tests

```bash
uv run pytest -q
```

Resultado:

```text
77 passed in 52.81s
```

### Diff hygiene

```bash
git diff --check
```

Resultado: sin salida / sin errores conocidos.

### Git

```bash
git status
```

Resultado conocido:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## 3. Estado técnico consolidado

### Conversación

Existe flujo funcional para:

```text
patient message
    ↓
ConversationOrchestrator
    ↓
ConversationAnalysisService
    ↓
SymptomClassifier / RiskLevel
    ↓
ClinicalQueryBuilder
    ↓
ClinicalKnowledgeService
    ↓
Evidence
    ↓
ClinicalResponseService
    ↓
LanguageModel
    ↓
assistant response
    ↓
ConversationContext
```

El `ConversationOrchestrator` actualmente recibe opcionalmente `ClinicalResponseService` y `ConversationAnalysisService`.

### RAG

Implementado y probado:

```text
text
 ↓
BGEEmbeddingProvider
 ↓
ChromaKnowledgeIndexer
 ↓
ChromaDB
 ↓
ChromaKnowledgeProvider
 ↓
Evidence
```

La factory `create_chroma_knowledge_stack()` construye un `RAGStack` con provider e indexer compartiendo el mismo embedding provider, path y collection.

### Knowledge ingestion

Existe:

- `KnowledgeIndexer`
- `ChromaKnowledgeIndexer`
- `ClinicalKnowledgeIngestionService`
- ingestión de chunks
- eliminación por documento
- pruebas de integración indexer → provider

Todavía no debe considerarse G5/Knowledge Vivo completamente cerrado: falta la ruta observable de documento externo → upload → extracción → chunking → ingestión → consulta → delete → verificación de olvido.

### Voz

Existe `SendVoiceMessageUseCase`, que:

1. transcribe mediante `VoiceProvider`;
2. recupera la conversación;
3. crea el `ConversationMessage` del paciente;
4. reutiliza `ConversationOrchestrator`;
5. persiste el contexto;
6. devuelve `SendMessageResponse`.

Esto no equivale todavía a tener demostrada la compuerta de voz en tiempo real end-to-end.

## 4. Archivos clave del estado actual

### Dominio

- `app/domain/services/conversation_orchestrator.py`
- `app/domain/services/conversation_analysis_service.py`
- `app/domain/services/clinical_knowledge_service.py`
- `app/domain/services/clinical_knowledge_ingestion_service.py`
- `app/domain/services/clinical_query_builder.py`
- `app/domain/services/clinical_prompt_builder.py`
- `app/domain/services/clinical_response_service.py`
- `app/domain/services/symptom_classifier.py`

### Application

- `app/application/use_cases/send_message.py`
- `app/application/use_cases/send_voice_message.py`
- `app/application/factories/conversation_orchestrator_factory.py`

### RAG

- `app/infrastructure/rag/factory.py`
- `app/infrastructure/rag/embedding.py`
- `app/infrastructure/rag/bge_embedding_provider.py`
- `app/infrastructure/rag/chroma_knowledge_indexer.py`
- `app/infrastructure/rag/chroma_knowledge_provider.py`

### Tests clave

- `tests/domain/services/test_conversation_orchestrator.py`
- `tests/domain/services/test_conversation_analysis_service.py`
- `tests/domain/services/test_clinical_knowledge_ingestion_service.py`
- `tests/infrastructure/rag/test_chroma_knowledge_indexer.py`
- `tests/infrastructure/rag/test_chroma_knowledge_provider.py`
- `tests/infrastructure/rag/test_factory.py`
- `tests/infrastructure/rag/test_bge_chroma_integration.py`

## 5. Prioridad de entrega

No hacer refactors arquitectónicos innecesarios.

Orden recomendado:

1. **Knowledge Vivo observable (G5).**
2. **Voz end-to-end / tiempo real (G4).**
3. **Pruebas de integración de los flujos críticos.**
4. **Observabilidad, trazabilidad y métricas exigidas.**
5. **Entregables finales: README, diagrama, informe y video.**
6. Solo al final: limpieza estética o refactors no esenciales.

## 6. Ciclo de trabajo obligatorio

Para cada incremento:

```text
leer checkpoint
    ↓
identificar requisito observable
    ↓
modificar lo mínimo necesario
    ↓
test específico
    ↓
pytest completo
    ↓
git diff --check
    ↓
git status
    ↓
commit pequeño
    ↓
push
    ↓
actualizar documentación
```

No dejar cambios relevantes únicamente explicados en el chat.

## 7. Al cambiar de chat

Primer mensaje recomendado:

> Continuemos el proyecto `tech-sphere-challenge-2-ai-voice-agent`. Lee `docs/CONTINUITY_CHECKPOINT.md`, `docs/CURRENT_STATE.md`, las últimas entradas de `docs/PROJECT_JOURNAL.md` y `docs/challenge/CHALLENGE_ANALYSIS.md`. El repositorio debe tratarse como fuente de verdad. No repitas trabajo ya validado. Primero indica el siguiente incremento prioritario y los archivos que debemos inspeccionar.

## 8. Prohibiciones operativas

- No modificar `ParticipantArtifacts`.
- No asumir que una interfaz o fake supera una compuerta de la rúbrica.
- No cambiar RAG por una optimización especulativa sin evidencia de fallo.
- No abrir refactors grandes mientras existan compuertas eliminatorias pendientes.
- No confiar únicamente en el historial del chat para recuperar el estado del proyecto.
