# TODO:
# Créer un script basic appelant notre LLM local pour voir si ça fonctionne.

import os
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

# Charger les variables d'environnement.
load_dotenv()

# Récupérer le nom de modèle que nous allons utiliser.
model_name = os.getenv("LLM_MODEL")

print(f"Modèle utilisé: {model_name}")

llm = ChatOllama(
   model=model_name,
   temperature=0,
)

# Échanger avec le LLM tant que l'utilisateur ne saisie pas "quit".
while True:
   user_input = input("you > ")

   if user_input == "quit":
      break

   llm_response = llm.invoke(user_input)

   print(f"llm > {llm_response.content}")

print("Merci pour la conversation :)")