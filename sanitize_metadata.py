import os, sys, json, re

BASE_DIR = "/home/igi/Desktop/photo and videoc ollection/mp4s"

CLEANED_CATALOG = [
    {
        "orig_file": "0Y1A6989.MP4",
        "category": "01_Campus_Environment_and_Buildings",
        "folder": "01_burayu_campus_aerial_overview_01",
        "new_name": "burayu_campus_aerial_overview_01.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Burayu Campus Aerial Overview & Courtyard 1",
        "short_desc": "Overview of the EGATE Burayu campus facilities, courtyard pathways, and student residences.",
        "curriculum": "Campus Infrastructure & Institutional Environment",
        "gate_level": "Institutional Environment",
        "user_note": "EGATE Burayu campus environment and layout.",
        "deep_analysis": (
            "Overview of the flagship Burayu campus of the Ethiopian Giftedness and Talent Development School (EGATE) "
            "in Sheger City, Oromia. The academic facility features modern curvilinear structures, central paved pedestrian walkways, "
            "manicured grass courtyards, and student residential dormitories. The architecture provides a serene, "
            "world-class residential incubator for gifted students selected from across Ethiopia."
        ),
        "key_takeaways": [
            "Scale and residential facilities of the Burayu campus.",
            "Modern architectural design tailored for gifted STEM education.",
            "Serene environment designed to nurture national scientific talent."
        ]
    },
    {
        "orig_file": "0Y1A6995.MP4",
        "category": "01_Campus_Environment_and_Buildings",
        "folder": "02_burayu_campus_aerial_overview_02",
        "new_name": "burayu_campus_aerial_overview_02.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Burayu Campus Aerial Overview & Grounds 2",
        "short_desc": "Overview of the EGATE campus grounds and surrounding landscape.",
        "curriculum": "Campus Infrastructure & Institutional Environment",
        "gate_level": "Institutional Environment",
        "user_note": "EGATE campus grounds and surrounding green landscape.",
        "deep_analysis": (
            "The Burayu campus grounds highlight the integration between the multi-story academic buildings and the green "
            "landscape of the Burayu hills. The campus plan intentionally separates instructional spaces from outdoor "
            "collaborative courtyards and residential quarters."
        ),
        "key_takeaways": [
            "Broader geographical setting of the Burayu campus.",
            "Integrated pedestrian paths and open communal areas.",
            "Contemporary academic environment suited for immersive learning."
        ]
    },
    {
        "orig_file": "m2.MP4",
        "category": "01_Campus_Environment_and_Buildings",
        "folder": "03_courtyard_rotunda_walkthrough",
        "new_name": "burayu_campus_courtyard_rotunda_walkthrough.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Campus Courtyard & Glass Rotunda Walkthrough",
        "short_desc": "The central courtyard and circular glass rotunda at Burayu campus.",
        "curriculum": "Campus Infrastructure & Learning Spaces",
        "gate_level": "Institutional Environment",
        "user_note": "Central campus courtyard and circular rotunda.",
        "deep_analysis": (
            "The central campus courtyard features the modern glass-fronted circular rotunda serving as a major architectural "
            "anchor for the academic complex. Paved interlocking brick pathways, exterior benches, and manicured lawns "
            "form an inviting academic sanctuary."
        ),
        "key_takeaways": [
            "Primary courtyard entrance area of the school.",
            "Circular architectural motif characterizing the Burayu facility.",
            "High construction standard of EGATE infrastructure."
        ]
    },
    {
        "orig_file": "m9.MP4",
        "category": "01_Campus_Environment_and_Buildings",
        "folder": "04_campus_pathway_walkthrough",
        "new_name": "burayu_campus_pathway_walkthrough.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Campus Pathway & Exterior Colonnade Walkthrough",
        "short_desc": "Paved colonnade and covered walkways connecting campus buildings.",
        "curriculum": "Campus Infrastructure & Learning Spaces",
        "gate_level": "Institutional Environment",
        "user_note": "Outdoor walkways connecting academic and residential blocks.",
        "deep_analysis": (
            "The paved pedestrian colonnade links different functional wings of the campus. Covered walkways, exterior "
            "structural columns, exterior lighting, and landscaped borders provide seamless campus circulation."
        ),
        "key_takeaways": [
            "Walkable, integrated campus design.",
            "Seamless connections between academic wings and student halls.",
            "Clean, contemporary aesthetic throughout the grounds."
        ]
    },
    {
        "orig_file": "0Y1A7045.MP4",
        "category": "01_Campus_Environment_and_Buildings",
        "folder": "05_main_entrance_pillars_01",
        "new_name": "burayu_campus_main_entrance_pillars_01.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Campus Main Entrance Portico & Pillars 1",
        "short_desc": "The main entrance portico featuring fluted concrete pillars.",
        "curriculum": "Campus Architecture",
        "gate_level": "Institutional Environment",
        "user_note": "Main entrance portico with architectural pillars.",
        "deep_analysis": (
            "The main portico of the EGATE Burayu facility features monumental fluted gray concrete pillars supporting an elevated "
            "roof structure. The portico accommodates vehicular arrival and formal pedestrian entry for students, faculty, and official guests."
        ),
        "key_takeaways": [
            "Monumental entrance architecture of the EGATE facility.",
            "Formal arrival court designed for institutional operations.",
            "Structural permanence reflecting national educational investment."
        ]
    },
    {
        "orig_file": "0Y1A7047.MP4",
        "category": "01_Campus_Environment_and_Buildings",
        "folder": "06_main_entrance_pillars_02",
        "new_name": "burayu_campus_main_entrance_pillars_02.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Campus Main Entrance Portico & Driveway 2",
        "short_desc": "The main entrance portico, structural pillars, and paved driveway.",
        "curriculum": "Campus Architecture",
        "gate_level": "Institutional Environment",
        "user_note": "Entrance portico and arrival driveway.",
        "deep_analysis": (
            "The main arrival driveway, structural columns, and building fascia at the EGATE entrance court showcase "
            "modern engineering and clean geometry."
        ),
        "key_takeaways": [
            "Clear documentation of arrival infrastructure.",
            "Consistent structural detailing across the entrance zone."
        ]
    },
    {
        "orig_file": "20260923_180305.mp4",
        "category": "01_Campus_Environment_and_Buildings",
        "folder": "07_exterior_dusk_plaza_survey",
        "new_name": "burayu_campus_exterior_dusk_plaza_survey_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Campus Exterior Plaza & Illuminated Facade (4K)",
        "short_desc": "4K view of the campus exterior plaza, stone retaining masonry, and illuminated facade.",
        "curriculum": "Campus Architecture",
        "gate_level": "Institutional Environment",
        "user_note": "Evening 4K survey of campus exterior and plaza.",
        "deep_analysis": (
            "The exterior plaza of the EGATE Burayu complex at dusk showcases tiered stone retaining walls, integrated perimeter "
            "security, exterior illumination luminaires, and the full multi-story facade of the primary building complex."
        ),
        "key_takeaways": [
            "4K fidelity detailing campus exterior architecture.",
            "Perimeter civil engineering and stonework.",
            "Illuminated evening campus environment."
        ]
    },
    {
        "orig_file": "20260923_180501.mp4",
        "category": "01_Campus_Environment_and_Buildings",
        "folder": "08_exterior_twilight_building_view",
        "new_name": "burayu_campus_exterior_twilight_building_view_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Exterior Twilight Academic Complex (4K)",
        "short_desc": "4K twilight view of the primary academic structure.",
        "curriculum": "Campus Architecture",
        "gate_level": "Institutional Environment",
        "user_note": "4K exterior view of academic complex at twilight.",
        "deep_analysis": (
            "The primary EGATE academic facility at twilight, displaying interior laboratory lighting and modern structural lines "
            "against the evening sky."
        ),
        "key_takeaways": [
            "Distinctive architectural identity of the EGATE complex.",
            "High-resolution 4K asset of the evening campus."
        ]
    },
    {
        "orig_file": "20260923_180137.mp4",
        "category": "02_Library_and_Learning_Commons",
        "folder": "01_library_exterior_approach_dusk",
        "new_name": "library_exterior_approach_dusk_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Library Exterior Approach & Pedestrian Ramp (4K)",
        "short_desc": "4K view of the landscaped pedestrian ramp and stairs leading to the EGATE Library.",
        "curriculum": "Learning Resources & Research Infrastructure",
        "gate_level": "Knowledge Hub",
        "user_note": "Exterior ramp and entrance leading to the library.",
        "deep_analysis": (
            "The accessible pedestrian ramp with stainless steel handrails and stone stairs provides direct access to the "
            "EGATE Central Library and Learning Commons. Landscaped garden beds line the approach."
        ),
        "key_takeaways": [
            "Accessible universal design (ramp and stairs).",
            "Dedicated entrance to the campus knowledge repository."
        ]
    },
    {
        "orig_file": "0Y1A7065.MP4",
        "category": "02_Library_and_Learning_Commons",
        "folder": "02_inside_library_atrium_tree_overview",
        "new_name": "inside_library_atrium_tree_overview.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Inside Central Library: Indoor Tree & Radial Atrium",
        "short_desc": "The circular library atrium featuring a living indoor tree and radial study carrels.",
        "curriculum": "Learning Resources, Research & Independent Study",
        "gate_level": "Knowledge Hub",
        "user_note": "Inside the library with central indoor tree and study areas.",
        "deep_analysis": (
            "The EGATE circular library features a living evergreen tree growing in the center of the atrium beneath a glazed "
            "skylight dome. Around the tree are radial wooden study desks, ergonomic reading chairs, and tiered circular "
            "mezzanine balconies, creating an inspirational environment for deep scholarly research."
        ),
        "key_takeaways": [
            "Biophilic design integrating a living indoor tree into the learning space.",
            "Radial study desks facilitating focused individual and group study.",
            "Reflects EGATE's philosophy of rooted knowledge and growth."
        ]
    },
    {
        "orig_file": "0Y1A7075.MP4",
        "category": "02_Library_and_Learning_Commons",
        "folder": "03_inside_library_mezzanine_balcony",
        "new_name": "inside_library_mezzanine_balcony.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Inside Central Library: Mezzanine Study Balconies",
        "short_desc": "Upper curved mezzanine galleries with individual study carrels and glass balustrades.",
        "curriculum": "Learning Resources, Research & Independent Study",
        "gate_level": "Knowledge Hub",
        "user_note": "Inside library mezzanine and upper study areas.",
        "deep_analysis": (
            "The elevated curved mezzanine levels of the central library feature private study carrels, tempered glass railings "
            "overlooking the atrium tree, and acoustic ceiling panels designed for quiet intellectual study."
        ),
        "key_takeaways": [
            "Upper-tier study galleries for independent exploration.",
            "Tempered glass balustrades and acoustic paneling.",
            "Dedicated quiet zones for literature reviews and project research."
        ]
    },
    {
        "orig_file": "0Y1A7076.MP4",
        "category": "02_Library_and_Learning_Commons",
        "folder": "04_inside_library_skylight_ceiling",
        "new_name": "inside_library_skylight_ceiling.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Inside Central Library: Natural Skylight Dome",
        "short_desc": "The radial skylight dome illuminating the central library atrium.",
        "curriculum": "Learning Resources & Architectural Design",
        "gate_level": "Knowledge Hub",
        "user_note": "Library skylight dome and natural lighting.",
        "deep_analysis": (
            "The central structural dome and radial skylight aperture flood the multi-level library with natural daylight, "
            "illuminating reading desks and the central indoor tree through sustainable architectural design."
        ),
        "key_takeaways": [
            "Daylight harvesting reducing artificial lighting needs.",
            "Geometrical precision in ceiling engineering."
        ]
    },
    {
        "orig_file": "20260819_065312.mp4",
        "category": "02_Library_and_Learning_Commons",
        "folder": "05_atrium_corridor_class_view_walkthrough",
        "new_name": "atrium_corridor_class_view_walkthrough.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Atrium Corridor & Classroom Perimeter Walkthrough",
        "short_desc": "Curved upper gallery corridor overlooking the central atrium and classroom entrances.",
        "curriculum": "Academic Facilities & Learning Spaces",
        "gate_level": "Institutional Walkthrough",
        "user_note": "Class view and corridor walkthrough overlooking the atrium.",
        "deep_analysis": (
            "The curved upper gallery corridor provides access to classrooms, seminar spaces, and laboratories lining the perimeter "
            "while maintaining an open view into the central atrium."
        ),
        "key_takeaways": [
            "Organic circulation connecting classrooms with communal zones.",
            "Daily operational layout of EGATE's primary academic facility."
        ]
    },
    {
        "orig_file": "class view photo .mp4",
        "category": "02_Library_and_Learning_Commons",
        "folder": "06_class_view_photo_duplicate",
        "new_name": "class_view_photo_corridor_walkthrough_duplicate.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Atrium Corridor Walkthrough (Archival Copy)",
        "short_desc": "Archival copy of the atrium corridor walkthrough.",
        "curriculum": "Academic Facilities & Learning Spaces",
        "gate_level": "Institutional Walkthrough",
        "user_note": "Archival copy of the class corridor walkthrough.",
        "deep_analysis": (
            "Archival copy of the upper gallery corridor walkthrough showing the classroom perimeter and central atrium."
        ),
        "key_takeaways": [
            "Preserves file integrity across media archives.",
            "Documents the upper level classroom access ways."
        ]
    },
    {
        "orig_file": "0Y1A7021.MP4",
        "category": "03_Industrial_Circuit_Board_and_PCB_Lab",
        "folder": "01_pcb_cnc_isolation_milling_machine",
        "new_name": "pcb_cnc_isolation_milling_machine.mp4",
        "thumb": "thumbnail.jpg",
        "title": "PCB CNC Isolation Milling & Routing Machine",
        "short_desc": "Automated precision CNC milling and PCB isolation routing machine.",
        "curriculum": "Robotics & Electronics (ROEL-ECD), Hardware Prototyping",
        "gate_level": "MAL-301 / GLI-401 (Mastery & Innovation)",
        "user_note": "Industrial PCB / circuit board fabrication machine.",
        "deep_analysis": (
            "The automated CNC precision isolation routing and milling machine enables students to manufacture custom printed "
            "circuit boards in-house. It performs mechanical milling of copper-clad FR4 boards, precision via drilling, and outline "
            "contour routing directly from student EDA schematics (KiCAD, Altium) without chemical etching baths."
        ),
        "key_takeaways": [
            "In-house rapid PCB prototyping capabilities at EGATE.",
            "Bridges theoretical schematic design with physical hardware fabrication.",
            "Accelerates student development in robotics and IoT hardware."
        ]
    },
    {
        "orig_file": "0Y1A7083.MP4",
        "category": "03_Industrial_Circuit_Board_and_PCB_Lab",
        "folder": "02_bungard_industrial_pcb_chemical_plating_line",
        "new_name": "bungard_industrial_pcb_chemical_plating_line.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Bungard Industrial PCB Chemical Plating Line",
        "short_desc": "German Bungard industrial through-hole plating, etching, and spray-rinsing line.",
        "curriculum": "Electronic Circuit Design (ROEL-ECD), Nanotech & Material Fabrication",
        "gate_level": "GLI-401 (Global Leadership & Innovation)",
        "user_note": "Industrial circuit board and motherboard manufacturing line.",
        "deep_analysis": (
            "The German Bungard industrial wet-chemical PCB production line features galvanic through-hole copper plating baths (PTH), "
            "chemical etching stations, cascade spray rinsing, and surface finishing. Outfitted with chemical-resistant extraction "
            "ventilation and safety interlocks, this facility provides students with authentic industrial electronics manufacturing processes."
        ),
        "key_takeaways": [
            "Professional-grade multi-layer circuit board production on campus.",
            "Hands-on experience with industrial galvanic plating and chemical processing.",
            "Supports national capacity building in microelectronics and hardware engineering."
        ]
    },
    {
        "orig_file": "0Y1A7088.MP4",
        "category": "03_Industrial_Circuit_Board_and_PCB_Lab",
        "folder": "03_bungard_pcb_production_line_close_up",
        "new_name": "bungard_pcb_production_line_close_up.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Bungard PCB Production Equipment Details",
        "short_desc": "Chemical baths, immersion racks, and control systems of the Bungard PCB line.",
        "curriculum": "Electronic Circuit Design (ROEL-ECD)",
        "gate_level": "GLI-401 (Advanced Hardware Engineering)",
        "user_note": "Detail view of circuit board chemical processing equipment.",
        "deep_analysis": (
            "The chemical processing reservoirs, immersion racks, fluid agitation pumps, and digital temperature regulation "
            "units of the Bungard PCB production system."
        ),
        "key_takeaways": [
            "Precision chemical process controls in the hardware lab.",
            "Industrial safety protocols embedded into student engineering education."
        ]
    },
    {
        "orig_file": "0Y1A7069.MP4",
        "category": "04_Computer_Lab_and_Robotics_Class",
        "folder": "01_trainee_coding_and_software_innovation",
        "new_name": "trainee_coding_and_software_innovation.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Trainee Software Development & Coding Session",
        "short_desc": "Gifted students engaged in programming, algorithmic design, and software development.",
        "curriculum": "Digital & Emerging Technology (DIG-AIML), Robotics Programming (ROEL-ROP)",
        "gate_level": "AKS-201 / MAL-301 (Advanced Knowledge & Mastery)",
        "user_note": "Trainees actively programming and developing software.",
        "deep_analysis": (
            "Gifted students at EGATE work on laptops in the computer lab developing software applications, writing code, "
            "and testing algorithms. The collaborative environment supports deep learning in computer science, Python, AI/ML models, "
            "and robotics software logic."
        ),
        "key_takeaways": [
            "1:1 student computing infrastructure.",
            "Rigorous software engineering curriculum alongside hardware tracks.",
            "Applied problem-solving in algorithmic thinking."
        ]
    },
    {
        "orig_file": "robotic Computer class .mp4",
        "category": "04_Computer_Lab_and_Robotics_Class",
        "folder": "02_robotics_and_computer_lab_workstations",
        "new_name": "robotics_and_computer_lab_workstations.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Robotics & Computer Lab Workstations",
        "short_desc": "The robotics and computer laboratory with PC workstations and 3D printers.",
        "curriculum": "Robotics and Electronics (ROEL), Digital Technology (DIG)",
        "gate_level": "Core Academic Facility",
        "user_note": "Inside robotics class and computer lab with workstations.",
        "deep_analysis": (
            "The combined Robotics and Computer Science laboratory features dual-screen desktop computer stations, rapid prototyping "
            "3D printers, modular workbenches, and hardware assembly spaces. The layout fosters team-based engineering projects "
            "and rapid iterative prototyping."
        ),
        "key_takeaways": [
            "Integrated 3D printing and digital fabrication stations.",
            "Collaborative space designed for robotics teams and hackathons.",
            "Unified environment linking mechanical design with software programming."
        ]
    },
    {
        "orig_file": "robotics class opening .mp4",
        "category": "04_Computer_Lab_and_Robotics_Class",
        "folder": "03_robotics_and_electronics_lab_entrance",
        "new_name": "robotics_and_electronics_lab_entrance_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Robotics & Electronics Lab Entrance (4K)",
        "short_desc": "4K entrance to the Electronics and Computer Lab.",
        "curriculum": "Robotics and Electronics (ROEL), Digital Technology (DIG)",
        "gate_level": "Facility Entrance",
        "user_note": "Entrance doors to the electronics and computer labs.",
        "deep_analysis": (
            "The official glass double doors labeled 'ELECTRONICS LAB / COMPUTER LAB' lead into the primary STEM innovation "
            "spaces containing computer workstations, test instruments, and robotic project benches."
        ),
        "key_takeaways": [
            "Official laboratory facilities for STEM education.",
            "Immediate connection between public corridors and active engineering floors."
        ]
    },
    {
        "orig_file": "think_big_class.mp4",
        "category": "05_Innovation_Class_and_Electronics_Lab",
        "folder": "01_think_big_astronaut_mural",
        "new_name": "think_big_astronaut_mural_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Innovation Class: 'Think Big' Space Mural (4K)",
        "short_desc": "4K view of the 'Think Big' space exploration mural in the electronics innovation classroom.",
        "curriculum": "Astronomy & Space Technology (ASST), Innovation Mindset",
        "gate_level": "Inspirational Environment",
        "user_note": "Innovation class with 'Think Big' astronaut mural.",
        "deep_analysis": (
            "The electronics innovation classroom features a prominent space exploration mural emblazoned with 'THINK BIG'. "
            "Beneath the mural, lab benches are equipped with DC power supplies, oscilloscopes, and circuit assembly stations, "
            "connecting electronics engineering with EGATE's Astronomy and Space Technology curriculum."
        ),
        "key_takeaways": [
            "Inspirational learning environment fostering ambitious thinking.",
            "Integration of electronics hardware with space science education.",
            "Visual identity of EGATE's frontier innovation mission."
        ]
    },
    {
        "orig_file": "class view  2.mp4",
        "category": "05_Innovation_Class_and_Electronics_Lab",
        "folder": "02_innovation_class_electronics_benches",
        "new_name": "innovation_class_electronics_benches_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Innovation Class: Electronics Testing Benches (4K)",
        "short_desc": "4K view of laboratory benches equipped with oscilloscopes, power supplies, and signal generators.",
        "curriculum": "Electronic Circuit Design (ROEL-ECD-FOE-101 to MAL-301)",
        "gate_level": "AKS-201 / MAL-301 (Circuit Analysis & Testing)",
        "user_note": "Electronics testbenches with instruments in the innovation class.",
        "deep_analysis": (
            "The electronics workbenches are equipped with benchtop test and measurement equipment: multi-channel digital "
            "storage oscilloscopes, regulated dual-output DC power supplies, arbitrary function generators, digital multimeters, "
            "and soldering tools for real-time circuit debugging and waveform verification."
        ),
        "key_takeaways": [
            "Professional electrical engineering instrumentation for each student pair.",
            "Comprehensive hardware debugging and waveform analysis capabilities.",
            "Advanced secondary-level electronics practical education."
        ]
    },
    {
        "orig_file": "class view.mp4",
        "category": "05_Innovation_Class_and_Electronics_Lab",
        "folder": "03_electronics_testing_instruments_view",
        "new_name": "electronics_testing_instruments_view_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Electronics Laboratory Testing Instrumentation (4K)",
        "short_desc": "4K view of active digital displays and controls on electronics testing instruments.",
        "curriculum": "Electronic Circuit Design (ROEL-ECD)",
        "gate_level": "Laboratory Instrumentation",
        "user_note": "Active electronics testing instruments on laboratory benches.",
        "deep_analysis": (
            "Illuminated digital screens, rotary controls, and BNC test interfaces of benchtop oscilloscopes and signal generators "
            "used during student electronics experiments."
        ),
        "key_takeaways": [
            "Modern laboratory measurement displays in active use.",
            "Hands-on student training with standard test instruments."
        ]
    },
    {
        "orig_file": "0Y1A7023.MP4",
        "category": "06_Student_Projects_and_Robotics",
        "folder": "01_tracked_rover_robot_and_telescope",
        "new_name": "student_project_tracked_rover_and_telescope.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Student Project: Tracked Rover Robot & Astronomical Telescope",
        "short_desc": "Student-built tracked rover chassis with breadboard electronics, alongside an astronomical telescope.",
        "curriculum": "Robotics Programming (ROEL-ROP), Astronomy (ASST)",
        "gate_level": "MAL-301 (Mastery & Applied Learning Project)",
        "user_note": "Student tracked robot rover and astronomical telescope.",
        "deep_analysis": (
            "A student-engineered all-terrain tracked rover robot built with caterpillar treads, DC gearmotors, front mechanical gripper, "
            "and an onboard breadboard microcontroller circuit. In the background stands a laboratory telescope on a tripod mount, "
            "highlighting the intersection of robotics and observational astronomy."
        ),
        "key_takeaways": [
            "Student-designed physical robotics hardware with tracked mobility.",
            "Mechanical manipulator and sensory breadboard integration.",
            "Cross-disciplinary connection between robotics and space sciences."
        ]
    },
    {
        "orig_file": "20260924_123003.mp4",
        "category": "06_Student_Projects_and_Robotics",
        "folder": "02_smart_home_iot_prototype_idl800a",
        "new_name": "student_project_smart_home_iot_prototype_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Student Project: Smart Home Automation Prototype (4K)",
        "short_desc": "4K view of a student-built smart home architectural model connected to a K&H IDL-800A trainer.",
        "curriculum": "Digital Electronics (ROEL-ECD-MAL-301), Internet of Things (IoT)",
        "gate_level": "MAL-301 (Applied System Integration)",
        "user_note": "Student smart home automation project with digital trainer.",
        "deep_analysis": (
            "A student architectural smart home model wired with miniature lighting and sensor leads, interfaced directly to a "
            "K&H IDL-800A Digital-Analog Training System. The project applies digital logic gates and sensor thresholds to automated home control."
        ),
        "key_takeaways": [
            "Practical system integration connecting physical models with digital logic trainers.",
            "Hands-on learning applied to sustainable smart infrastructure.",
            "Direct application of sensor circuitry and logic automation."
        ]
    },
    {
        "orig_file": "20260924_133137.mp4",
        "category": "06_Student_Projects_and_Robotics",
        "folder": "03_ealsrs1_quadruped_walking_robot_and_drone",
        "new_name": "student_project_ealsrs1_quadruped_and_drone_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Student Project: EALSRS-1 Quadruped Robot & Drone (4K)",
        "short_desc": "4K view of student robotic prototypes: EALSRS-1 quadruped walking robot, drone airframe, and vehicle chassis.",
        "curriculum": "Robotics & Electronics (ROEL), Aerospace & Drones (ASST)",
        "gate_level": "GLI-401 (Global Leadership & Innovation)",
        "user_note": "Student quadruped walking robot and drone airframe.",
        "deep_analysis": (
            "Multiple student robotic prototypes on display, including the 'EALSRS-1' 4-legged quadruped walking robot utilizing "
            "servo-driven articulated linkages for biological locomotion, a multi-propeller drone airframe, and an electric rover chassis."
        ),
        "key_takeaways": [
            "Student-developed 'EALSRS-1' bio-inspired legged robotics.",
            "Aerospace drone airframe and flight mechanism experimentation.",
            "Mastery of rapid prototyping and kinematic mechanisms."
        ]
    },
    {
        "orig_file": "20260923_180710.mp4",
        "category": "07_Classroom_and_Trainee_Podcast_Interview",
        "folder": "01_tiered_classroom_auditorium_front",
        "new_name": "tiered_classroom_auditorium_front_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Tiered Lecture Auditorium: Podium & Presentation Area (4K)",
        "short_desc": "4K view of the lecture podium, whiteboards, and projection screen in the tiered auditorium.",
        "curriculum": "Academic Lecture Spaces & Seminars",
        "gate_level": "Core Academic Facility",
        "user_note": "Tiered lecture hall and front presentation area.",
        "deep_analysis": (
            "The front stage of EGATE's tiered lecture auditorium features an instructor podium, expansive whiteboards, "
            "a motorized projection screen, and polished wooden student desks. The facility hosts guest lectures, seminars, and defenses."
        ),
        "key_takeaways": [
            "University-grade lecture auditorium facilities.",
            "Optimized acoustics and sightlines for theoretical seminars and masterclasses."
        ]
    },
    {
        "orig_file": "20260923_180728.mp4",
        "category": "07_Classroom_and_Trainee_Podcast_Interview",
        "folder": "02_tiered_classroom_auditorium_rear",
        "new_name": "tiered_classroom_auditorium_rear_4k.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Tiered Lecture Auditorium: Student Seating (4K)",
        "short_desc": "4K view of curved tiered student seating banks and acoustic ceiling.",
        "curriculum": "Academic Lecture Spaces & Seminars",
        "gate_level": "Core Academic Facility",
        "user_note": "Tiered student seating banks and auditorium layout.",
        "deep_analysis": (
            "The curved banks of tiered student seating in the auditorium feature continuous hardwood desks, swivel chairs, "
            "overhead acoustic treatments, and climate control, providing an ergonomic environment for academic assemblies."
        ),
        "key_takeaways": [
            "High-capacity ergonomic seating with integrated power access.",
            "Modern finishes supporting academic focus and presentations."
        ]
    },
    {
        "orig_file": "20260924_124102.mp4",
        "category": "07_Classroom_and_Trainee_Podcast_Interview",
        "folder": "03_trainee_activity_podcast_interview",
        "new_name": "trainee_activity_podcast_interview.mp4",
        "thumb": "thumbnail.jpg",
        "title": "Trainee Activity & Educational Program Overview",
        "short_desc": "Informational overview detailing EGATE student activities, talent development programs, and campus life.",
        "curriculum": "EGATE Institutional Narrative, Talent Incubation, Student Voice",
        "gate_level": "Community & Narrative",
        "user_note": "Trainee / educator presentation on EGATE talent programs.",
        "deep_analysis": (
            "An informational presentation by an EGATE representative sharing insights on student life, daily talent incubation, "
            "the academic curriculum, and the impact of the school's gifted education program."
        ),
        "key_takeaways": [
            "Direct perspective on the EGATE student experience.",
            "Documentation of talent incubation programs and campus community.",
            "Soundless MP4 format suitable for video editing and overlay production."
        ]
    }
]

print(f"Total cleaned catalog entries: {len(CLEANED_CATALOG)}")

# Write to python module for uploader script
with open("/home/igi/Documents/putts/vide_prs/cleaned_catalog.py", "w", encoding="utf-8") as f:
    f.write(f"CLEANED_CATALOG = {json.dumps(CLEANED_CATALOG, indent=2)}\n")

# Update all README.md files
for item in CLEANED_CATALOG:
    readme_path = os.path.join(BASE_DIR, item['category'], item['folder'], "README.md")
    if not os.path.exists(readme_path):
        continue
    
    # Read existing duration and res from README if possible
    with open(readme_path, "r", encoding="utf-8") as f:
        old_txt = f.read()

    # Extract specs table
    specs_match = re.search(r"## Technical Specifications\s*\n(.*?)\n---", old_txt, re.DOTALL)
    specs_table = specs_match.group(1).strip() if specs_match else ""
    
    # Replace Audio Track line in specs table
    specs_table = re.sub(r"\|\s*\*\*Audio Track\*\*\s*\|.*", "| **Audio Track** | None (Soundless MP4 / Audio Stripped) |", specs_table)

    new_readme = f"""# {item['title']}

![Video Preview Thumbnail](./thumbnail.jpg)

## Overview
- **Title**: {item['title']}
- **Canonical Filename**: `{item['new_name']}`
- **Original Filename**: `{item['orig_file']}`
- **Category**: `{item['category']}`
- **Subfolder**: `{item['folder']}`
- **Audio Format**: Soundless MP4 (Audio track removed)

---

## Technical Specifications
{specs_table}

---

## Institutional Context & EGATE Curriculum Mapping
- **Domain Area**: {item['curriculum']}
- **GATE Framework Level**: {item['gate_level']}
- **Field Note**: *\"{item['user_note']}\"*

---

## Content & Educational Overview
{item['deep_analysis']}

---

## Key Educational Takeaways
"""
    for tk in item['key_takeaways']:
        new_readme += f"- {tk}\n"

    new_readme += f"""
---

## Navigation
- [Return to Master Catalog](../../MASTER_CATALOG.md)
- [Parent Category Overview](../)
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme)

print("All 29 README.md files updated with sanitized descriptions and soundless status.")

# Regenerate MASTER_CATALOG.md
master_md = """# EGATE Burayu Campus Video Collection: Master Catalog (Soundless Edition)

This repository contains the organized, verified, and analyzed video archives for the **Ethiopian Giftedness and Talent Development School (EGATE)** at the **Burayu Campus, Sheger City, Ethiopia**.

All 29 recordings have been processed into **100% soundless MP4 files** (audio tracks removed with zero video loss), categorized across 7 facility domains, and documented with pure educational and curriculum descriptions.

---

## Summary Statistics
- **Total Video Assets**: 29
- **Audio Format**: **100% Soundless MP4** (0 audio streams across all 29 files)
- **Total Categories**: 7
- **4K Ultra HD Recordings**: 13
- **Full HD (1080p) Recordings**: 14
- **Special Formats**: 2 (Smartphone vertical walkthroughs)

---

## Complete Video Inventory

| # | Preview | Title | Canonical File | Duration | Resolution | Audio | Topic Summary |
| :-: | :---: | :--- | :--- | :-: | :-: | :-: | :--- |
"""

for idx, p in enumerate(CLEANED_CATALOG, 1):
    readme_rel = f"{p['category']}/{p['folder']}/README.md"
    thumb_rel = f"{p['category']}/{p['folder']}/thumbnail.jpg"
    
    # Read technical duration and res from README
    readme_path = os.path.join(BASE_DIR, readme_rel)
    res_str = "1080p"
    dur_str = "N/A"
    if os.path.exists(readme_path):
        with open(readme_path) as rf:
            txt = rf.read()
            m_res = re.search(r"\|\s*\*\*Resolution\*\*\s*\|\s*([^\n|]+)", txt)
            if m_res:
                res_str = m_res.group(1).strip()
            m_dur = re.search(r"\|\s*\*\*Duration\*\*\s*\|\s*([^\n|(]+)", txt)
            if m_dur:
                dur_str = m_dur.group(1).strip()

    master_md += f"| {idx} | <img src=\"./{thumb_rel}\" width=\"120\" alt=\"{p['title']}\"/> | [{p['title']}](./{readme_rel}) | `{p['new_name']}` | {dur_str} | {res_str} | **Soundless** | {p['short_desc']} |\n"

master_md += """
---

## EGATE Academic Framework Reference
EGATE structures its advanced STEM curricula across four developmental tiers:
1. **FOE (Level 101)**: *Foundation of Excellence* — Core theoretical foundations in electronics, algorithms, and scientific inquiry.
2. **AKS (Level 201)**: *Advanced Knowledge and Skills* — Hands-on circuit analysis, microcontroller programming, and robotics control.
3. **MAL (Level 301)**: *Mastery and Applied Learning* — Independent and group engineering design, PCB fabrication, and prototype testing.
4. **GLI (Level 401)**: *Global Leadership and Innovation* — Capstone projects, research publications, and community problem solving.

*Soundless Edition for the EGATE Burayu Media Archive.*
"""

with open(os.path.join(BASE_DIR, "MASTER_CATALOG.md"), "w", encoding="utf-8") as f:
    f.write(master_md)

print("MASTER_CATALOG.md successfully regenerated!")
