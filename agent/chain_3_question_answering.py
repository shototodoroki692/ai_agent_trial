import os
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from llm import get_llm
from prompts import RESEARCH_REPORT_PROMPT_TEMPLATE

# Chaîne permettant de répondre à une question en ayant le résumé de chaque
# plusieurs recherches effectuées sur le web.
#
# Input: Liste de dictionnaires {"search_query", "summary"}
# Output: Réponse à la question de l'utilisateur.
question_answering_chain = (
   RunnableLambda(lambda x:
      {
         'user_question': os.getenv("USER_QUESTION"),
         'research_summary': '\n\n'.join(web_search_result['summary'] for web_search_result in x)
      }
   )
   | RESEARCH_REPORT_PROMPT_TEMPLATE 
   | get_llm()
   | StrOutputParser()
)