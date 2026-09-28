import json

with open("/home/igi/Documents/putts/vide_prs/catalog.json") as f:
    items = json.load(f)

readme = """# EGATE Burayu Campus — Video Archive & Streaming CDN

[![Release](https://img.shields.io/badge/Release-v1.0.0-emerald.svg)](https://github.com/Overloadpy/egate-videos/releases/tag/v1.0.0)
[![Audio](https://img.shields.io/badge/Audio-Soundless%20B--Roll-blue.svg)](#)
[![CDN](https://img.shields.io/badge/CDN-Fastly%20Global-purple.svg)](#)
[![License](https://img.shields.io/badge/License-Educational%20Public-amber.svg)](#)

This repository hosts the verified, soundless high-definition (1080p & 4K UHD) video archives for the **Ethiopian Giftedness and Talent Development School (EGATE)** at the **Burayu Campus, Sheger City, Oromia, Ethiopia**.

All **29 video recordings** are permanently hosted on GitHub's global Fastly CDN under release [`v1.0.0`](https://github.com/Overloadpy/egate-videos/releases/tag/v1.0.0). They can be streamed directly into any website (Vercel, Next.js, React, HTML) using standard HTML5 video elements without consuming hosting bandwidth.

---

## ⚡ Quick Start: Embedding in Your Website

### Standard HTML5 Player
```html
<video 
  src="https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/burayu_campus_aerial_overview_01.mp4" 
  controls 
  autoplay 
  muted 
  loop 
  playsinline 
  preload="metadata"
  style="width: 100%; border-radius: 8px;">
</video>
```

### React / Next.js Component
```jsx
export function VideoPlayer({ url }) {
  return (
    <video
      src={url}
      controls
      autoPlay
      muted
      loop
      playsInline
      preload="metadata"
      className="w-full rounded-xl shadow-lg border border-slate-800"
    />
  );
}
```

---

## 🚀 Live Interactive Showcase

This repository includes a standalone, mobile-responsive video gallery at [`index.html`](./index.html):
- Live filtering across all 7 academic categories.
- Soundless continuous looping and native playback.
- 1-click **Copy Embed** button for every video.
- Deployable to **Vercel** with zero configuration!

---

## 📋 Complete Video Inventory (29 Assets)

| # | Title | Category | Size | Direct Stream URL | Topic Summary |
| :-: | :--- | :--- | :-: | :--- | :--- |
"""

for idx, it in enumerate(items, 1):
    readme += f"| **{idx:02d}** | {it['title']} | `{it['category']}` | {it['size_mb']} MB | [Direct Stream]({it['url']}) | {it['short_description']} |\n"

readme += """
---

## 🏛️ Academic Domain Categories

### 1. Campus Environment and Buildings
- Architectural overviews of the Burayu residential campus, pedestrian colonnades, circular courtyard rotunda, and illuminated dusk facade.

### 2. Library and Learning Commons
- The signature central circular library featuring a living evergreen tree growing beneath the natural skylight dome, radial study desks, and upper mezzanine galleries.

### 3. Industrial Circuit Board & PCB Lab
- Rare secondary-level hardware manufacturing facilities: the automated **CNC isolation routing mill** and the German **Bungard industrial chemical plating and etching line** for multi-layer PCB production.

### 4. Computer Lab & Robotics Class
- Collaborative STEM computing labs with 1:1 student computing workstations, filament 3D printers, and integrated robotics development suites.

### 5. Innovation Class & Electronics Lab
- Dedicated circuit design lab featuring the inspirational **"THINK BIG"** astronaut space mural and professional benchtop oscilloscopes, DC power supplies, and function generators.

### 6. Student Projects and Robotics
- Working student-engineered prototypes: all-terrain tracked rover robot with telescope, smart home automation model interfaced to a **K&H IDL-800A digital logic trainer**, and the **EALSRS-1** 4-legged quadruped walking robot with drone airframe.

### 7. Classroom and Lecture Auditorium
- University-caliber tiered lecture amphitheater and educational presentation detailing student life and talent incubation.

---

## 🎓 EGATE Academic Curriculum Framework
EGATE structures its advanced STEM learning across four developmental tiers:
1. **FOE (Level 101) — Foundation of Excellence**: Core theoretical foundations in electronics, computational algorithms, and scientific inquiry.
2. **AKS (Level 201) — Advanced Knowledge & Skills**: Hands-on circuit analysis, microcontroller programming, and robotics locomotion.
3. **MAL (Level 301) — Mastery & Applied Learning**: Independent engineering design, PCB fabrication, and prototype testing.
4. **GLI (Level 401) — Global Leadership & Innovation**: Capstone research, bio-inspired engineering, and community-focused technical solutions.

---

## 📄 License & Attribution
Curated and organized for the **Ethiopian Giftedness and Talent Development School (EGATE)**. Hosted for educational and institutional showcase purposes.
"""

with open("/home/igi/Documents/putts/vide_prs/README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README.md created successfully!")
