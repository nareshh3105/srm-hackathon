import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME   = "llama-3.3-70b-versatile"
LANGUAGES    = ["Hinglish", "Tanglish"]

# ── Class & Group structure ──────────────────────────────────────────────────
CLASSES      = ["Class 8", "Class 9", "Class 10", "Class 11", "Class 12"]
GROUPS_11_12 = ["Bio-Maths", "Computer Science", "Commerce"]

SUBJECTS_8_10 = ["Science", "Social Science", "Mathematics", "English", "Hindi", "Tamil"]

SUBJECTS_11_12 = {
    "Bio-Maths":        ["Physics", "Chemistry", "Biology", "Mathematics", "English"],
    "Computer Science": ["Physics", "Chemistry", "Mathematics", "Computer Science", "English"],
    "Commerce":         ["Business Studies", "Economics", "Accountancy", "Mathematics", "English"],
}

# ── Chapter lists ────────────────────────────────────────────────────────────

_CHAPTERS_8 = {
    "Science": [
        "Crop Production and Management",
        "Microorganisms: Friend and Foe",
        "Synthetic Fibres and Plastics",
        "Materials: Metals and Non-Metals",
        "Coal and Petroleum",
        "Combustion and Flame",
        "Conservation of Plants and Animals",
        "Cell - Structure and Functions",
        "Reproduction in Animals",
        "Reaching the Age of Adolescence",
        "Force and Pressure",
        "Friction",
        "Sound",
        "Chemical Effects of Electric Current",
        "Some Natural Phenomena",
        "Light",
    ],
    "Social Science": [
        "History: How, When and Where",
        "History: From Trade to Territory",
        "History: Ruling the Countryside",
        "History: Tribals, Dikus and the Vision of a Golden Age",
        "History: When People Rebel",
        "History: Weavers, Iron Smelters and Factory Owners",
        "History: Civilising the Native, Educating the Nation",
        "History: Women, Caste and Reform",
        "History: The Making of the National Movement",
        "History: India After Independence",
        "Geography: Resources",
        "Geography: Land, Soil, Water, Natural Vegetation and Wildlife",
        "Geography: Mineral and Power Resources",
        "Geography: Agriculture",
        "Geography: Industries",
        "Geography: Human Resources",
        "Civics: The Indian Constitution",
        "Civics: Understanding Secularism",
        "Civics: Why Do We Need a Parliament",
        "Civics: Understanding Laws",
        "Civics: Judiciary",
        "Civics: Understanding Our Criminal Justice System",
        "Civics: Understanding Marginalisation",
        "Civics: Confronting Marginalisation",
        "Civics: Public Facilities",
        "Civics: Law and Social Justice",
    ],
    "Mathematics": [
        "Rational Numbers",
        "Linear Equations in One Variable",
        "Understanding Quadrilaterals",
        "Data Handling",
        "Squares and Square Roots",
        "Cubes and Cube Roots",
        "Comparing Quantities",
        "Algebraic Expressions and Identities",
        "Mensuration",
        "Exponents and Powers",
        "Direct and Inverse Proportions",
        "Factorisation",
        "Introduction to Graphs",
    ],
    "English": [
        "Honeydew: The Best Christmas Present in the World",
        "Honeydew: The Tsunami",
        "Honeydew: Glimpses of the Past",
        "Honeydew: Bepin Choudhury's Lapse of Memory",
        "Honeydew: The Summit Within",
        "Honeydew: This is Jody's Fawn",
        "Honeydew: A Visit to Cambridge",
        "Honeydew: A Short Monsoon Diary",
        "It So Happened: How the Camel Got His Hump",
        "It So Happened: Children at Work",
        "It So Happened: The Selfish Giant",
        "It So Happened: The Treasure Within",
        "It So Happened: Princess September",
        "It So Happened: The Fight",
        "It So Happened: The Open Window",
        "It So Happened: Jalebis",
    ],
    "Hindi": [
        "Vasant: Dhwani",
        "Vasant: Lakh ki Chudiyan",
        "Vasant: Bus ki Yatra",
        "Vasant: Diwanon ki Hasti",
        "Vasant: Chitthiyon ki Anoothi Duniya",
        "Vasant: Bhagwan ke Dakiye",
        "Vasant: Kya Nirash Hua Jaye",
        "Vasant: Yeh Sabse Kathin Samay Nahin",
        "Vasant: Kabir ki Sakhiyan",
        "Vasant: Kamchor",
        "Vasant: Jab Cinema ne Bolna Seekha",
        "Vasant: Sudama Charit",
        "Vasant: Jahan Pahiya Hai",
        "Vasant: Akbari Lota",
        "Vasant: Sur ke Pad",
        "Vasant: Paani ki Kahani",
        "Durva: Chapters (Various)",
    ],
    "Tamil": [
        "Iyal 1: Mudhal Padalam",
        "Iyal 2: Irandaam Padalam",
        "Iyal 3: Moondram Padalam",
        "Iyal 4: Nankam Padalam",
        "Iyal 5: Aindham Padalam",
        "Tamil Grammar: Ezhuttu",
        "Tamil Grammar: Sol",
        "Tamil Grammar: Porul",
    ],
}

_CHAPTERS_9 = {
    "Science": [
        "Matter in Our Surroundings",
        "Is Matter Around Us Pure",
        "Atoms and Molecules",
        "Structure of the Atom",
        "The Fundamental Unit of Life",
        "Tissues",
        "Motion",
        "Force and Laws of Motion",
        "Gravitation",
        "Work and Energy",
        "Sound",
        "Improvement in Food Resources",
    ],
    "Social Science": [
        "History: The French Revolution",
        "History: Socialism in Europe and the Russian Revolution",
        "History: Nazism and the Rise of Hitler",
        "History: Forest Society and Colonialism",
        "History: Pastoralists in the Modern World",
        "Geography: India - Size and Location",
        "Geography: Physical Features of India",
        "Geography: Drainage",
        "Geography: Climate",
        "Geography: Natural Vegetation and Wildlife",
        "Geography: Population",
        "Civics: What is Democracy? Why Democracy?",
        "Civics: Constitutional Design",
        "Civics: Electoral Politics",
        "Civics: Working of Institutions",
        "Civics: Democratic Rights",
        "Economics: The Story of Village Palampur",
        "Economics: People as Resource",
        "Economics: Poverty as a Challenge",
        "Economics: Food Security in India",
    ],
    "Mathematics": [
        "Number Systems",
        "Polynomials",
        "Coordinate Geometry",
        "Linear Equations in Two Variables",
        "Introduction to Euclid's Geometry",
        "Lines and Angles",
        "Triangles",
        "Quadrilaterals",
        "Circles",
        "Heron's Formula",
        "Surface Areas and Volumes",
        "Statistics",
    ],
    "English": [
        "Beehive: The Fun They Had",
        "Beehive: The Sound of Music",
        "Beehive: The Little Girl",
        "Beehive: A Truly Beautiful Mind",
        "Beehive: The Snake and the Mirror",
        "Beehive: My Childhood",
        "Beehive: Packing",
        "Beehive: Reach for the Top",
        "Beehive: The Bond of Love",
        "Beehive: Kathmandu",
        "Beehive: If I Were You",
        "Moments: The Lost Child",
        "Moments: The Adventures of Toto",
        "Moments: Iswaran the Storyteller",
        "Moments: In the Kingdom of Fools",
        "Moments: The Happy Prince",
        "Moments: Weathering the Storm in Ersama",
        "Moments: The Last Leaf",
        "Moments: A House is Not a Home",
        "Moments: The Accidental Tourist",
        "Moments: The Beggar",
    ],
    "Hindi": [
        "Kshitij: Surdas - Pad",
        "Kshitij: Mirabai - Pad",
        "Kshitij: Raidas - Pad",
        "Kshitij: Kabirdas - Sakhiyan evam Sabad",
        "Kshitij: Dharamvir Bharati - Agnipath",
        "Kshitij: Harivansh Rai Bachchan - Madhushala",
        "Kshitij: Mahadevi Verma - Ateet ke Chalchitr",
        "Kshitij: Hazari Prasad Dwivedi - Kalaram",
        "Kshitij: Premchand - Do Bailon ki Katha",
        "Kshitij: Rahul Sankrityayan - Smritiyon ki Karwan",
        "Kshitij: Shivpujan Sahay - Mera Chhota sa Niji Pulsataka",
        "Kshitij: Mannu Bhandari - Kailash Mansarovar",
        "Kritika: Is Jal Pralay Mein",
        "Kritika: Mere Sang ki Auraten",
        "Kritika: Reedh ki Haddi",
        "Kritika: Maati wali",
        "Kritika: Kis Tarah Aakhirkar Mein Hindi Mein Aaya",
    ],
    "Tamil": [
        "Iyal 1: Mudhal Padalam",
        "Iyal 2: Irandaam Padalam",
        "Iyal 3: Moondram Padalam",
        "Iyal 4: Nankam Padalam",
        "Iyal 5: Aindham Padalam",
        "Iyal 6: Aaram Padalam",
        "Tamil Grammar: Ezhuttu",
        "Tamil Grammar: Sol",
        "Tamil Grammar: Porul",
    ],
}

_CHAPTERS_10 = {
    "Science": [
        "Chemical Reactions and Equations",
        "Acids, Bases and Salts",
        "Metals and Non-metals",
        "Carbon and its Compounds",
        "Life Processes",
        "Control and Coordination",
        "How do Organisms Reproduce",
        "Heredity",
        "Light - Reflection and Refraction",
        "The Human Eye and the Colourful World",
        "Electricity",
        "Magnetic Effects of Electric Current",
        "Our Environment",
        "Sustainable Management of Natural Resources",
    ],
    "Social Science": [
        "History: The Rise of Nationalism in Europe",
        "History: Nationalism in India",
        "History: The Making of a Global World",
        "History: The Age of Industrialisation",
        "History: Print Culture and the Modern World",
        "Geography: Resources and Development",
        "Geography: Forest and Wildlife Resources",
        "Geography: Water Resources",
        "Geography: Agriculture",
        "Geography: Minerals and Energy Resources",
        "Geography: Manufacturing Industries",
        "Geography: Lifelines of National Economy",
        "Civics: Power Sharing",
        "Civics: Federalism",
        "Civics: Democracy and Diversity",
        "Civics: Gender, Religion and Caste",
        "Civics: Popular Struggles and Movements",
        "Civics: Political Parties",
        "Civics: Outcomes of Democracy",
        "Civics: Challenges to Democracy",
        "Economics: Development",
        "Economics: Sectors of the Indian Economy",
        "Economics: Money and Credit",
        "Economics: Globalisation and the Indian Economy",
        "Economics: Consumer Rights",
    ],
    "Mathematics": [
        "Real Numbers",
        "Polynomials",
        "Pair of Linear Equations in Two Variables",
        "Quadratic Equations",
        "Arithmetic Progressions",
        "Triangles",
        "Coordinate Geometry",
        "Introduction to Trigonometry",
        "Some Applications of Trigonometry",
        "Circles",
        "Areas Related to Circles",
        "Surface Areas and Volumes",
        "Statistics",
        "Probability",
    ],
    "English": [
        "FF: A Letter to God",
        "FF: Nelson Mandela - Long Walk to Freedom",
        "FF: Two Stories About Flying",
        "FF: From the Diary of Anne Frank",
        "FF: Glimpses of India",
        "FF: Mijbil the Otter",
        "FF: Madam Rides the Bus",
        "FF: The Sermon at Benares",
        "FF: The Proposal",
        "Footprints: A Triumph of Surgery",
        "Footprints: The Thief's Story",
        "Footprints: The Midnight Visitor",
        "Footprints: A Question of Trust",
        "Footprints: Footprints without Feet",
        "Footprints: The Making of a Scientist",
        "Footprints: The Necklace",
        "Footprints: The Hack Driver",
        "Footprints: Bholi",
        "Footprints: The Book That Saved the Earth",
    ],
    "Hindi": [
        "Kshitij: Surdas - Pad",
        "Kshitij: Tulsidas - Ram-Lakshman-Parshuram Samvad",
        "Kshitij: Dev - Savaiya aur Kavitt",
        "Kshitij: Jaishankar Prasad - Atmakadya",
        "Kshitij: Suryakant Tripathi Nirala - Utsah aur At Nahi Rahi Hai",
        "Kshitij: Nagarjun - Yeh Danturit Muskan aur Fasal",
        "Kshitij: Girija Kumar Mathur - Chhaya Mat Chuna",
        "Kshitij: Rituraj - Kanyadan",
        "Kshitij: Manglesh Dabral - Sangatkar",
        "Kshitij: Swayyam Prakash - Netaji ka Chashma",
        "Kshitij: Ramvriksha Benipuri - Balgobin Bhagat",
        "Kshitij: Yashpal - Lucknow ki Bhool",
        "Kshitij: Sarveshwar Dayal Saxena - Manviya Karuna ki Divya Chamak",
        "Kshitij: Manu Bhandari - Ek Kahani Yeh Bhi",
        "Kshitij: Mahavir Prasad Dwivedi - Stri Shiksha ke Virodhi Kutarkon ka Khandan",
        "Kshitij: Yatindra Mishra - Naubatkhane Mein Ibadat",
        "Kritika: Mata ka Anchal",
        "Kritika: George Pancham ki Naak",
        "Kritika: Sana Sana Hath Jodi",
        "Kritika: Ahi Thaiya Jhulni Herani Ho Rama",
        "Kritika: Maine Dekha Ek Aandha Maidan",
    ],
    "Tamil": [
        "Iyal 1: Karumai Niram",
        "Iyal 2: Vazhkai Payiram",
        "Iyal 3: Illam",
        "Iyal 4: Veedu",
        "Iyal 5: Maruthuvam",
        "Iyal 6: Vivasayam",
        "Iyal 7: Vilayattu",
        "Iyal 8: Kalaigal",
        "Tamil Grammar: Tholkappiyam",
        "Tamil Grammar: Idaichol",
        "Tamil Grammar: Punarchi",
        "Tamil Grammar: Porul Ilakkanam",
    ],
}

# ── Class 11 chapters ────────────────────────────────────────────────────────

_PHY_11 = [
    "Physical World",
    "Units and Measurements",
    "Motion in a Straight Line",
    "Motion in a Plane",
    "Laws of Motion",
    "Work, Energy and Power",
    "System of Particles and Rotational Motion",
    "Gravitation",
    "Mechanical Properties of Solids",
    "Mechanical Properties of Fluids",
    "Thermal Properties of Matter",
    "Thermodynamics",
    "Kinetic Theory",
    "Oscillations",
    "Waves",
]

_CHEM_11 = [
    "Some Basic Concepts of Chemistry",
    "Structure of Atom",
    "Classification of Elements and Periodicity in Properties",
    "Chemical Bonding and Molecular Structure",
    "Thermodynamics",
    "Equilibrium",
    "Redox Reactions",
    "Organic Chemistry: Basic Principles and Techniques",
    "Hydrocarbons",
    "Environmental Chemistry",
]

_BIO_11 = [
    "The Living World",
    "Biological Classification",
    "Plant Kingdom",
    "Animal Kingdom",
    "Morphology of Flowering Plants",
    "Anatomy of Flowering Plants",
    "Structural Organisation in Animals",
    "Cell: The Unit of Life",
    "Biomolecules",
    "Cell Cycle and Cell Division",
    "Photosynthesis in Higher Plants",
    "Respiration in Plants",
    "Plant Growth and Development",
    "Digestion and Absorption",
    "Breathing and Exchange of Gases",
    "Body Fluids and Circulation",
    "Excretory Products and their Elimination",
    "Locomotion and Movement",
    "Neural Control and Coordination",
    "Chemical Coordination and Integration",
]

_MATH_11 = [
    "Sets",
    "Relations and Functions",
    "Trigonometric Functions",
    "Complex Numbers and Quadratic Equations",
    "Linear Inequalities",
    "Permutations and Combinations",
    "Binomial Theorem",
    "Sequences and Series",
    "Straight Lines",
    "Conic Sections",
    "Introduction to Three Dimensional Geometry",
    "Limits and Derivatives",
    "Statistics",
    "Probability",
]

_CS_11 = [
    "Computer System",
    "Encoding Schemes and Number System",
    "Emerging Trends",
    "Introduction to Problem Solving",
    "Getting Started with Python",
    "Flow of Control",
    "Functions",
    "Strings",
    "Lists",
    "Tuples and Dictionaries",
    "Societal Impacts",
]

_ENG_11 = [
    "Hornbill: The Portrait of a Lady",
    "Hornbill: We're Not Afraid to Die",
    "Hornbill: Discovering Tut: The Saga Continues",
    "Hornbill: Landscape of the Soul",
    "Hornbill: The Ailing Planet",
    "Hornbill: The Browning Version",
    "Hornbill: The Adventure",
    "Hornbill: Silk Road",
    "Snapshots: The Summer of the Beautiful White Horse",
    "Snapshots: The Address",
    "Snapshots: Ranga's Marriage",
    "Snapshots: Albert Einstein at School",
    "Snapshots: Mother's Day",
    "Snapshots: The Ghat of the Only World",
    "Snapshots: Birth",
    "Snapshots: The Tale of Melon City",
]

_HINDI_11 = [
    "Aroh: Hum Toh Ek Ek Kar Jananenge",
    "Aroh: Meera ke Pad",
    "Aroh: Pathik",
    "Aroh: Veh Aankhein",
    "Aroh: Ghar ki Yaad",
    "Aroh: Chandragahana se Lautan Beli",
    "Aroh: Janmajat",
    "Aroh: Spiti Mein Baarish",
    "Aroh: Rajasthan ki Rajdhani Jaipur",
    "Aroh: Aao Milein Aashiqon Se",
    "Aroh: Main Kyun Likhta Hoon",
    "Vitan: Bhaarat Maata",
    "Vitan: Rajasthan ki Rajdhani",
    "Vitan: Aalo Aandhhari",
]

_TAMIL_11 = [
    "Iyal 1: Mudhal Padalam",
    "Iyal 2: Irandaam Padalam",
    "Iyal 3: Moondram Padalam",
    "Iyal 4: Nankam Padalam",
    "Iyal 5: Aindham Padalam",
    "Iyal 6: Aaram Padalam",
    "Tamil Grammar: Ezhuttu Ilakkanam",
    "Tamil Grammar: Sol Ilakkanam",
    "Tamil Grammar: Porul Ilakkanam",
    "Tamil Literature: Sangam Ilakkiyam",
]

_BS_11 = [
    "Business, Trade and Commerce",
    "Forms of Business Organisation",
    "Public, Private and Global Enterprises",
    "Business Services",
    "Emerging Modes of Business",
    "Social Responsibilities of Business and Business Ethics",
    "Formation of a Company",
    "Sources of Business Finance",
    "Small Business",
    "Internal Trade",
    "International Business",
]

_ECO_11 = [
    "Statistics: Introduction",
    "Statistics: Collection of Data",
    "Statistics: Organisation of Data",
    "Statistics: Presentation of Data",
    "Statistics: Measures of Central Tendency",
    "Statistics: Measures of Dispersion",
    "Statistics: Correlation",
    "Statistics: Index Numbers",
    "Statistics: Use of Statistical Tools",
    "IED: Indian Economy on the Eve of Independence",
    "IED: Indian Economy 1950-1990",
    "IED: Liberalisation, Privatisation and Globalisation",
    "IED: Poverty",
    "IED: Human Capital Formation in India",
    "IED: Rural Development",
    "IED: Employment: Growth, Informalisation and Other Issues",
    "IED: Infrastructure",
    "IED: Environment and Sustainable Development",
]

_ACC_11 = [
    "Introduction to Accounting",
    "Theory Base of Accounting",
    "Recording of Transactions I",
    "Recording of Transactions II",
    "Bank Reconciliation Statement",
    "Trial Balance and Rectification of Errors",
    "Depreciation, Provisions and Reserves",
    "Bill of Exchange",
    "Financial Statements I",
    "Financial Statements II",
    "Accounts from Incomplete Records",
    "Applications of Computers in Accounting",
    "Computerised Accounting System",
]

_CHAPTERS_11 = {
    "Bio-Maths": {
        "Physics":     _PHY_11,
        "Chemistry":   _CHEM_11,
        "Biology":     _BIO_11,
        "Mathematics": _MATH_11,
        "English":     _ENG_11,
        "Hindi":       _HINDI_11,
        "Tamil":       _TAMIL_11,
    },
    "Computer Science": {
        "Physics":          _PHY_11,
        "Chemistry":        _CHEM_11,
        "Mathematics":      _MATH_11,
        "Computer Science": _CS_11,
        "English":          _ENG_11,
        "Hindi":            _HINDI_11,
        "Tamil":            _TAMIL_11,
    },
    "Commerce": {
        "Business Studies": _BS_11,
        "Economics":        _ECO_11,
        "Accountancy":      _ACC_11,
        "Mathematics":      _MATH_11,
        "English":          _ENG_11,
        "Hindi":            _HINDI_11,
        "Tamil":            _TAMIL_11,
    },
}

# ── Class 12 chapters ────────────────────────────────────────────────────────

_PHY_12 = [
    "Electric Charges and Fields",
    "Electrostatic Potential and Capacitance",
    "Current Electricity",
    "Moving Charges and Magnetism",
    "Magnetism and Matter",
    "Electromagnetic Induction",
    "Alternating Current",
    "Electromagnetic Waves",
    "Ray Optics and Optical Instruments",
    "Wave Optics",
    "Dual Nature of Radiation and Matter",
    "Atoms",
    "Nuclei",
    "Semiconductor Electronics",
]

_CHEM_12 = [
    "The Solid State",
    "Solutions",
    "Electrochemistry",
    "Chemical Kinetics",
    "Surface Chemistry",
    "General Principles and Processes of Isolation of Elements",
    "The p-Block Elements",
    "The d- and f-Block Elements",
    "Coordination Compounds",
    "Haloalkanes and Haloarenes",
    "Alcohols, Phenols and Ethers",
    "Aldehydes, Ketones and Carboxylic Acids",
    "Amines",
    "Biomolecules",
    "Polymers",
    "Chemistry in Everyday Life",
]

_BIO_12 = [
    "Reproduction in Organisms",
    "Sexual Reproduction in Flowering Plants",
    "Human Reproduction",
    "Reproductive Health",
    "Principles of Inheritance and Variation",
    "Molecular Basis of Inheritance",
    "Evolution",
    "Human Health and Disease",
    "Strategies for Enhancement in Food Production",
    "Microbes in Human Welfare",
    "Biotechnology: Principles and Processes",
    "Biotechnology and its Applications",
    "Organisms and Populations",
    "Ecosystem",
    "Biodiversity and Conservation",
    "Environmental Issues",
]

_MATH_12 = [
    "Relations and Functions",
    "Inverse Trigonometric Functions",
    "Matrices",
    "Determinants",
    "Continuity and Differentiability",
    "Application of Derivatives",
    "Integrals",
    "Application of Integrals",
    "Differential Equations",
    "Vector Algebra",
    "Three Dimensional Geometry",
    "Linear Programming",
    "Probability",
]

_CS_12 = [
    "Python Revision Tour",
    "Exception Handling",
    "File Handling",
    "Recursion",
    "Searching",
    "Sorting",
    "Database Concepts and SQL",
    "Networking and Communication Technology",
    "Cybersecurity",
]

_ENG_12 = [
    "Flamingo: The Last Lesson",
    "Flamingo: Lost Spring",
    "Flamingo: Deep Water",
    "Flamingo: The Rattrap",
    "Flamingo: Indigo",
    "Flamingo: Poets and Pancakes",
    "Flamingo: The Interview",
    "Flamingo: Going Places",
    "Vistas: The Third Level",
    "Vistas: The Tiger King",
    "Vistas: Journey to the End of the Earth",
    "Vistas: The Enemy",
    "Vistas: Should Wizard Hit Mommy",
    "Vistas: On the Face of It",
    "Vistas: Evans Tries an O-level",
    "Vistas: Memories of Childhood",
]

_HINDI_12 = [
    "Aroh: Harivanshrai Bachchan - Madhushala",
    "Aroh: Algy Vajpayee - Kavitayen",
    "Aroh: Kunwar Narayan - Kavitayen",
    "Aroh: Raghuvir Sahay - Kavitayen",
    "Aroh: Sham Narayan Pandey - Hamid Khan",
    "Aroh: Umashankara Joshi - Kavitayen",
    "Aroh: Phaniswarnath Renu - Paanch Parmeshwar",
    "Aroh: Harishankar Parsai - Apna Apna Bhagya",
    "Aroh: Mannu Bhandari - Tin Jawab",
    "Aroh: Rambriksh Benipuri - Asthi Ksheera",
    "Aroh: Hari Shankar Parsai - Bichhaa",
    "Vitan: Surdas ki Jhopadi",
    "Vitan: Pahelvan ki Dholak",
    "Vitan: Shrinkhala ki Kadiyan",
]

_TAMIL_12 = [
    "Iyal 1: Mudhal Padalam",
    "Iyal 2: Irandaam Padalam",
    "Iyal 3: Moondram Padalam",
    "Iyal 4: Nankam Padalam",
    "Iyal 5: Aindham Padalam",
    "Iyal 6: Aaram Padalam",
    "Tamil Grammar: Ezhuttu Ilakkanam",
    "Tamil Grammar: Sol Ilakkanam",
    "Tamil Grammar: Porul Ilakkanam",
    "Tamil Literature: Sangam Ilakkiyam",
    "Tamil Literature: Bhakthi Ilakkiyam",
]

_BS_12 = [
    "Nature and Significance of Management",
    "Principles of Management",
    "Business Environment",
    "Planning",
    "Organising",
    "Staffing",
    "Directing",
    "Controlling",
    "Financial Management",
    "Financial Markets",
    "Marketing Management",
    "Consumer Protection",
]

_ECO_12_MACRO = [
    "Macro: Introduction to Macroeconomics",
    "Macro: National Income Accounting",
    "Macro: Money and Banking",
    "Macro: Income Determination",
    "Macro: Government Budget and the Economy",
    "Macro: Open Economy Macroeconomics",
]

_ECO_12_MICRO = [
    "Micro: Introduction to Microeconomics",
    "Micro: Theory of Consumer Behaviour",
    "Micro: Production and Costs",
    "Micro: The Theory of the Firm under Perfect Competition",
    "Micro: Market Equilibrium",
    "Micro: Non-Competitive Markets",
]

_ECO_12 = _ECO_12_MICRO + _ECO_12_MACRO

_ACC_12 = [
    "Accounting for Not-for-Profit Organisation",
    "Accounting for Partnership: Basic Concepts",
    "Reconstitution of a Partnership Firm — Admission of a Partner",
    "Reconstitution of a Partnership Firm — Retirement/Death of a Partner",
    "Dissolution of Partnership Firm",
    "Accounting for Share Capital",
    "Issue and Redemption of Debentures",
    "Financial Statements of a Company",
    "Analysis of Financial Statements",
    "Accounting Ratios",
    "Cash Flow Statement",
]

_CHAPTERS_12 = {
    "Bio-Maths": {
        "Physics":     _PHY_12,
        "Chemistry":   _CHEM_12,
        "Biology":     _BIO_12,
        "Mathematics": _MATH_12,
        "English":     _ENG_12,
        "Hindi":       _HINDI_12,
        "Tamil":       _TAMIL_12,
    },
    "Computer Science": {
        "Physics":          _PHY_12,
        "Chemistry":        _CHEM_12,
        "Mathematics":      _MATH_12,
        "Computer Science": _CS_12,
        "English":          _ENG_12,
        "Hindi":            _HINDI_12,
        "Tamil":            _TAMIL_12,
    },
    "Commerce": {
        "Business Studies": _BS_12,
        "Economics":        _ECO_12,
        "Accountancy":      _ACC_12,
        "Mathematics":      _MATH_12,
        "English":          _ENG_12,
        "Hindi":            _HINDI_12,
        "Tamil":            _TAMIL_12,
    },
}

# Master lookup
_ALL_CHAPTERS = {
    "Class 8":  _CHAPTERS_8,
    "Class 9":  _CHAPTERS_9,
    "Class 10": _CHAPTERS_10,
    "Class 11": _CHAPTERS_11,
    "Class 12": _CHAPTERS_12,
}

# ── Public helper functions ──────────────────────────────────────────────────

def get_subjects(class_name: str, group: str = None) -> list:
    if class_name in ("Class 11", "Class 12"):
        return SUBJECTS_11_12.get(group, list(SUBJECTS_11_12["Bio-Maths"]))
    return SUBJECTS_8_10


def get_chapters(class_name: str, subject: str, group: str = None) -> list:
    data = _ALL_CHAPTERS.get(class_name, {})
    if class_name in ("Class 11", "Class 12"):
        chapters = data.get(group, {}).get(subject, [])
    else:
        chapters = data.get(subject, [])
    return chapters or ["General Topics"]


# ── Starter questions ────────────────────────────────────────────────────────
# Chapter-specific ones only for Class 10 (existing); all others use fallback

STARTER_QUESTIONS_HINGLISH = {
    # Class 10 Science
    "Chemical Reactions and Equations": [
        "Bhai chemical reaction aur physical change mein kya difference hai?",
        "Oxidation aur reduction samjhao with example",
        "Balancing equations kaise karte hai?",
    ],
    "Acids, Bases and Salts": [
        "pH scale kya hota hai?",
        "Strong acid aur weak acid mein difference kya hai?",
        "Neutralisation reaction explain karo",
    ],
    "Metals and Non-metals": [
        "Metals aur non-metals ki properties kya hain?",
        "Ionic bond kaise banta hai?",
        "Corrosion kya hota hai aur isse kaise rokein?",
    ],
    "Carbon and its Compounds": [
        "Carbon ke allotropes kya hain?",
        "Organic compounds ke functional groups samjhao",
        "Soap kaise kaam karta hai?",
    ],
    "Life Processes": [
        "Photosynthesis aur respiration mein kya difference hai?",
        "Human digestive system explain karo",
        "Excretion kya hota hai?",
    ],
    "Control and Coordination": [
        "Nervous system kaise kaam karta hai?",
        "Hormones kya hote hain?",
        "Reflex action kya hota hai?",
    ],
    "How do Organisms Reproduce": [
        "Asexual aur sexual reproduction mein kya farak hai?",
        "Binary fission kya hota hai?",
        "Flowers mein reproduction kaise hota hai?",
    ],
    "Heredity": [
        "Mendel ke laws kya hain?",
        "Dominant aur recessive traits explain karo",
        "DNA kya hota hai?",
    ],
    "Light - Reflection and Refraction": [
        "Reflection ke laws kya hain?",
        "Concave aur convex mirror mein kya difference hai?",
        "Refraction kya hota hai?",
    ],
    "The Human Eye and the Colourful World": [
        "Human eye kaise kaam karta hai?",
        "Myopia aur hypermetropia kya hain?",
        "Rainbow kaise banta hai?",
    ],
    "Electricity": [
        "Ohm's Law kya hai?",
        "Series aur parallel circuits mein kya difference hai?",
        "Electric power kya hota hai?",
    ],
    "Magnetic Effects of Electric Current": [
        "Electromagnet kaise kaam karta hai?",
        "Electric motor ka principle kya hai?",
        "Faraday's law kya hai?",
    ],
    "Our Environment": [
        "Food chain aur food web kya hote hain?",
        "Biodegradable aur non-biodegradable waste mein fark?",
        "Ozone layer kya hoti hai?",
    ],
    "Sustainable Management of Natural Resources": [
        "Natural resources kya hain?",
        "3 R's (Reduce, Reuse, Recycle) explain karo",
        "Forest conservation kyu zaroori hai?",
    ],
    # Class 10 Maths
    "Real Numbers": [
        "Euclid's division lemma kya hai?",
        "Rational aur irrational numbers mein kya fark hai?",
        "HCF aur LCM kaise nikalte hain?",
    ],
    "Polynomials": [
        "Polynomial ke zeroes kaise nikalte hain?",
        "Division algorithm for polynomials explain karo",
        "Quadratic polynomial ka graph kaisa hota hai?",
    ],
    "Pair of Linear Equations in Two Variables": [
        "Substitution method se equations kaise solve karte hain?",
        "Graphically equations solve karne ka tarika samjhao",
        "Consistent aur inconsistent equations kya hoti hain?",
    ],
    "Quadratic Equations": [
        "Quadratic formula kya hai?",
        "Discriminant kya hota hai?",
        "Factorisation se quadratic equations kaise solve karte hain?",
    ],
    "Arithmetic Progressions": [
        "AP ki general term kya hoti hai?",
        "Sum of n terms formula samjhao",
        "AP mein common difference kaise nikaalte hain?",
    ],
    "Triangles": [
        "Similar triangles ki properties kya hain?",
        "Basic Proportionality Theorem kya hai?",
        "Pythagoras theorem prove karo",
    ],
    "Coordinate Geometry": [
        "Distance formula kya hai?",
        "Midpoint formula explain karo",
        "Section formula kya hoti hai?",
    ],
    "Introduction to Trigonometry": [
        "sin, cos, tan kya hote hain?",
        "Trigonometric identities yaad karne ka tarika kya hai?",
        "Complementary angles ka relation kya hai?",
    ],
    "Some Applications of Trigonometry": [
        "Angle of elevation aur depression kya hote hain?",
        "Height and distance problems kaise solve karte hain?",
        "Real life mein trigonometry kahan use hoti hai?",
    ],
    "Circles": [
        "Tangent aur chord mein kya difference hai?",
        "Tangent lengths equal kyu hoti hain?",
        "Cyclic quadrilateral ki property kya hai?",
    ],
    "Areas Related to Circles": [
        "Sector aur segment ka area kaise nikalte hain?",
        "Arc length formula kya hai?",
        "Semicircle ka area kaise nikalte hain?",
    ],
    "Surface Areas and Volumes": [
        "Cylinder ka curved surface area kya hota hai?",
        "Cone aur sphere ka volume formula samjhao",
        "Combination of solids ke problems kaise karte hain?",
    ],
    "Statistics": [
        "Mean, Median, Mode mein kya fark hai?",
        "Cumulative frequency table kaise banate hain?",
        "Ogive curve kya hoti hai?",
    ],
    "Probability": [
        "Probability ki definition kya hai?",
        "Complementary events kya hote hain?",
        "Equally likely outcomes explain karo",
    ],
}

STARTER_QUESTIONS_TANGLISH = {
    # Class 10 Science
    "Chemical Reactions and Equations": [
        "Chemical reaction-um physical change-um enna difference?",
        "Oxidation aur reduction-a example-oda explain pannu",
        "Equations balance pannuvadhu epdi?",
    ],
    "Acids, Bases and Salts": [
        "pH scale enna solludhu?",
        "Strong acid-um weak acid-um enna difference?",
        "Neutralisation reaction explain pannu",
    ],
    "Metals and Non-metals": [
        "Metals-um non-metals-um properties enna?",
        "Ionic bond epdi form aagudhu?",
        "Corrosion enna, epdi thadukkiradhu?",
    ],
    "Carbon and its Compounds": [
        "Carbon allotropes enna?",
        "Functional groups explain pannu",
        "Soap epdi work pannudhu?",
    ],
    "Life Processes": [
        "Photosynthesis-um respiration-um enna difference?",
        "Human digestive system explain pannu",
        "Excretion enna?",
    ],
    "Control and Coordination": [
        "Nervous system epdi work pannudhu?",
        "Hormones enna?",
        "Reflex action enna?",
    ],
    "How do Organisms Reproduce": [
        "Asexual-um sexual reproduction-um enna difference?",
        "Binary fission explain pannu",
        "Flowers-la reproduction epdi nadakkudhu?",
    ],
    "Heredity": [
        "Mendel laws enna?",
        "Dominant-um recessive traits-um explain pannu",
        "DNA enna?",
    ],
    "Light - Reflection and Refraction": [
        "Reflection laws enna?",
        "Concave-um convex mirror-um enna difference?",
        "Refraction enna?",
    ],
    "The Human Eye and the Colourful World": [
        "Human eye epdi work pannudhu?",
        "Myopia-um hypermetropia-um enna?",
        "Rainbow epdi form aagudhu?",
    ],
    "Electricity": [
        "Ohm's Law enna?",
        "Series-um parallel circuits-um enna difference?",
        "Electric power explain pannu",
    ],
    "Magnetic Effects of Electric Current": [
        "Electromagnet epdi work pannudhu?",
        "Electric motor principle enna?",
        "Faraday's law explain pannu",
    ],
    "Our Environment": [
        "Food chain-um food web-um enna?",
        "Biodegradable-um non-biodegradable-um enna difference?",
        "Ozone layer enna?",
    ],
    "Sustainable Management of Natural Resources": [
        "Natural resources enna?",
        "3 R's explain pannu",
        "Forest conservation yen mukkiyam?",
    ],
    # Class 10 Maths
    "Real Numbers": [
        "Euclid's division lemma enna?",
        "Rational-um irrational numbers-um enna difference?",
        "HCF-um LCM-um epdi kaankiradhu?",
    ],
    "Polynomials": [
        "Polynomial zeroes epdi kaankiradhu?",
        "Division algorithm explain pannu",
        "Quadratic polynomial graph epdi irukkum?",
    ],
    "Quadratic Equations": [
        "Quadratic formula enna?",
        "Discriminant enna?",
        "Factorisation-la solve pannuvadhu epdi?",
    ],
    "Arithmetic Progressions": [
        "AP general term enna?",
        "Sum of n terms formula explain pannu",
        "Common difference epdi kaankiradhu?",
    ],
    "Triangles": [
        "Similar triangles properties enna?",
        "Basic Proportionality Theorem enna?",
        "Pythagoras theorem prove pannu",
    ],
    "Introduction to Trigonometry": [
        "sin, cos, tan enna?",
        "Trigonometric identities epdi remember pannuradhu?",
        "Complementary angles relation enna?",
    ],
    "Statistics": [
        "Mean, Median, Mode enna difference?",
        "Cumulative frequency table epdi podukiradhu?",
        "Ogive curve enna?",
    ],
    "Probability": [
        "Probability definition enna?",
        "Complementary events enna?",
        "Equally likely outcomes explain pannu",
    ],
}

# Subject-level fallback starter questions (used for Class 8, 9, 11, 12)
_FALLBACKS_HINGLISH = {
    "Science":          ["Is chapter ka main concept samjhao", "Exam mein kya important hai?", "Ek real-life example do"],
    "Physics":          ["Is chapter ka main concept kya hai?", "Formula explain karo", "Numericals kaise solve karte hain?"],
    "Chemistry":        ["Is chapter ke key reactions samjhao", "Important definitions kya hain?", "Exam ke liye kya yaad rakhein?"],
    "Biology":          ["Is topic ka diagram explain karo", "Important terms kya hain?", "Humans mein yeh kaise kaam karta hai?"],
    "Mathematics":      ["Is chapter ka main formula kya hai?", "Ek example solve karke dikhao", "Common mistakes kya hoti hain?"],
    "Social Science":   ["Is chapter ka main point kya hai?", "Important dates ya events kya hain?", "India se connection samjhao"],
    "History":          ["Is event ki main wajah kya thi?", "Important dates yaad karne ka tarika?", "India pe kya asar hua?"],
    "Geography":        ["Is chapter mein kya main concept hai?", "Map pe kahan hota hai yeh?", "India mein kahan relevant hai?"],
    "Civics":           ["Is chapter ki main baat kya hai?", "Constitution mein kahan hai yeh?", "Real life mein kaise kaam karta hai?"],
    "Economics":        ["Is chapter ka main idea kya hai?", "India ki economy se kaise joda?", "Important terms samjhao"],
    "English":          ["Is chapter ki main theme kya hai?", "Important characters kaun hain?", "Exam ke liye kya important hai?"],
    "Hindi":            ["Is kavita/gadya ka bhaav kya hai?", "Lekhak kya kehna chahte hain?", "Important lines yaad karne ka tarika?"],
    "Tamil":            ["Idha pathi main concept enna?", "Important lines enna?", "Exam-la enna important?"],
    "Computer Science": ["Is chapter ka main concept kya hai?", "Program example dikhao", "Common errors kya hoti hain?"],
    "Business Studies": ["Is chapter ka main concept kya hai?", "Real company example do", "Exam ke liye kya important hai?"],
    "Accountancy":      ["Journal entry kaise likhte hain?", "Important formulas kya hain?", "Common mistakes kya hoti hain?"],
}

_FALLBACKS_TANGLISH = {
    "Science":          ["Idha pathi main concept enna?", "Exam-la enna important?", "Oru real-life example kudu"],
    "Physics":          ["Idha pathi main concept enna?", "Formula explain pannu", "Numericals epdi solve pannuradhu?"],
    "Chemistry":        ["Key reactions explain pannu", "Important definitions enna?", "Exam-ku enna remember pannanum?"],
    "Biology":          ["Diagram explain pannu", "Important terms enna?", "Humans-la idhu epdi work pannudhu?"],
    "Mathematics":      ["Main formula enna?", "Oru example solve pannu", "Common mistakes enna?"],
    "Social Science":   ["Main point enna?", "Important events enna?", "India-kku connection explain pannu"],
    "History":          ["Idha nadandhadhu yen?", "Important dates epdi remember pannuradhu?", "India-la enna aana?"],
    "Geography":        ["Main concept enna?", "Map-la enga irukkudhu?", "India-la enge relevant?"],
    "Civics":           ["Main point enna?", "Constitution-la enga irukku?", "Real life-la epdi work pannudhu?"],
    "Economics":        ["Main idea enna?", "India economy-la epdi jodikkiradhu?", "Important terms explain pannu"],
    "English":          ["Main theme enna?", "Important characters yaar?", "Exam-ku enna important?"],
    "Hindi":            ["Kavithai bhaav enna?", "Lekhak enna solla varen?", "Important lines epdi remember pannuradhu?"],
    "Tamil":            ["Idha pathi main concept enna?", "Important lines enna?", "Exam-la enna important?"],
    "Computer Science": ["Main concept enna?", "Program example kaattu", "Common errors enna?"],
    "Business Studies": ["Main concept enna?", "Real company example kudu", "Exam-ku enna important?"],
    "Accountancy":      ["Journal entry epdi ezhudhuradhu?", "Important formulas enna?", "Common mistakes enna?"],
}

_DEFAULT_FALLBACK_H = [
    "Is chapter ke baare mein kuch bhi pooch!",
    "Koi bhi concept clear karna ho toh bol!",
    "Exam mein kya aata hai? Discuss karte hain!",
]
_DEFAULT_FALLBACK_T = [
    "Idha pathi enna doubt-um kekko!",
    "Yedhaavathu concept clear pannanum-na kelu!",
    "Exam-la enna varudhu? Pesuvom!",
]


def get_starter_questions(language: str, class_name: str, subject: str, chapter: str) -> list:
    """Return 3 starter questions for the given context."""
    if language == "Tanglish":
        # Try chapter-specific (Class 10 only)
        if class_name == "Class 10" and chapter in STARTER_QUESTIONS_TANGLISH:
            return STARTER_QUESTIONS_TANGLISH[chapter]
        return _FALLBACKS_TANGLISH.get(subject, _DEFAULT_FALLBACK_T)
    else:
        if class_name == "Class 10" and chapter in STARTER_QUESTIONS_HINGLISH:
            return STARTER_QUESTIONS_HINGLISH[chapter]
        return _FALLBACKS_HINGLISH.get(subject, _DEFAULT_FALLBACK_H)


# ── Legacy aliases (keep app.py imports working during transition) ────────────
SUBJECTS        = SUBJECTS_8_10
SUBJECT_CHAPTERS = _CHAPTERS_10
