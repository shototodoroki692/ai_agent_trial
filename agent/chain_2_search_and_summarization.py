from llm import get_llm
from prompts import WEB_PAGE_CONTENT_SUMMARY_PROMPT_TEMPLATE
from web_scraping import web_scrape
from web_searching import web_search
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

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

# Chaîne permettant d'effectuer des recherches sur les pages web correspondant aux URLs fournies
# en entrée, et de résumer chacune de ces dernières.
#
# Input: Dictionnaire de type {'search_query', 'url'}
# Output: Dictionnaire de type {'search_query', 'summary'}
scrape_url_and_summarization_chain = (
   RunnableLambda(lambda x:
      {
         'search_query': x['search_query'],
         'url': x['url'],
         'web_page_content': web_scrape(x['url']),   
      }
   )
   # RunnableParallel permet d'effectuer les actions qu'il contient en parallèle.
   | RunnableParallel(
      {
         'search_query': lambda x: x['search_query'],
         'summary': WEB_PAGE_CONTENT_SUMMARY_PROMPT_TEMPLATE | get_llm() | StrOutputParser(),
      }
   )
)

# Chaîne permettant de récupérer une liste de résumés de pages web pour une
# recherche donnée.
#
# Input: Recherche à effectuer sur le web.
# Output: Chaîne de caractère contenant les résumés concaténés des pages web
# pour cette recherche.
search_and_summarization_chain = (
   get_urls_chain
   | scrape_url_and_summarization_chain.map() # Parallèliser l'action pour chaque URL.
   | RunnableLambda(lambda x:
      {
         'search_query': x[0]['search_query'] if len(x) > 0 else '',
         'summary': '\n'.join([i['summary'] for i in x])
      }
   )
)

# # Test.
# result = search_and_summarization_chain.invoke("Désiré Doué")
# print(f"Résumé des recherches sur le GOAT:\n\n{result}")