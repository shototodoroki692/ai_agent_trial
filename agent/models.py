from typing import List
from pydantic import BaseModel

# WebSearchQueryGenerationOutput définit le schéma de sortie du modèle générant des 
# requêtes web. À savoir une liste de requêtes au format string.
class WebSearchQueryGenerationOutput(BaseModel):
   list: List[str]