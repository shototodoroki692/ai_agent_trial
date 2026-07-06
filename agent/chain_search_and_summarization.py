from web_searching import web_search
from langchain_core.runnables import RunnableLambda

# Nombre de résultats de recherche à garder par recherche.
RESULT_BY_QUERY_NUMBER=3

# Chaîne permettant de récupérer les URLs pour une recherche sur le web.
#
# Input: Recherche web.
# Output: Liste d'URL à consulter.
get_urls_chain = (
   RunnableLambda(lambda search_query:
      [
         {
            'search_query': search_query,
            'url': url 
         } 
         for url in web_search(search_query, RESULT_BY_QUERY_NUMBER)
      ]
   )
)

# Test.
urls = get_urls_chain.invoke("Désiré Doué")
print(f"urls trouvées:\n{urls}")