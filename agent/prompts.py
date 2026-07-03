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

# WEB_PAGE_CONTENT_SUMMARY_INSTRUCTION définit le format du prompt permettant 
# résumer le contenu d'une page web.
WEB_PAGE_CONTENT_SUMMARY_INSTRUCTIONS="""
   Lis le texte suivant.
   Texte: {web_page_content}

   ----------

   D'après le texte ci-dessus, réponds de manière très concise à la question suivante.
   Question: {search_query}

   Si tu ne peux pas répondre à la question suivante, alors résume le texte de manière très concise.
"""

# WEB_PAGE_CONTENT_SUMMARY_PROMPT_TEMPLATE définit la template du prompt qui sera utilisé
# pour demander au LLM de générer le résumé du contenu d'une page web.
WEB_PAGE_CONTENT_SUMMARY_PROMPT_TEMPLATE = PromptTemplate.from_template(
   template=WEB_PAGE_CONTENT_SUMMARY_INSTRUCTIONS
)

# REASEARCH_REPORT_PROMPT_TEMPLATE définit le template du prompt permettant 
# de répondre à la question initiale posée par l'utilisateur avec le résumé 
# des recherches effectuées.
RESEARCH_REPORT_PROMPT_TEMPLATE = PromptTemplate.from_template(
   template="""
      Tu disposes d'un résumé d'informations issue de différentes sources. Les informations
      que tu as à ta disposition sont les suivantes.
      Informations: {research_summary}

      ----------

      À partir des informations qui te sont fournies ci-dessus, tu dois répondre de manière très concise 
      à la question qui suit.
      Question: {user_question}
   """
)