import json
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from prompts import WEB_SEARCH_PROMPT_TEMPLATE
from llm import get_llm
from models import WebSearchQueryGenerationOutput

SEARCH_QUERY_NUMBER=2

# Configurer une instance de notre LLM pour fournir une réponse au format attendu.
llm = get_llm()
llm = llm.with_structured_output(
   schema=WebSearchQueryGenerationOutput,
   strict=True
)

# web_search_chain permet de récupérer une liste de recherches à effectuer
# sur le web pour obtenir des informations quant à la question fournie en
# entrée.
#
# Input: Question utilisateur.
# Output: Liste de recherches à effectuer sur le web.
web_search_chain = (
   RunnableLambda(lambda user_input:
      {
         "search_query_number": SEARCH_QUERY_NUMBER,
         "user_question": user_input
      }
   )
   | WEB_SEARCH_PROMPT_TEMPLATE
   | llm 
   | RunnableLambda(lambda output: output.list) # Renvoyer directement le contenu de la liste.
)

# # Test:
# search_queries = web_search_chain.invoke("Qui est Désiré Doué ?")
# print(f"Résultat de la chaîne:\n{search_queries}")