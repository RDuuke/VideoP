import logging
import whisper
import warnings
from pathlib import Path
from tqdm import tqdm
from config import TRANSCRIPTS_DIR, WHISPER_MODEL, WHISPER_CACHE_DIR

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logger = logging.getLogger(__name__)

def model_exists(model_name: str) -> bool:
    model_path = Path(WHISPER_CACHE_DIR)
    return model_path.exists()

def load_model():
    if model_exists(WHISPER_MODEL):
        logger.info(f"✅  El modelo {WHISPER_MODEL} ya está descargado.")
    else:
        logger.info(f"⬇️  Descargando el modelo {WHISPER_MODEL} por primera vez. Esto puede tardar unos minutos...")

    model = whisper.load_model(WHISPER_MODEL)
    return model

def transcriber_audio(
    audio_files: list,
    session_name: str,
    word_timestamps: bool = True,
    language: str = "es"
) -> str:
    model = load_model()
    transcription_path = Path(TRANSCRIPTS_DIR) / session_name
    transcription_path.mkdir(parents=True, exist_ok=True)

    for existing_transcription in tqdm(list(transcription_path.glob("*.txt")), desc=f"🗑️ Eliminando transcripciones: ", unit="archivo", colour="green", ncols=100):
        existing_transcription.unlink()

    transcript_files = []

    for audio_file in tqdm(audio_files, desc=f"⏳  Creando transcripciones: "):
        audio_file = Path(audio_file)
        transcription_file = transcription_path / audio_file.name.replace(".wav", ".txt")

        if transcription_file.exists():
            logger.warning(f"⚠️ {transcription_file} ya existe, saltando...")
            continue

        try:
            result = model.transcribe(str(audio_file), word_timestamps=word_timestamps, language=language)
            transcript_text = f"\n=== {audio_file.name} ===\n" + result["text"]

            with open(transcription_file, "w", encoding="utf-8") as f:
                f.write(transcript_text)
            transcript_files.append(str(transcription_file))
        except Exception as e:
            logger.error(f"❌  Error al transcribir {audio_file.name}: {e}")
            continue

    full_transcription_file = transcription_path / "transcripcion_completa.txt"
    with open(full_transcription_file, "w", encoding="utf-8") as f_out:
        for file in transcript_files:
            with open(file, "r", encoding="utf-8") as f_in:
                f_out.write(f_in.read() + "\n")

    logger.info("📜 Transcripción de todos los fragmentos completada.")
    return str(full_transcription_file)