import os, sys, json, subprocess, time

sys.path.append('/home/igi/Documents/putts/vide_prs')
from cleaned_catalog import CLEANED_CATALOG

BASE_DIR = "/home/igi/Desktop/photo and videoc ollection/mp4s"
REPO = "Overloadpy/egate-videos"
TAG = "v1.0.0"
STATE_FILE = os.path.join(BASE_DIR, "github_uploaded_videos.json")

uploaded = {}
if os.path.exists(STATE_FILE):
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            uploaded = json.load(f)
    except Exception:
        uploaded = {}

print(f"Starting GitHub Releases upload for {len(CLEANED_CATALOG)} videos to {REPO} [{TAG}]...")

for idx, item in enumerate(CLEANED_CATALOG, 1):
    canonical_name = item['new_name']
    video_path = os.path.join(BASE_DIR, item['category'], item['folder'], canonical_name)
    direct_url = f"https://github.com/{REPO}/releases/download/{TAG}/{canonical_name}"

    if canonical_name in uploaded and uploaded[canonical_name].get("verified"):
        print(f"[{idx}/29] Already uploaded & verified: {canonical_name}")
        continue

    print(f"\n[{idx}/29] Uploading: {canonical_name} ({os.path.getsize(video_path) / (1024*1024):.1f} MB)...")
    cmd = [
        "gh", "release", "upload", TAG, video_path,
        "--repo", REPO, "--clobber"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Uploaded successfully! Direct URL: {direct_url}")
        uploaded[canonical_name] = {
            "title": item['title'],
            "file": canonical_name,
            "url": direct_url,
            "size_mb": round(os.path.getsize(video_path) / (1024*1024), 2),
            "category": item['category'],
            "folder": item['folder'],
            "verified": True
        }
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(uploaded, f, indent=2)
    else:
        print(f"Error uploading {canonical_name}: {res.stderr}")
        uploaded[canonical_name] = {"verified": False, "error": res.stderr}

print(f"\nUpload run complete! Total verified uploads: {sum(1 for v in uploaded.values() if v.get('verified'))} / 29")

# Update README files and MASTER_CATALOG.md
for item in CLEANED_CATALOG:
    name = item['new_name']
    readme_path = os.path.join(BASE_DIR, item['category'], item['folder'], "README.md")
    if not os.path.exists(readme_path) or name not in uploaded or not uploaded[name].get("verified"):
        continue

    url = uploaded[name]['url']
    with open(readme_path, "r", encoding="utf-8") as rf:
        rc = rf.read()

    # Append direct video link and HTML5 embed snippet
    badge_info = f"\n- **Direct Video Stream (CDN)**: [{url}]({url})\n"
    if "- **Direct Video Stream (CDN)**:" not in rc:
        rc = rc.replace("- **Audio Format**: Soundless MP4 (Audio track removed)",
                        f"- **Audio Format**: Soundless MP4 (Audio track removed){badge_info}")

    embed_snippet = f"""
---

## HTML5 Embed Code (For Vercel / Web)
```html
<video 
  src="{url}" 
  controls 
  autoplay 
  muted 
  loop 
  playsinline 
  preload="metadata"
  style="width: 100%; max-width: 900px; border-radius: 8px;">
</video>
```
"""
    if "## HTML5 Embed Code" not in rc:
        rc = rc.replace("## Navigation", f"{embed_snippet}\n## Navigation")

    with open(readme_path, "w", encoding="utf-8") as wf:
        wf.write(rc)

# Update MASTER_CATALOG.md
with open(os.path.join(BASE_DIR, "MASTER_CATALOG.md"), "r", encoding="utf-8") as f:
    master_lines = f.readlines()

new_master = []
for line in master_lines:
    for name, data in uploaded.items():
        if f"`{name}`" in line and data.get("verified") and "Direct Stream" not in line:
            line = line.replace(f"`{name}`", f"`{name}`<br/>🚀 [Direct Stream]({data['url']})")
            break
    new_master.append(line)

with open(os.path.join(BASE_DIR, "MASTER_CATALOG.md"), "w", encoding="utf-8") as f:
    f.writelines(new_master)

print("MASTER_CATALOG.md and all individual READMEs successfully updated with direct CDN links and HTML5 embed snippets!")
