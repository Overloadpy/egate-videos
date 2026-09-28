import os, sys, json, time, re
from pathlib import Path
from googleapiclient.errors import HttpError

sys.path.append('/home/igi/.agents/skills/youtube-video-manager/scripts')
from youtube_ops import get_authenticated_service, upload_single_video

from cleaned_catalog import CLEANED_CATALOG

BASE_DIR = "/home/igi/Desktop/photo and videoc ollection/mp4s"
STATE_FILE = os.path.join(BASE_DIR, "uploaded_videos.json")

CAT_TAGS = {
    "01_Campus_Environment_and_Buildings": ["Campus Tour", "Architecture", "Sheger City", "Burayu Campus", "Aerial Overview"],
    "02_Library_and_Learning_Commons": ["Library", "Learning Commons", "Biophilic Architecture", "Study Space", "Atrium"],
    "03_Industrial_Circuit_Board_and_PCB_Lab": ["PCB Manufacturing", "Circuit Board", "Bungard", "Electronics Lab", "Hardware Engineering", "CNC Milling"],
    "04_Computer_Lab_and_Robotics_Class": ["Coding", "Robotics", "Computer Science", "3D Printing", "Programming", "STEM Lab"],
    "05_Innovation_Class_and_Electronics_Lab": ["Electronics", "Think Big", "Oscilloscope", "Space Tech", "Circuit Design", "Astronomy"],
    "06_Student_Projects_and_Robotics": ["Student Project", "Robotics", "Smart Home", "Quadruped Robot", "Drone", "Telescope", "IoT"],
    "07_Classroom_and_Trainee_Podcast_Interview": ["Interview", "Presentation", "Auditorium", "Classroom", "Student Life", "Talent Development"]
}

# Load state
uploaded = {}
if os.path.exists(STATE_FILE):
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            uploaded = json.load(f)
    except Exception:
        uploaded = {}

print(f"Connecting to YouTube Data API for soundless video upload...")
youtube = get_authenticated_service("upload")

total = len(CLEANED_CATALOG)
quota_hit = False

for idx, item in enumerate(CLEANED_CATALOG, 1):
    canonical_name = item['new_name']
    video_path = os.path.join(BASE_DIR, item['category'], item['folder'], canonical_name)

    if canonical_name in uploaded and uploaded[canonical_name].get("url"):
        print(f"[{idx}/{total}] Already uploaded: {item['title']} -> {uploaded[canonical_name]['url']}")
        continue

    print(f"\n[{idx}/{total}] Uploading soundless video: {item['title']}")
    print(f"File: {video_path}")

    desc = f"""{item['title']} - EGATE Burayu Campus

{item['short_desc']}

CONTENT & EDUCATIONAL OVERVIEW:
{item['deep_analysis']}

KEY EDUCATIONAL TAKEAWAYS:
""" + "\n".join([f"• {k}" for k in item['key_takeaways']]) + f"""

EGATE CURRICULUM MAPPING:
• Domain Area: {item['curriculum']}
• GATE Framework Level: {item['gate_level']}
• Verification Note: {item['user_note']}
• Media Format: Soundless MP4

Institutional Background:
Ethiopian Giftedness and Talent Development School (EGATE)
Burayu Campus, Sheger City, Oromia, Ethiopia

#EGATE #Ethiopia #STEM #Robotics #Electronics #GiftedEducation #TalentDevelopment #Burayu
"""

    tags = ["EGATE", "Ethiopian Giftedness and Talent Development", "Burayu", "STEM Education", "Ethiopia", "Soundless"]
    tags.extend(CAT_TAGS.get(item['category'], []))
    tags = list(dict.fromkeys(tags))[:15]

    try:
        res = upload_single_video(
            youtube,
            video_path,
            title=item['title'][:100],
            description=desc,
            privacy="unlisted",
            tags=tags,
            category="27" # Education
        )
        if res:
            uploaded[canonical_name] = res
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(uploaded, f, indent=2)
            print(f"Successfully uploaded: {res['url']}")
            
            # Immediately update the README.md in the folder
            readme_path = os.path.join(BASE_DIR, item['category'], item['folder'], "README.md")
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as rf:
                    rc = rf.read()
                if "- **YouTube Video**:" not in rc:
                    rc = rc.replace("- **Audio Format**: Soundless MP4 (Audio track removed)", 
                                    f"- **Audio Format**: Soundless MP4 (Audio track removed)\n- **YouTube Video**: [{res['url']}]({res['url']}) *(Status: Unlisted | ID: `{res['id']}`)*")
                    with open(readme_path, "w", encoding="utf-8") as wf:
                        wf.write(rc)
        else:
            print(f"Upload failed (returned None) for {canonical_name}")
    except HttpError as err:
        err_str = str(err)
        print(f"\n[HTTP ERROR] During upload of {canonical_name}: {err_str}")
        if "quotaExceeded" in err_str or "uploadLimitExceeded" in err_str:
            print("\n" + "!"*60)
            print("ALERT: YouTube upload limit encountered.")
            print(err_str)
            print("!"*60)
            quota_hit = True
            break
        else:
            print(f"Continuing to next file...")
    except Exception as exc:
        print(f"\n[ERROR] Unexpected error: {exc}")
        break

# Regenerate MASTER_CATALOG.md with all new YouTube links
with open(os.path.join(BASE_DIR, "MASTER_CATALOG.md"), "r", encoding="utf-8") as f:
    master_lines = f.readlines()

new_master = []
for line in master_lines:
    matched = False
    for name, data in uploaded.items():
        if f"`{name}`" in line and "Watch on YouTube" not in line:
            line = line.replace(f"`{name}`", f"`{name}`<br/>🎥 [Watch on YouTube]({data['url']})")
            matched = True
            break
    new_master.append(line)

with open(os.path.join(BASE_DIR, "MASTER_CATALOG.md"), "w", encoding="utf-8") as f:
    f.writelines(new_master)

print(f"\nUpload process finished! Total videos uploaded: {len(uploaded)} / {total}")
