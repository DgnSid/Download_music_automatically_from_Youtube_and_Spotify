# Download_music_automatically_from_Youtube_and_Spotify
Un script python qui vous permet de télécharger automatiquement vos musiques préférés depuis Youtube et Spotify
Voici la documentation GitHub en markdown pour votre projet :

# Spotify Music Downloader 🎵

Un script Python automatisé pour télécharger de la musique à partir de playlists Spotify en utilisant YouTube comme source.

## ✨ Fonctionnalités

- 📥 Téléchargement automatique de playlists Spotify complètes
- 🎧 Conversion en fichiers MP3 de qualité
- 🔍 Recherche intelligente sur YouTube
- 🎯 Interface menu interactive
- 📁 Gestion des métadonnées audio
- 🔄 Support multiple : playlists, singles, listes personnalisées

## 🛠️ Technologies Utilisées

### Bibliothèques Python
- **`yt-dlp`** - Téléchargement et extraction audio depuis YouTube
- **`spotipy`** - Interface avec l'API Spotify officielle
- **`youtube-search-python`** - Recherche de vidéos sur YouTube
- **`FFmpeg`** - Conversion et traitement audio

### APIs et Services
- **Spotify Web API** - Récupération des métadonnées musicales
- **YouTube** - Source des fichiers audio

## 📦 Installation

### Prérequis
- Python 3.7+
- FFmpeg installé sur le système
- Compte développeur Spotify

### Installation des dépendances
```bash
pip install yt-dlp spotipy youtube-search-python
```

### Configuration Spotify
1. Créer une application sur [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Récupérer le `CLIENT_ID` et `CLIENT_SECRET`
3. Configurer les variables d'environnement :
```bash
export SPOTIFY_CLIENT_ID="votre_client_id"
export SPOTIFY_CLIENT_SECRET="votre_client_secret"
```

## 🚀 Utilisation

```bash
python3 download.py
```

### Options du menu :
1. **Télécharger depuis une playlist Spotify**
2. **Télécharger depuis une playlist YouTube**
3. **Télécharger depuis une liste de chansons**
4. **Télécharger une chanson (recherche)**
5. **Télécharger une chanson (lien direct)**
6. **Aide**

## 🎯 Fonctionnement

Le script fonctionne en 3 étapes :

1. **Récupération des métadonnées** via l'API Spotify
2. **Recherche automatique** sur YouTube des correspondances
3. **Téléchargement et conversion** en MP3 avec métadonnées

## ⚠️ Important

- Usage strictement personnel uniquement
- Respectez les droits d'auteur
- Les credentials Spotify ne doivent pas être partagés
- Régénérez vos clés API si compromises

## 📝 Structure du Projet

```
spotify-downloader/
├── download.py          # Script principal
├── requirements.txt     # Dépendances Python
└── README.md           # Documentation
```

## 🐛 Résolution de Problèmes

### Erreur d'import
```bash
pip install --upgrade yt-dlp spotipy
```

### Problème audio
Vérifiez que FFmpeg est installé et accessible dans le PATH.

## 👨‍💻 Auteur

**Sid DEGUENON**

[🔗 Voir mon GitHub](https://github.com/DgnSid)

