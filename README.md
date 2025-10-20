# I. Download Musics Automatically from YouTube and Spotify and rename all of them

A Python script that allows you to automatically download your favorite music from YouTube and Spotify.

# Spotify Music Downloader 🎵 (File download.py )

An automated Python script to download music from Spotify playlists using YouTube as the source.

## ✨ Features

- 📥 Automatic download of complete Spotify playlists
- 🎧 Conversion to quality MP3 files
- 🔍 Smart YouTube search
- 🎯 Interactive menu interface
- 📁 Audio metadata management
- 🔄 Multiple support: playlists, singles, custom lists

## 🛠️ Technologies Used

### Python Libraries
- **`yt-dlp`** - Download and audio extraction from YouTube
- **`spotipy`** - Interface with official Spotify API
- **`youtube-search-python`** - YouTube video search
- **`FFmpeg`** - Audio conversion and processing

### APIs and Services
- **Spotify Web API** - Music metadata retrieval
- **YouTube** - Audio file source

## 📦 Installation

### Prerequisites
- Python 3.7+
- FFmpeg installed on the system
- Spotify developer account

### Installing Dependencies
```bash
pip install yt-dlp spotipy youtube-search-python
```

### Spotify Configuration
1. Create an application on [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Retrieve `CLIENT_ID` and `CLIENT_SECRET`
3. Configure environment variables:
```bash
export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"
```

## 🚀 Usage

```bash
python3 download.py
```

### Menu Options:
1. **Download from Spotify playlist**
2. **Download from YouTube playlist**
3. **Download from song list**
4. **Download a single song (search)**
5. **Download a single song (direct link)**
6. **Help**

## 🎯 How It Works

The script works in 3 steps:

1. **Metadata retrieval** via Spotify API
2. **Automatic search** for matches on YouTube
3. **Download and conversion** to MP3 with metadata

## ⚠️ Important

- Strictly personal use only
- Respect copyright laws
- Spotify credentials should not be shared
- Regenerate API keys if compromised

## 🐛 Troubleshooting

### Import Error
```bash
pip install --upgrade yt-dlp spotipy
```

### Audio Issues
Verify that FFmpeg is installed and accessible in PATH.


# II. Audio File Renamer (File compte.py )

A simple Python script to rename all audio files in a directory sequentially from 1 to N.

## Features

- Renames audio files in numerical order (1.mp3, 2.wav, 3.flac, etc.)
- Supports multiple audio formats (MP3, WAV, FLAC, AAC, OGG, M4A, WMA)
- Simple and interactive versions available
- Optional prefix for renamed files
- Safe operation with confirmation prompt

## Usage

### Basic Version

```python
# Modify the directory path and run the script
chemin_dossier = "/path/to/your/audio/folder"
renommer_fichiers_audio(chemin_dossier)
```

### Interactive Version

```python
# Run the script and follow the prompts
python audio_renamer.py
```

The script will:
1. Ask for the directory path (default: current directory)
2. Ask for an optional prefix
3. Show the files that will be renamed
4. Ask for confirmation before proceeding

## Supported Formats

- MP3 (`.mp3`)
- WAV (`.wav`) 
- FLAC (`.flac`)
- AAC (`.aac`)
- OGG (`.ogg`)
- M4A (`.m4a`)
- WMA (`.wma`)

## Example

**Before:**
```
song1.mp3
recording.wav
audio_file.flac
podcast.m4a
```

**After:**
```
1.mp3
2.wav
3.flac
4.m4a
```

**With prefix "audio_":**
```
audio_1.mp3
audio_2.wav
audio_3.flac
audio_4.m4a
```

## Requirements

- Python 3.x
- No external dependencies

## Installation

1. Clone or download the script
2. Navigate to the directory containing your audio files
3. Run the script:

```bash
python audio_renamer.py
```

## Warning

⚠️ **Always backup your files** before running this script, as the renaming operation cannot be easily undone.

## License

MIT License


## 👨‍💻 Author

**Sid DEGUENON**

[🔗 View my GitHub](https://github.com/DgnSid)
[🔗 EMail](deguenonsid@gmail.com)

