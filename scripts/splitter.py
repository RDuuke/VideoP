import logging
from tqdm import tqdm
from pathlib import Path
import subprocess
from config import FRAGMENTS_DIR

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def splitter(
    video_path: str,
    session_name: str,
    fragment_duration: int = 500,
    codec: str = "copy"
) -> list:
    video_path = Path(video_path)
    if not video_path.exists():
        logger.error(f"❌ El archivo {video_path} no existe.")
        return []

    if fragment_duration <= 0:
        logger.error("❌ La duración del fragmento debe ser un valor positivo.")
        return []

    fragment_path = Path(FRAGMENTS_DIR) / session_name
    fragment_path.mkdir(parents=True, exist_ok=True)

    for existing_fragment in tqdm(list(fragment_path.glob("*.mp4")), desc=f"🗑️ Eliminando fragmentos: "):
        existing_fragment.unlink()

    try:
        result = subprocess.run(
            ["ffmpeg", "-i", str(video_path)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Error al procesar el video: {e.stderr}")
        return []
    except FileNotFoundError:
        logger.error("❌ Error: ffmpeg no está instalado. Por favor, instala ffmpeg.")
        return []

    output = result.stderr
    for line in output.split("\n"):
        if "Duration: " in line:
            duration_str = line.split("Duration: ")[1].split(",")[0].strip()

    h, m, s = map(float, duration_str.split(":"))
    total_seconds = int(h * 3600 + m * 60 + s)

    if total_seconds <= 0:
        logger.error("❌ La duración del video es inválida.")
        return []

    num_fragments = total_seconds // fragment_duration + (1 if total_seconds % fragment_duration else 0)
    logger.info(f"📹 Dividiendo {video_path} en {num_fragments} fragmentos de {fragment_duration} segundos.")

    fragment_files = []
    for i in tqdm(range(num_fragments), desc=f"⏳   Creando fragmentos: "):
        start_time = i * fragment_duration
        fragment_output = fragment_path / f"fragmento_{i + 1}.mp4"

        cmd_split = [
            "ffmpeg",
            "-i", str(video_path),
            "-ss", str(start_time),
            "-t", str(fragment_duration),
            "-c", str(codec),
            str(fragment_output)
        ]

        try:
            subprocess.run(cmd_split, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            fragment_files.append(str(fragment_output))
        except subprocess.CalledProcessError as e:
            logger.error(f"❌  Error al crear el fragmento {i + 1}: {e.stderr.decode('utf-8')}")
            continue

    return fragment_files