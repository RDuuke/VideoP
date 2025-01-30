import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
VIDEO_DIR = os.path.join(BASE_DIR, 'videos')

FRAGMENTS_DIR = os.path.join(DATA_DIR, 'fragments')
AUDIO_DIR = os.path.join(DATA_DIR, 'audios')

for folder in [FRAGMENTS_DIR]:
    os.makedirs(folder, exist_ok=True)

