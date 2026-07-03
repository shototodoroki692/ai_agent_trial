# TODO:
# Créer un script basic appelant notre LLM local pour voir si ça fonctionne.

import os
from models import WebSearchQueryGenerationOutput
from prompts import WEB_SEARCH_PROMPT_TEMPLATE
from web_searching import web_search
from web_scraping import web_scrape
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

SEARCH_QUERY_NUMBER=2
RESULT_BY_QUERY_NUMBER=3

while True:
   print("\n\n------------------------------------")
   user_input = input("Recherche web > ")

   # Quitter la boucle si l'utilisateur saisi "quit".
   if user_input == "quit":
      break

   # print("\nRésultat des recherches:")
   # for result in web_searching.web_search(user_input, 5):
   #    print(result) 
   # Nombre recherches à effectuer sur le web.

   # Chaîne renvoyant une liste de recherches à effectuer sur le web selon une
   # question posée par l'utilisateur.
   prompt = WEB_SEARCH_PROMPT_TEMPLATE.format(
      search_query_number=SEARCH_QUERY_NUMBER,
      user_question=user_input
   )

   llm = llm.with_structured_output(
      schema=WebSearchQueryGenerationOutput,
      strict=True,
      include_raw=True # Permet d'obtenir des détails liés à l'invocation du modèle.
   )

   llm_response = llm.invoke(prompt)
   response_content: WebSearchQueryGenerationOutput = llm_response['parsed']
   web_queries_list = response_content.list

   # Débug
   print("\nRecherches à effectuer sur le web:\n")
   for i, query in enumerate(web_queries_list):
      print(f"{i+1}: {query}")

   # Pour chaque requête formulée, effectuer la recherche sur le web.
   for i, query in enumerate(web_queries_list):
      urls = web_search(query, RESULT_BY_QUERY_NUMBER)

      print(f"\nURLs à consulter pour la recherche n°{i+1}:")
      for y, url in enumerate(urls):
         print(f"\t{y+1}: {url}")

         # Récupérer le contenu de la page web rattachée à l'URL:
         page_content = web_scrape(url)

print("C'est la fin du programme :)")