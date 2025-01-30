import os
import whisper

from config import TRANSCRIPTS_DIR, WHISPER_MODEL, WHISPER_CACHE_DIR

def model_exists(model_name) -> bool:
    model_path = os.path.join(WHISPER_CACHE_DIR, model_name)
    return os.path.exists(model_path)

def load_model():
    if model_exists(WHISPER_MODEL):
        print(f"✅ El modelo {WHISPER_MODEL} ya está descargado.")
    else:
        print(f"⬇️ Descargando el modelo {WHISPER_MODEL} por primera vez. Esto puede tardar unos minutos...")

    model = whisper.load_model(WHISPER_MODEL)
    return model


def transcriber_audio(audio_path:str, session_name:str) -> str:
    model = load_model()

    transcription_path = os.path.join(TRANSCRIPTS_DIR, session_name)
    os.makedirs(transcription_path, exist_ok=True)

    transcript_files = []

    for file in os.listdir(audio_path):
        if file.endswith(".wav"):
            wav_file = os.path.join(audio_path, file)
            transcription_file = os.path.join(transcription_path, file.replace(".wav", ".txt"))

            if not os.path.exists(transcription_file):
                print(f"⏳ Transcribiendo {file}...")
                result = model.transcribe(wav_file, word_timestamps=True, language="es")
                transcript_text = f"\n=== {file} ===\n" + result["text"]

                with open(transcription_file, "w", encoding="utf-8") as file:
                    file.write(transcript_text)
                print(f"✅  Transcripción guardada en {transcription_file}")
            else:
                print(f"⚠️ {transcription_file} ya existe, saltando...")

            transcript_files.append(transcription_file)

    full_transcription_file = os.path.join(transcription_path, "transcripcion_completa.txt")

    with open(full_transcription_file, "w", encoding="utf-8") as f_out:
        for file in transcript_files:
            with open(file, "r", encoding="utf-8") as f_in:
                f_out.write(f_in.read() + "\n")

    print("📜 Transcripción de todos los fragmentos completada.")
    return full_transcription_file