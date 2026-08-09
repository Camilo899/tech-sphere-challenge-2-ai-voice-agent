# CHALLENGE_ANALYSIS.md

# Tech Sphere Challenge 2026 — Matriz de trazabilidad

## 1. Propósito

Este documento traduce los requisitos oficiales del reto en elementos concretos de
implementación, validación y evidencia.

Los documentos oficiales son:

- `docs/rubrica-evaluacion.md`
- `docs/stack-tecnico.md`

Estos documentos son normativos y **no se modifican**.

Esta matriz sí se modifica durante el desarrollo porque representa el estado real de
nuestra implementación.

### Convención de estados

- 🟢 **IMPLEMENTADO**: existe implementación funcional y verificable en el repositorio.
- 🟡 **PARCIAL**: existe base arquitectónica, contrato o parte funcional, pero todavía
  falta cerrar el requisito observable.
- 🔴 **PENDIENTE**: todavía no existe implementación funcional suficiente.
- ⬜ **NO VALIDADO**: existe implementación, pero aún no se ha ejecutado la prueba
  correspondiente.

---

# 2. Compuertas eliminatorias

| ID | Requisito | Implementación actual | Prueba requerida | Evidencia requerida | Estado |
|---|---|---|---|---|---|
| **G1** | 4 entregables completos | Repositorio público + documentación propia en construcción. Diagrama, informe y video aún pendientes. | Checklist final de los 4 entregables | GitHub + diagrama + informe + video | 🟡 |
| **G2** | Levantamiento ≤15 min | Proyecto Python/FastAPI con `pyproject.toml` y `uv.lock`; procedimiento final todavía no cerrado. | Levantamiento cronometrado siguiendo exclusivamente README | README + logs + tiempo medido | 🟡 |
| **G3** | Modelo permitido | Google Gemini 1.5 Flash integrado mediante `google-genai`, con adaptador `GeminiLanguageModel` y configuración mediante `GEMINI_API_KEY`. | Verificar modelo contra `docs/stack-tecnico.md` y ejecutar flujo de respuesta | Código + configuración + pruebas + README + informe | 🟢 |
| **G4** | Voz en tiempo real | Existe `VoiceProvider` como puerto arquitectónico, pero no hay pipeline STT → LLM → TTS funcional. | Saludo + pregunta trivial en llamada real | Demo + logs + video | 🔴 |
| **G5** | Knowledge vivo | Existe infraestructura RAG funcional con BGE-M3, ChromaDB, indexación, recuperación y evidencia. Todavía no existe el flujo completo de upload → procesamiento → consulta → delete → verificación de olvido. | Documento externo: subir → consultar → eliminar → comprobar olvido | Consola + logs + video | 🔴 |

### Regla operativa

Ninguna compuerta se considera superada por la existencia de interfaces, fakes,
schemas o placeholders. Debe existir una ruta funcional y observable que permita
ejecutar la prueba definida por la rúbrica.

---

# 3. Estado de implementación actual

## 3.1 Dominio y aplicación

Actualmente existe una base funcional de dominio y aplicación que incluye:

- `ConversationContext`
- `FollowUpCase`
- `Patient`
- `ClinicalDecision`
- estados de conversación
- mensajes y turnos
- observaciones del paciente
- niveles de riesgo
- evidencia clínica
- explicación de decisión
- resumen clínico
- recomendaciones
- eventos de dominio
- `ConversationOrchestrator`
- `ClinicalKnowledgeService`
- `ClinicalReasoner`
- `DecisionEngine`
- `RiskAssessmentService`
- `SymptomClassifier`
- `ConversationAnalysisService`
- `SummaryGenerationService`
- `StartFollowUpUseCase`
- DTOs de inicio y envío de mensajes
- rutas FastAPI de health y follow-up
- manejo global de excepciones

### Estado

🟢 **Base de dominio/aplicación implementada.**

Esto constituye infraestructura de arquitectura, no implica todavía que las
integraciones externas del reto estén terminadas.

---

## 3.2 Puertos y adaptadores

Existen contratos para:

- `ConversationRepository`
- `KnowledgeProvider`
- `DecisionEngine`
- `AuditProvider`
- `LanguageNormalizer`
- `SummaryProvider`
- `VoiceProvider`
- `LanguageModel`

También existen fakes para pruebas, incluyendo:

- `FakeConversationRepository`
- `FakeKnowledgeProvider`
- `FakeLanguageModel`

### Estado

🟡 **Arquitectura preparada para integración.**

Los contratos permiten extender la solución sin rediseñar el dominio, pero la
rúbrica exige implementaciones reales para las funcionalidades evaluables.

---

## 3.3 API

Actualmente existe:

- aplicación FastAPI
- endpoint de health
- endpoint de inicio de follow-up
- endpoint de envío de mensajes
- schemas Pydantic
- DTOs de aplicación
- dependency injection
- exception handler global

### Estado

🟢 **API base implementada y probada.**

---

## 3.4 RAG y conocimiento clínico

La infraestructura RAG real ya está implementada.

Actualmente existe:

1. `BGEEmbeddingProvider` basado en `BAAI/bge-m3`;
2. `ChromaKnowledgeProvider` basado en ChromaDB persistente;
3. generación de embeddings normalizados;
4. indexación de chunks clínicos;
5. recuperación mediante búsqueda vectorial;
6. transformación de resultados recuperados en `Evidence`;
7. factory para construir el proveedor RAG;
8. pruebas unitarias de embeddings;
9. pruebas del proveedor ChromaDB;
10. prueba de integración BGE-M3 → ChromaDB.

El flujo actualmente validado es:

`texto → BGE-M3 → embedding → ChromaDB → búsqueda → Evidence`

Todavía debe cerrarse el flujo completo requerido por el reto:

`documento → extracción → chunking → embeddings → ChromaDB → recuperación → evidencia → respuesta fundamentada`

También permanece pendiente el Knowledge Vivo completo:

`upload → indexación → consulta → delete → verificación de olvido`

### Estado

🟢 **RAG base y grounding del LLM implementados; ingestión documental y Knowledge Vivo pendientes.**

### Prioridad

**Máxima**, porque afecta directamente:

- G5;
- 20 puntos de RAG, precisión clínica y conocimiento vivo;
- trazabilidad clínica;
- reducción de alucinaciones.

---

## 3.5 LLM

Se seleccionó e integró **Google Gemini 1.5 Flash**, uno de los modelos
permitidos por `docs/stack-tecnico.md`.

La integración se realiza mediante:

- puerto de dominio `LanguageModel`;
- adaptador `GeminiLanguageModel`;
- SDK oficial `google-genai`;
- configuración mediante `GEMINI_API_KEY`;
- `ClinicalPromptBuilder`;
- `ClinicalResponseService`;
- integración con `ConversationOrchestrator`;
- endpoint `/messages`.

El dominio permanece desacoplado del proveedor concreto mediante el puerto
`LanguageModel`.

### Validación

La implementación cuenta con pruebas para:

- contrato del `LanguageModel`;
- `FakeLanguageModel`;
- `ClinicalResponseService`;
- `GeminiLanguageModel`;
- caso de uso `SendMessageUseCase`;
- endpoint `/messages`.

La suite completa fue ejecutada con:

`uv run python -m pytest -q`

Resultado:

`60 passed`

### Estado

🟢 **LLM real integrado y probado.**

### Pendiente

Todavía falta instrumentar:

- tokens de entrada por turno;
- tokens de salida por turno;
- invocaciones LLM por turno;
- costo estimado por llamada;
- pruebas adversariales de prompt injection.

La validación clínica integral también permanece pendiente.

---

## 3.6 Voz

Existe `VoiceProvider`, pero todavía no existe implementación funcional de:

```text
Micrófono
   ↓
STT
   ↓
Análisis / RAG / LLM
   ↓
Respuesta
   ↓
TTS
   ↓
Audio al paciente
```

### Estado

🔴 **Voz en tiempo real pendiente.**

Esto es requisito eliminatorio G4.

---

## 3.7 Consola de administración

La estructura contiene:

`apps/admin/`

pero actualmente no existe una consola funcional que permita:

- subir documento;
- listar documentos;
- mostrar documento procesado/disponible;
- eliminar documento.

### Estado

🔴 **Pendiente.**

La estética no es prioridad. La prioridad es satisfacer el contrato funcional
mínimo exigido por el README oficial.

---

## 3.8 Interfaz de llamada

La estructura contiene:

`apps/web/`

pero todavía no existe una interfaz funcional que permita:

- iniciar llamada desde navegador;
- conceder acceso al micrófono;
- hablar con el agente;
- escuchar la respuesta.

### Estado

🔴 **Pendiente.**

---

# 4. Criterios de puntuación

## 4.1 RAG, precisión clínica y conocimiento vivo — 20 pts

### Objetivos

- Respuestas fundamentadas en el corpus.
- Trazabilidad de las respuestas.
- Manejo explícito de información desconocida.
- Incorporación dinámica de documentos.
- Eliminación efectiva del conocimiento.
- Ausencia de alucinación clínica.

### Evidencia requerida

- Logs RAG.
- Fuentes recuperadas.
- Documento utilizado.
- Respuesta generada.
- Prueba upload/delete.
- Pruebas de preguntas fuera del corpus.

### Estado

🟢 **RAG y grounding del LLM implementados; validación clínica y Knowledge Vivo pendientes.**

---

## 4.2 Lógica de decisión y escalamiento — 20 pts

### Base actualmente disponible

Existe una base de dominio relacionada con:

- `DecisionEngine`
- `ClinicalReasoner`
- `RiskAssessmentService`
- `SymptomClassifier`
- `ClinicalDecision`
- `RiskLevel`
- `DecisionExplanation`
- eventos de decisión y alerta.

### Falta demostrar

- clasificación correcta de verde/amarillo/rojo;
- investigación de ambigüedad;
- política conservadora ante riesgo;
- escalamiento;
- persistencia de alertas;
- resumen final;
- próximos pasos;
- comportamiento sobre los casos del dataset.

### Estado

🟡 **Base implementada; validación clínica integral pendiente.**

---

## 4.3 Comprensión del problema y diseño de la conversación — 15 pts

### Base disponible

Existe:

- estado conversacional;
- mensajes;
- turnos;
- orquestador;
- análisis conversacional;
- flujo de conversación.

### Falta demostrar

- apertura de llamada;
- recolección progresiva de síntomas;
- manejo de respuestas evasivas;
- manejo de interrupciones;
- instrucciones largas adaptadas a voz;
- cierre;
- correspondencia entre diagrama, implementación y comportamiento real.

### Estado

🟡 **Base implementada; conversación evaluable pendiente.**

---

## 4.4 Calidad de la conversación de voz — 15 pts

### Requisitos

- tono apropiado;
- respuestas concisas;
- latencia;
- manejo de silencios;
- interrupciones;
- audio degradado;
- regionalismos colombianos;
- paciente hostil/asustado;
- prompt injection;
- solicitudes fuera de misión.

### Métricas

- P50;
- P95;
- latencia por turno.

### Estado

🔴 **Pendiente de integración de voz y observabilidad.**

---

## 4.5 Video de argumentación y demo — 15 pts

### Debe demostrar

- funcionamiento real;
- correspondencia con el repositorio;
- flujo de demo;
- respuesta a pregunta 1;
- respuesta a pregunta 2.

### Estado

🔴 **Pendiente.**

---

## 4.6 Repositorio, proceso y buenas prácticas — 15 pts

### Base disponible

- repositorio Git activo;
- historial de commits;
- dependencias declaradas;
- arquitectura documentada;
- pruebas automatizadas;
- Ruff;
- documentación propia de continuidad.

### Falta

- README final reproducible;
- métricas;
- logs verificables;
- documentación de prompts;
- evolución de decisiones;
- informe final;
- diagrama final;
- coherencia demostrable entre código, documentación y demo.

### Estado

🟡 **Base sólida; evidencia final pendiente.**

---

# 5. Métricas obligatorias

| Métrica | Fuente | Instrumentación | Estado |
|---|---|---|---|
| Latencia P50 | Logs | Middleware/instrumentación de turnos | 🔴 |
| Latencia P95 | Logs | Middleware/instrumentación de turnos | 🔴 |
| Input tokens/turno | LLM | Captura de usage del proveedor | 🔴 |
| Output tokens/turno | LLM | Captura de usage del proveedor | 🔴 |
| Tokens/llamada | LLM | Agregación por conversation/call ID | 🔴 |
| Invocaciones LLM/turno | LLM | Contador por turno | 🔴 |
| Consultas RAG/llamada | RAG | Contador por llamada | 🔴 |
| Costo/llamada | Métricas + precios | Cálculo documentado | 🔴 |

### Regla

No se registrarán métricas manualmente para aparentar precisión.

Las métricas finales deben derivarse de logs estructurados y ser contrastables con
la sesión de evaluación.

---

# 6. Dataset y evaluación

El reto proporciona:

- `dataset_final.xlsx`
- `trayectorias_postop_silver.xlsx`
- `perfiles_clinicos_pacientes_silver_contest.xlsx`
- `perfiles_pacientes_co.xlsx`
- `dataset/textos/`

Características relevantes:

- 40 pacientes;
- 160 casos;
- 3 niveles de criticidad: verde, amarillo y rojo;
- conversaciones en dos capas;
- capa limpia;
- capa ruidosa;
- corpus clínico de 107 documentos;
- material de evaluación adicional no incluido en el corpus entregado.

### Implicación

El dataset no debe utilizarse únicamente como conjunto de ejemplos de desarrollo.
Debe servir para:

1. reconstruir casos;
2. probar extracción de síntomas;
3. evaluar decisiones;
4. comparar comportamiento contra `label_ground_truth`;
5. identificar falsos negativos;
6. generar evidencia reproducible.

---

# 7. Riesgos críticos

| Riesgo | Severidad | Mitigación | Evidencia | Estado |
|---|---|---|---|---|
| Falso negativo clínico | Crítica | Política conservadora de escalamiento + pruebas | Casos rojo/ambiguos | 🔴 |
| Alucinación clínica | Crítica | RAG + límites explícitos + abstención | Evaluaciones | 🔴 |
| Prompt injection | Crítica | Separación de instrucciones + validación | Pruebas adversariales | 🔴 |
| Métricas inconsistentes | Alta | Logs estructurados | Logs | 🔴 |
| Demo ≠ repositorio | Alta | Build reproducible + commit/tag | Release | 🟡 |
| Levantamiento >15 min | Crítica | README + automatización | Prueba cronometrada | 🟡 |

---

# 8. Estrategia de incremento

Cada incremento debe producir al menos uno de:

- funcionalidad;
- prueba;
- evidencia;
- métrica;
- documentación;
- reducción de riesgo.

No se priorizan funcionalidades puramente estéticas.

### Orden de prioridad actual

1. **Cerrar integración y grounding del RAG existente.**
2. **Implementar knowledge vivo.**
3. **Conectar decisión clínica con evidencia real.**
4. **Implementar STT/LLM/TTS.**
5. **Construir interfaz de llamada mínima.**
6. **Construir consola administrativa mínima.**
7. **Instrumentar métricas obligatorias.**
8. **Validar dataset y escenarios adversariales.**
9. **Cerrar README ≤15 minutos.**
10. **Preparar diagrama, informe y video.**

---

# 9. Estado global

## Compuertas

- G1 🟡
- G2 🟡
- G3 🟢
- G4 🔴
- G5 🔴

## Núcleo de puntuación

- RAG 🟢
- LLM 🟢
- Decisión clínica 🟡
- Conversación 🟡
- Voz 🔴
- Video 🔴
- Repositorio/proceso 🟡

## Observabilidad

- Latencia 🔴
- Tokens 🔴
- Invocaciones 🔴
- RAG 🔴
- Costos 🔴

---

### INC-001 — Selección del modelo y diseño de integración RAG

1. Modelo permitido seleccionado: 🟢 **Google Gemini 1.5 Flash**
2. Justificación técnica de la elección: 🟢 **Documentada en PROJECT_JOURNAL.md**
3. Proveedor y mecanismo de inferencia: 🟢 **API oficial de Google AI Studio mediante `google-genai`**
4. Estrategia de embeddings: 🟢 **text-embedding-004**
5. Almacenamiento vectorial: 🟢 **ChromaDB (Embebido / Local)**
6. Estrategia de chunking: 🟢 **300-500 tokens con 50 de overlap basado en estructuras clínicas**
7. Contrato de recuperación: 🟢 **Vinculado a KnowledgeProvider**
8. Formato de evidencia: 🟢 **Estructura de evidencia con ID de documento y fuente**
9. Estrategia de actualización y eliminación: 🟢 **Definida para la infraestructura RAG**
10. Puntos de instrumentación para métricas: 🟢 **Definidos para tokens e invocaciones**

**Estado del diseño:** 🟢 **COMPLETADO**

### INC-002 — Integración del LLM Gemini

1. Modelo implementado: 🟢 **Google Gemini 1.5 Flash**
2. Adaptador de infraestructura: 🟢 **`GeminiLanguageModel`**
3. Puerto desacoplado: 🟢 **`LanguageModel`**
4. Servicio de respuesta clínica: 🟢 **`ClinicalResponseService`**
5. Constructor de prompts: 🟢 **`ClinicalPromptBuilder`**
6. Integración con orquestador: 🟢 **`ConversationOrchestrator`**
7. Endpoint de mensajes: 🟢 **`POST /messages`**
8. Fake para pruebas: 🟢 **`FakeLanguageModel`**
9. Suite automatizada: 🟢 **60 tests pasando**

**Estado del incremento:** 🟢 **IMPLEMENTADO Y VALIDADO**

### Pendiente para los siguientes incrementos

- RAG real completo.
- Knowledge vivo.
- Instrumentación de tokens, invocaciones y costos.
- Voz en tiempo real.

