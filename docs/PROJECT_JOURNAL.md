PROJECT_JOURNAL.md
Project Journal

Registro de decisiones técnicas, avances, validaciones y aprendizajes relevantes
del desarrollo del Tech Sphere Challenge 2026.

2026-08-07 — Separación de repositorios confirmada
Contexto

El directorio de trabajo contiene dos repositorios Git independientes:

tech-sphere-challenge-2-ai-voice-agent
ParticipantArtifacts
Decisión

Mantener ambos repositorios separados.

ParticipantArtifacts se considera la fuente oficial del reto.

El repositorio de desarrollo contiene nuestra implementación, pruebas,
documentación y evolución.

Razón

Evitar mezclar el historial Git oficial con el historial de desarrollo y mantener
una trazabilidad clara entre requisitos oficiales e implementación.

2026-08-07 — Documentación oficial protegida
Decisión

No modificar:

ParticipantArtifacts/docs/rubrica-evaluacion.md
ParticipantArtifacts/docs/stack-tecnico.md
ParticipantArtifacts/README.md
Razón

Son documentos normativos del reto.

La interpretación operativa se realiza mediante:

docs/CURRENT_STATE.md
docs/AI_CONTEXT.md
docs/PROJECT_JOURNAL.md
docs/challenge/CHALLENGE_ANALYSIS.md
2026-08-07 — Matriz de trazabilidad
Decisión

Crear:

docs/challenge/CHALLENGE_ANALYSIS.md

Propósito

Traducir:

Requisito → Implementación → Prueba → Evidencia → Entregable

Razón

La rúbrica evalúa aquello que puede observarse y verificarse.

Cada funcionalidad debe planificarse junto con su prueba y evidencia.

2026-08-07 — Estrategia incremental
Decisión

No desarrollar funcionalidades por estética o complejidad.

Cada incremento debe aportar al menos:

funcionalidad;
prueba;
evidencia;
métrica;
documentación;
reducción de riesgo.
Razón

El reto contiene compuertas eliminatorias y criterios de puntuación.

La prioridad es maximizar la probabilidad de superar las compuertas y generar
evidencia objetiva.

2026-08-07 — Prioridad clínica
Decisión

El diseño debe ser conservador frente a escenarios clínicos ambiguos o
potencialmente peligrosos.

Razón

El falso negativo clínico representa un riesgo crítico.

La lógica de decisión tendrá prioridad sobre respuestas conversacionales genéricas.

2026-08-07 — Estado técnico de partida
Estado

La arquitectura hexagonal y la primera capa de dominio/aplicación estaban
implementadas.

Existían:

dominio clínico;
servicios de conocimiento;
orquestación;
casos de uso;
DTOs;
puertos;
FastAPI;
endpoints iniciales;
exception handler.
Próximo foco

Integrar progresivamente:

Conversación
→ conocimiento
→ decisión
→ escalamiento
→ resumen
→ observabilidad
2026-08-07 — INC-001: Selección del modelo e infraestructura RAG
Contexto

Se requirió seleccionar un modelo permitido por el reto y definir la arquitectura
para RAG y Knowledge Vivo.

Alternativas consideradas
Llama 3.1 70B vía Groq.
Phi-3.5 Mini / Llama 3.2 local.
Google Gemini 1.5 Flash vía API.
Decisión

Se seleccionó:

Google Gemini 1.5 Flash

para el razonamiento clínico.

La arquitectura RAG utilizaría:

BGE-M3 para embeddings;
ChromaDB como almacenamiento vectorial;
puertos desacoplados;
evidencia estructurada.
Razón

La solución busca mantener baja complejidad operativa, preservar una arquitectura
hexagonal y facilitar el levantamiento del proyecto.

2026-08-09 — INC-001: Implementación y validación del LLM
Contexto

La selección de Gemini pasó de diseño a integración real.

Objetivo:

mensaje
→ recuperación de evidencia
→ prompt
→ LLM
→ respuesta
Implementación

Se implementó:

app/infrastructure/llm/gemini_language_model.py

Utilizando:

google-genai

y el puerto:

LanguageModel

Configuración:

GEMINI_API_KEY

Modelo:

gemini-1.5-flash

Integración

La evidencia se mantiene encapsulada mediante:

KnowledgeProvider → ClinicalKnowledgeService

La evidencia recuperada llega a:

ClinicalPromptBuilder

Posteriormente:

ClinicalResponseService

coordina:

KnowledgeService
→ PromptBuilder
→ LanguageModel
Integración con conversación

ConversationOrchestrator utiliza ClinicalResponseService.

Flujo:

registrar mensaje;
recuperar evidencia;
generar respuesta;
registrar respuesta;
conservar evidencia;
ejecutar decisión;
actualizar estado.
Validación

La suite correspondiente fue ejecutada satisfactoriamente.

Estado

🟢 LLM integrado y validado.

2026-08-09 — INC-003: Infraestructura RAG con BGE-M3 y ChromaDB
Contexto

Se requiere recuperación de conocimiento clínico fundamentado para reducir
alucinaciones y proporcionar trazabilidad.

La arquitectura ya contaba con KnowledgeProvider.

Decisión

Implementar:

BGEEmbeddingProvider;
ChromaKnowledgeProvider;
ChromaKnowledgeIndexer;
embeddings normalizados;
persistencia ChromaDB;
recuperación;
eliminación por documento;
transformación a Evidence;
factory de infraestructura.
Flujo validado
texto
→ BGE-M3
→ embedding
→ ChromaDB
→ búsqueda
→ Evidence
Razón

Permite disponer de recuperación vectorial local sin acoplar el dominio a
ChromaDB ni al modelo de embeddings.

Riesgos reducidos
dependencia exclusiva del LLM;
falta de trazabilidad;
acoplamiento del dominio;
ausencia de infraestructura para Knowledge Vivo.
Evidencia

Implementación:

app/infrastructure/rag/bge_embedding_provider.py
app/infrastructure/rag/chroma_knowledge_provider.py
app/infrastructure/rag/chroma_knowledge_indexer.py
app/infrastructure/rag/factory.py

Pruebas:

tests/infrastructure/rag/test_bge_embedding_provider.py
tests/infrastructure/rag/test_chroma_knowledge_provider.py
tests/infrastructure/rag/test_chroma_knowledge_indexer.py
tests/infrastructure/rag/test_bge_chroma_integration.py
tests/infrastructure/rag/test_factory.py
Estado

🟢 Infraestructura RAG implementada y validada.

2026-08-09 — INC-004: Servicio de ingestión de conocimiento clínico
Contexto

La infraestructura RAG ya dispone de:

embeddings;
almacenamiento;
recuperación;
eliminación.

El siguiente paso fue separar la responsabilidad de ingestión del almacenamiento
concreto.

Decisión

Implementar:

ClinicalKnowledgeIngestionService

Ubicación:

app/domain/services/clinical_knowledge_ingestion_service.py

El servicio recibe:

document_name;
section;
chunk_id;
text.

y delega la operación a:

KnowledgeIndexer

Flujo
ClinicalKnowledgeIngestionService
            ↓
      KnowledgeIndexer
            ↓
  ChromaKnowledgeIndexer
            ↓
         ChromaDB
Razón

La ingestión no debe depender directamente de ChromaDB.

El servicio utiliza el puerto KnowledgeIndexer para mantener la separación entre
la lógica y la infraestructura.

Pruebas

Se incorporó:

tests/domain/services/test_clinical_knowledge_ingestion_service.py

La prueba verifica que el servicio delega correctamente la información del chunk.

También se amplió:

tests/infrastructure/rag/test_chroma_knowledge_indexer.py

para verificar que la eliminación de un documento no elimina chunks de otros
documentos.

Validación

Ruff:

uv run ruff check app tests
All checks passed!

Pytest:

uv run python -m pytest
69 passed in 77.92s
Evidencia

Commit:

94217df feat: integrate clinical knowledge ingestion

Estado

🟢 Servicio de ingestión implementado y probado.

🟡 Knowledge Vivo todavía no está cerrado.

Pendiente
upload
→ extracción
→ chunking
→ ingestión
→ indexación
→ consulta
→ evidencia
→ respuesta
→ delete
→ verificación de olvido
2026-08-09 — Checkpoint de continuidad
Estado Git

Branch:

main

Working tree:

clean

Remote:

origin/main

Último commit:

94217df feat: integrate clinical knowledge ingestion

Validación

Ruff:

All checks passed!

Pytest:

69 passed

Estado de compuertas
G1 🟡
G2 🟡
G3 🟢
G4 🔴
G5 🟡
Estado técnico
Dominio              🟢
Application          🟢
API                  🟢
LLM                  🟢
RAG                  🟢
Grounding            🟢
Ingestion            🟢
Knowledge Vivo       🟡
Decisión clínica     🟡
Voz                  🔴
Observabilidad       🔴
Administración       🔴
Demo                 🔴
Próximo objetivo

Completar:

INC-004 — Knowledge Vivo

con el flujo observable:

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

Este checkpoint debe utilizarse como punto de recuperación si el desarrollo
continúa en una nueva conversación.

Formato para futuras entradas

Cada decisión significativa deberá registrar:

Contexto

Qué problema o requisito originó la decisión.

Alternativas

Qué opciones fueron consideradas.

Decisión

Qué se implementó.

Razón

Por qué se eligió.

Riesgos

Qué riesgos introduce o reduce.

Evidencia

Qué prueba, log, commit o artefacto permite verificarla.

Estado

Debe distinguir claramente entre:

implementado;
parcial;
pendiente;
validado.

No declarar una compuerta como superada únicamente por la existencia de código.