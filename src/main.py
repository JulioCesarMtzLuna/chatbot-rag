from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from .generate_answer import Generator
from pydantic import BaseModel
import os
from src.utils.read_file import read_file
from src.utils.create_dataset import create_dataset
from .document_indexing import create_index
from dotenv import load_dotenv

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    document_url = os.path.join(os.path.dirname(__file__), 'data', os.getenv("DOCUMENT_PATH"))
    global document_info
    document_info = read_file(document_url)
    dataset = create_dataset(document_info)
    create_index(dataset)
    global answer_generator
    answer_generator = Generator(dataset)
    yield


app = FastAPI(lifespan=lifespan)

class Question(BaseModel):
    question: str

@app.post("/question")
async def ask_for_document(question: Question):
    if not question.question:
            raise HTTPException(status_code=400, detail="La pregunta es un parámetro obligatorio.")
    context = "El contenido del documento cargado es el siguiente: " + document_info
    answer = await answer_generator.generate_answer(context, question.question)
    return answer