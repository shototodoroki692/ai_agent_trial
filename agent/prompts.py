from langchain_core.prompts import PromptTemplate

# WEB_SEARCH_PROMPT_INSTRUCTION définit le format du prompt qui sera utilisé
# pour demander au LLM de générer des requêtes sur le web concernant une
# demande.
WEB_SEARCH_INSTRUCTIONS="""
   Rédige moi {search_query_number} recherches web me permettant de recueillir
   autant d'informations que possible pour répondre à la question suivante:
   {user_question}

   Le contenu récupéré suite aux recherches web dont tu auras formulé les
   requêtes doit dans un premier temps permettre de ressembler des
   informations nécessaires à la réponse à la question ci-dessus.
"""

# WEB_SEARCH_PROMPT_TEMPLATE définit la template du prompt qui sera utilisé
# pour demander au LLM de générer des requête sur le web concernant une 
# demande.
WEB_SEARCH_PROMPT_TEMPLATE=PromptTemplate.from_template(
   template=WEB_SEARCH_INSTRUCTIONS
)