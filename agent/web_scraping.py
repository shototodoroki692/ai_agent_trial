import requests
from bs4 import BeautifulSoup

# web_scrape permet de récupérer le contenu d'une page web identifiée par son
# URL, sous forme de texte (string).
def web_scrape(url: str) -> str:
   try:
      # Ajout des headers pour simuler l'envoi de la requête depuis un
      # navigateur.
      headers = {
         "User-Agent": (
            "Mozilla/5.0 (X11, Linux x86_64)"
            "AppleWebKit/537.36 (KHTML, like Gecko)" 
            "Chrome/149.0.0.0 Safari/537.36"
         ),
         "Accept-Language": "en-US,en;q=0.6"
      }

      response = requests.get(url, headers=headers, timeout=15)

      # Si la réponse à notre requête pour récupérer le contenu de la page
      # est de status 200, renvoyer le contenu de la page sous forme de texte.
      if response.status_code == 200:
         soup = BeautifulSoup(response.text, "html.parser")

         page_content = soup.get_text(separator=" ", strip=True)
         return page_content

      else:
         return f"Impossible de récupérer la page web: status code {response.status_code}"

   except Exception as e:
      print(e)
      return f"Impossible de récupérer la page web. Exception: {e}"

