import logging
import time
from pathlib import Path
from typing import Optional
from tqdm import tqdm

from config import VIDEO_DIR
from scripts.converter import converter_to_wav
from scripts.splitter import splitter
from scripts.transcriber import transcriber_audio
from scripts.summarizer import summary_generate

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def selected_video() -> Optional[str]:
    video_files = list(Path(VIDEO_DIR).glob("*.mp4"))

    if not video_files:
        logger.error("❌ No hay videos en la carpeta 'videos/'. Agrega un archivo MP4 para procesar.")
        return None

    logger.info("📂 Videos disponibles para procesar:")
    for ids, file in enumerate(video_files):
        logger.info(f"{ids + 1}. {file.name}")

    try:
        selected_index = int(input("\n🔹 Ingresa el número del video que deseas procesar: ")) - 1
        if selected_index < 0 or selected_index >= len(video_files):
            logger.error("❌  Índice inválido. Por favor, selecciona un número dentro del rango.")
            return None
        return str(video_files[selected_index])
    except ValueError:
        logger.error("❌ Entrada inválida. Por favor, ingresa un número válido.")
        return None

def main():
    while True:
        print("\n🔹 Menú Principal:")
        print("1. Procesar un video")
        print("2. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            start_time = time.time()
            video_path = selected_video()
            if not video_path:
                continue

            session_name = Path(video_path).stem

            fragment_files = splitter(video_path=video_path, session_name=session_name)
            if not fragment_files:
                logger.error("❌  Error al dividir el video.")
                continue

            audio_files = converter_to_wav(fragment_files=fragment_files, session_name=session_name)
            if not audio_files:
                logger.error("❌ Error al convertir el video a audio.")
                continue

            transcription_path = transcriber_audio(audio_files=audio_files, session_name=session_name)
            if not transcription_path:
                logger.error("❌ Error al transcribir el audio.")
                continue

            summary_file = summary_generate(transcription=transcription_path, session_name=session_name)
            if not summary_file:
                logger.error("❌ Error al generar el resumen.")
                continue

            end_time = time.time()
            elapsed_time = end_time - start_time

            logger.info(f"✅  Proceso completado. Resumen guardado en: {summary_file}")
            logger.info(f"⏱️ Tiempo total de ejecución: {elapsed_time:.2f} segundos.")

        elif choice == "2":
            logger.info("👋 Saliendo del programa...")
            break
        else:
            logger.error("❌ Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()