# Tech Sphere Challenge 2 - Clinical AI Voice Agent

## 📌 Overview
Este proyecto implementa un **Agente Clínico con Voz y Conocimiento Vivo (PMV)**.  
Objetivos principales:
- Validar ingestión y olvido de conocimiento clínico (G5).
- Mantener conversaciones clínicas estructuradas (G3).
- Integrar voz en tiempo real con STT → Gemini → TTS (G4).
- Entregar documentación reproducible y demo observable.

---

## 🏗️ Architecture
![Diagrama de Arquitectura](docs/ARCHITECTURE.png)

Flujos principales:
- **Conocimiento (G5):** ingestión y olvido validados en pruebas.  
- **Conversación clínica (G3):** `/follow-up/start` → `/messages`.  
- **Voz (G4):** `/messages/voice` con pipeline STT/TTS.  
- **Health:** `/health` y `/health/error`.

---

## 📂 Project Structure

clinical-ai-voice-agent/
├── apps/api/                # Código fuente FastAPI
├── tests/                   # Suite de pruebas (82 tests)
├── docs/                    # Documentación y entregables
│   ├── FINAL_REPORT.pdf     # Informe técnico
│   ├── ARCHITECTURE.png     # Diagrama de arquitectura
│   └── DELIVERY_NOTES.md    # Resumen de entrega
└── README.md                # Este archivo


---

## ⚙️ Installation
```bash
git clone https://github.com/Camilo899/tech-sphere-challenge-2-ai-voice-agent.git
cd tech-sphere-challenge-2-ai-voice-agent
uv sync

## 🚀 Usage
Levantar la API:
```bash
uv run uvicorn app.main:app --reload
URL: http://127.0.0.1:8000

Endpoints disponibles:

POST /follow-up/start

json
{ "patient_id": "12345", "context": "Hipertensión arterial controlada" }
POST /messages

json
{ "conversation_id": "abcde-12345", "message": "El paciente reporta dolor de cabeza persistente." }
POST /messages/voice

json
{ "conversation_id": "abcde-12345", "audio": "<base64>" }
GET /health

json
{ "status": "ok" }
🛠️ Development
Lenguaje: Python 3.11

Framework: FastAPI

Dependencias: uv, pytest, mypy

✅ Testing
Ejecutar pruebas:

bash
uv run pytest -q
→ 82/82 tests en verde

Validar tipado:

bash
uv run mypy app
→ Success: no issues found

📹 Demo
Video Demo: https://drive.google.com/file/d/1K1FppL0JCVYcBVLIr6LsmzkoHT9ZGagA/view?usp=sharing

Informe Final:PDF

Diagrama PDF

📦 Deployment
El proyecto puede desplegarse en cualquier entorno con Python ≥3.11.
Se recomienda usar contenedores Docker para producción.

📜 License
MIT License