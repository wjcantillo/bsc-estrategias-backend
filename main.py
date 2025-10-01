from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

# Inicializar modelo HuggingFace
generator = pipeline("text2text-generation", model="google/flan-t5-nano")

# Inicializar FastAPI
app = FastAPI()

# Permitir CORS para todas las apps frontend (ej. Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para solicitud
class EstrategiaRequest(BaseModel):
    objetivo: str
    iniciativa: str

# Ruta principal
@app.post("/generar_estrategia")
def generar_estrategia(data: EstrategiaRequest):
    prompt = (
        f"Eres un experto en planeación estratégica.\n"
        f"Objetivo: {data.objetivo}\n"
        f"Iniciativa: {data.iniciativa}\n"
        f"Redacta una estrategia clara que relacione la iniciativa con el cumplimiento del objetivo."
    )
    result = generator(prompt, max_length=256, do_sample=True, temperature=0.7)
    return {"estrategia": result[0]["generated_text"]}
