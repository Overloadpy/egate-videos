# EGATE Burayu Campus — Video Archive & Streaming CDN

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
| **01** | Burayu Campus Aerial Overview & Courtyard 1 | `Campus Environment and Buildings` | 44.28 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/burayu_campus_aerial_overview_01.mp4) | Overview of the EGATE Burayu campus facilities, courtyard pathways, and student residences. |
| **02** | Burayu Campus Aerial Overview & Grounds 2 | `Campus Environment and Buildings` | 31.68 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/burayu_campus_aerial_overview_02.mp4) | Overview of the EGATE campus grounds and surrounding landscape. |
| **03** | Campus Courtyard & Glass Rotunda Walkthrough | `Campus Environment and Buildings` | 73.61 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/burayu_campus_courtyard_rotunda_walkthrough.mp4) | The central courtyard and circular glass rotunda at Burayu campus. |
| **04** | Campus Pathway & Exterior Colonnade Walkthrough | `Campus Environment and Buildings` | 53.41 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/burayu_campus_pathway_walkthrough.mp4) | Paved colonnade and covered walkways connecting campus buildings. |
| **05** | Campus Main Entrance Portico & Pillars 1 | `Campus Environment and Buildings` | 17.3 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/burayu_campus_main_entrance_pillars_01.mp4) | The main entrance portico featuring fluted concrete pillars. |
| **06** | Campus Main Entrance Portico & Driveway 2 | `Campus Environment and Buildings` | 16.88 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/burayu_campus_main_entrance_pillars_02.mp4) | The main entrance portico, structural pillars, and paved driveway. |
| **07** | Campus Exterior Plaza & Illuminated Facade (4K) | `Campus Environment and Buildings` | 153.02 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/burayu_campus_exterior_dusk_plaza_survey_4k.mp4) | 4K view of the campus exterior plaza, stone retaining masonry, and illuminated facade. |
| **08** | Exterior Twilight Academic Complex (4K) | `Campus Environment and Buildings` | 33.45 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/burayu_campus_exterior_twilight_building_view_4k.mp4) | 4K twilight view of the primary academic structure. |
| **09** | Library Exterior Approach & Pedestrian Ramp (4K) | `Library and Learning Commons` | 30.77 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/library_exterior_approach_dusk_4k.mp4) | 4K view of the landscaped pedestrian ramp and stairs leading to the EGATE Library. |
| **10** | Inside Central Library: Indoor Tree & Radial Atrium | `Library and Learning Commons` | 26.22 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/inside_library_atrium_tree_overview.mp4) | The circular library atrium featuring a living indoor tree and radial study carrels. |
| **11** | Inside Central Library: Mezzanine Study Balconies | `Library and Learning Commons` | 26.71 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/inside_library_mezzanine_balcony.mp4) | Upper curved mezzanine galleries with individual study carrels and glass balustrades. |
| **12** | Inside Central Library: Natural Skylight Dome | `Library and Learning Commons` | 14.53 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/inside_library_skylight_ceiling.mp4) | The radial skylight dome illuminating the central library atrium. |
| **13** | Atrium Corridor & Classroom Perimeter Walkthrough | `Library and Learning Commons` | 87.89 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/atrium_corridor_class_view_walkthrough.mp4) | Curved upper gallery corridor overlooking the central atrium and classroom entrances. |
| **14** | Atrium Corridor Walkthrough (Archival Copy) | `Library and Learning Commons` | 87.89 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/class_view_photo_corridor_walkthrough_duplicate.mp4) | Archival copy of the atrium corridor walkthrough. |
| **15** | PCB CNC Isolation Milling & Routing Machine | `Industrial Circuit Board and PCB Lab` | 43.48 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/pcb_cnc_isolation_milling_machine.mp4) | Automated precision CNC milling and PCB isolation routing machine. |
| **16** | Bungard Industrial PCB Chemical Plating Line | `Industrial Circuit Board and PCB Lab` | 39.66 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/bungard_industrial_pcb_chemical_plating_line.mp4) | German Bungard industrial through-hole plating, etching, and spray-rinsing line. |
| **17** | Bungard PCB Production Equipment Details | `Industrial Circuit Board and PCB Lab` | 9.22 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/bungard_pcb_production_line_close_up.mp4) | Chemical baths, immersion racks, and control systems of the Bungard PCB line. |
| **18** | Trainee Software Development & Coding Session | `Computer Lab and Robotics Class` | 37.71 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/trainee_coding_and_software_innovation.mp4) | Gifted students engaged in programming, algorithmic design, and software development. |
| **19** | Robotics & Computer Lab Workstations | `Computer Lab and Robotics Class` | 83.72 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/robotics_and_computer_lab_workstations.mp4) | The robotics and computer laboratory with PC workstations and 3D printers. |
| **20** | Robotics & Electronics Lab Entrance (4K) | `Computer Lab and Robotics Class` | 119.36 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/robotics_and_electronics_lab_entrance_4k.mp4) | 4K entrance to the Electronics and Computer Lab. |
| **21** | Innovation Class: 'Think Big' Space Mural (4K) | `Innovation Class and Electronics Lab` | 40.61 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/think_big_astronaut_mural_4k.mp4) | 4K view of the 'Think Big' space exploration mural in the electronics innovation classroom. |
| **22** | Innovation Class: Electronics Testing Benches (4K) | `Innovation Class and Electronics Lab` | 61.91 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/innovation_class_electronics_benches_4k.mp4) | 4K view of laboratory benches equipped with oscilloscopes, power supplies, and signal generators. |
| **23** | Electronics Laboratory Testing Instrumentation (4K) | `Innovation Class and Electronics Lab` | 18.41 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/electronics_testing_instruments_view_4k.mp4) | 4K view of active digital displays and controls on electronics testing instruments. |
| **24** | Student Project: Tracked Rover Robot & Astronomical Telescope | `Student Projects and Robotics` | 30.3 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/student_project_tracked_rover_and_telescope.mp4) | Student-built tracked rover chassis with breadboard electronics, alongside an astronomical telescope. |
| **25** | Student Project: Smart Home Automation Prototype (4K) | `Student Projects and Robotics` | 10.34 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/student_project_smart_home_iot_prototype_4k.mp4) | 4K view of a student-built smart home architectural model connected to a K&H IDL-800A trainer. |
| **26** | Student Project: EALSRS-1 Quadruped Robot & Drone (4K) | `Student Projects and Robotics` | 29.36 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/student_project_ealsrs1_quadruped_and_drone_4k.mp4) | 4K view of student robotic prototypes: EALSRS-1 quadruped walking robot, drone airframe, and vehicle chassis. |
| **27** | Tiered Lecture Auditorium: Podium & Presentation Area (4K) | `Classroom and Trainee Podcast Interview` | 45.72 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/tiered_classroom_auditorium_front_4k.mp4) | 4K view of the lecture podium, whiteboards, and projection screen in the tiered auditorium. |
| **28** | Tiered Lecture Auditorium: Student Seating (4K) | `Classroom and Trainee Podcast Interview` | 45.14 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/tiered_classroom_auditorium_rear_4k.mp4) | 4K view of curved tiered student seating banks and acoustic ceiling. |
| **29** | Trainee Activity & Educational Program Overview | `Classroom and Trainee Podcast Interview` | 157.03 MB | [Direct Stream](https://github.com/Overloadpy/egate-videos/releases/download/v1.0.0/trainee_activity_podcast_interview.mp4) | Informational overview detailing EGATE student activities, talent development programs, and campus life. |

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
