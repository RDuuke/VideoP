import os
import subprocess

from config import FRAGMENTS_DIR


def splitter(video_path: str, session_name:str, fragment_duration:int = 500) -> str:
    fragment_path = os.path.join(FRAGMENTS_DIR, session_name)
    os.makedirs(fragment_path, exist_ok=True)

    cmd_duration = f'ffmpeg -i "{video_path}" 2>&1 | findstr "Duration"'

    result = subprocess.run(cmd_duration, shell=True, capture_output=True, text=True)
    duration_str = result.stdout.split("Duration: ")[1].split(",")[0]
    h, m, s = map(float, duration_str.split(":"))
    total_seconds = int(h * 3600 + m * 60 + s)

    num_fragments = total_seconds // fragment_duration + (1 if total_seconds % fragment_duration else 0)
    print(f"📹 Dividiendo {video_path} en {num_fragments} fragmentos de {fragment_duration} segundos.")

    for i in range(num_fragments):
        start_time = i * fragment_duration
        fragment_output = os.path.join(fragment_path, f"fragmento_{i + 1}.mp4")

        if os.path.exists(fragment_output):
            print(f"⚠️ Fragmento {i + 1} ya existe, saltando...")
            continue

        cmd_split = f'ffmpeg -i "{video_path}" -ss {start_time} -t {fragment_duration} -c copy "{fragment_output}"'
        subprocess.run(cmd_split, shell=True, stderr=subprocess.DEVNULL)

    return fragment_path
