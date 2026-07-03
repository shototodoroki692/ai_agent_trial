# TODO:
# Créer un script basic appelant notre LLM local pour voir si ça fonctionne.

import os
from models import WebSearchQueryGenerationOutput
from prompts import (
   WEB_SEARCH_PROMPT_TEMPLATE,
   WEB_PAGE_CONTENT_SUMMARY_PROMPT_TEMPLATE,
   RESEARCH_REPORT_PROMPT_TEMPLATE
)
from web_searching import web_search
from web_scraping import web_scrape
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

# Charger les variables d'environnement.
load_dotenv()

# Récupérer le nom de modèle que nous allons utiliser.
model_name = os.getenv("LLM_MODEL")

print(f"Modèle utilisé: {model_name}")

base_llm = ChatOllama(
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

   llm = base_llm.with_structured_output(
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

   # Liste des pages web à consulter, rattachées à la recherche associée.
   web_pages = []

   # Pour chaque requête formulée, effectuer la recherche sur le web.
   for i, query in enumerate(web_queries_list):
      urls = web_search(query, RESULT_BY_QUERY_NUMBER)

      # print(f"\nURLs à consulter pour la recherche n°{i+1}:")
      for y, url in enumerate(urls):

         # Ajouter l'url et la recherche associée à la liste des pages web
         # à consulter.
         web_pages.append({
            "search_query": query,
            "url": url
         })

         # Récupérer le contenu de la page web rattachée à l'URL:
         # page_content = web_scrape(url)

   # Pour chaque URL de notre liste, y ajouter le contenu de la page.
   # print("\nContenu utilisé pour répondre à la question:\n\n")
   for i, page in enumerate(web_pages):
      page["content"] = web_scrape(page["url"])

      # # débug:
      # print(f"...........PAGE WEB N°{i+1}...........\n")
      # print(f"Recherche: {page["search_query"]}\n\nURL: {page["url"]}\n\nContenu de la page:\n{page["content"]}\n\n\n")

   # Résumer le contenu de chaque page web consulter et l'ajouter à la liste des
   # résumés.
   for i, page in enumerate(web_pages):
      prompt = WEB_PAGE_CONTENT_SUMMARY_PROMPT_TEMPLATE.format(
         web_page_content=page["content"],
         search_query=page["search_query"]
      )

      llm_response = base_llm.invoke(prompt)

      # # débug:
      # print(f"Résumé n°{i+1}:\n{llm_response.content}")

      page["content_summary"] = llm_response.content

   # Stringifier la liste des résumés.
   stringified_summaries = [
      f'URL: {page["url"]}\nRésumé: {page["content_summary"]}' for page in web_pages
   ]

   # Définir la liste des résumés comme étant une seule chaîne de caractères.
   appended_stringified_summaries = '\n'.join(stringified_summaries)

   # débug:
   print(f"Pages web résumées:\n{appended_stringified_summaries}")

   prompt = RESEARCH_REPORT_PROMPT_TEMPLATE.format(
      research_summary=appended_stringified_summaries,
      user_question=user_input
   )

   # Envoi de la liste des résumés au LLM pour obtenir la réponse finale à
   # la question de l'utilisateur.
   final_response = base_llm.invoke(prompt)

   print(f"Réponse à votre question:\n", final_response.content)

print("C'est la fin du programme :)")