from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers_agents import Agents

# REST framework class instantiation
app = FastAPI()

# Transformers agents class instantiation
agent = Agents()

# Adding cors validation 
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model to receive data via JSON
class TranslationRequest(BaseModel):
    origin_text: str
    origin_lang: str
    dest_lang: str

# Model to receive data via JSON
class GenereteTextResquest(BaseModel):
    inputed_text: str

@app.post("/translate")
def translate(request: TranslationRequest):
    """
    Endpoint to translate the provided text in the input JSON.

    :param request: Data provided for translation (text, source language, and target language)
    :return: Translated text
    """
    try: 
        return {"translated_text": agent.translate_text(request.origin_text, request.origin_lang, request.dest_lang)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/gen_text")
def gen_text(request: TranslationRequest):
    """
    Endpoint to do a text input using JSON.

    :param request: sume text
    :return: generated text
    """
    try:
        return {"agent_response": agent.generate_text(request.inputed_text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    """
    Root endpoint to test the API.
    """
    return {"message": "Translation API is working!"}
