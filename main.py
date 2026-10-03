import os
import base64
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement du fichier .env
load_dotenv()
api_key = os.getenv("RODIUMAI_API_KEY")

# L'en-tête Authorization 
headers = {
    "Authorization": f"Bearer {api_key.strip() if api_key else ''}",
    "Content-Type": "application/json"
}

etape = 1
print("=== SCRIPT INTERACTIF RODIUMAI ===")

if not api_key:
    print(" Erreur : Impossible de lire la clé API. Vérifiez votre fichier .env")
    etape = 4 

while 1 <= etape <= 3:

    # ÉTAPE 1 : CHAT
    
    if etape == 1:
        print("\n=== Étape 1 : Chat ===")
        votre_question = input("Votre question : ")
        
        donnees_chat = {
            "model": "openai/gpt-4o-mini",
            "messages": [{"role": "user", "content": votre_question}],
            "temperature": 0.7
        }
        
        print("Envoi de la question...")
        try:
            reponse = requests.post("https://api.rodiumai.io/v1/chat/completions", headers=headers, json=donnees_chat)
            
            if reponse.status_code == 200:
                resultat = reponse.json()
                choices = resultat.get("choices", [])
                
                if choices and isinstance(choices, list):
                    texte_reponse = choices[0].get("message", {}).get("content", "Pas de contenu")
                else:
                    texte_reponse = "Structure de réponse inconnue."
                    
                cout_rodi = resultat.get("cost_rodi") or resultat.get("usage", {}).get("total_tokens", "Non spécifié")
                print(f"\n[réponse du modèle]\n{texte_reponse}")
                print(f"Coût : {cout_rodi} RODI")
            else:
                print(f" Erreur de chat. Statut HTTP : {reponse.status_code}")
        except Exception as e:
            print(f" Erreur : {e}")
        
        print("")
        choix = input("Rester (r) ou passer à la suivante (s) ? ").lower()
        if choix == 's': etape = 2

    # ÉTAPE 2 : IMAGE
    
    elif etape == 2:
        print("\n=== Étape 2 : Image ===")
        description_image = input("Décrivez l'image : ")
        
        donnees_image = {
            "model": "google/gemini-3.1-flash-image",
            "prompt": description_image,
            "n": 1,
            "size": "1024x1536",
            "quality": "medium"
        }
        
        print("Génération de l'image, patientez...")
        try:
            reponse = requests.post("https://api.rodiumai.io/v1/images/generations", headers=headers, json=donnees_image)
            
            if reponse.status_code == 200:
                resultat = reponse.json()
                liste_data = resultat.get("data", [])
                
                if liste_data and isinstance(liste_data, list):
                    base64_data = liste_data[0].get("b64_json")
                    with open("image.png", "wb") as f:
                        f.write(base64.b64decode(base64_data))
                    print(" Image enregistrée avec succès : image.png")
                else:
                    print(" Erreur : Données d'image introuvables.")
            else:
                print(f" Erreur image. Statut HTTP : {reponse.status_code}")
        except Exception as e:
            print(f" Erreur : {e}")
            
        print("")
        choix = input("Revenir (b), rester (r) ou passer à la suivante (s) ? ").lower()
        if choix == 'b': etape = 1
        elif choix == 's': etape = 3

    
    # ÉTAPE 3 : VIDÉO
   
    elif etape == 3:
        print("\n=== Étape 3 : Vidéo ===")
        description_video = input("Décrivez la vidéo : ")
        
        donnees_video = {
            "model": "google/veo-3.1-fast",
            "prompt": description_video,
            "duration_seconds": 2,
            "aspect_ratio": "9:16"
        }
        
        print("Génération de la vidéo, patientez...")
        try:
            reponse = requests.post("https://api.rodiumai.io/v1/videos/generations", headers=headers, json=donnees_video, timeout=600)
            
            if reponse.status_code == 200:
                resultat = reponse.json()
                liste_video = resultat.get("data", [])
                
                if liste_video and isinstance(liste_video, list):
                    base64_video = liste_video.get("b64_json") if isinstance(liste_video, dict) else (liste_video[0].get("b64_json") if liste_video else None)
                    with open("video.mp4", "wb") as f:
                        f.write(base64.b64decode(base64_video))
                    print(" Vidéo enregistrée avec succès : video.mp4")
                else:
                    print(" Erreur : Données vidéo introuvables.")
            else:
                print(f" Erreur vidéo. Statut HTTP : {reponse.status_code}")
        except requests.exceptions.Timeout:
            print("\n Erreur : Le délai d'attente maximum a été dépassé.")
        except Exception as e:
            print(f" Erreur : {e}")
            
        print("")
        choix = input("Revenir (b), rester (r) ou quitter (q) ? ").lower()
        if choix == 'b': etape = 2
        elif choix == 'q': 
            print("\nFin du programme. Bye !")
            break
