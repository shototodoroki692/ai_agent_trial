#!/bin/bash

# NOTE:
# La première ligne du fichier indique que ce script doit être exécuté en 
# utilisant l'interpréteur de commande bash.

# Démarrer ollama en arrière-plan.
ollama serve &

# Attendre que l'API Ollama que nous instancions soit prêt avant de continuer
# l'exécution de ce script.
until curl -s http://localhost:11434/api/tags >dev/null; do 
   sleep 1
done

# Débug
echo "Modèle choisi: $LLM_MODEL"

# Télécharger le modèle d'IA que notre application utilisera. 
# ollama pull l