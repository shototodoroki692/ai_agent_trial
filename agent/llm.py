import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from prompts import WEB_SEARCH_PROMPT_TEMPLATE

# Charger les variables d'environnement.
load_dotenv()

# Récupérer le nom de modèle que nous allons utiliser.
model_name = os.getenv("LLM_MODEL")

# get_llm retourne une instance d'un LLM disponible avec Ollama.
def get_llm():
   return ChatOllama(
      model=model_name,
      temperature=0,
   )