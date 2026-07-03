from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from typing import List

# web_search permet d'effectuer une requête sur internet en fournissant la requête
# et le nombre de résultats que nous attendons. Les résultats sont renvoyés sous
# forme de liste d'URL de site web, résultants de la recherche.
def web_search(web_query: str, num_results: int) -> List[str]:
   # Renvoyer les liens (URL) des resultats des recherches sur le web dans une liste.
   return [result["link"] for result in DuckDuckGoSearchAPIWrapper().results(web_query, num_results)]