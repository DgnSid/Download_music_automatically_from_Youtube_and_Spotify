import os
import glob

def renommer_fichiers_audio_avance(dossier, prefixe="", start=109):
    """
    Renomme tous les fichiers audio d'un dossier de start à N
    avec un préfixe optionnel.

    Args:
        dossier (str): chemin du dossier contenant les fichiers audio
        prefixe (str): préfixe optionnel placé avant le numéro
        start (int): numéro de départ (par défaut 109)
    """
    # Extensions de fichiers audio courantes
    extensions_audio = ['*.mp3', '*.wav', '*.flac', '*.aac', '*.ogg', '*.m4a', '*.wma']
    
    # Récupérer tous les fichiers audio
    fichiers_audio = []
    for extension in extensions_audio:
        fichiers_audio.extend(glob.glob(os.path.join(dossier, extension)))
    
    # Trier les fichiers par nom
    fichiers_audio.sort()
    
    print(f"Fichiers audio trouvés : {len(fichiers_audio)}")
    
    # Afficher la liste avant renommage
    print("\nAvant renommage :")
    for fichier in fichiers_audio:
        print(f"  - {os.path.basename(fichier)}")
    
    # Demander confirmation
    reponse = input(f"\nVoulez-vous renommer ces {len(fichiers_audio)} fichiers ? (o/n) : ")
    if reponse.lower() != 'o':
        print("Opération annulée.")
        return
    
    # Renommer les fichiers
    for i, fichier in enumerate(fichiers_audio, start):
        # Obtenir l'extension du fichier
        _, extension = os.path.splitext(fichier)
        
        # Nouveau nom de fichier
        if prefixe:
            nouveau_nom = os.path.join(dossier, f"{prefixe}{i}{extension}")
        else:
            nouveau_nom = os.path.join(dossier, f"{i}{extension}")
        
        # Renommer le fichier
        os.rename(fichier, nouveau_nom)
        print(f"Renommé: {os.path.basename(fichier)} -> {os.path.basename(nouveau_nom)}")
    
    print(f"\nTerminé ! {len(fichiers_audio)} fichiers renommés.")

# Utilisation
if __name__ == "__main__":
    # Demander le chemin du dossier
    dossier = input("Entrez le chemin du dossier (laisser vide pour le dossier courant) : ").strip()
    if not dossier:
        dossier = "."
    
    # Demander un préfixe optionnel
    prefixe = input("Entrez un préfixe optionnel (laisser vide si aucun) : ").strip()
    # Demander le numéro de départ (par défaut 109)
    numero_depart_input = input("Entrez le numéro de départ (laisser vide pour 109) : ").strip()
    try:
        numero_depart = int(numero_depart_input) if numero_depart_input else 109
    except ValueError:
        print("Entrée invalide pour le numéro de départ ; utilisation de 109.")
        numero_depart = 192

    if not os.path.exists(dossier):
        print("Le dossier spécifié n'existe pas.")
    else:
        renommer_fichiers_audio_avance(dossier, prefixe, start=numero_depart)