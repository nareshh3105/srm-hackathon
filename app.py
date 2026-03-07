import time
import urllib.request
import json
import base64
import io
import streamlit as st
import streamlit.components.v1 as components
from groq import Groq

try:
    import pypdf
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False

from config import (
    GROQ_API_KEY, MODEL_NAME, CHAPTERS, LANGUAGES,
    get_starter_questions, CHAPTER_WIKI_MAP,
)
from prompts import get_system_prompt

VISION_MODEL = "llama-3.2-11b-vision-preview"

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
if "pdf_context" not in st.session_state:
    st.session_state.pdf_context = None
if "uploaded_img" not in st.session_state:
    st.session_state.uploaded_img = None
if "last_file_hash" not in st.session_state:
    st.session_state.last_file_hash = None
if "regen_lang" not in st.session_state:
    st.session_state.regen_lang = False


# --- Helper Functions ---

@st.cache_data(ttl=3600)
def get_chapter_diagram(chapter):
    """Fetch a diagram image + caption from Wikipedia for the chapter."""
    topic = CHAPTER_WIKI_MAP.get(chapter)
    if not topic:
        return None, None
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
        req = urllib.request.Request(url, headers={"User-Agent": "PadhAI-NCERT/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
            img_url = data.get("thumbnail", {}).get("source")
            caption = data.get("description", topic.replace("_", " "))
            return img_url, caption
    except Exception:
        return None, None


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


def get_vision_response(image_bytes, mime_type, question, language, chapter):
    """Send image to Groq Vision and return explanation."""
    system_prompt = get_system_prompt(language, chapter)
    b64 = base64.b64encode(image_bytes).decode()
    if not question or not question.strip():
        question = (
            "Is image mein kya dikh raha hai? NCERT Class 10 Science ke hisaab se explain karo."
            if language == "Hinglish"
            else "Idha paaru — NCERT Class 10 Science context-la enna irukku, explain pannu."
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
            max_tokens=1024,
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"⚠️ Vision error: {e}"


def get_response(user_message, language, chapter):
    """Send message to Groq and return the response."""
    system_prompt = get_system_prompt(language, chapter)
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
        st.session_state.regen_lang = True   # flag — regenerate in main area
        st.rerun()

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
        st.session_state.pdf_context = None
        st.session_state.uploaded_img = None
        st.rerun()

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
        welcome = "👋 Vanakkam! Naan unoda Class 10 Science personal tutor.<br>Enna doubt-um kekko — Tanglish-la solluven! 🎓"
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

# --- Language-switch regeneration (runs in main area, not sidebar) ---
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
            if clean.startswith("📎") or clean.startswith("📄"):
                clean = "Summarize the uploaded content briefly."
            spin = "Translate kar raha hoon... 🔄" if st.session_state.language == "Hinglish" else "Maarikirein... 🔄"
            st.session_state.messages.pop()   # remove old-language reply so it doesn't bias the model
            with st.spinner(spin):
                new_resp = get_response(clean, st.session_state.language, st.session_state.chapter)
            st.session_state.messages.append({"role": "assistant", "content": new_resp})
            st.rerun()

# --- Chat Messages ---
last_idx = len(st.session_state.messages) - 1
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        # Show diagram expander only under the latest assistant message
        if msg["role"] == "assistant" and i == last_idx:
            with st.expander("📊 See related diagram"):
                img_url, caption = get_chapter_diagram(st.session_state.chapter)
                if img_url:
                    st.image(img_url, caption=caption, use_container_width=True)
                else:
                    st.caption("No diagram found for this chapter.")

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

# --- Chat Input with file attachment ---
accepted_types = ["png", "jpg", "jpeg", "pdf"] if PDF_SUPPORT else ["png", "jpg", "jpeg"]
result = st.chat_input(
    "Ask anything",
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
            # PDF — extract text and use as context
            pdf_text = extract_pdf_text(file_bytes)
            if pdf_text:
                st.session_state.pdf_context = pdf_text
                user_label = f"📄 {file.name}" + (f" — {text}" if text else " — Please explain this document.")
                spinner_text = "Padh raha hoon... 📖" if st.session_state.language == "Hinglish" else "Padikiren... 📖"
                st.session_state.messages.append({"role": "user", "content": user_label})
                with st.chat_message("user"):
                    st.markdown(user_label)
                with st.chat_message("assistant"):
                    with st.spinner(spinner_text):
                        response = get_response(text or "Summarize this document briefly.", st.session_state.language, st.session_state.chapter)
                    st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                st.error("Couldn't read this PDF. Try an image instead.")
        else:
            # Image — send to vision model
            user_label = f"📎 {file.name}" + (f" — {text}" if text else "")
            spinner_text = "Dekh raha hoon... 👀" if st.session_state.language == "Hinglish" else "Paakkiren... 👀"
            st.session_state.messages.append({"role": "user", "content": user_label})
            with st.chat_message("user"):
                st.image(file_bytes, width=200)
                if text:
                    st.markdown(text)
            with st.chat_message("assistant"):
                with st.spinner(spinner_text):
                    response = get_vision_response(file_bytes, file.type, text, st.session_state.language, st.session_state.chapter)
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    elif text:
        # Text only
        st.session_state.messages.append({"role": "user", "content": text})
        with st.chat_message("user"):
            st.markdown(text)
        with st.chat_message("assistant"):
            with st.spinner("Soch raha hoon... 🤔" if st.session_state.language == "Hinglish" else "Yosikirein... 🤔"):
                response = get_response(text, st.session_state.language, st.session_state.chapter)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

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
        'position:fixed',
        'z-index:999999',
        'border:none',
        'background:#3d4450',
        'color:white',
        'cursor:pointer',
        'padding:0',
        'display:none',
        'align-items:center',
        'justify-content:center',
        'box-shadow:0 2px 8px rgba(0,0,0,0.4)',
        'transition:background 0.2s',
    ].join(';');
    pd.body.appendChild(btn);

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

    // Find the send button and snap the mic button right next to it, same size
    function snapToSendBtn() {
        var sendBtn = pd.querySelector('[data-testid="stChatInputSubmitButton"]')
                   || pd.querySelector('[data-testid="stChatInput"] button');
        if (!sendBtn) return;
        var r = sendBtn.getBoundingClientRect();
        // Match exact size of the send button
        btn.style.width  = r.width  + 'px';
        btn.style.height = r.height + 'px';
        btn.style.lineHeight = r.height + 'px';
        btn.style.borderRadius = pw.getComputedStyle(sendBtn).borderRadius;
        // Place mic button directly to the LEFT of the send button, vertically centered
        btn.style.top  = r.top + 'px';
        btn.style.left = (r.left - r.width - 6) + 'px';
        btn.style.display = 'flex';
    }

    // Poll until the send button appears, then keep in sync
    var snapInterval = setInterval(snapToSendBtn, 300);
    // Stop polling after 30 s to avoid memory leak
    setTimeout(function() { clearInterval(snapInterval); }, 30000);

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
