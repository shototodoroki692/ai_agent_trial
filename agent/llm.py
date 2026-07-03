import os
from langchain_ollama import ChatOllama
from prompts import WEB_SEARCH_PROMPT_TEMPLATE

# Récupérer le nom de modèle que nous allons utiliser.
#
# NOTE:
# Les variables d'environnement sont chargées lors de l'exécution du script
# principal (main.py).
model_name = os.getenv("LLM_MODEL")

print(f"Modèle utilisé: {model_name}")

# Instanciation de notre LLM avec Ollama.
llm = ChatOllama(
   model=model_name,
   temperature=0,
)

# Nombre recherches à effectuer sur le web.
SEARCH_QUERY_NUMBER=2

# Chaîne renvoyant une liste de recherches à effectuer sur le web selon une
# question posée par l'utilisateur.
prompt = WEB_SEARCH_PROMPT_TEMPLATE.format(
   search_query_number=SEARCH_QUERY_NUMBER,
   # user_question= 
)
