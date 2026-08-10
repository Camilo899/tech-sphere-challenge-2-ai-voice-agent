CHALLENGE_ANALYSIS.md
Tech Sphere Challenge 2026 — Matriz de trazabilidad

1. Propósito

Este documento traduce los requisitos oficiales del reto en elementos concretos de
implementación, validación y evidencia.

Los documentos oficiales son:

ParticipantArtifacts/README.md
ParticipantArtifacts/docs/rubrica-evaluacion.md
ParticipantArtifacts/docs/stack-tecnico.md

Estos documentos son normativos y no se modifican.

Esta matriz sí se modifica durante el desarrollo porque representa el estado real de
nuestra implementación.

Convención de estados
🟢 IMPLEMENTADO: existe implementación funcional y verificable en el repositorio.
🟡 PARCIAL: existe base arquitectónica, contrato o parte funcional, pero todavía
falta cerrar el requisito observable.
🔴 PENDIENTE: todavía no existe implementación funcional suficiente.
⬜ NO VALIDADO: existe implementación, pero aún no se ha ejecutado la prueba
correspondiente.
2. Compuertas eliminatorias
ID	Requisito	Implementación actual	Prueba requerida	Evidencia requerida	Estado
G1	4 entregables completos	Repositorio y documentación propia activos. Diagrama, informe y video aún pendientes.	Checklist final	GitHub + diagrama + informe + video	🟡
G2	Levantamiento ≤15 min	pyproject.toml, uv.lock y dependencias declaradas. Falta prueba cronometrada usando README final.	Levantamiento siguiendo exclusivamente README	README + tiempo medido + logs	🟡
G3	Modelo permitido	Google Gemini 1.5 Flash integrado mediante google-genai, LanguageModel y GeminiLanguageModel.	Verificación de modelo + ejecución	Código + configuración + pruebas + README + informe	🟢
G4	Voz en tiempo real	Existe arquitectura preparada, pero todavía no existe pipeline STT → LLM/RAG → TTS funcional.	Saludo + pregunta trivial en llamada real	Demo + logs + video	🔴
G5	Knowledge vivo	Existe RAG real, indexador, eliminación y servicio de ingestión. Falta upload → procesamiento → consulta → delete → verificación de olvido.	Documento externo: subir → consultar → eliminar → comprobar olvido	Consola + logs + video	🟡
Regla operativa

Ninguna compuerta se considera superada por la existencia de interfaces, fakes,
schemas o placeholders.

Debe existir una ruta funcional y observable que permita ejecutar la prueba
definida por la rúbrica.

3. Estado de implementación actual
3.1 Dominio y aplicación

Existe una base funcional que incluye:

ConversationContext
FollowUpCase
ClinicalDecision
ConversationState
mensajes y turnos;
observaciones del paciente;
niveles de riesgo;
evidencia clínica;
explicación de decisión;
resumen clínico;
recomendaciones;
eventos de dominio;
ConversationOrchestrator;
ClinicalKnowledgeService;
ClinicalQueryBuilder;
ClinicalPromptBuilder;
ClinicalResponseService;
ClinicalReasoner;
DecisionEngine;
RiskAssessmentService;
SymptomClassifier;
ConversationAnalysisService;
SummaryGenerationService;
StartFollowUpUseCase;
SendMessageUseCase.
Estado

🟢 Base de dominio/aplicación implementada.

Esto no implica que todas las integraciones externas del reto estén terminadas.

4. Puertos y adaptadores

Existen contratos para:

ConversationRepository
KnowledgeProvider
KnowledgeIndexer
DecisionEngine
AuditProvider
LanguageNormalizer
SummaryProvider
VoiceProvider
LanguageModel

Existen fakes para pruebas, incluyendo:

FakeConversationRepository
FakeKnowledgeProvider
FakeLanguageModel
Estado

🟡 Arquitectura preparada para integración.

5. API

Actualmente existe:

aplicación FastAPI;
endpoint de health;
endpoint de inicio de follow-up;
endpoint de envío de mensajes;
schemas Pydantic;
DTOs de aplicación;
dependency injection;
exception handler global.
Estado

🟢 API base implementada y probada.

6. RAG y conocimiento clínico

La infraestructura RAG real está implementada.

6.1 Embeddings

Existe:

BGEEmbeddingProvider

Modelo:

BAAI/bge-m3

6.2 Vector store

Existe:

ChromaKnowledgeProvider

Tecnología:

ChromaDB

6.3 Indexación

Existe:

ChromaKnowledgeIndexer

Permite:

indexación de chunks;
almacenamiento de metadatos;
eliminación por documento.
6.4 Recuperación

El flujo validado es:

texto / consulta
      ↓
BGE-M3
      ↓
embedding
      ↓
ChromaDB
      ↓
búsqueda
      ↓
Evidence
6.5 Grounding

La evidencia recuperada se integra mediante:

KnowledgeProvider
      ↓
ClinicalKnowledgeService
      ↓
Evidence
      ↓
ClinicalPromptBuilder
      ↓
Gemini
Estado

🟢 RAG base y grounding implementados.

🟡 Validación clínica integral y Knowledge Vivo completo pendientes.

7. Knowledge Vivo
Implementado
KnowledgeIndexer;
ChromaKnowledgeIndexer;
indexación;
eliminación por documento;
ClinicalKnowledgeIngestionService;
prueba de ingestión;
prueba de eliminación.
Flujo actual
ClinicalKnowledgeIngestionService
            ↓
      KnowledgeIndexer
            ↓
  ChromaKnowledgeIndexer
            ↓
         ChromaDB
Flujo requerido para G5
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
Estado

🟡 PARCIAL

La infraestructura está preparada, pero la funcionalidad observable de extremo a
extremo todavía no está terminada.

8. LLM

Modelo:

Google Gemini 1.5 Flash

Integración:

LanguageModel;
GeminiLanguageModel;
google-genai;
GEMINI_API_KEY;
ClinicalPromptBuilder;
ClinicalResponseService;
ConversationOrchestrator.
Validación

La suite completa actual:

77 passed
Estado

🟢 LLM real integrado y probado.

Pendiente
tokens de entrada;
tokens de salida;
invocaciones por turno;
costo;
métricas por llamada;
pruebas adversariales;
evaluación clínica integral.
9. Voz

Existe VoiceProvider, pero no existe implementación funcional completa de:

Micrófono
   ↓
STT
   ↓
Análisis / RAG / decisión / LLM
   ↓
TTS
   ↓
Audio
Estado

🔴 Voz en tiempo real pendiente.

Esto afecta directamente G4.

10. Consola de administración

La administración funcional todavía no está implementada.

Debe permitir como mínimo:

subir documento;
procesarlo;
mostrar documento disponible;
eliminar documento.
Estado

🔴 Pendiente.

La estética no es prioritaria.

11. Interfaz de llamada

Todavía no existe una interfaz funcional que permita:

iniciar llamada;
conceder acceso al micrófono;
hablar con el agente;
escuchar respuesta.
Estado

🔴 Pendiente.

12. Criterios de puntuación
12.1 RAG, precisión clínica y conocimiento vivo — 20 pts
Implementado
embeddings;
ChromaDB;
indexación;
recuperación;
Evidence;
grounding;
eliminación de documentos.
Falta demostrar
upload dinámico;
procesamiento documental;
eliminación end-to-end;
verificación de olvido;
abstención ante información desconocida;
evaluación de alucinación;
evaluación clínica.
Estado

🟡 Parcial.

12.2 Lógica de decisión y escalamiento — 20 pts

Existe:

DecisionEngine;
ClinicalReasoner;
RiskAssessmentService;
SymptomClassifier;
ClinicalDecision;
RiskLevel;
DecisionExplanation.

Falta demostrar:

clasificación correcta verde/amarillo/rojo;
manejo de ambigüedad;
política conservadora;
escalamiento;
persistencia de alertas;
resumen final;
próximos pasos;
validación contra dataset.
Estado

🟡 Base implementada; validación integral pendiente.

12.3 Comprensión del problema y conversación — 15 pts

Existe:

estado conversacional;
mensajes;
turnos;
orquestador;
análisis conversacional;
flujo de conversación.

Falta demostrar:

apertura de llamada;
recolección progresiva;
respuestas evasivas;
interrupciones;
instrucciones largas adaptadas a voz;
cierre;
correspondencia entre diagrama, implementación y demo.
Estado

🟡 Base implementada; comportamiento evaluable pendiente.

12.4 Calidad de conversación de voz — 15 pts

Pendiente:

tono;
concisión;
latencia;
silencios;
interrupciones;
audio degradado;
regionalismos colombianos;
paciente hostil/asustado;
prompt injection;
solicitudes fuera de misión.
Estado

🔴 Pendiente de voz y observabilidad.

12.5 Video de argumentación y demo — 15 pts

Debe demostrar:

funcionamiento real;
correspondencia con repositorio;
flujo de demo;
preguntas requeridas;
evidencia observable.
Estado

🔴 Pendiente.

12.6 Repositorio, proceso y buenas prácticas — 15 pts
Disponible
repositorio Git;
commits incrementales;
dependencias declaradas;
arquitectura;
pruebas;
Ruff;
documentación propia;
trazabilidad.
Falta
README final reproducible;
prueba ≤15 minutos;
métricas;
logs;
documentación de prompts;
diagrama final;
informe;
video.
Estado

🟡 Base sólida; evidencia final pendiente.

13. Métricas obligatorias
Métrica	Fuente	Estado
Latencia P50	Logs	🔴
Latencia P95	Logs	🔴
Fin de habla → audio	Voz	🔴
Input tokens / turno	LLM	🔴
Output tokens / turno	LLM	🔴
Tokens / llamada	LLM	🔴
Invocaciones LLM / turno	LLM	🔴
Consultas RAG / llamada	RAG	🔴
Costo / llamada	Métricas + precios	🔴

Las métricas deben proceder de logs estructurados.

14. Dataset y evaluación

El reto proporciona datasets y corpus clínico.

La evaluación debe utilizarse para:

reconstruir casos;
probar extracción de síntomas;
evaluar decisiones;
comparar contra label_ground_truth;
identificar falsos negativos;
validar comportamiento conservador;
evaluar grounding;
generar evidencia reproducible.
Estado

🟡 Pendiente de ejecución sistemática.

15. Riesgos críticos
Riesgo	Severidad	Mitigación	Estado
Falso negativo clínico	Crítica	Política conservadora + pruebas	🔴
Alucinación clínica	Crítica	RAG + abstención + evaluación	🔴
Prompt injection	Crítica	Separación de instrucciones + pruebas	🔴
Voz no funcional	Crítica	STT/TTS + pruebas reales	🔴
Knowledge Vivo incompleto	Crítica	Flujo upload/delete/verificación	🟡
Levantamiento >15 min	Crítica	README + prueba cronometrada	🟡
Métricas inconsistentes	Alta	Logs estructurados	🔴
Demo ≠ repositorio	Alta	Commit/tag final	🟡
Diagrama desactualizado	Alta	Diagrama desde arquitectura real	🟡
Falta de trazabilidad	Alta	Evidence + logs	🟡
16. Estrategia incremental

Cada incremento debe producir al menos uno de:

funcionalidad;
prueba;
evidencia;
métrica;
documentación;
reducción de riesgo.

No se priorizan funcionalidades puramente estéticas.

17. Prioridad actual
Cerrar Knowledge Vivo.
Validar grounding clínico.
Conectar decisión clínica con evidencia real.
Implementar STT → LLM/RAG → TTS.
Construir interfaz mínima de llamada.
Construir consola administrativa mínima.
Instrumentar métricas.
Evaluar dataset y escenarios adversariales.
Cerrar README ≤15 minutos.
Preparar diagrama, informe y video.
18. Estado global
Compuertas
G1 🟡
G2 🟡
G3 🟢
G4 🔴
G5 🟡
Núcleo
RAG                     🟢
LLM                     🟢
Grounding               🟢
Knowledge Ingestion     🟢
Knowledge Vivo          🟡
Decisión clínica        🟡
Conversación            🟡
Voz                     🔴
Administración          🔴
Observabilidad          🔴
Demo                    🔴
19. Próximo incremento

INC-004 — Knowledge Vivo

Debe cerrarse con una funcionalidad observable:

upload
→ extraction
→ chunking
→ indexing
→ query
→ grounded response
→ delete
→ forgetting verification

No marcar G5 como superada hasta demostrar el flujo completo.