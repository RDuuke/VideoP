import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
VIDEO_DIR = os.path.join(BASE_DIR, 'videos')

FRAGMENTS_DIR = os.path.join(DATA_DIR, 'fragments')
AUDIO_DIR = os.path.join(DATA_DIR, 'audios')
TRANSCRIPTS_DIR = os.path.join(DATA_DIR, 'transcripts')
SUMMARY_DIR = os.path.join(DATA_DIR, 'summaries')

WHISPER_CACHE_DIR = os.path.expanduser("~/.cache/whisper")
WHISPER_MODEL = "base"  # Opciones: "tiny", "base", "small", "medium", "large"
WHISPER_LANGUAGE = "es"  # Idioma forzado en español

for folder in [FRAGMENTS_DIR]:
    os.makedirs(folder, exist_ok=True)

USE_OPENAI_API = False



