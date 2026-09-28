import json

with open("/home/igi/Desktop/photo and videoc ollection/mp4s/github_uploaded_videos.json") as f:
    uploaded = json.load(f)

with open("/home/igi/Documents/putts/vide_prs/cleaned_catalog.py") as f:
    code = f.read()

globs = {}
exec(code, globs)
catalog = globs['CLEANED_CATALOG']

items = []
for c in catalog:
    name = c['new_name']
    url = uploaded[name]['url'] if (name in uploaded and uploaded[name].get("verified")) else f"https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/{name}"
    size_mb = uploaded[name].get('size_mb', 0) if name in uploaded else 0
    items.append({
        "filename": name,
        "title": c['title'],
        "category": c['category'].replace("_", " ")[3:],
        "category_slug": c['category'],
        "url": url,
        "size_mb": size_mb,
        "short_description": c['short_desc'],
        "deep_analysis": c['deep_analysis'],
        "takeaways": c['key_takeaways'],
        "curriculum": c['curriculum'],
        "gate_level": c['gate_level'],
        "embed_html": f'<video src="{url}" controls autoplay muted loop playsinline preload="metadata" style="width: 100%; border-radius: 8px;"></video>'
    })

with open("/home/igi/Documents/putts/vide_prs/catalog.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2)

print(f"catalog.json generated with {len(items)} items!")
