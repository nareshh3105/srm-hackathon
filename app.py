import time
import base64
import io
import json
import os
import re
import random
import uuid
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components
from groq import Groq

try:
    import pypdf
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False

from config import (
    GROQ_API_KEY, MODEL_NAME, LANGUAGES,
    CLASSES, GROUPS_11_12,
    get_subjects, get_chapters,
    get_starter_questions,
)
from prompts import get_system_prompt

VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# --- Page Config ---
st.set_page_config(
    page_title="Studybuddy AI - NCERT Tutor (Class 8–12)",
    page_icon="S",
    layout="centered",
)

# --- Load mascot image as base64 ---
_mascot_b64 = ""
_mascot_path = os.path.join(os.path.dirname(__file__), "mascot.png")
if os.path.exists(_mascot_path):
    with open(_mascot_path, "rb") as _f:
        _mascot_b64 = base64.b64encode(_f.read()).decode()

# --- Initialize Groq ---
client = Groq(api_key=GROQ_API_KEY)

# --- Custom CSS ---
st.markdown("""
<style>
    /* ── Always: structural + branded elements ── */
    .main-header { text-align: center; padding: 1rem 0 0.5rem 0; }
    .main-header h1 { font-size: 2.5rem; margin-bottom: 0; }
    .main-header p  { font-size: 1rem; margin-top: 0.25rem; }

    @keyframes studyBob {
        0%   { transform: translateY(0px)  rotate(0deg);   }
        20%  { transform: translateY(-6px) rotate(-5deg);  }
        40%  { transform: translateY(-3px) rotate(3deg);   }
        60%  { transform: translateY(-7px) rotate(-4deg);  }
        80%  { transform: translateY(-2px) rotate(2deg);   }
        100% { transform: translateY(0px)  rotate(0deg);   }
    }
    .mascot-anim {
        display: inline-block;
        animation: studyBob 2.8s ease-in-out infinite;
        transform-origin: bottom center;
    }

    .chapter-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .welcome-box {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        color: white !important;
        box-shadow: 0 4px 16px rgba(102,126,234,0.35);
    }

    [data-testid="stChatMessage"] {
        border-radius: 12px !important;
        margin-bottom: 6px !important;
    }

    div[data-testid="stButton"] button {
        border-radius: 10px !important;
        font-weight: 500 !important;
        transition: all 0.18s !important;
    }
    div[data-testid="stButton"] button:hover {
        background: #667eea !important;
        color: white !important;
        border-color: #667eea !important;
    }

    /* ── Light mode overrides ── */
    @media (prefers-color-scheme: light) {
        .stApp { background-color: #f0f2f8 !important; }
        section[data-testid="stSidebar"] { background-color: #e8eaf2 !important; }
        .main-header h1 { color: #1e1e2e; }
        .main-header p  { color: #555; }

        [data-testid="stChatMessage"] {
            background: #ffffff !important;
            border: 1px solid #dde1ef !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.07) !important;
        }

        div[data-testid="stButton"] button {
            background: #ffffff !important;
            color: #3b3b5c !important;
            border: 1.5px solid #c5cadf !important;
        }

        section[data-testid="stSidebar"] div[data-testid="stButton"] button {
            color: #c0392b !important;
            border-color: #e0c5c5 !important;
        }
        section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
            background: #c0392b !important;
            border-color: #c0392b !important;
        }

        /* History buttons override — grey, not red */
        section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="secondary"] {
            color: #3b3b5c !important;
            border-color: #c5cadf !important;
        }
        section[data-testid="stSidebar"] div[data-testid="stButton"] button[kind="secondary"]:hover {
            background: #667eea !important;
            color: white !important;
            border-color: #667eea !important;
        }

        [data-testid="stChatInput"] {
            background: #ffffff !important;
            border: 1.5px solid #c5cadf !important;
            border-radius: 14px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08) !important;
        }

        .stBottom > div {
            background: #f0f2f8 !important;
            border-top: 1px solid #dde1ef !important;
        }

        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] .stRadio,
        section[data-testid="stSidebar"] p {
            color: #2c2c54 !important;
        }
    }

    /* ── Dark mode enhancements ── */
    @media (prefers-color-scheme: dark) {
        [data-testid="stChatMessage"] {
            border: 1px solid rgba(255,255,255,0.07) !important;
            box-shadow: 0 1px 6px rgba(0,0,0,0.35) !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- Multi-Session Chat History ---
SESSIONS_FILE = "chat_sessions.json"


def _new_session_id():
    return str(uuid.uuid4())


def _session_title(messages):
    """Use first user message as session title (truncated to 50 chars)."""
    for m in messages:
        if m["role"] == "user":
            text = m["content"].lstrip("🎤 📎 📄").strip()
            return text[:50] + ("…" if len(text) > 50 else "")
    return "New Chat"


def load_sessions_data():
    """Load all sessions from disk. Migrates old chat_history.json if needed."""
    try:
        if os.path.exists(SESSIONS_FILE):
            with open(SESSIONS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict) and "sessions" in data:
                    return data
    except Exception:
        pass
    # Migrate old single-session file if it exists
    old_messages = []
    try:
        if os.path.exists("chat_history.json"):
            with open("chat_history.json", "r", encoding="utf-8") as f:
                old_messages = json.load(f)
                if not isinstance(old_messages, list):
                    old_messages = []
    except Exception:
        pass
    new_id = _new_session_id()
    sessions = []
    if old_messages:
        sessions = [{"id": new_id, "title": _session_title(old_messages),
                     "created_at": datetime.now().isoformat(), "messages": old_messages}]
    return {"current_id": new_id, "sessions": sessions}


def save_sessions_data(data):
    """Persist all sessions to disk."""
    try:
        with open(SESSIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def sync_current_session():
    """Sync current session messages into sessions_data and save to disk."""
    data = st.session_state._sessions_data
    cid = st.session_state.current_session_id
    messages = st.session_state.messages
    for s in data["sessions"]:
        if s["id"] == cid:
            s["messages"] = messages
            s["title"] = _session_title(messages)
            break
    save_sessions_data(data)

# --- Session State ---
if "_sessions_data" not in st.session_state:
    _data = load_sessions_data()
    if not _data.get("sessions"):
        _new_id = _new_session_id()
        _data["sessions"] = [{"id": _new_id, "title": "New Chat",
                               "created_at": datetime.now().isoformat(), "messages": []}]
        _data["current_id"] = _new_id
    elif not _data.get("current_id") or not any(s["id"] == _data["current_id"] for s in _data["sessions"]):
        _data["current_id"] = _data["sessions"][-1]["id"]
    st.session_state._sessions_data = _data
    st.session_state.current_session_id = _data["current_id"]
    _current = next((s for s in _data["sessions"] if s["id"] == st.session_state.current_session_id),
                    _data["sessions"][0])
    st.session_state.messages = _current["messages"]
if "current_session_id" not in st.session_state:
    st.session_state.current_session_id = st.session_state._sessions_data["current_id"]
if "messages" not in st.session_state:
    st.session_state.messages = []
if "st_class" not in st.session_state:
    st.session_state.st_class = "Class 10"
if "st_group" not in st.session_state:
    st.session_state.st_group = GROUPS_11_12[0]
if "subject" not in st.session_state:
    st.session_state.subject = get_subjects("Class 10")[0]
if "chapter" not in st.session_state:
    st.session_state.chapter = get_chapters("Class 10", get_subjects("Class 10")[0])[0]
if "language" not in st.session_state:
    st.session_state.language = LANGUAGES[0]
if "pending_voice" not in st.session_state:
    st.session_state.pending_voice = None
if "last_audio_hash" not in st.session_state:
    st.session_state.last_audio_hash = None
if "pdf_context" not in st.session_state:
    st.session_state.pdf_context = None
if "uploaded_img" not in st.session_state:
    st.session_state.uploaded_img = None
if "last_file_hash" not in st.session_state:
    st.session_state.last_file_hash = None
if "regen_lang" not in st.session_state:
    st.session_state.regen_lang = False
if "mode" not in st.session_state:
    st.session_state.mode = "chat"
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "flashcard_data" not in st.session_state:
    st.session_state.flashcard_data = None
if "flashcard_idx" not in st.session_state:
    st.session_state.flashcard_idx = 0
if "flashcard_flipped" not in st.session_state:
    st.session_state.flashcard_flipped = False
if "notes_content" not in st.session_state:
    st.session_state.notes_content = None


# --- Helper Functions ---


def extract_pdf_text(pdf_bytes):
    """Extract text from PDF bytes (max 5 pages, 4000 chars)."""
    if not PDF_SUPPORT:
        return None
    try:
        reader = pypdf.PdfReader(io.BytesIO(pdf_bytes))
        text = ""
        for page in reader.pages[:5]:
            text += page.extract_text() or ""
        return text[:4000].strip() or None
    except Exception:
        return None


def get_vision_response(image_bytes, mime_type, question, language, subject, chapter, class_name="Class 10"):
    """Send image to Groq Vision and return explanation."""
    system_prompt = get_system_prompt(language, subject, chapter, class_name)
    b64 = base64.b64encode(image_bytes).decode()
    if not question or not question.strip():
        question = (
            "Yeh image dekh. Isme jo bhi text, headings, diagrams, equations, ya figures hain — "
            "sab kuch padh aur samajh. Phir us poore topic ko ek friendly tutor ki tarah "
            "step-by-step samjha: pehle concept kya hai, phir kaise kaam karta hai, "
            "aur agar koi formula ya diagram ho toh usse bhi clearly explain kar. "
            f"NCERT {class_name} {subject} style mein rakh."
            if language == "Hinglish"
            else "Idha image-a paaru. Ula irukkura text, headings, diagrams, equations, figures — "
            "ellathayum padhi purinjukko. Aparam aa topic-a oru friendly tutor maari "
            "step-by-step explain pannu: concept enna, epdi work aaguthu, "
            "formula ya diagram iruntha atha kuda clearly explain pannu. "
            f"NCERT {class_name} {subject} context-la sollu."
        )
    try:
        resp = client.chat.completions.create(
            model=VISION_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": [
                    {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{b64}"}},
                    {"type": "text", "text": question},
                ]},
            ],
            max_tokens=2048,
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"Vision error: {e}"


def get_response(user_message, language, subject, chapter, class_name="Class 10"):
    """Send message to Groq and return the response."""
    system_prompt = get_system_prompt(language, subject, chapter, class_name)
    messages = [{"role": "system", "content": system_prompt}]

    # Inject PDF context if a document is loaded
    if st.session_state.pdf_context:
        messages.append({
            "role": "system",
            "content": (
                f"The student has uploaded a document. Use its content to help answer their question:\n\n"
                f"{st.session_state.pdf_context}"
            ),
        })

    for msg in st.session_state.messages[-10:]:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": user_message})

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=0.75,
                max_tokens=1024,
            )
            return response.choices[0].message.content
        except Exception as e:
            if "429" in str(e) and attempt < 2:
                time.sleep(3)
                continue
            return f"API error: {e}\n\nPlease try again in a few seconds."


# --- Tool: Generate helpers ---

def _call_api_json(user_prompt):
    """Call Groq with a structured prompt and parse JSON from the response."""
    system = get_system_prompt(st.session_state.language, st.session_state.subject, st.session_state.chapter, st.session_state.st_class)
    try:
        resp = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system},
                {"role": "user",   "content": user_prompt},
            ],
            temperature=0.4,
            max_tokens=2048,
        )
        content = resp.choices[0].message.content
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception:
        pass
    return None


def generate_quiz():
    lang = st.session_state.language
    subj = st.session_state.subject
    chap = st.session_state.chapter
    cls = st.session_state.st_class
    if lang == "Tanglish":
        prompt = (
            f"NCERT {cls} {subj}, chapter '{chap}' pathi exactly 5 MCQ questions "
            f"Tanglish-la generate pannu.\n"
            f"ONLY valid JSON return pannu — vera enna-um vendam:\n"
            f'{{"questions":[{{"q":"...","options":{{"A":"...","B":"...","C":"...","D":"..."}},"answer":"A","explanation":"Tanglish-la brief explanation"}}]}}'
        )
    else:
        prompt = (
            f"NCERT {cls} {subj}, chapter '{chap}' ke liye exactly 5 MCQ questions "
            f"Hinglish mein banao.\n"
            f"ONLY valid JSON return karo — kuch aur mat likhna:\n"
            f'{{"questions":[{{"q":"...","options":{{"A":"...","B":"...","C":"...","D":"..."}},"answer":"A","explanation":"Hinglish mein brief explanation"}}]}}'
        )
    data = _call_api_json(prompt)
    return data.get("questions", []) if data else None


def generate_flashcards():
    lang = st.session_state.language
    subj = st.session_state.subject
    chap = st.session_state.chapter
    cls = st.session_state.st_class
    if lang == "Tanglish":
        prompt = (
            f"NCERT {cls} {subj}, chapter '{chap}' pathi exactly 8 revision flashcards "
            f"Tanglish-la generate pannu.\n"
            f"ONLY valid JSON return pannu:\n"
            f'{{"flashcards":[{{"front":"term or question","back":"answer or definition in Tanglish"}}]}}'
        )
    else:
        prompt = (
            f"NCERT {cls} {subj}, chapter '{chap}' ke liye exactly 8 revision flashcards "
            f"Hinglish mein banao.\n"
            f"ONLY valid JSON return karo:\n"
            f'{{"flashcards":[{{"front":"term or question","back":"answer or definition in Hinglish"}}]}}'
        )
    data = _call_api_json(prompt)
    return data.get("flashcards", []) if data else None


def generate_notes():
    lang = st.session_state.language
    subj = st.session_state.subject
    chap = st.session_state.chapter
    cls = st.session_state.st_class
    system = get_system_prompt(lang, subj, chap, cls)
    if lang == "Tanglish":
        prompt = (
            f"NCERT {cls} {subj}, chapter '{chap}' pathi oru concise revision cheat sheet "
            f"Tanglish-la create pannu. Include: key concepts, important formulas/dates/events, "
            f"quick summary points, exam tips. Headings and bullet points use pannu."
        )
    else:
        prompt = (
            f"NCERT {cls} {subj}, chapter '{chap}' ka ek concise revision cheat sheet "
            f"Hinglish mein banao. Include: key concepts, important formulas/dates/events, "
            f"quick summary points, exam tips. Headings aur bullet points use karo."
        )
    try:
        resp = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system},
                {"role": "user",   "content": prompt},
            ],
            temperature=0.4,
            max_tokens=2048,
        )
        return resp.choices[0].message.content
    except Exception:
        return None


# --- Tool: Render functions ---

def render_notes():
    lang = st.session_state.language
    if st.session_state.notes_content is None:
        spin = "Notes ready panren..." if lang == "Tanglish" else "Notes bana raha hoon..."
        with st.spinner(spin):
            content = generate_notes()
        if content:
            st.session_state.notes_content = content
        else:
            st.error("Notes generate aagala, try again!" if lang == "Tanglish" else "Notes generate nahi hua, dobara try karo!")
            return

    st.markdown(f"### {st.session_state.chapter} — Quick Notes")
    st.markdown(st.session_state.notes_content)
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "Download Notes",
            data=st.session_state.notes_content,
            file_name=f"{st.session_state.subject}_{st.session_state.chapter[:30]}_notes.txt",
            mime="text/plain",
            use_container_width=True,
        )
    with col2:
        if st.button("Back to Chat", key="notes_back", use_container_width=True):
            st.session_state.mode = "chat"
            st.rerun()


def render_quiz():
    lang = st.session_state.language
    if st.session_state.quiz_data is None:
        spin = "Quiz ready panren..." if lang == "Tanglish" else "Quiz bana raha hoon..."
        with st.spinner(spin):
            questions = generate_quiz()
        if questions:
            st.session_state.quiz_data = questions
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
        else:
            st.error("Quiz generate aagala, try again!" if lang == "Tanglish" else "Quiz generate nahi hua, dobara try karo!")
            if st.button("← Back", key="quiz_err_back"):
                st.session_state.mode = "chat"
                st.rerun()
            return

    questions = st.session_state.quiz_data
    st.markdown(f"### Quiz — {st.session_state.chapter}")

    if not st.session_state.quiz_submitted:
        with st.form("quiz_form"):
            for i, q in enumerate(questions):
                st.markdown(f"**Q{i+1}. {q['q']}**")
                opts = [f"{k}) {v}" for k, v in q["options"].items()]
                choice = st.radio("", opts, key=f"qr_{i}", index=None, label_visibility="collapsed")
                if choice:
                    st.session_state.quiz_answers[i] = choice[0]  # "A" / "B" / "C" / "D"
                st.markdown("")
            submitted = st.form_submit_button(
                "Submit Quiz" if lang != "Tanglish" else "Submit pannunga",
                use_container_width=True, type="primary"
            )
        if submitted:
            st.session_state.quiz_submitted = True
            st.rerun()
    else:
        correct = sum(
            1 for i, q in enumerate(questions)
            if st.session_state.quiz_answers.get(i) == q["answer"]
        )
        total = len(questions)
        pct = int(correct / total * 100)
        st.markdown(f"## Score: {correct}/{total} ({pct}%)")
        st.progress(pct / 100)
        st.divider()
        for i, q in enumerate(questions):
            user_ans = st.session_state.quiz_answers.get(i, "—")
            correct_ans = q["answer"]
            ok = user_ans == correct_ans
            with st.expander(f"{'Correct' if ok else 'Wrong'} — Q{i+1}. {q['q']}"):
                st.markdown(f"**Your answer:** {user_ans}) {q['options'].get(user_ans, 'Not answered')}")
                st.markdown(f"**Correct answer:** {correct_ans}) {q['options'][correct_ans]}")
                if q.get("explanation"):
                    st.info(q["explanation"])
        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Try Again", key="quiz_retry", use_container_width=True):
                st.session_state.quiz_data = None
                st.session_state.quiz_answers = {}
                st.session_state.quiz_submitted = False
                st.rerun()
        with c2:
            if st.button("Back to Chat", key="quiz_back", use_container_width=True):
                st.session_state.mode = "chat"
                st.rerun()


def render_flashcards():
    lang = st.session_state.language
    if st.session_state.flashcard_data is None:
        spin = "Flashcards ready panren..." if lang == "Tanglish" else "Flashcards bana raha hoon..."
        with st.spinner(spin):
            cards = generate_flashcards()
        if cards:
            st.session_state.flashcard_data = cards
            st.session_state.flashcard_idx = 0
            st.session_state.flashcard_flipped = False
        else:
            st.error("Flashcards generate aagala!" if lang == "Tanglish" else "Flashcards generate nahi hua!")
            if st.button("← Back", key="fc_err_back"):
                st.session_state.mode = "chat"
                st.rerun()
            return

    cards = st.session_state.flashcard_data
    idx   = st.session_state.flashcard_idx
    total = len(cards)
    card  = cards[idx]

    st.markdown(f"### Flashcards — {st.session_state.chapter}")
    st.caption(f"Card {idx + 1} of {total}")
    st.progress((idx + 1) / total)

    flipped = st.session_state.flashcard_flipped
    if not flipped:
        st.markdown(
            f'<div style="background:linear-gradient(135deg,#667eea,#764ba2);border-radius:16px;'
            f'padding:2.5rem 2rem;text-align:center;min-height:140px;display:flex;'
            f'align-items:center;justify-content:center;">'
            f'<h3 style="color:white;margin:0;">{card["front"]}</h3></div>',
            unsafe_allow_html=True,
        )
        st.markdown("")
        if st.button("Flip — see answer", key="fc_flip", use_container_width=True):
            st.session_state.flashcard_flipped = True
            st.rerun()
    else:
        st.markdown(
            f'<div style="background:linear-gradient(135deg,#1e1e3f,#2d2d5e);border:2px solid #667eea;'
            f'border-radius:16px;padding:2.5rem 2rem;text-align:center;min-height:140px;display:flex;'
            f'align-items:center;justify-content:center;">'
            f'<p style="color:white;margin:0;font-size:1.1rem;">{card["back"]}</p></div>',
            unsafe_allow_html=True,
        )
        st.markdown("")
        if st.button("Show question", key="fc_flip_back", use_container_width=True):
            st.session_state.flashcard_flipped = False
            st.rerun()

    st.markdown("")
    c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
    with c1:
        if st.button("◀ Prev", key="fc_prev", use_container_width=True, disabled=(idx == 0)):
            st.session_state.flashcard_idx -= 1
            st.session_state.flashcard_flipped = False
            st.rerun()
    with c2:
        if st.button("Next ▶", key="fc_next", use_container_width=True, disabled=(idx == total - 1)):
            st.session_state.flashcard_idx += 1
            st.session_state.flashcard_flipped = False
            st.rerun()
    with c3:
        if st.button("Shuffle", key="fc_shuffle", use_container_width=True):
            random.shuffle(st.session_state.flashcard_data)
            st.session_state.flashcard_idx = 0
            st.session_state.flashcard_flipped = False
            st.rerun()
    with c4:
        if st.button("Chat", key="fc_back", use_container_width=True):
            st.session_state.mode = "chat"
            st.rerun()


# --- Sidebar ---
with st.sidebar:
    st.title("Settings")

    if st.button("New Chat", use_container_width=True, type="primary"):
        sync_current_session()
        _nid = _new_session_id()
        _new_sess = {"id": _nid, "title": "New Chat",
                     "created_at": datetime.now().isoformat(), "messages": []}
        st.session_state._sessions_data["sessions"].append(_new_sess)
        st.session_state._sessions_data["current_id"] = _nid
        st.session_state.current_session_id = _nid
        st.session_state.messages = []
        st.session_state.pdf_context = None
        st.session_state.uploaded_img = None
        save_sessions_data(st.session_state._sessions_data)
        st.rerun()

    st.divider()

    selected_language = st.radio(
        "Language / भाषा",
        LANGUAGES,
        index=LANGUAGES.index(st.session_state.language),
        help="Hinglish = Hindi + English | Tanglish = Tamil + English",
    )
    if selected_language != st.session_state.language:
        st.session_state.language = selected_language
        # Reset tool content so it regenerates in the new language
        st.session_state.notes_content = None
        st.session_state.quiz_data = None
        st.session_state.flashcard_data = None
        st.session_state.quiz_answers = {}
        st.session_state.quiz_submitted = False
        st.session_state.flashcard_idx = 0
        st.session_state.flashcard_flipped = False
        st.session_state.regen_lang = True   # flag — regenerate last chat reply in new language
        st.rerun()

    # Class selector
    selected_class = st.selectbox(
        "Class",
        CLASSES,
        index=CLASSES.index(st.session_state.st_class),
    )
    if selected_class != st.session_state.st_class:
        if st.session_state.messages:
            sync_current_session()
            _nid = _new_session_id()
            _new_sess = {"id": _nid, "title": "New Chat",
                         "created_at": datetime.now().isoformat(), "messages": []}
            st.session_state._sessions_data["sessions"].append(_new_sess)
            st.session_state._sessions_data["current_id"] = _nid
            st.session_state.current_session_id = _nid
            st.session_state.messages = []
            st.session_state.pdf_context = None
            st.session_state.uploaded_img = None
            save_sessions_data(st.session_state._sessions_data)
        st.session_state.st_class = selected_class
        _subjs = get_subjects(selected_class, st.session_state.st_group)
        st.session_state.subject = _subjs[0]
        st.session_state.chapter = get_chapters(selected_class, _subjs[0], st.session_state.st_group)[0]
        st.session_state.quiz_data = None
        st.session_state.flashcard_data = None
        st.session_state.notes_content = None
        st.rerun()

    # Group selector — only for Class 11/12
    if st.session_state.st_class in ("Class 11", "Class 12"):
        selected_group = st.selectbox(
            "Group / Stream",
            GROUPS_11_12,
            index=GROUPS_11_12.index(st.session_state.st_group),
        )
        if selected_group != st.session_state.st_group:
            if st.session_state.messages:
                sync_current_session()
                _nid = _new_session_id()
                _new_sess = {"id": _nid, "title": "New Chat",
                             "created_at": datetime.now().isoformat(), "messages": []}
                st.session_state._sessions_data["sessions"].append(_new_sess)
                st.session_state._sessions_data["current_id"] = _nid
                st.session_state.current_session_id = _nid
                st.session_state.messages = []
                st.session_state.pdf_context = None
                st.session_state.uploaded_img = None
                save_sessions_data(st.session_state._sessions_data)
            st.session_state.st_group = selected_group
            _subjs = get_subjects(st.session_state.st_class, selected_group)
            st.session_state.subject = _subjs[0]
            st.session_state.chapter = get_chapters(st.session_state.st_class, _subjs[0], selected_group)[0]
            st.session_state.quiz_data = None
            st.session_state.flashcard_data = None
            st.session_state.notes_content = None
            st.rerun()

    # Subject selector
    subject_list = get_subjects(st.session_state.st_class, st.session_state.st_group)
    if st.session_state.subject not in subject_list:
        st.session_state.subject = subject_list[0]

    selected_subject = st.selectbox(
        "Subject",
        subject_list,
        index=subject_list.index(st.session_state.subject),
    )
    if selected_subject != st.session_state.subject:
        if st.session_state.messages:
            sync_current_session()
            _nid = _new_session_id()
            _new_sess = {"id": _nid, "title": "New Chat",
                         "created_at": datetime.now().isoformat(), "messages": []}
            st.session_state._sessions_data["sessions"].append(_new_sess)
            st.session_state._sessions_data["current_id"] = _nid
            st.session_state.current_session_id = _nid
            st.session_state.messages = []
            st.session_state.pdf_context = None
            st.session_state.uploaded_img = None
            save_sessions_data(st.session_state._sessions_data)
        st.session_state.subject = selected_subject
        st.session_state.chapter = get_chapters(st.session_state.st_class, selected_subject, st.session_state.st_group)[0]
        st.rerun()

    chapter_list = get_chapters(st.session_state.st_class, st.session_state.subject, st.session_state.st_group)
    if st.session_state.chapter not in chapter_list:
        st.session_state.chapter = chapter_list[0]

    selected_chapter = st.selectbox(
        "Chapter",
        chapter_list,
        index=chapter_list.index(st.session_state.chapter),
    )
    if selected_chapter != st.session_state.chapter:
        st.session_state.chapter = selected_chapter
        st.session_state.quiz_data = None
        st.session_state.flashcard_data = None
        st.session_state.notes_content = None

    st.divider()
    st.markdown("**Tools**")
    t1, t2, t3 = st.columns(3)
    with t1:
        if st.button("Notes", key="btn_notes", use_container_width=True,
                     type="primary" if st.session_state.mode == "notes" else "secondary"):
            st.session_state.mode = "notes"
            st.session_state.notes_content = None
            st.rerun()
    with t2:
        if st.button("Quiz", key="btn_quiz", use_container_width=True,
                     type="primary" if st.session_state.mode == "quiz" else "secondary"):
            st.session_state.mode = "quiz"
            st.session_state.quiz_data = None
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
            st.rerun()
    with t3:
        if st.button("Cards", key="btn_cards", use_container_width=True,
                     type="primary" if st.session_state.mode == "flashcards" else "secondary"):
            st.session_state.mode = "flashcards"
            st.session_state.flashcard_data = None
            st.session_state.flashcard_idx = 0
            st.session_state.flashcard_flipped = False
            st.rerun()

    st.divider()

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        sync_current_session()
        st.session_state.pdf_context = None
        st.session_state.uploaded_img = None
        st.rerun()

    # --- History Panel ---
    past_sessions = [
        s for s in st.session_state._sessions_data.get("sessions", [])
        if s["id"] != st.session_state.current_session_id and s.get("messages")
    ]
    if past_sessions:
        st.divider()
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("**History**")
        with col2:
            if st.button("Clear All", key="clear_history", use_container_width=True):
                # Keep only the current session, delete all past sessions
                current = next(
                    (s for s in st.session_state._sessions_data["sessions"]
                     if s["id"] == st.session_state.current_session_id), None
                )
                st.session_state._sessions_data["sessions"] = [current] if current else []
                save_sessions_data(st.session_state._sessions_data)
                st.rerun()
        for s in reversed(past_sessions):
            label = s.get("title") or "Chat"
            if st.button(label, key=f"hist_{s['id']}", use_container_width=True):
                sync_current_session()
                st.session_state._sessions_data["current_id"] = s["id"]
                st.session_state.current_session_id = s["id"]
                st.session_state.messages = s["messages"]
                st.session_state.pdf_context = None
                st.session_state.uploaded_img = None
                save_sessions_data(st.session_state._sessions_data)
                st.rerun()

    st.divider()
    st.caption("Built with Streamlit + Groq AI")
    st.caption("AI-generated answers. Always verify with your NCERT textbook.")

# --- Main Header ---
_mascot_tag = (
    f'<span class="mascot-anim">'
    f'<img src="data:image/png;base64,{_mascot_b64}" '
    f'style="height:5rem;width:auto;display:block;">'
    f'</span>'
    if _mascot_b64 else ""
)
st.markdown(f"""
<div class="main-header">
    <div style="display:flex;align-items:center;justify-content:center;gap:14px;">
        {_mascot_tag}
        <div style="text-align:left;">
            <h1 style="margin:0;line-height:1.1;">Studybuddy AI</h1>
            <p style="margin:0;">Your AI NCERT tutor — in your language!</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<div style="text-align:center"><span class="chapter-badge">{st.session_state.st_class} › {st.session_state.subject} › {st.session_state.chapter}</span></div>',
    unsafe_allow_html=True
)

# --- Mode Routing ---
if st.session_state.mode == "notes":
    st.session_state.regen_lang = False   # clear flag — not applicable here
    render_notes()

elif st.session_state.mode == "quiz":
    st.session_state.regen_lang = False
    render_quiz()

elif st.session_state.mode == "flashcards":
    st.session_state.regen_lang = False
    render_flashcards()

else:
    # ── Chat mode ──

    # Starter Questions (show only when chat is empty)
    if not st.session_state.messages:
        if st.session_state.language == "Hinglish":
            welcome = f"Namaste! Main tera {st.session_state.st_class} {st.session_state.subject} ka personal tutor hoon.<br>Koi bhi doubt pooch — Hinglish mein samjhunga!"
        else:
            welcome = f"Vanakkam! Naan unoda {st.session_state.st_class} {st.session_state.subject} personal tutor.<br>Enna doubt-um kekko — Tanglish-la solluven!"
        st.markdown(f'<div class="welcome-box">{welcome}</div>', unsafe_allow_html=True)

        st.markdown("**Try asking:**")
        chapter_questions = get_starter_questions(st.session_state.language, st.session_state.st_class, st.session_state.subject, st.session_state.chapter)
        for i, q in enumerate(chapter_questions):
            if st.button(f" {q}", key=f"starter_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": q})
                spinner_text = "Soch raha hoon..." if st.session_state.language == "Hinglish" else "Yosikirein..."
                with st.spinner(spinner_text):
                    response = get_response(q, st.session_state.language, st.session_state.subject, st.session_state.chapter, st.session_state.st_class)
                st.session_state.messages.append({"role": "assistant", "content": response})
                sync_current_session()
                st.rerun()

    # Language-switch regeneration
    if st.session_state.regen_lang:
        st.session_state.regen_lang = False
        msgs = st.session_state.messages
        if msgs and msgs[-1]["role"] == "assistant":
            last_user = next(
                (m["content"] for m in reversed(msgs[:-1]) if m["role"] == "user"),
                None
            )
            if last_user:
                clean = last_user.lstrip("🎤 ")
                if clean.startswith("📎") or clean.startswith("📄") or " — " in clean[:60]:
                    clean = "Summarize the uploaded content briefly."
                spin = "Translate kar raha hoon..." if st.session_state.language == "Hinglish" else "Maarikirein..."
                st.session_state.messages.pop()
                with st.spinner(spin):
                    new_resp = get_response(clean, st.session_state.language, st.session_state.subject, st.session_state.chapter, st.session_state.st_class)
                st.session_state.messages.append({"role": "assistant", "content": new_resp})
                sync_current_session()
                st.rerun()

    # Chat Messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Handle pending voice input
    if st.session_state.pending_voice:
        user_input = st.session_state.pending_voice
        st.session_state.pending_voice = None

        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        spinner_text = "Soch raha hoon..." if st.session_state.language == "Hinglish" else "Yosikirein..."
        with st.chat_message("assistant"):
            with st.spinner(spinner_text):
                response = get_response(user_input, st.session_state.language, st.session_state.subject, st.session_state.chapter, st.session_state.st_class)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        sync_current_session()

    # Chat Input with file attachment
    accepted_types = ["png", "jpg", "jpeg", "pdf"] if PDF_SUPPORT else ["png", "jpg", "jpeg"]
    result = st.chat_input(
        "Edha doubt kelu../Kuch doubt pooch...",
        accept_file=True,
        file_type=accepted_types,
    )

    if result:
        text = result.text or ""
        files = result.files if result.files else []

        if files:
            file = files[0]
            file_bytes = file.getvalue()

            if file.type == "application/pdf":
                pdf_text = extract_pdf_text(file_bytes)
                if pdf_text:
                    st.session_state.pdf_context = pdf_text
                    user_label = f"{file.name}" + (f" — {text}" if text else " — Please explain this document.")
                    spinner_text = "Padh raha hoon..." if st.session_state.language == "Hinglish" else "Padikiren..."
                    st.session_state.messages.append({"role": "user", "content": user_label})
                    with st.chat_message("user"):
                        st.markdown(user_label)
                    with st.chat_message("assistant"):
                        with st.spinner(spinner_text):
                            response = get_response(text or "Summarize this document briefly.", st.session_state.language, st.session_state.subject, st.session_state.chapter, st.session_state.st_class)
                        st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    sync_current_session()
                else:
                    st.error("Couldn't read this PDF. Try an image instead.")
            else:
                user_label = f"{file.name}" + (f" — {text}" if text else "")
                spinner_text = "Dekh raha hoon..." if st.session_state.language == "Hinglish" else "Paakkiren..."
                st.session_state.messages.append({"role": "user", "content": user_label})
                with st.chat_message("user"):
                    st.image(file_bytes, width=200)
                    if text:
                        st.markdown(text)
                with st.chat_message("assistant"):
                    with st.spinner(spinner_text):
                        response = get_vision_response(file_bytes, file.type, text, st.session_state.language, st.session_state.subject, st.session_state.chapter, st.session_state.st_class)
                    st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                sync_current_session()

        elif text:
            st.session_state.messages.append({"role": "user", "content": text})
            with st.chat_message("user"):
                st.markdown(text)
            with st.chat_message("assistant"):
                with st.spinner("Soch raha hoon..." if st.session_state.language == "Hinglish" else "Yosikirein..."):
                    response = get_response(text, st.session_state.language, st.session_state.subject, st.session_state.chapter, st.session_state.st_class)
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
            sync_current_session()

# --- Floating Mic Button (dynamically positioned next to the send button) ---
components.html("""
<script>
(function() {
    var pd = window.parent.document;
    var pw = window.parent;

    // Remove old button
    var old = pd.getElementById('padhai-mic');
    if (old) old.remove();

    // SVG mic icon (white, matches the style in the screenshot)
    var MIC_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="white" style="display:block;margin:auto"><path d="M12 2a3 3 0 0 1 3 3v7a3 3 0 0 1-6 0V5a3 3 0 0 1 3-3zm-1 3v7a1 1 0 0 0 2 0V5a1 1 0 0 0-2 0zM7 12a5 5 0 0 0 10 0h2a7 7 0 0 1-6 6.93V21h2a1 1 0 1 1 0 2H9a1 1 0 1 1 0-2h2v-2.07A7 7 0 0 1 5 12H7z"/></svg>';
    var STOP_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="white" style="display:block;margin:auto"><rect x="4" y="4" width="16" height="16" rx="3"/></svg>';

    // Create mic button
    var btn = pd.createElement('button');
    btn.id = 'padhai-mic';
    btn.innerHTML = MIC_SVG;
    btn.title = 'Voice Input — click and speak';
    btn.style.cssText = [
        'border:none',
        'background:#3d4450',
        'color:white',
        'cursor:pointer',
        'padding:0',
        'display:flex',
        'align-items:center',
        'justify-content:center',
        'box-shadow:0 2px 8px rgba(0,0,0,0.4)',
        'transition:background 0.2s',
        'margin-right:6px',
        'flex-shrink:0'
    ].join(';');
    // Removed direct body append

    // Inject CSS to make the send button match the mic button style
    if (!pd.getElementById('padhai-send-style')) {
        var style = pd.createElement('style');
        style.id = 'padhai-send-style';
        style.textContent = [
            '[data-testid="stChatInputSubmitButton"] {',
            '  background: #3d4450 !important;',
            '  border-radius: 10px !important;',
            '  box-shadow: 0 2px 8px rgba(0,0,0,0.4) !important;',
            '  border: none !important;',
            '  transition: background 0.2s !important;',
            '}',
            '[data-testid="stChatInputSubmitButton"]:hover {',
            '  background: #4b5563 !important;',
            '}',
            '[data-testid="stChatInputSubmitButton"] svg {',
            '  fill: white !important;',
            '  color: white !important;',
            '}',
        ].join('');
        pd.head.appendChild(style);
    }

    // Insert mic button snugly as a sibling BEFORE the send button,
    // leaning on native CSS layout to fix any movement delay (woggling)
    var pdRAF = pw.requestAnimationFrame;
    var attachLoop = setInterval(function() {
        if (!window.parent) { clearInterval(attachLoop); return; }
        var sendBtn = pd.querySelector('[data-testid="stChatInputSubmitButton"]')
                   || pd.querySelector('[data-testid="stChatInput"] button');
        
        if (sendBtn && sendBtn.parentNode) {
            if (sendBtn.previousSibling !== btn) {
                var compStyle = pw.getComputedStyle(sendBtn);
                btn.style.height = compStyle.height;
                btn.style.width = compStyle.height; // Square by default, same size as send height
                btn.style.borderRadius = compStyle.borderRadius;
                sendBtn.parentNode.insertBefore(btn, sendBtn);
            }
        }
    }, 250);
    // Cleanup interval after long idle mapping
    setTimeout(function() { clearInterval(attachLoop); }, 60000);

    // Stop existing loop from previous script execution and start new
    if (pw.padhaiMicRAF) pw.cancelAnimationFrame(pw.padhaiMicRAF);

    // Speech recognition logic
    var rec = null;
    var going = false;

    btn.onclick = function() {
        if (going) { if (rec) rec.abort(); return; }

        var SR = pw.SpeechRecognition || pw.webkitSpeechRecognition;
        if (!SR) {
            pw.alert('Voice input needs Google Chrome!');
            return;
        }

        rec = new SR();
        rec.lang = 'en-IN';
        rec.continuous = false;
        rec.interimResults = false;

        rec.onstart = function() {
            going = true;
            btn.innerHTML = STOP_SVG;
            btn.style.background = '#dc2626';
        };

        rec.onresult = function(e) {
            var text = e.results[0][0].transcript;
            var ta = pd.querySelector('[data-testid="stChatInputTextArea"]');
            if (ta) {
                var desc = Object.getOwnPropertyDescriptor(pw.HTMLTextAreaElement.prototype, 'value');
                if (desc && desc.set) {
                    desc.set.call(ta, text);
                    ta.dispatchEvent(new pw.Event('input', { bubbles: true }));
                    ta.focus();
                }
            }
        };

        rec.onend = function() {
            going = false;
            btn.innerHTML = MIC_SVG;
            btn.style.background = '#3d4450';
        };

        rec.onerror = function() {
            going = false;
            btn.innerHTML = MIC_SVG;
            btn.style.background = '#3d4450';
        };

        try { rec.start(); } catch(err) {
            going = false;
            btn.innerHTML = MIC_SVG;
            btn.style.background = '#3d4450';
        }
    };
})();
</script>
""", height=0, scrolling=False)