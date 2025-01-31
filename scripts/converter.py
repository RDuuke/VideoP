import logging
from pathlib import Path
import subprocess
from tqdm import tqdm

from config import AUDIO_DIR

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def converter_to_wav(fragment_files: list, session_name: str) -> list:
    audio_path = Path(AUDIO_DIR) / session_name
    audio_path.mkdir(parents=True, exist_ok=True)

    for existing_audio in tqdm(list(audio_path.glob("*.wav")), desc=f"🗑️ Eliminando Audios: "):
        existing_audio.unlink()

    logger.info("🎧 Iniciando conversión de MP4 a WAV...")

    audio_files = []  # Lista para almacenar las rutas de los archivos de audio generados

    for fragment_file in tqdm(fragment_files, desc=f"⏳  Convirtiendo a WAV: "):
        fragment_file = Path(fragment_file)
        wav_file = audio_path / fragment_file.name.replace(".mp4", ".wav")

        if wav_file.exists():
            logger.warning(f"⚠️  {wav_file} ya existe, saltando...")
            continue

        cmd_convert = [
            "ffmpeg",
            "-i", str(fragment_file),
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            str(wav_file)
        ]

        try:
            subprocess.run(cmd_convert, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            audio_files.append(str(wav_file))  # Agregar la ruta del archivo .wav a la lista
        except subprocess.CalledProcessError as e:
            logger.error(f"❌  Error al convertir {fragment_file}: {e}")
            continue

    return audio_files