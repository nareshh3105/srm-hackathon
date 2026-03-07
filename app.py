import time
import streamlit as st
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME, CHAPTERS, LANGUAGES, get_starter_questions
from prompts import get_system_prompt

# --- Page Config ---
st.set_page_config(
    page_title="PadhAI - NCERT Class 10 Science Tutor",
    page_icon="📚",
    layout="centered",
)

# --- Initialize Groq ---
client = Groq(api_key=GROQ_API_KEY)

# --- Custom CSS ---
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0 0.5rem 0;
    }
    .main-header h1 { font-size: 2.5rem; margin-bottom: 0; }
    .main-header p { color: #888; font-size: 1rem; margin-top: 0.25rem; }
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
    }
    .stChatMessage { border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chapter" not in st.session_state:
    st.session_state.chapter = CHAPTERS[0]
if "language" not in st.session_state:
    st.session_state.language = LANGUAGES[0]
if "pending_voice" not in st.session_state:
    st.session_state.pending_voice = None
if "last_audio_hash" not in st.session_state:
    st.session_state.last_audio_hash = None


def get_response(user_message: str, language: str, chapter: str) -> str:
    """Send message to Groq and return the response."""
    system_prompt = get_system_prompt(language, chapter)

    # Build proper messages array with history
    messages = [{"role": "system", "content": system_prompt}]
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
            return f"⚠️ API error: {e}\n\nPlease try again in a few seconds."


# --- Sidebar ---
with st.sidebar:
    st.title("⚙️ Settings")

    selected_language = st.radio(
        "🌐 Language / भाषा",
        LANGUAGES,
        index=LANGUAGES.index(st.session_state.language),
        help="Hinglish = Hindi + English | Tanglish = Tamil + English",
    )
    if selected_language != st.session_state.language:
        st.session_state.language = selected_language

    selected_chapter = st.selectbox(
        "📖 Chapter",
        CHAPTERS,
        index=CHAPTERS.index(st.session_state.chapter),
    )
    if selected_chapter != st.session_state.chapter:
        st.session_state.chapter = selected_chapter

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    # --- Voice Input ---
    st.markdown("**🎤 Voice Input**")
    audio_input = st.audio_input("Record your doubt", key="voice_input")
    if audio_input is not None:
        audio_bytes = audio_input.read()
        audio_hash = hash(audio_bytes)
        if st.session_state.last_audio_hash != audio_hash:
            st.session_state.last_audio_hash = audio_hash
            listen_text = "Sun raha hoon... 🎧" if st.session_state.language == "Hinglish" else "Kekkiren... 🎧"
            with st.spinner(listen_text):
                try:
                    result = client.audio.transcriptions.create(
                        file=("audio.wav", audio_bytes, "audio/wav"),
                        model="whisper-large-v3",
                    )
                    voice_text = result.text.strip()
                    if voice_text:
                        st.session_state.pending_voice = voice_text
                        st.rerun()
                except Exception as e:
                    st.error(f"Voice error: {e}")

    st.divider()
    st.caption("Built with Streamlit + Groq AI")
    st.caption("⚠️ AI-generated answers. Always verify with your NCERT textbook.")

# --- Main Header ---
st.markdown("""
<div class="main-header">
    <h1>📚 PadhAI</h1>
    <p>Your AI tutor for NCERT Class 10 Science — in your language!</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<div style="text-align:center"><span class="chapter-badge">📖 {st.session_state.chapter}</span></div>',
    unsafe_allow_html=True
)

# --- Starter Questions (show only when chat is empty) ---
if not st.session_state.messages:
    if st.session_state.language == "Hinglish":
        welcome = "👋 Namaste! Main tera Class 10 Science ka personal tutor hoon.<br>Koi bhi doubt pooch — Hinglish mein samjhunga! 🎓"
    else:
        welcome = "👋 Vanakkam! Naan unoda Class 10 Science personal tutor.<br>Enna doubt naalu kelu"
    st.markdown(f'<div class="welcome-box">{welcome}</div>', unsafe_allow_html=True)

    st.markdown("**💡 Try asking:**")
    chapter_questions = get_starter_questions(st.session_state.language, st.session_state.chapter)
    for i, q in enumerate(chapter_questions):
        if st.button(f" {q}", key=f"starter_{i}", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": q})
            spinner_text = "Soch raha hoon... 🤔" if st.session_state.language == "Hinglish" else "Yosikirein... 🤔"
            with st.spinner(spinner_text):
                response = get_response(q, st.session_state.language, st.session_state.chapter)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# --- Chat Messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Handle pending voice input ---
if st.session_state.pending_voice:
    user_input = st.session_state.pending_voice
    st.session_state.pending_voice = None

    st.session_state.messages.append({"role": "user", "content": f"🎤 {user_input}"})
    with st.chat_message("user"):
        st.markdown(f"🎤 {user_input}")

    spinner_text = "Soch raha hoon... 🤔" if st.session_state.language == "Hinglish" else "Yosikirein... 🤔"
    with st.chat_message("assistant"):
        with st.spinner(spinner_text):
            response = get_response(user_input, st.session_state.language, st.session_state.chapter)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# --- Chat Input ---
if user_input := st.chat_input("Apna doubt pooch... / Enna doubt naalu kelu..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get and show bot response
    with st.chat_message("assistant"):
        with st.spinner("Soch raha hoon... 🤔" if st.session_state.language == "Hinglish" else "Yosikirein... 🤔"):
            response = get_response(user_input, st.session_state.language, st.session_state.chapter)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
