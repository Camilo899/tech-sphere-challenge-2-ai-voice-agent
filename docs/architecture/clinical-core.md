# Clinical Core

The Clinical Core is the heart of the application.

Every external technology communicates with this module.

```
Voice
      │
LLM
      │
RAG
      │
Database
      │
      ▼
+----------------------+
|    Clinical Core     |
+----------------------+
```

The Clinical Core never depends on external providers.

External providers depend on the Clinical Core contracts.