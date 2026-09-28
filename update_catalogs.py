import os, sys, json

sys.path.append('/home/igi/.gemini/antigravity/brain/c115a309-5949-4c46-ace2-e384fa323d49/scratch')
from organize_videos import VIDEO_CATALOG

BASE_DIR = "/home/igi/Desktop/photo and videoc ollection/mp4s"
STATE_FILE = os.path.join(BASE_DIR, "uploaded_videos.json")

with open(STATE_FILE, "r", encoding="utf-8") as f:
    uploaded = json.load(f)

print(f"Total uploaded videos to link: {len(uploaded)}")

# Update individual README.md files
for item in VIDEO_CATALOG:
    name = item['new_name']
    readme_path = os.path.join(BASE_DIR, item['category'], item['folder'], "README.md")
    if not os.path.exists(readme_path):
        continue
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    if name in uploaded:
        yt_url = uploaded[name]['url']
        yt_id = uploaded[name]['id']
        yt_badge = f"\n- **YouTube Video**: [{yt_url}]({yt_url}) *(Status: Unlisted | ID: `{yt_id}`)*\n"
        if "- **YouTube Video**:" not in content:
            # insert after Canonical Filename
            content = content.replace(f"- **Canonical Filename**: `{name}`", f"- **Canonical Filename**: `{name}`{yt_badge}")
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated README: {item['folder']}")

# Update MASTER_CATALOG.md
with open(os.path.join(BASE_DIR, "MASTER_CATALOG.md"), "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    matched = False
    for name, data in uploaded.items():
        if f"`{name}`" in line:
            # Add or update the link in the table
            yt_link = f"[{data['url']}]({data['url']})"
            # Check if YouTube column already exists, if not we can add it or annotate the title
            line = line.replace(f"`{name}`", f"`{name}`<br/>🎥 [Watch on YouTube]({data['url']})")
            matched = True
            break
    new_lines.append(line)

with open(os.path.join(BASE_DIR, "MASTER_CATALOG.md"), "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("MASTER_CATALOG.md updated with YouTube links.")
