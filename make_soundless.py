import os, sys, subprocess, json

sys.path.append('/home/igi/.gemini/antigravity/brain/c115a309-5949-4c46-ace2-e384fa323d49/scratch')
from organize_videos import VIDEO_CATALOG

BASE_DIR = "/home/igi/Desktop/photo and videoc ollection/mp4s"

def check_audio_streams(file_path):
    cmd = [
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_streams", "-select_streams", "a", file_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        return -1
    data = json.loads(res.stdout)
    return len(data.get("streams", []))

print(f"Starting audio removal for all {len(VIDEO_CATALOG)} videos...")

converted_count = 0
already_soundless = 0

for idx, item in enumerate(VIDEO_CATALOG, 1):
    canonical_name = item['new_name']
    video_path = os.path.join(BASE_DIR, item['category'], item['folder'], canonical_name)
    temp_path = os.path.join(BASE_DIR, item['category'], item['folder'], "temp_soundless.mp4")

    if not os.path.exists(video_path):
        print(f"[{idx}/29] ERROR: File not found: {video_path}")
        continue

    audio_count = check_audio_streams(video_path)
    if audio_count == 0:
        print(f"[{idx}/29] Already soundless: {canonical_name}")
        already_soundless += 1
        continue

    # Demux audio out losslessly
    cmd = ["ffmpeg", "-y", "-i", video_path, "-c:v", "copy", "-an", temp_path]
    res = subprocess.run(cmd, capture_output=True, text=True)

    if res.returncode == 0 and os.path.exists(temp_path) and os.path.getsize(temp_path) > 0:
        os.replace(temp_path, video_path)
        new_audio_count = check_audio_streams(video_path)
        if new_audio_count == 0:
            print(f"[{idx}/29] Successfully stripped audio: {canonical_name} (0 audio streams)")
            converted_count += 1
        else:
            print(f"[{idx}/29] Warning: {canonical_name} still has {new_audio_count} audio streams!")
    else:
        print(f"[{idx}/29] Error converting {canonical_name}: {res.stderr[:200]}")
        if os.path.exists(temp_path):
            os.remove(temp_path)

print(f"\nCompleted! Converted: {converted_count}, Previously soundless: {already_soundless}, Total soundless: {converted_count + already_soundless}/29")
