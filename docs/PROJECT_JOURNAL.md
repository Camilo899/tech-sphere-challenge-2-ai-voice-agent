# PROJECT_JOURNAL.md

## Project Journal

Registro de decisiones técnicas, avances, validaciones y aprendizajes relevantes del
desarrollo del Tech Sphere Challenge 2026.

---

## 2026-08-07 — Separación de repositorios confirmada

### Contexto

El directorio de trabajo contiene dos repositorios Git independientes:

- `tech-sphere-challenge-2-ai-voice-agent`
- `ParticipantArtifacts`

### Decisión

Mantener ambos repositorios separados.

`ParticipantArtifacts` se considera la fuente oficial del reto.

El repositorio `tech-sphere-challenge-2-ai-voice-agent` contiene nuestra implementación,
documentación propia, pruebas y evolución.

### Razón

Evitar mezclar el historial Git oficial con el historial de desarrollo y mantener una
trazabilidad clara entre requisitos oficiales e implementación.

---

## 2026-08-07 — Documentación oficial protegida

### Decisión

No modificar:

- `docs/rubrica-evaluacion.md`
- `docs/stack-tecnico.md`

### Razón

Son documentos normativos del reto.

La interpretación operativa se realizará mediante:

- `docs/CURRENT_STATE.md`
- `docs/AI_CONTEXT.md`
- `docs/challenge/CHALLENGE_ANALYSIS.md`

---

## 2026-08-07 — Matriz de trazabilidad

### Decisión

Crear y utilizar:

`docs/challenge/CHALLENGE_ANALYSIS.md`

### Propósito

Traducir cada requisito oficial en:

`Requisito → Implementación → Prueba → Evidencia → Entregable`

### Razón

La rúbrica evalúa únicamente aquello que puede observarse o verificarse.

Por tanto, cada funcionalidad debe planificarse junto con su prueba y evidencia.

---

## 2026-08-07 — Estrategia incremental

### Decisión

No desarrollar funcionalidades por estética o complejidad.

Cada incremento debe aportar al menos:

- funcionalidad;
- prueba;
- evidencia;
- métrica;
- documentación;
- reducción de riesgo.

### Razón

El reto contiene cinco compuertas eliminatorias y seis criterios de puntuación.
La prioridad es maximizar la probabilidad de superar las compuertas y generar evidencia
objetiva.

---

## 2026-08-07 — Prioridad clínica

### Decisión

El diseño debe ser conservador frente a escenarios clínicos ambiguos o potencialmente
peligrosos.

### Razón

La rúbrica establece que el falso negativo es la falla catastrófica.

La lógica de decisión tendrá prioridad sobre respuestas conversacionales genéricas.

---

## 2026-08-07 — Estado técnico de partida

### Estado

La arquitectura hexagonal y una primera capa de dominio/aplicación ya están implementadas.

Existe:

- dominio clínico;
- servicios de conocimiento;
- orquestación de conversación;
- casos de uso;
- DTOs;
- puertos;
- FastAPI;
- endpoints iniciales;
- manejo global de excepciones.

### Próximo foco

Integrar progresivamente los componentes necesarios para:

`Conversación → conocimiento → decisión → escalamiento → resumen → observabilidad`

---

## Formato para futuras entradas

Cada decisión significativa deberá registrar:

### Contexto

Qué problema o requisito originó la decisión.

### Alternativas

Qué opciones fueron consideradas.

### Decisión

Qué se implementó.

### Razón

Por qué se eligió.

### Riesgos

Qué riesgos introduce o reduce.

### Evidencia

Qué prueba, log, commit o artefacto permite verificarla.

## 2026-08-07 — INC-001: Selección de Modelos e Infraestructura RAG

### Contexto
Se requiere definir el modelo de lenguaje permitido (Compuerta G3) y diseñar la estrategia técnica para el RAG y Knowledge Vivo (Compuerta G5) con el fin de avanzar en el flujo operativo sin alterar el dominio.

### Alternativas Consideradas
1. **Llama 3.1 70B (vía Groq):** Excelente velocidad en texto, pero sujeta a límites de rate-limiting severos para flujos continuos de audio/voz de múltiples usuarios.
2. **Phi-3.5 Mini / Llama 3.2 (Local vía Ollama):** Ideal para privacidad absoluta, pero introduce penalizaciones de latencia críticas en setups de hardware estándar, arriesgando el P95 de la interfaz de voz.
3. **Google Gemini 1.5 Flash (API):** Óptima relación entre velocidad (Time-to-First-Token bajo para voz), ventana de contexto amplia para RAG clínico extenso y costo por token reducido.

### Decisión
1. **LLM Principal:** Google Gemini 1.5 Flash mediante el SDK oficial.
2. **Vector Store:** ChromaDB en modo embebido local o persistencia en disco ligero dentro del repositorio.
3. **Embeddings:** `text-embedding-004` de Google (o complementado con un modelo compatible local si se requiere aislamiento estricto de pruebas).

### Razón
Gemini 1.5 Flash asegura latencias ultra bajas requeridas para que la conversación simulada o real de voz se sienta fluida, mitigando el riesgo de la métrica de fin-de-habla-a-audio. ChromaDB en modo embebido elimina dependencias de infraestructura externa compleja (como instancias de Docker separadas para bases vectoriales), garantizando que el levantamiento del proyecto se mantenga estrictamente por debajo de los 15 minutos (Compuerta G2).

### Riesgos Mitigados
- **Latencia excesiva en turnos:** Mitigado por la velocidad de Gemini 1.5 Flash.
- **Complejidad de despliegue:** Reducida al mínimo usando bases de datos vectoriales en bebidas en Python controladas por `uv`.

### Evidencia
Este diseño técnico queda plasmado como el punto de partida para las implementaciones de los adaptadores en `infrastructure/`.
---

## 2026-08-09 — INC-001: Implementación y validación de LLM + RAG

### Contexto

La decisión registrada en INC-001 pasó de diseño arquitectónico a implementación
funcional dentro del flujo de conversación.

El objetivo fue cerrar el circuito:

`mensaje del paciente → recuperación de evidencia → construcción de prompt → LLM → respuesta → conversación`

sin introducir lógica de infraestructura dentro del dominio clínico.

### Implementación

Se implementó el adaptador:

`app/infrastructure/llm/gemini_language_model.py`

El adaptador utiliza el SDK oficial `google-genai` y expone el contrato definido por:

`app.domain.ports.language_model.LanguageModel`

La configuración de la API se realiza mediante:

`GEMINI_API_KEY`

El modelo seleccionado es:

`gemini-1.5-flash`

### Integración con RAG

La recuperación de conocimiento permanece encapsulada mediante:

`KnowledgeProvider → ClinicalKnowledgeService`

La evidencia recuperada se entrega al:

`ClinicalPromptBuilder`

que construye el prompt clínico incluyendo el mensaje del paciente y los fragmentos
recuperados.

Posteriormente:

`ClinicalResponseService`

coordina:

`KnowledgeService → PromptBuilder → LanguageModel`

y devuelve un `LLMResponse`.

### Integración con la conversación

`ConversationOrchestrator` fue ampliado para utilizar `ClinicalResponseService`.

El flujo resultante es:

1. Se registra el mensaje del paciente.
2. Se recupera evidencia clínica.
3. Se genera la respuesta mediante el servicio clínico.
4. La respuesta del LLM se registra como mensaje del asistente.
5. Se conserva la evidencia recuperada en el contexto.
6. Se ejecuta la decisión clínica.
7. Se actualiza el estado de la conversación.

La integración mantiene la separación entre dominio, aplicación e infraestructura.

### Pruebas

Se incorporaron pruebas para:

- contrato `LanguageModel`;
- fake del modelo de lenguaje;
- adaptador `GeminiLanguageModel`;
- `ClinicalPromptBuilder`;
- `ClinicalResponseService`;
- `ConversationOrchestrator`;
- `SendMessageUseCase`;
- endpoint `/messages`.

La validación completa de la aplicación quedó en:

`60 passed`

### Validación

Comando utilizado:

`uv run python -m pytest -q`

Resultado:

`60 passed`

También fueron validadas individualmente las piezas críticas del circuito:

- `ClinicalResponseService`: 1 passed
- `SendMessageUseCase`: 1 passed
- endpoint `/messages`: 1 passed

### Evidencia

La implementación quedó integrada en el commit técnico correspondiente a INC-001.

Los principales artefactos implementados o modificados son:

- `app/infrastructure/llm/gemini_language_model.py`
- `app/domain/services/clinical_response_service.py`
- `app/domain/services/conversation_orchestrator.py`
- `app/application/factories/conversation_orchestrator_factory.py`
- `app/application/use_cases/send_message.py`
- `app/presentation/api/dependencies.py`
- pruebas del adaptador, servicio, caso de uso y endpoint
- `pyproject.toml`
- `uv.lock`

### Estado

INC-001 queda implementado y validado.

La integración real del LLM está funcional bajo configuración mediante
`GEMINI_API_KEY`, mientras que la recuperación RAG continúa utilizando la
abstracción `KnowledgeProvider` y su implementación basada en ChromaDB.

El siguiente objetivo es continuar con el cierre del circuito operativo y las
compuertas restantes, especialmente Knowledge Vivo y el pipeline de voz.

---

## 2026-08-09 — INC-003: Infraestructura RAG con BGE-M3 y ChromaDB

### Contexto

El proyecto requiere recuperación de conocimiento clínico fundamentado para
reducir alucinaciones y permitir trazabilidad de la evidencia utilizada por
el agente.

La arquitectura ya contaba con el puerto `KnowledgeProvider`, por lo que la
implementación se realizó mediante adaptadores de infraestructura sin alterar
el dominio.

### Alternativas

Se evaluó mantener únicamente el `FakeKnowledgeProvider` para las pruebas o
implementar una infraestructura RAG real.

Se eligió implementar el stack RAG real con embeddings locales y almacenamiento
vectorial persistente.

### Decisión

Se implementó:

- `BGEEmbeddingProvider` utilizando `BAAI/bge-m3`;
- `ChromaKnowledgeProvider` utilizando ChromaDB persistente;
- embeddings normalizados;
- indexación de chunks mediante `index(...)`;
- recuperación mediante `retrieve(...)`;
- transformación de resultados en `Evidence`;
- factory `create_chroma_knowledge_provider()`;
- pruebas unitarias y de integración.

El flujo validado es:

`texto → BGE-M3 → embedding → ChromaDB → búsqueda → Evidence`

### Razón

La solución permite disponer de recuperación vectorial local sin acoplar el
dominio a ChromaDB ni al modelo concreto de embeddings.

Esto mantiene la arquitectura hexagonal y permite sustituir posteriormente
los adaptadores sin modificar los contratos del dominio.

### Riesgos reducidos

- Dependencia de conocimiento exclusivamente generado por el LLM.
- Acoplamiento del dominio con infraestructura vectorial.
- Falta de trazabilidad de fragmentos recuperados.
- Ausencia de una base técnica para Knowledge Vivo.

### Evidencia

La implementación se encuentra en:

- `app/infrastructure/rag/bge_embedding_provider.py`
- `app/infrastructure/rag/chroma_knowledge_provider.py`
- `app/infrastructure/rag/factory.py`

Las pruebas correspondientes se encuentran en:

- `tests/infrastructure/rag/test_bge_embedding_provider.py`
- `tests/infrastructure/rag/test_chroma_knowledge_provider.py`
- `tests/infrastructure/rag/test_bge_chroma_integration.py`
- `tests/infrastructure/rag/test_factory.py`

### Estado

🟢 **Infraestructura RAG implementada y validada.**

🟡 **Integración completa con grounding clínico y Knowledge Vivo pendientes.**

### Próximo paso

Cerrar el circuito:

`recuperación → Evidence → ClinicalPromptBuilder → Gemini → respuesta fundamentada`

y posteriormente implementar:

`upload → extracción → chunking → indexación → consulta → delete → verificación de olvido`