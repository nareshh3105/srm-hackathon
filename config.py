import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"

SUBJECTS = ["Science", "Social Science", "Mathematics", "English", "Hindi", "Tamil"]

SUBJECT_CHAPTERS = {
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
        # History — India and the Contemporary World II
        "History: The Rise of Nationalism in Europe",
        "History: Nationalism in India",
        "History: The Making of a Global World",
        "History: The Age of Industrialisation",
        "History: Print Culture and the Modern World",
        # Geography — Contemporary India II
        "Geography: Resources and Development",
        "Geography: Forest and Wildlife Resources",
        "Geography: Water Resources",
        "Geography: Agriculture",
        "Geography: Minerals and Energy Resources",
        "Geography: Manufacturing Industries",
        "Geography: Lifelines of National Economy",
        # Civics — Democratic Politics II
        "Civics: Power Sharing",
        "Civics: Federalism",
        "Civics: Gender, Religion and Caste",
        "Civics: Political Parties",
        "Civics: Outcomes of Democracy",
        # Economics — Understanding Economic Development
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
        # First Flight — Main Reader
        "FF: A Letter to God",
        "FF: Nelson Mandela - Long Walk to Freedom",
        "FF: Two Stories about Flying",
        "FF: From the Diary of Anne Frank",
        "FF: The Hundred Dresses-I",
        "FF: The Hundred Dresses-II",
        "FF: Glimpses of India",
        "FF: Mijbil the Otter",
        "FF: Madam Rides the Bus",
        "FF: The Sermon at Benares",
        "FF: The Proposal",
        # Footprints Without Feet — Supplementary
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
        # Kshitij — Main Reader
        "Kshitij: Surdas - Pad",
        "Kshitij: Tulsidas - Ram-Lakshman-Parashuram Samvad",
        "Kshitij: Dev - Savaiya aur Kavitt",
        "Kshitij: Jay Shankar Prasad - Aatm Parichay",
        "Kshitij: Suryakant Tripathi Nirala - Utsaah",
        "Kshitij: Nagarjun - Yeh Danturit Muskan",
        "Kshitij: Rituraj - Kanyadan",
        "Kshitij: Mangalesh Dabral - Sangatkar",
        "Kshitij: Swayam Prakash - Netaji ka Chashma",
        "Kshitij: Ramvriksh Benipuri - Balgobin Bhagat",
        "Kshitij: Yadavendra Sharma - Lakhnavi Andaaz",
        "Kshitij: Mannu Bhandari - Ek Kahani Yeh Bhi",
        "Kshitij: Mahavir Prasad Dwivedi - Stri Shiksha",
        # Kritika — Supplementary
        "Kritika: Mata Ka Anchal",
        "Kritika: George Pancham Ki Naak",
        "Kritika: Sana-Sana Haath Jodi",
        "Kritika: Maine Dekha Ek Aandha Maidan",
    ],
    "Tamil": [
        # TN Samacheer Kalvi Class 10 Tamil
        "Iyal 1: Karumai Niram",
        "Iyal 2: Inaindha Kai",
        "Iyal 3: Manidha Neyam",
        "Iyal 4: Thamizhin Sirappu",
        "Iyal 5: Bharathiyar Kavithaigal",
        "Iyal 6: Thirukkural",
        "Iyal 7: Sangam Ilakkiyam",
        "Iyal 8: Naadaka Ilakkiyam",
        "Iyal 9: Adutha Kathai",
        "Tamil Grammar: Ezhuthu",
        "Tamil Grammar: Sol",
        "Tamil Grammar: Tholkappiyam",
    ],
}

# Keep CHAPTERS pointing to Science for any legacy code
CHAPTERS = SUBJECT_CHAPTERS["Science"]

LANGUAGES = ["Hinglish", "Tanglish"]

# ─────────────────────────────────────────────
# STARTER QUESTIONS — HINGLISH
# ─────────────────────────────────────────────
STARTER_QUESTIONS_HINGLISH = {
    # ── Science ──
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

    # ── Social Science — History ──
    "History: The Rise of Nationalism in Europe": [
        "Nationalism kya hota hai bhai? Easy mein samjhao",
        "French Revolution ka nationalism se kya connection hai?",
        "Frederic Sorrieu ki painting mein kya dikhaya gaya tha?",
    ],
    "History: Nationalism in India": [
        "Non-Cooperation Movement kyun shuru hua?",
        "Gandhi ji ka Civil Disobedience Movement kya tha?",
        "Jallianwala Bagh massacre kya tha?",
    ],
    "History: The Making of a Global World": [
        "Globalisation pehle kaise hoti thi? History batao",
        "Silk Route kya tha bhai?",
        "Great Depression kya tha aur kab hua?",
    ],
    "History: The Age of Industrialisation": [
        "Industrial Revolution pehle England mein kyun hua?",
        "Proto-industrialisation kya hoti hai?",
        "India mein industrialisation ki history kya hai?",
    ],
    "History: Print Culture and the Modern World": [
        "Printing press ka invention kaise hua?",
        "Print culture ne nationalism ko kaise affect kiya?",
        "India mein printing kab aayi?",
    ],

    # ── Social Science — Geography ──
    "Geography: Resources and Development": [
        "Resources kya hote hai? Types batao",
        "Sustainable development kya hota hai?",
        "Resource planning kya hai aur kyun zaroori hai?",
    ],
    "Geography: Forest and Wildlife Resources": [
        "Van aur wildlife kyun important hain?",
        "Deforestation ke kya consequences hain?",
        "India mein wildlife conservation kaise hoti hai?",
    ],
    "Geography: Water Resources": [
        "India mein water scarcity ka problem kya hai?",
        "Multipurpose river projects ke fayde aur nuksan kya hain?",
        "Rainwater harvesting kya hoti hai?",
    ],
    "Geography: Agriculture": [
        "India mein farming ke types kya hain?",
        "Green Revolution kya tha?",
        "Kharif aur Rabi crops mein kya farak hai?",
    ],
    "Geography: Minerals and Energy Resources": [
        "Minerals kahan se milte hain India mein?",
        "Conventional aur non-conventional energy mein kya farak hai?",
        "Solar energy kyun important hai?",
    ],
    "Geography: Manufacturing Industries": [
        "Industries ka economy mein kya role hai?",
        "Agro-based industries kya hoti hain?",
        "Industrial pollution kaise reduce karein?",
    ],
    "Geography: Lifelines of National Economy": [
        "Transport aur communication desh ke liye kyun zaroori hain?",
        "Roadways aur railways mein kya difference hai?",
        "India ke major ports kaun se hain?",
    ],

    # ── Social Science — Civics ──
    "Civics: Power Sharing": [
        "Power sharing kya hoti hai aur kyun zaroori hai?",
        "Belgium aur Sri Lanka ka example kyun use karte hain?",
        "Horizontal aur vertical power sharing mein kya farak hai?",
    ],
    "Civics: Federalism": [
        "Federalism kya hota hai bhai?",
        "India mein federalism kaise kaam karta hai?",
        "Decentralisation kya hai?",
    ],
    "Civics: Gender, Religion and Caste": [
        "Gender inequality kya hoti hai?",
        "Communalism kya hota hai?",
        "Caste aur politics ka kya connection hai?",
    ],
    "Civics: Political Parties": [
        "Political parties kyun zaroori hain democracy mein?",
        "India ki major political parties kaun si hain?",
        "Political parties ke functions kya hote hain?",
    ],
    "Civics: Outcomes of Democracy": [
        "Democracy ke kya fayde hain?",
        "Democracy ki limitations kya hain?",
        "Democracy aur economic growth ka kya connection hai?",
    ],

    # ── Social Science — Economics ──
    "Economics: Development": [
        "Development kya hota hai? Sirf income se kya nahi hota?",
        "Human Development Index kya hai?",
        "Per capita income kya hoti hai?",
    ],
    "Economics: Sectors of the Indian Economy": [
        "Primary, secondary aur tertiary sector mein kya farak hai?",
        "Organised aur unorganised sector kya hote hain?",
        "India mein service sector itna bada kyun hai?",
    ],
    "Economics: Money and Credit": [
        "Barter system se money system kaise aaya?",
        "Bank se loan lene ka process kya hai?",
        "Formal aur informal credit mein kya farak hai?",
    ],
    "Economics: Globalisation and the Indian Economy": [
        "Globalisation kya hoti hai?",
        "MNCs kya hote hain? India pe kya impact hai?",
        "WTO kya hai?",
    ],
    "Economics: Consumer Rights": [
        "Consumer rights kya hote hain?",
        "COPRA kya hai?",
        "Consumer forum mein complaint kaise karein?",
    ],

    # ── Mathematics ──
    "Real Numbers": [
        "Rational aur irrational numbers mein kya farak hai?",
        "Euclid's division lemma kya hai?",
        "HCF aur LCM kaise nikaalte hain?",
    ],
    "Polynomials": [
        "Polynomial kya hoti hai? Types batao",
        "Zeroes of a polynomial kya hote hain?",
        "Relationship between zeroes and coefficients kya hai?",
    ],
    "Pair of Linear Equations in Two Variables": [
        "Linear equations solve karne ke methods kya hain?",
        "Substitution method se equations kaise solve karein?",
        "Graphically linear equations kaise solve karein?",
    ],
    "Quadratic Equations": [
        "Quadratic equation kya hoti hai?",
        "Discriminant kya hota hai aur kya batata hai?",
        "Quadratic formula se roots kaise nikaalein?",
    ],
    "Arithmetic Progressions": [
        "AP kya hoti hai? Simple mein batao",
        "nth term of AP kaise nikaalte hain?",
        "Sum of n terms of AP formula samjhao",
    ],
    "Triangles": [
        "Similar triangles kya hote hain?",
        "Pythagoras theorem prove karo",
        "AA, SAS, SSS similarity criteria kya hain?",
    ],
    "Coordinate Geometry": [
        "Distance formula kya hai aur kaise use karein?",
        "Section formula kya hota hai?",
        "Area of triangle with coordinates kaise nikaalein?",
    ],
    "Introduction to Trigonometry": [
        "Sin, cos, tan kya hote hain? Simply samjhao",
        "Trigonometric ratios kaise yaad karein?",
        "Complementary angles ka trigonometry mein kya role hai?",
    ],
    "Some Applications of Trigonometry": [
        "Angle of elevation aur depression kya hote hain?",
        "Height and distance problems kaise solve karein?",
        "Real life mein trigonometry kahan use hoti hai?",
    ],
    "Circles": [
        "Tangent to a circle kya hoti hai?",
        "Tangent perpendicular to radius kyun hoti hai?",
        "Two tangents from external point ke properties kya hain?",
    ],
    "Areas Related to Circles": [
        "Area of sector kaise nikalte hain?",
        "Arc length ka formula kya hai?",
        "Area of segment kaise calculate karein?",
    ],
    "Surface Areas and Volumes": [
        "Cylinder ka surface area aur volume kaise nikaalein?",
        "Cone aur sphere ka volume formula samjhao",
        "Frustum kya hota hai?",
    ],
    "Statistics": [
        "Mean, median, mode mein kya difference hai?",
        "Grouped data ka mean kaise nikaalein?",
        "Cumulative frequency graph kya hota hai?",
    ],
    "Probability": [
        "Probability kya hoti hai? Daily life example do",
        "Theoretical aur experimental probability mein kya farak hai?",
        "Playing cards aur dice ke probability questions kaise solve karein?",
    ],

    # ── English ──
    "FF: A Letter to God": [
        "Lencho ka God pe itna strong belief kyun tha?",
        "Post office workers ne kya kiya aur kyun?",
        "Story ka main theme kya hai?",
    ],
    "FF: Nelson Mandela - Long Walk to Freedom": [
        "Nelson Mandela ki life struggle kya thi?",
        "Apartheid kya tha?",
        "Freedom ke baare mein Mandela kya sochte the?",
    ],
    "FF: Two Stories about Flying": [
        "Young seagull ne flying kyun avoid ki?",
        "Black aero plane story mein mysterious kya tha?",
        "Dono stories ka common theme kya hai?",
    ],
    "FF: From the Diary of Anne Frank": [
        "Anne Frank ki diary kyun famous hai?",
        "Anne ne Kitty ko best friend kyun choose kiya?",
        "Story ka historical context kya hai?",
    ],
    "FF: The Hundred Dresses-I": [
        "Wanda Petronski ko school mein kya problems face karni padti thi?",
        "Maddie aur Peggy mein kya difference tha?",
        "Hundred dresses ka story mein kya symbolism hai?",
    ],
    "FF: The Hundred Dresses-II": [
        "Wanda ke drawing competition mein jeetneke baad kya hua?",
        "Maddie ko kaisa feel hua? Usne kya decision liya?",
        "Story mein bullying ke baare mein kya message hai?",
    ],
    "FF: Glimpses of India": [
        "Coorg ke baare mein interesting facts kya hain?",
        "Tea industry ka Coorg se kya connection hai?",
        "Lokesh story mein kya describe kiya gaya?",
    ],
    "FF: Mijbil the Otter": [
        "Maxwell ne otter ko kahan se liya?",
        "Mijbil ki funny habits kya thi?",
        "Otter ko ghar mein rakhna kaisa experience tha?",
    ],
    "FF: Madam Rides the Bus": [
        "Valli ki bus ride ki planning kaise ki?",
        "Valli ne journey mein kya dekha?",
        "Story ka ending sad kyun tha?",
    ],
    "FF: The Sermon at Benares": [
        "Kisa Gotami ki story kya hai?",
        "Buddha ne mustard seeds kyun maange?",
        "Death aur grief ke baare mein story ka message kya hai?",
    ],
    "FF: The Proposal": [
        "Lomov kyun Natalya ke paas rishta leke aaya?",
        "Chukmuhovsky Meadows ka jhagda kis baat pe tha?",
        "Play mein comedy kaise create ki gayi hai?",
    ],
    "Footprints: A Triumph of Surgery": [
        "Tricki ko kya problem thi?",
        "Mr. Herriot ne Tricki ka kya treatment kiya?",
        "Mrs. Pumphrey ki mistake kya thi?",
    ],
    "Footprints: The Thief's Story": [
        "Hari Singh ne Anil ke saath stay kyun choose kiya?",
        "Hari Singh ne paise steal kiye lekin return kyun kiye?",
        "Story mein Anil ka character kaisa tha?",
    ],
    "Footprints: The Midnight Visitor": [
        "Ausable ne Fowler ko kya impress kiya?",
        "Balcony wali story ka twist kya tha?",
        "Ausable ki clever thinking ka example do",
    ],
    "Footprints: A Question of Trust": [
        "Horace Danby kon tha aur kya karta tha?",
        "Lady in red ne Horace ke saath kya kiya?",
        "Story ka ironic twist kya tha?",
    ],
    "Footprints: Footprints without Feet": [
        "Griffin ne invisible hone ki power kaise achieve ki?",
        "Griffin ne invisibility ka use kaise kiya?",
        "Story mein science fiction ka element kya hai?",
    ],
    "Footprints: The Making of a Scientist": [
        "Richard Ebright ka passion kya tha?",
        "Ebright ne butterflies pe kya discovery ki?",
        "Scientific curiosity ke baare mein story kya batati hai?",
    ],
    "Footprints: The Necklace": [
        "Matilda ki problem kya thi?",
        "Necklace kho jaane ke baad kya hua?",
        "Story ka moral kya hai?",
    ],
    "Footprints: The Hack Driver": [
        "Narrator Lutkins ko kyun dhundh raha tha?",
        "Bill Magnuson actually kaun tha?",
        "Story ka humorous ending kya tha?",
    ],
    "Footprints: Bholi": [
        "Bholi ko neglected kyun feel hota tha?",
        "Teacher ne Bholi ki life kaise change ki?",
        "Story mein women empowerment ka message kya hai?",
    ],
    "Footprints: The Book That Saved the Earth": [
        "Story future mein set hai — kya interesting hai?",
        "Martians ne Earth attack kyun cancel kiya?",
        "Humpty Dumpty ka story mein kya role tha?",
    ],

    # ── Hindi ──
    "Kshitij: Surdas - Pad": [
        "Surdas ke pad mein Krishna ki kaisi image hai?",
        "Bhakti rasa ka is kavita mein kya role hai?",
        "Surdas ki bhasha aur shaili kaisi hai?",
    ],
    "Kshitij: Tulsidas - Ram-Lakshman-Parashuram Samvad": [
        "Parashuram ka gussa kyun tha?",
        "Lakshman ne Parashuram ko kya jawab diya?",
        "Ram ki shaant pratikriya ka kya mahatva hai?",
    ],
    "Kshitij: Dev - Savaiya aur Kavitt": [
        "Dev ki kavita mein nature ka kya varnan hai?",
        "Savaiya aur Kavitt mein kya antar hota hai?",
        "Dev ki bhakti bhavna kaisi hai?",
    ],
    "Kshitij: Jay Shankar Prasad - Aatm Parichay": [
        "Kavita mein kaviyon ne kya parichay diya apna?",
        "Prem aur dard ka kavita mein kya sansleshan hai?",
        "Prasad ji ki chhayavadi shaili kaisi hai?",
    ],
    "Kshitij: Suryakant Tripathi Nirala - Utsaah": [
        "Utsaah kavita mein badal se kya prerna li gayi hai?",
        "Nirala ki kranti bhaavna kavita mein kaise jhalakti hai?",
        "Kavita ka mukhy sandesh kya hai?",
    ],
    "Kshitij: Nagarjun - Yeh Danturit Muskan": [
        "Shishu ki muskan ka kavi pe kya prabhav pada?",
        "Kavita mein kis prakar ki kalpana ki gayi hai?",
        "Nagarjun ki lokbhaasha ka udaharan do",
    ],
    "Kshitij: Rituraj - Kanyadan": [
        "Maa ne beti ko vidai ke samay kya sikhaya?",
        "Kavita mein stri-jeevan ki kaisi chinta hai?",
        "Kavita ka bhaavarthh kya hai?",
    ],
    "Kshitij: Mangalesh Dabral - Sangatkar": [
        "Sangatkar kaun hota hai? Uski bhumika kya hai?",
        "Kavita mein kalpana aur vastavikata ka kya sansleshan hai?",
        "Kavita ka pramukhh sandesh kya hai?",
    ],
    "Kshitij: Swayam Prakash - Netaji ka Chashma": [
        "Halwai Capt. Chashma ke baare mein kahanee mein kya bataya gaya?",
        "Desh bhakti ke baare mein kahanee kya sandesh deti hai?",
        "Mukhy patra kaun hain aur unka charitra kaisa hai?",
    ],
    "Kshitij: Ramvriksh Benipuri - Balgobin Bhagat": [
        "Balgobin Bhagat ki khasiyat kya thi?",
        "Unka beta ke marne pe kya pratikriya thi?",
        "Unke jeevan ka darshanik pahlu kya tha?",
    ],
    "Kshitij: Yadavendra Sharma - Lakhnavi Andaaz": [
        "Train mein kaviyon ki mulaqaat kaisi rahi?",
        "Nawabi andaaz ke baare mein kya vyangya hai?",
        "Pathh ka mudda kya tha?",
    ],
    "Kshitij: Mannu Bhandari - Ek Kahani Yeh Bhi": [
        "Lekhika ki rashtriya chetna kaise jagriit hui?",
        "Pita ke charitra ka unke jeevan pe kya prabhav pada?",
        "Naari swatantrata ke baare mein pathh kya kehta hai?",
    ],
    "Kshitij: Mahavir Prasad Dwivedi - Stri Shiksha": [
        "Stri shiksha ke virodhi kaun the aur kya tark dete the?",
        "Lekhak ne unka khandann kaise kiya?",
        "Stri shiksha kyun zaroori hai?",
    ],
    "Kritika: Mata Ka Anchal": [
        "Bacchpan ki yaadein kahanee mein kaisi hain?",
        "Maa ka pyaar kahanee mein kaise dikhaya gaya hai?",
        "Gramin jeevan ka chitran kaisa hai?",
    ],
    "Kritika: George Pancham Ki Naak": [
        "George Pancham ki naak ki samasya kya thi?",
        "Vyangya ki drishti se kahanee ka arth kya hai?",
        "Rashtriya gaurav ke baare mein kahanee kya kehti hai?",
    ],
    "Kritika: Sana-Sana Haath Jodi": [
        "Sikkim ki prakriti ka varnan kaisa tha?",
        "Lekhika ne kin logon se mulaqat ki?",
        "Yatra se kya seekhne ko mila?",
    ],
    "Kritika: Maine Dekha Ek Aandha Maidan": [
        "Lekhak ne kya ajeeb anubhav kiya?",
        "Pathh ka kendra-bindu kya hai?",
        "Iss anubhav ka kya prabhav pada?",
    ],

    # ── Tamil ──
    "Iyal 1: Karumai Niram": [
        "Karumai Niram kavithai pathi sollu",
        "Kavithaiyil enna vishayam pesapadukiarthu?",
        "Kavignar yaar, avar kavithai shaili epdi irukku?",
    ],
    "Iyal 2: Inaindha Kai": [
        "Inaindha Kai-la enna sandesh irukku?",
        "Pathyathil yaara pathi pesapadukiarthu?",
        "Unity pathi enna solkirathu?",
    ],
    "Iyal 3: Manidha Neyam": [
        "Manidha Neyam pathyathil enna mukhiya vishayam?",
        "Manitha araval pathi enna solkirathu?",
        "Examples koodu explain pannu",
    ],
    "Iyal 4: Thamizhin Sirappu": [
        "Tamil mozhi enna karana sirappu vaaikkirathu?",
        "Thamizhin thoymaiyin varalaru enna?",
        "Thamizh ilakkiyam pathi konjam sollu",
    ],
    "Iyal 5: Bharathiyar Kavithaigal": [
        "Bharathiyar yaar? Avar kavithai pathi sollu",
        "Desha bhakti Bharathiyar kavithailadum epdi varuthu?",
        "Bharathiyar kavithaiyil pennin nilamai pathi enna solkirathu?",
    ],
    "Iyal 6: Thirukkural": [
        "Thirukkural enna, yaaru ezhuthinar?",
        "Arathupal, Porutpal, Inbathupal pathi sollu",
        "Oru Kural-a example-a sollu, explain pannu",
    ],
    "Iyal 7: Sangam Ilakkiyam": [
        "Sangam ilakkiyam enna, en important?",
        "Akam aur Puram kavithai pathi sollu",
        "Sangam kaala thamizhar vazhakai pathi enna theriyum?",
    ],
    "Iyal 8: Naadaka Ilakkiyam": [
        "Naadakam - drama - ilakkiyathil enna vishesham?",
        "Tamil naadakam varalaru konjam sollu",
        "Pathyathil enna naadakam irukkiriarthu?",
    ],
    "Iyal 9: Adutha Kathai": [
        "Kathai summary sollu",
        "Mukhya pattirangal yaavar?",
        "Kathai enna sandesh tharuthu?",
    ],
    "Tamil Grammar: Ezhuthu": [
        "Tamil ezhuthu vaagai patti sollu",
        "Uyir ezhuthu aur Mei ezhuthu-la enna farak?",
        "Tamil alphabet structure epdi irukku?",
    ],
    "Tamil Grammar: Sol": [
        "Sol vaagai patti sollu",
        "Peyar sol, vinai sol patti sollu",
        "Tamil grammar-la sol epdi work pannudhu?",
    ],
    "Tamil Grammar: Tholkappiyam": [
        "Tholkappiyam enna? Yaaru ezhuthinar?",
        "Tholkappiyam Tamil grammar-la enna role vaikkiriarthu?",
        "Tholkappiyathil enna vishayangal pesukirathu?",
    ],
}

# ─────────────────────────────────────────────
# STARTER QUESTIONS — TANGLISH
# ─────────────────────────────────────────────
STARTER_QUESTIONS_TANGLISH = {
    # ── Science ──
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

    # ── Social Science — History ──
    "History: The Rise of Nationalism in Europe": [
        "Nationalism enna-nu simple-a sollu anna",
        "French Revolution-um nationalism-um epdi connect aaguthu?",
        "Frederic Sorrieu painting-la enna kaatinaar?",
    ],
    "History: Nationalism in India": [
        "Non-Cooperation Movement yen start aaguthu?",
        "Gandhi Civil Disobedience Movement enna?",
        "Jallianwala Bagh-la enna nadanthathu?",
    ],
    "History: The Making of a Global World": [
        "Globalisation history-la epdi irundhuthu?",
        "Silk Route enna anna?",
        "Great Depression enna, eppo nadanthathu?",
    ],
    "History: The Age of Industrialisation": [
        "Industrial Revolution England-la-ye yen mudhalla nadanthathu?",
        "Proto-industrialisation enna?",
        "India-la industrialisation history enna?",
    ],
    "History: Print Culture and the Modern World": [
        "Printing press epdi invent aaguthu?",
        "Print culture nationalism-a epdi affect pannuthu?",
        "India-la printing eppo vandhathu?",
    ],

    # ── Social Science — Geography ──
    "Geography: Resources and Development": [
        "Resources enna? Types sollu",
        "Sustainable development enna?",
        "Resource planning yen important?",
    ],
    "Geography: Forest and Wildlife Resources": [
        "Van and wildlife yen important?",
        "Deforestation-oda consequences enna?",
        "India-la wildlife conservation epdi nadukkirathu?",
    ],
    "Geography: Water Resources": [
        "India-la water scarcity problem enna?",
        "Multipurpose river projects-oda advantages and disadvantages enna?",
        "Rainwater harvesting enna?",
    ],
    "Geography: Agriculture": [
        "India-la farming types enna?",
        "Green Revolution enna?",
        "Kharif and Rabi crops-la farak enna?",
    ],
    "Geography: Minerals and Energy Resources": [
        "India-la minerals enga kidaikum?",
        "Conventional and non-conventional energy-la farak enna?",
        "Solar energy yen important?",
    ],
    "Geography: Manufacturing Industries": [
        "Industries economy-la enna role vaikkudhu?",
        "Agro-based industries enna?",
        "Industrial pollution epdi reduce pannuvom?",
    ],
    "Geography: Lifelines of National Economy": [
        "Transport and communication yen important?",
        "Roadways and railways-la enna difference?",
        "India major ports edhellam?",
    ],

    # ── Social Science — Civics ──
    "Civics: Power Sharing": [
        "Power sharing enna, yen important?",
        "Belgium and Sri Lanka example yen use pannuvanga?",
        "Horizontal and vertical power sharing-la farak enna?",
    ],
    "Civics: Federalism": [
        "Federalism enna-nu sollu anna",
        "India-la federalism epdi work pannudhu?",
        "Decentralisation enna?",
    ],
    "Civics: Gender, Religion and Caste": [
        "Gender inequality enna?",
        "Communalism enna?",
        "Caste and politics epdi connect aaguthu?",
    ],
    "Civics: Political Parties": [
        "Political parties democracy-la yen important?",
        "India major political parties edhellam?",
        "Political parties functions enna?",
    ],
    "Civics: Outcomes of Democracy": [
        "Democracy-oda advantages enna?",
        "Democracy-oda limitations enna?",
        "Democracy and economic growth epdi connect aaguthu?",
    ],

    # ── Social Science — Economics ──
    "Economics: Development": [
        "Development enna? Sirf income mattum-a?",
        "Human Development Index enna?",
        "Per capita income enna?",
    ],
    "Economics: Sectors of the Indian Economy": [
        "Primary, secondary, tertiary sector-la enna farak?",
        "Organised and unorganised sector enna?",
        "India-la service sector ipdi perusa yen?",
    ],
    "Economics: Money and Credit": [
        "Barter system-la irundhu money system epdi vandhathu?",
        "Bank-la loan edukkira process enna?",
        "Formal and informal credit-la farak enna?",
    ],
    "Economics: Globalisation and the Indian Economy": [
        "Globalisation enna?",
        "MNCs enna? India-la enna impact?",
        "WTO enna?",
    ],
    "Economics: Consumer Rights": [
        "Consumer rights enna?",
        "COPRA enna?",
        "Consumer forum-la complaint epdi pannuvom?",
    ],

    # ── Mathematics ──
    "Real Numbers": [
        "Rational and irrational numbers-la enna farak?",
        "Euclid's division lemma enna?",
        "HCF and LCM epdi nikaaluvom?",
    ],
    "Polynomials": [
        "Polynomial enna? Types sollu",
        "Zeroes of polynomial enna?",
        "Zeroes and coefficients-la relationship enna?",
    ],
    "Pair of Linear Equations in Two Variables": [
        "Linear equations solve panna methods enna?",
        "Substitution method-la solve epdi pannuvom?",
        "Graphically equations epdi solve pannuvom?",
    ],
    "Quadratic Equations": [
        "Quadratic equation enna?",
        "Discriminant enna, enna solludhu?",
        "Quadratic formula-la roots epdi nikaaluvom?",
    ],
    "Arithmetic Progressions": [
        "AP enna? Simple-a sollu",
        "nth term of AP epdi nikaaluvom?",
        "Sum of n terms formula explain pannu",
    ],
    "Triangles": [
        "Similar triangles enna?",
        "Pythagoras theorem prove pannu",
        "AA, SAS, SSS similarity criteria enna?",
    ],
    "Coordinate Geometry": [
        "Distance formula enna, epdi use pannuvom?",
        "Section formula enna?",
        "Coordinates-la triangle area epdi nikaaluvom?",
    ],
    "Introduction to Trigonometry": [
        "Sin, cos, tan enna? Simple-a sollu",
        "Trigonometric ratios epdi remember pannuvom?",
        "Complementary angles trigonometry-la enna role?",
    ],
    "Some Applications of Trigonometry": [
        "Angle of elevation and depression enna?",
        "Height and distance problems epdi solve pannuvom?",
        "Real life-la trigonometry enga use aagudhu?",
    ],
    "Circles": [
        "Tangent to circle enna?",
        "Tangent radius-ku perpendicular yen?",
        "External point-la irundhu two tangents properties enna?",
    ],
    "Areas Related to Circles": [
        "Sector area epdi nikaluvom?",
        "Arc length formula enna?",
        "Segment area epdi calculate pannuvom?",
    ],
    "Surface Areas and Volumes": [
        "Cylinder surface area and volume epdi nikaaluvom?",
        "Cone and sphere volume formula explain pannu",
        "Frustum enna?",
    ],
    "Statistics": [
        "Mean, median, mode-la enna difference?",
        "Grouped data mean epdi nikaaluvom?",
        "Cumulative frequency graph enna?",
    ],
    "Probability": [
        "Probability enna? Daily life example sollu",
        "Theoretical and experimental probability-la farak enna?",
        "Playing cards and dice probability questions epdi solve pannuvom?",
    ],

    # ── English ──
    "FF: A Letter to God": [
        "Lencho God-la ipdi strong belief yen vaichirundhan?",
        "Post office workers enna pannanga, yen?",
        "Story main theme enna?",
    ],
    "FF: Nelson Mandela - Long Walk to Freedom": [
        "Nelson Mandela life struggle enna?",
        "Apartheid enna?",
        "Freedom pathi Mandela enna nenachaan?",
    ],
    "FF: Two Stories about Flying": [
        "Young seagull flying yen avoid pannan?",
        "Black aeroplane story-la mysterious enna?",
        "Rendhu story-oda common theme enna?",
    ],
    "FF: From the Diary of Anne Frank": [
        "Anne Frank diary yen famous?",
        "Anne Kitty-ya best friend-a yen choose pannaanga?",
        "Story historical context enna?",
    ],
    "FF: The Hundred Dresses-I": [
        "Wanda Petronski school-la enna problems face pannaanga?",
        "Maddie and Peggy-la enna difference?",
        "Hundred dresses story-la enna symbolism?",
    ],
    "FF: The Hundred Dresses-II": [
        "Wanda drawing competition-la jettukku appuram enna nadanthathu?",
        "Maddie epdi feel pannaanga? Enna decision eduththaanga?",
        "Bullying pathi story enna message tharuthu?",
    ],
    "FF: Glimpses of India": [
        "Coorg pathi interesting facts enna?",
        "Tea industry Coorg-oda connection enna?",
        "Lokesh story-la enna describe pannaaru?",
    ],
    "FF: Mijbil the Otter": [
        "Maxwell otter-a enga irundhu eduththaan?",
        "Mijbil funny habits enna?",
        "Otter-a veetla vaichukka epdi experience?",
    ],
    "FF: Madam Rides the Bus": [
        "Valli bus ride epdi plan pannaanga?",
        "Valli journey-la enna paathaanga?",
        "Story ending yen sad-a irundhathu?",
    ],
    "FF: The Sermon at Benares": [
        "Kisa Gotami story enna?",
        "Buddha mustard seeds yen kettan?",
        "Death and grief pathi story message enna?",
    ],
    "FF: The Proposal": [
        "Lomov Natalya-kita yen vandhan?",
        "Chukmuhovsky Meadows-la enna debate?",
        "Play-la comedy epdi create pannaaru?",
    ],
    "Footprints: A Triumph of Surgery": [
        "Tricki-ku enna problem irundhathu?",
        "Mr. Herriot Tricki-ya epdi treat pannaaru?",
        "Mrs. Pumphrey mistake enna?",
    ],
    "Footprints: The Thief's Story": [
        "Hari Singh Anil-kita yen stay pannan?",
        "Hari Singh paisa steal pannittu yen thirumba kuduththaan?",
        "Story-la Anil character epdi irundhaan?",
    ],
    "Footprints: The Midnight Visitor": [
        "Ausable Fowler-a epdi impress pannaaru?",
        "Balcony story twist enna?",
        "Ausable clever thinking example sollu",
    ],
    "Footprints: A Question of Trust": [
        "Horace Danby yaar, enna pannan?",
        "Red dress-la lady Horace-kita enna pannaanga?",
        "Story ironic twist enna?",
    ],
    "Footprints: Footprints without Feet": [
        "Griffin invisible power epdi achieve pannaaru?",
        "Griffin invisibility-a epdi use pannaaru?",
        "Story-la science fiction element enna?",
    ],
    "Footprints: The Making of a Scientist": [
        "Richard Ebright passion enna?",
        "Ebright butterflies-la enna discovery pannaaru?",
        "Scientific curiosity pathi story enna solkiarthu?",
    ],
    "Footprints: The Necklace": [
        "Matilda problem enna?",
        "Necklace thavalittukku appuram enna nadanthathu?",
        "Story moral enna?",
    ],
    "Footprints: The Hack Driver": [
        "Narrator Lutkins-a yen thedi vandhan?",
        "Bill Magnuson actually yaar?",
        "Story humorous ending enna?",
    ],
    "Footprints: Bholi": [
        "Bholi yen neglected-a feel pannaanga?",
        "Teacher Bholi life epdi change pannaaru?",
        "Story-la women empowerment message enna?",
    ],
    "Footprints: The Book That Saved the Earth": [
        "Story future-la set — enna interesting?",
        "Martians Earth attack yen cancel pannaanga?",
        "Humpty Dumpty story-la enna role?",
    ],

    # ── Hindi ──
    "Kshitij: Surdas - Pad": [
        "Surdas pad-la Krishna pathi epdi sollaaru?",
        "Bhakti rasa kavithaiyil epdi varuthu?",
        "Surdas mozhi shaili epdi irukku?",
    ],
    "Kshitij: Tulsidas - Ram-Lakshman-Parashuram Samvad": [
        "Parashuram yen kopapattaar?",
        "Lakshman Parashuram-ku enna sollaaru?",
        "Ram shaant response-oda maatchimai enna?",
    ],
    "Kshitij: Dev - Savaiya aur Kavitt": [
        "Dev kavithaiyil nature pathi epdi sollaaru?",
        "Savaiya and Kavitt-la enna difference?",
        "Dev bhakti bhava epdi irukku?",
    ],
    "Kshitij: Jay Shankar Prasad - Aatm Parichay": [
        "Kavithaiyil kaviyor enna parichay kudukkaaru?",
        "Prem and dard kavithaiyil epdi mix aagudhu?",
        "Prasad Chhayavadi style epdi irukku?",
    ],
    "Kshitij: Suryakant Tripathi Nirala - Utsaah": [
        "Utsaah kavithaiyil badal-la irundhu enna prerna?",
        "Nirala kranti feeling kavithaiyil epdi varuthu?",
        "Kavithai main message enna?",
    ],
    "Kshitij: Nagarjun - Yeh Danturit Muskan": [
        "Shishu muskan kavi-la epdi impact pannudhu?",
        "Kavithaiyil enna karpanai irukku?",
        "Nagarjun lokbhasha example sollu",
    ],
    "Kshitij: Rituraj - Kanyadan": [
        "Maa beti-ku vidai-la enna sollaanga?",
        "Kavithaiyil stri jeevan pathi epdi concern irukku?",
        "Kavithai bhaavarthh enna?",
    ],
    "Kshitij: Mangalesh Dabral - Sangatkar": [
        "Sangatkar yaar? Avar role enna?",
        "Kavithaiyil kalpana and reality epdi mix aagudhu?",
        "Kavithai main message enna?",
    ],
    "Kshitij: Swayam Prakash - Netaji ka Chashma": [
        "Capt. Chashma pathi story-la enna sollaaru?",
        "Desh bhakti pathi story enna message?",
        "Main characters yaar, epdi irukkaanga?",
    ],
    "Kshitij: Ramvriksh Benipuri - Balgobin Bhagat": [
        "Balgobin Bhagat-oda khasiyat enna?",
        "Magan maranathukku appuram avar reaction enna?",
        "Avar jeevanathil darshana element enna?",
    ],
    "Kshitij: Yadavendra Sharma - Lakhnavi Andaaz": [
        "Train-la meeting epdi nadanthathu?",
        "Nawabi style pathi enna vyangyam?",
        "Pathyam mudda enna?",
    ],
    "Kshitij: Mannu Bhandari - Ek Kahani Yeh Bhi": [
        "Lekhika rashtriya chetna epdi jagriit aaguthu?",
        "Thanthai character avar jeevanathil enna impact?",
        "Naari swatantrata pathi pathyam enna solkiarthu?",
    ],
    "Kshitij: Mahavir Prasad Dwivedi - Stri Shiksha": [
        "Stri shiksha virodhi yaar, enna argument?",
        "Lekhak epdi khandanam pannaaru?",
        "Stri shiksha yen important?",
    ],
    "Kritika: Mata Ka Anchal": [
        "Bacchpan memories kathaiyil epdi irukku?",
        "Amma aasai kathaiyil epdi kaattu irukku?",
        "Village life chitram epdi irukku?",
    ],
    "Kritika: George Pancham Ki Naak": [
        "George Pancham naak samasya enna?",
        "Vyangyam drishti-la kathai arth enna?",
        "Rashtriya gaurav pathi kathai enna solkiarthu?",
    ],
    "Kritika: Sana-Sana Haath Jodi": [
        "Sikkim nature pathi enna solluvanga?",
        "Lekhika yaarai santhiththaanga?",
        "Travel-la enna learn pannaanga?",
    ],
    "Kritika: Maine Dekha Ek Aandha Maidan": [
        "Lekhak enna ajeeb experience pannaar?",
        "Pathyam core vishayam enna?",
        "Aa anubhavam enna impact?",
    ],

    # ── Tamil ──
    "Iyal 1: Karumai Niram": [
        "Karumai Niram kavithai pathi sollu",
        "Kavithaiyil enna vishayam pesapadukiarthu?",
        "Kavignar yaar, avar kavithai shaili epdi irukku?",
    ],
    "Iyal 2: Inaindha Kai": [
        "Inaindha Kai-la enna sandesh irukku?",
        "Pathyathil yaara pathi pesapadukiarthu?",
        "Ottrumai pathi enna solkirathu?",
    ],
    "Iyal 3: Manidha Neyam": [
        "Manidha Neyam-la mukhiya vishayam enna?",
        "Manitha araval pathi enna solkirathu?",
        "Examples koodu explain pannu",
    ],
    "Iyal 4: Thamizhin Sirappu": [
        "Tamil mozhi yen sirappu vaaikkirathu?",
        "Thamizhin thoymaiyin varalaru enna?",
        "Thamizh ilakkiyam pathi sollu",
    ],
    "Iyal 5: Bharathiyar Kavithaigal": [
        "Bharathiyar yaar? Avar kavithai pathi sollu",
        "Desa bhakti Bharathiyar kavithaiyil epdi varuthu?",
        "Bharathiyar kavithaiyil pennin nilamai enna?",
    ],
    "Iyal 6: Thirukkural": [
        "Thirukkural enna, yaaru ezhuthinar?",
        "Arathupal, Porutpal, Inbathupal pathi sollu",
        "Oru Kural example-a sollu, explain pannu",
    ],
    "Iyal 7: Sangam Ilakkiyam": [
        "Sangam ilakkiyam enna, yen important?",
        "Akam and Puram kavithai pathi sollu",
        "Sangam kaala thamizhar vazhakai pathi enna?",
    ],
    "Iyal 8: Naadaka Ilakkiyam": [
        "Tamil drama ilakkiyathil enna vishesham?",
        "Tamil naadakam varalaru sollu",
        "Pathyathil enna naadakam?",
    ],
    "Iyal 9: Adutha Kathai": [
        "Kathai summary sollu",
        "Mukhya pattirangal yaavar?",
        "Kathai enna sandesh tharuthu?",
    ],
    "Tamil Grammar: Ezhuthu": [
        "Tamil ezhuthu vaagai patti sollu",
        "Uyir ezhuthu and Mei ezhuthu-la enna farak?",
        "Tamil alphabet structure epdi irukku?",
    ],
    "Tamil Grammar: Sol": [
        "Sol vaagai patti sollu",
        "Peyar sol, vinai sol patti sollu",
        "Tamil grammar-la sol epdi work pannudhu?",
    ],
    "Tamil Grammar: Tholkappiyam": [
        "Tholkappiyam enna? Yaaru ezhuthinar?",
        "Tholkappiyam Tamil grammar-la enna role?",
        "Tholkappiyathil enna vishayangal?",
    ],
}


def get_starter_questions(language: str, subject: str, chapter: str) -> list:
    """Return 3 starter questions for the given language/subject/chapter."""
    questions = STARTER_QUESTIONS_TANGLISH if language == "Tanglish" else STARTER_QUESTIONS_HINGLISH
    fallback = (
        ["Is chapter ke baare mein kuch bhi pooch!", "Koi bhi concept confusing lage toh bol!", "Yahan se start kar — basics pooch!"]
        if language != "Tanglish"
        else ["Idha pathi enna doubt-um kekko!", "Ethaavathu concept confuse-a irundha kelu!", "Basics-la irundhu start pannalam!"]
    )
    return questions.get(chapter, fallback)


# Legacy compat
STARTER_QUESTIONS = STARTER_QUESTIONS_HINGLISH
