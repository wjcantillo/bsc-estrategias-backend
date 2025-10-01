# Backend BSC Estrategias con IA

Este backend expone una API REST usando FastAPI y el modelo `google/flan-t5-base` de HuggingFace para generar estrategias organizacionales.

## Endpoint principal
POST /generar_estrategia

### Ejemplo de request
{
  "objetivo": "Mejorar la satisfacción del cliente",
  "iniciativa": "Capacitación del personal de servicio"
}

### Ejemplo de response
{
  "estrategia": "Implementar un programa de formación continua..."
}