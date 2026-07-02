#!/bin/bash

# NOTE:
# La première ligne du fichier indique que ce script doit être exécuté en 
# utilisant l'interpréteur de commande bash.

# Démarrer ollama en arrière-plan.
ollama serve &

# Attendre que Ollama soit lancé avant de continuer l'exécution de ce script.
until ollama list >/dev/null 2>&1; do 
   sleep 1
done

# Débug
echo "Modèle choisi: $LLM_MODEL"

# Télécharger le modèle d'IA que notre application utilisera. 
# ollama pull l