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