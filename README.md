# Exercice 2 : Tester l'API sans SDK

Il s'agit d'un programme interactif en ligne de commande permettant de tester l'API de RodiumAi sans SDK, via des requêtes.

## Fonctionnalités : 03 actions

- **Étape 1 (Chat) :** Envoi d'une question à un modèle textuel (`openai/gpt-4o-mini`) et affichage du coût en RODI.
- **Étape 2 (Image) :** Génération d'une image à partir d'une description textuelle et sauvegarde au format PNG.
- **Étape 3 (Vidéo) :** Génération d'une courte vidéo animée à partir d'un prompt et sauvegarde au format MP4.

## Installation
Pour installer et exécuter ce projet, vous devez disposer de **Python 3.10** (ou une version supérieure).

1. Installez les dépendances nécessaires :
     pip install -r requirements.txt
   
## Configuration
1. Copiez le fichier d'exemple pour créer votre environnement privé :
   
   cp .env.example .env
  
2. Ouvrez le fichier `.env` et ajoutez votre clé API secrète :
  
   RODIUMAI_API_KEY=votre_cle_ici
   
## Lancement
Pour démarrer le script interactif, exécutez la commande suivante dans votre terminal :

python3 main.py

