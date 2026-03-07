import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"

CHAPTERS = [
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
]

LANGUAGES = ["Hinglish", "Tanglish"]

STARTER_QUESTIONS_HINGLISH = {
    "Chemical Reactions and Equations": [
        "Bhai chemical reaction aur physical change mein kya difference hai?",
        "Oxidation aur reduction samjhao with example",
        "Balancing equations kaise karte hai?",
    ],
    "Acids, Bases and Salts": [
        "Acid aur base mein kya farak hota hai bhai?",
        "pH scale kya hoti hai? Simple mein samjhao",
        "Neutralization reaction kya hai?",
    ],
    "Metals and Non-metals": [
        "Metals aur non-metals mein kya difference hai?",
        "Corrosion kya hota hai? Rust kyun lagta hai?",
        "Reactivity series kya hai bhai?",
    ],
    "Carbon and its Compounds": [
        "Carbon ke itne saare compounds kyun hote hai?",
        "Organic aur inorganic compounds mein kya farak hai?",
        "Soap aur detergent kaise kaam karte hai?",
    ],
    "Life Processes": [
        "Photosynthesis kya hota hai bhai?",
        "Digestion ka pura process samjhao",
        "Respiration aur breathing mein kya difference hai?",
    ],
    "Control and Coordination": [
        "Nervous system kaise kaam karta hai?",
        "Hormones kya hote hai? Examples do",
        "Reflex action kya hota hai? Example se samjhao",
    ],
    "How do Organisms Reproduce": [
        "Asexual aur sexual reproduction mein kya farak hai?",
        "Binary fission kya hoti hai?",
        "Human reproduction system samjhao simply",
    ],
    "Heredity": [
        "Heredity matlab kya hota hai bhai?",
        "Mendel ke experiments kya the?",
        "Dominant aur recessive traits kya hai?",
    ],
    "Light - Reflection and Refraction": [
        "Reflection aur refraction mein kya difference hai?",
        "Concave aur convex mirror mein farak kya hai?",
        "Snell's law kya hai? Simple mein batao",
    ],
    "The Human Eye and the Colourful World": [
        "Aankh mein image kaise banti hai?",
        "Myopia aur hypermetropia kya hai?",
        "Rainbow kaise banta hai bhai?",
    ],
    "Electricity": [
        "Ohm's law kya hai? Simple mein samjhao",
        "Series aur parallel circuit mein kya farak hai?",
        "Resistance kya hota hai bhai?",
    ],
    "Magnetic Effects of Electric Current": [
        "Electromagnet kaise banta hai?",
        "Fleming's left hand rule kya hai?",
        "Electric motor kaise kaam karta hai?",
    ],
    "Our Environment": [
        "Ecosystem kya hota hai bhai?",
        "Food chain aur food web mein kya farak hai?",
        "Ozone layer kya hai aur kyun important hai?",
    ],
    "Sustainable Management of Natural Resources": [
        "3 R's kya hai - Reduce, Reuse, Recycle?",
        "Water harvesting kya hota hai?",
        "Natural resources ko kaise conserve karein?",
    ],
}

STARTER_QUESTIONS_TANGLISH = {
    "Chemical Reactions and Equations": [
        "Anna chemical reaction vs physical change explain pannu",
        "Oxidation and reduction-a example koodu sollu",
        "Balancing equations epdi pannuvanga?",
    ],
    "Acids, Bases and Salts": [
        "Acid and base-la enna difference da?",
        "pH scale-a simple-a explain pannu",
        "Neutralization reaction enna?",
    ],
    "Metals and Non-metals": [
        "Metals and non-metals-la enna difference?",
        "Rust epdi varuthu? Corrosion explain pannu",
        "Reactivity series enna anna?",
    ],
    "Carbon and its Compounds": [
        "Carbon compounds ipdi romba irukka karanam enna?",
        "Organic and inorganic compounds-la enna difference?",
        "Soap and detergent epdi work pannudhu?",
    ],
    "Life Processes": [
        "Photosynthesis-a simple-a sollu anna",
        "Digestion process-a explain pannu",
        "Respiration and breathing-la enna difference?",
    ],
    "Control and Coordination": [
        "Nervous system epdi work pannudhu?",
        "Hormones enna? Examples sollu",
        "Reflex action enna? Example koodu",
    ],
    "How do Organisms Reproduce": [
        "Asexual and sexual reproduction-la enna farak?",
        "Binary fission enna?",
        "Human reproduction-a simple-a explain pannu",
    ],
    "Heredity": [
        "Heredity enna-nu sollu anna",
        "Mendel experiments enna?",
        "Dominant and recessive traits enna?",
    ],
    "Light - Reflection and Refraction": [
        "Reflection and refraction-la enna difference?",
        "Concave and convex mirror-la farak enna?",
        "Snell's law-a simple-a sollu",
    ],
    "The Human Eye and the Colourful World": [
        "Kaanla image epdi form aagudhu?",
        "Myopia and hypermetropia enna?",
        "Rainbow epdi varuthu anna?",
    ],
    "Electricity": [
        "Ohm's law-a simple-a explain pannu",
        "Series and parallel circuit-la enna farak?",
        "Resistance enna-nu sollu",
    ],
    "Magnetic Effects of Electric Current": [
        "Electromagnet epdi seivanga?",
        "Fleming's left hand rule enna?",
        "Electric motor epdi work pannudhu?",
    ],
    "Our Environment": [
        "Ecosystem enna-nu sollu anna",
        "Food chain and food web-la enna farak?",
        "Ozone layer enna, yen important?",
    ],
    "Sustainable Management of Natural Resources": [
        "3 R's enna - Reduce, Reuse, Recycle?",
        "Water harvesting enna?",
        "Natural resources-a epdi conserve pannuvom?",
    ],
}

# Wikipedia article titles for chapter diagrams (used by get_chapter_diagram)
CHAPTER_WIKI_MAP = {
    "Chemical Reactions and Equations": "Chemical_reaction",
    "Acids, Bases and Salts": "Acid%E2%80%93base_reaction",
    "Metals and Non-metals": "Metal",
    "Carbon and its Compounds": "Carbon",
    "Life Processes": "Photosynthesis",
    "Control and Coordination": "Neuron",
    "How do Organisms Reproduce": "Reproduction",
    "Heredity": "Heredity",
    "Light - Reflection and Refraction": "Reflection_(physics)",
    "The Human Eye and the Colourful World": "Human_eye",
    "Electricity": "Electric_circuit",
    "Magnetic Effects of Electric Current": "Magnetic_field",
    "Our Environment": "Food_web",
    "Sustainable Management of Natural Resources": "Natural_resource_management",
}


def get_starter_questions(language: str, chapter: str) -> list:
    if language == "Tanglish":
        return STARTER_QUESTIONS_TANGLISH.get(chapter, [])
    return STARTER_QUESTIONS_HINGLISH.get(chapter, [])

# Keep backward compatibility
STARTER_QUESTIONS = STARTER_QUESTIONS_HINGLISH
