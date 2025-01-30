import os
import subprocess

from config import AUDIO_DIR


def converter_to_wav(fragment_path: str, session_name:str) -> str:
    audio_path = os.path.join(AUDIO_DIR, session_name)
    os.makedirs(audio_path, exist_ok=True)

    print("🎧  Iniciando conversión de MP4 a WAV...")

    for file in os.listdir(fragment_path):
        if file.endswith(".mp4"):
            mp4_file = os.path.join(fragment_path, file)
            wav_file = os.path.join(audio_path, file.replace(".mp4", ".wav"))

            if os.path.exists(wav_file):
                print(f"⚠️  {wav_file} ya existe, saltando...")
                continue

            cmd_convert = f'ffmpeg -i "{mp4_file}" -vn -acodec pcm_s16le -ar 16000 -ac 1 "{wav_file}"'
            subprocess.run(cmd_convert, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("✅  Conversión completada.")
    return audio_path