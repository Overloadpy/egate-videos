import os, sys, json, time
from pathlib import Path
from googleapiclient.errors import HttpError

sys.path.append('/home/igi/.agents/skills/youtube-video-manager/scripts')
from youtube_ops import get_authenticated_service, upload_single_video

sys.path.append('/home/igi/.gemini/antigravity/brain/c115a309-5949-4c46-ace2-e384fa323d49/scratch')
from organize_videos import VIDEO_CATALOG

BASE_DIR = "/home/igi/Desktop/photo and videoc ollection/mp4s"
STATE_FILE = os.path.join(BASE_DIR, "uploaded_videos.json")

# Category specific tag mappings
CAT_TAGS = {
    "01_Campus_Environment_and_Buildings": ["Campus Tour", "Architecture", "Sheger City", "Burayu Campus", "Aerial Overview"],
    "02_Library_and_Learning_Commons": ["Library", "Learning Commons", "Biophilic Architecture", "Study Space", "Atrium"],
    "03_Industrial_Circuit_Board_and_PCB_Lab": ["PCB Manufacturing", "Circuit Board", "Bungard", "Electronics Lab", "Hardware Engineering", "CNC Milling"],
    "04_Computer_Lab_and_Robotics_Class": ["Coding", "Robotics", "Computer Science", "3D Printing", "Programming", "STEM Lab"],
    "05_Innovation_Class_and_Electronics_Lab": ["Electronics", "Think Big", "Oscilloscope", "Space Tech", "Circuit Design", "Astronomy"],
    "06_Student_Projects_and_Robotics": ["Student Project", "Robotics", "Smart Home", "Quadruped Robot", "Drone", "Telescope", "IoT"],
    "07_Classroom_and_Trainee_Podcast_Interview": ["Interview", "Podcast", "Auditorium", "Classroom", "Student Life", "Talent Development"]
}

# Load existing state if available
uploaded = {}
if os.path.exists(STATE_FILE):
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            uploaded = json.load(f)
    except Exception as e:
        print(f"Warning: Could not read existing state file: {e}")
        uploaded = {}

# Seed video 1 if not present
if "burayu_campus_aerial_overview_01.mp4" not in uploaded:
    uploaded["burayu_campus_aerial_overview_01.mp4"] = {
        "id": "MdttGusDvtU",
        "title": "Burayu Campus Aerial Overview & Courtyard View 1",
        "url": "https://youtu.be/MdttGusDvtU",
        "privacy": "unlisted",
        "category": "01_Campus_Environment_and_Buildings",
        "file": os.path.join(BASE_DIR, "01_Campus_Environment_and_Buildings", "01_burayu_campus_aerial_overview_01", "burayu_campus_aerial_overview_01.mp4")
    }
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(uploaded, f, indent=2)

print(f"State file initialized with {len(uploaded)} uploaded video(s).")
print(f"Connecting to YouTube Data API...")
youtube = get_authenticated_service("upload")

total = len(VIDEO_CATALOG)
quota_hit = False

for idx, item in enumerate(VIDEO_CATALOG, 1):
    canonical_name = item['new_name']
    video_path = os.path.join(BASE_DIR, item['category'], item['folder'], canonical_name)
    
    if canonical_name in uploaded:
        print(f"[{idx}/{total}] Already uploaded: {item['title']} -> {uploaded[canonical_name]['url']}")
        continue

    print(f"\n[{idx}/{total}] Preparing upload for: {item['title']}")
    print(f"Path: {video_path}")

    # Build detailed educational description
    desc = f"""{item['title']} - EGATE Burayu Campus

{item['short_desc']}

ABOUT THIS RECORDING:
{item['deep_analysis']}

KEY EDUCATIONAL TAKEAWAYS:
""" + "\n".join([f"• {k}" for k in item['key_takeaways']]) + f"""

EGATE CURRICULUM MAPPING:
• Domain Area: {item['curriculum']}
• GATE Framework Level: {item['gate_level']}
• Verification Note: {item['user_note']}

Institutional Background:
Ethiopian Giftedness and Talent Development School (EGATE)
Burayu Campus, Sheger City, Oromia, Ethiopia

#EGATE #Ethiopia #STEM #Robotics #Electronics #GiftedEducation #TalentDevelopment #Burayu
"""

    tags = ["EGATE", "Ethiopian Giftedness and Talent Development", "Burayu", "STEM Education", "Ethiopia"]
    tags.extend(CAT_TAGS.get(item['category'], []))
    # Deduplicate tags and limit to 500 chars total for YouTube API
    tags = list(dict.fromkeys(tags))[:15]

    try:
        res = upload_single_video(
            youtube,
            video_path,
            title=item['title'][:100], # YouTube max title length is 100
            description=desc,
            privacy="unlisted",
            tags=tags,
            category="27" # Education
        )
        if res:
            uploaded[canonical_name] = res
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(uploaded, f, indent=2)
            print(f"Successfully recorded: {res['url']}")
        else:
            print(f"Upload returned None for {canonical_name}")
    except HttpError as err:
        err_str = str(err)
        print(f"\n[HTTP ERROR] During upload of {canonical_name}: {err_str}")
        if "quotaExceeded" in err_str or "uploadLimitExceeded" in err_str:
            print("\n" + "!"*60)
            print("ALERT: YouTube API daily upload quota or limit reached!")
            print("The YouTube Data API allows a limited number of uploads per 24-hour cycle.")
            print("State is preserved. Remaining videos can be resumed when quota resets.")
            print("!"*60)
            quota_hit = True
            break
        else:
            print(f"Non-quota error occurred: {err_str}. Continuing to next file...")
    except Exception as exc:
        print(f"\n[ERROR] Unexpected error during upload: {exc}")
        break

print(f"\nBatch processing finished. Total videos uploaded: {len(uploaded)} / {total}")
