import json

with open("/home/igi/Desktop/photo and videoc ollection/mp4s/github_uploaded_videos.json") as f:
    uploaded = json.load(f)

# Load catalog metadata
with open("/home/igi/Documents/putts/vide_prs/cleaned_catalog.py") as f:
    code = f.read()

globs = {}
exec(code, globs)
catalog = globs['CLEANED_CATALOG']

videos = []
for c in catalog:
    name = c['new_name']
    if name in uploaded and uploaded[name].get("verified"):
        videos.append({
            "title": c['title'],
            "category": c['category'].replace("_", " ")[3:],
            "cat_slug": c['category'],
            "file": name,
            "url": uploaded[name]['url'],
            "short_desc": c['short_desc'],
            "deep_analysis": c['deep_analysis'],
            "takeaways": c['key_takeaways'],
            "curriculum": c['curriculum'],
            "gate_level": c['gate_level']
        })

categories = sorted(list(set(v['category'] for v in videos)))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EGATE Burayu Campus - Video Showcase</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
    body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    .video-card:hover .play-overlay {{ opacity: 1; }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen">
  <!-- Header -->
  <header class="border-b border-slate-800 bg-slate-900/60 backdrop-blur sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-6 py-4 flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div class="flex items-center gap-3">
          <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
            Fastly CDN Streaming
          </span>
          <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-blue-500/10 text-blue-400 border border-blue-500/20">
            Soundless B-Roll
          </span>
        </div>
        <h1 class="text-2xl font-bold tracking-tight text-white mt-1">EGATE Burayu Campus Video Gallery</h1>
        <p class="text-sm text-slate-400">29 Soundless HD & 4K video assets ready for website embedding</p>
      </div>
      <div class="flex items-center gap-3">
        <a href="https://github.com/Overloadpy/egate-videos/releases/tag/v1.0.0" target="_blank" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white text-sm font-medium rounded-lg border border-slate-700 transition">
          View GitHub Release ↗
        </a>
      </div>
    </div>
    <!-- Category Filter Tabs -->
    <div class="max-w-7xl mx-auto px-6 overflow-x-auto py-2 flex items-center gap-2 border-t border-slate-800/60 scrollbar-none">
      <button onclick="filterCategory('all')" id="btn-all" class="cat-btn px-3 py-1.5 rounded-md text-xs font-medium bg-emerald-600 text-white whitespace-nowrap">
        All Categories (29)
      </button>
"""

for cat in categories:
    count = sum(1 for v in videos if v['category'] == cat)
    slug = cat.lower().replace(" ", "-")
    html += f"""      <button onclick="filterCategory('{cat}')" id="btn-{slug}" class="cat-btn px-3 py-1.5 rounded-md text-xs font-medium text-slate-400 hover:text-white hover:bg-slate-800 whitespace-nowrap transition">
        {cat} ({count})
      </button>\n"""

html += """    </div>
  </header>

  <!-- Main Content -->
  <main class="max-w-7xl mx-auto px-6 py-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="video-grid">
"""

for idx, v in enumerate(videos, 1):
    html += f"""      <div class="video-item bg-slate-900 border border-slate-800 rounded-xl overflow-hidden shadow-lg flex flex-col group" data-category="{v['category']}">
        <!-- Video Player -->
        <div class="relative aspect-video bg-black">
          <video 
            src="{v['url']}" 
            controls 
            muted 
            loop 
            playsinline 
            preload="metadata"
            class="w-full h-full object-cover">
          </video>
        </div>
        <!-- Card Body -->
        <div class="p-5 flex-1 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between text-xs text-slate-400 mb-2">
              <span class="font-medium text-emerald-400">{v['category']}</span>
              <span class="bg-slate-800 px-2 py-0.5 rounded text-[11px] font-mono">#{idx:02d}</span>
            </div>
            <h3 class="font-semibold text-white text-base leading-snug group-hover:text-emerald-400 transition">
              {v['title']}
            </h3>
            <p class="text-xs text-slate-400 mt-2 line-clamp-3 leading-relaxed">
              {v['short_desc']}
            </p>
          </div>
          <!-- Embed Code Popover / Copy -->
          <div class="mt-4 pt-4 border-t border-slate-800/80 flex items-center justify-between gap-2">
            <span class="text-[11px] text-slate-500 font-mono truncate max-w-[170px]">{v['file']}</span>
            <button onclick="copyEmbed('{v['url']}')" class="px-2.5 py-1 text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 rounded border border-slate-700 transition flex items-center gap-1.5">
              <span>📋 Copy Embed</span>
            </button>
          </div>
        </div>
      </div>
"""

html += """    </div>
  </main>

  <!-- Notification Toast -->
  <div id="toast" class="fixed bottom-6 right-6 bg-emerald-600 text-white px-4 py-2.5 rounded-lg shadow-xl text-sm font-medium transition-all transform translate-y-20 opacity-0 pointer-events-none flex items-center gap-2">
    <span>✓</span> HTML5 Embed code copied to clipboard!
  </div>

  <script>
    function filterCategory(cat) {
      document.querySelectorAll('.cat-btn').forEach(b => {
        b.classList.remove('bg-emerald-600', 'text-white');
        b.classList.add('text-slate-400');
      });
      const btn = event.target;
      btn.classList.add('bg-emerald-600', 'text-white');
      btn.classList.remove('text-slate-400');

      const items = document.querySelectorAll('.video-item');
      items.forEach(el => {
        if (cat === 'all' || el.getAttribute('data-category') === cat) {
          el.style.display = 'flex';
        } else {
          el.style.display = 'none';
        }
      });
    }

    function copyEmbed(url) {
      const code = `<video src="${url}" controls autoplay muted loop playsinline preload="metadata" style="width: 100%; border-radius: 8px;"></video>`;
      navigator.clipboard.writeText(code).then(() => {
        const toast = document.getElementById('toast');
        toast.classList.remove('translate-y-20', 'opacity-0');
        setTimeout(() => {
          toast.classList.add('translate-y-20', 'opacity-0');
        }, 2200);
      });
    }
  </script>
</body>
</html>
"""

with open("/home/igi/Documents/putts/vide_prs/index.html", "w") as f:
    f.write(html)

print("index.html showcase gallery created successfully!")
