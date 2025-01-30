import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'  # Directorio para almacenar datos generados
VIDEO_DIR = BASE_DIR / 'videos'  # Directorio para almacenar videos de entrada

FRAGMENTS_DIR = DATA_DIR / 'fragments'  # Fragmentos de video
AUDIO_DIR = DATA_DIR / 'audios'  # Archivos de audio convertidos
TRANSCRIPTS_DIR = DATA_DIR / 'transcripts'  # Transcripciones de audio
SUMMARY_DIR = DATA_DIR / 'summaries'  # Resúmenes generados

for folder in [FRAGMENTS_DIR, AUDIO_DIR, TRANSCRIPTS_DIR, SUMMARY_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

WHISPER_CACHE_DIR = Path.home() / ".cache" / "whisper"  # Directorio de caché para Whisper
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")  # Modelo de Whisper, por defecto "base"
WHISPER_LANGUAGE = os.getenv("WHISPER_LANGUAGE", "es")  # Idioma, por defecto español

WHISPER_MODELS = ["tiny", "base", "small", "medium", "large"]
if WHISPER_MODEL not in WHISPER_MODELS:
    raise ValueError(f"WHISPER_MODEL debe ser uno de: {', '.join(WHISPER_MODELS)}")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Clave de API de OpenAI
USE_OPENAI_API = bool(OPENAI_API_KEY)  # Usar OpenAI solo si la clave está configurada