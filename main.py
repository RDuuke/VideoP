import glob
import os.path
from typing import Optional, List

from config import VIDEO_DIR
from scripts.splitter import splitter


def selected_video()-> Optional[str]:

    video_files = glob.glob(os.path.join(VIDEO_DIR, '*.mp4'))

    if not video_files:
        print("❌  No hay videos en la carpeta 'videos/'. Agrega un archivo MP4 para procesar.")
        return None

    print("\n📂  Videos disponibles para procesar:")
    for ids, file in enumerate(video_files):
        print(f"{ids}. {os.path.basename(file)}")

    selected_index = int(input("\n🔹 Ingresa el número del video que deseas procesar: ")) - 1

    return video_files[selected_index]


def main():
    video_path = selected_video()
    if not video_path:
        return

    session_name = os.path.splitext(os.path.basename(video_path))[0]

    fragment_path = splitter(video_path=video_path, session_name=session_name)

if __name__ == "__main__":
    main()
