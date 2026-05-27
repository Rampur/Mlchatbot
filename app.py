import streamlit as st
import time
from openai import OpenAI
from course_data import MODULES, COURSE_INFO, SYSTEM_PROMPT

# ── Config ──────────────────────────────────────────────────────────
GROQ_API_KEY = "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"
GROQ_BASE = "https://api.groq.com/openai/v1"
MODEL = "llama-3.1-8b-instant"

# Rate limit: max 5 requests per 60 seconds
RATE_LIMIT = 5
RATE_WINDOW = 60

# Token limit per response
MAX_TOKENS = 512

st.set_page_config(page_title="ML Bot - BIS602", page_icon="🤖", layout="wide")

st.markdown(
    """
<style>
    .chat-msg { padding: 0.75rem 1rem; border-radius: 12px; margin-bottom: 0.5rem; max-width: 85%; }
    .user-msg { background: #1e88e5; color: white; margin-left: auto; }
    .bot-msg { background: #f0f2f6; color: #1a1a2e; margin-right: auto; }
    .stApp { background: #ffffff; }
    h1, h2, h3 { color: #1a1a2e; }
    .block-container { padding-top: 1.5rem; }
    .stSidebar .sidebar-content { background: #f8f9fa; }
</style>
""",
    unsafe_allow_html=True,
)

client = OpenAI(base_url=GROQ_BASE, api_key=GROQ_API_KEY)

def enforce_rate_limit():
    now = time.time()
    timestamps = st.session_state.get("request_timestamps", [])
    timestamps = [t for t in timestamps if now - t < RATE_WINDOW]
    st.session_state.request_timestamps = timestamps
    if len(timestamps) >= RATE_LIMIT:
        wait = int(RATE_WINDOW - (now - timestamps[0]))
        st.warning(f"⏳ Rate limit reached. Please wait ~{wait}s before asking another question.")
        return False
    st.session_state.request_timestamps.append(now)
    return True

def call_llm(messages):
    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=0.3,
            extra_headers={
                "HTTP-Referer": "http://localhost:8501",
                "X-Title": "NIE-ML-Chatbot: Rampur Srinath",
            },
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {e}. Please try again."

# ── Layout ──────────────────────────────────────────────────────────
C1, C2 = st.columns([1.2, 2.8])

with C1:
    st.image(
        "NIE_University_logo.svg",
        width=120,
    )
    st.markdown(f"### {COURSE_INFO['code']}: {COURSE_INFO['title']}")
    st.markdown(f"**Instructor:** {COURSE_INFO['instructor']}")
    st.markdown(f"**Semester:** {COURSE_INFO['semester']}")
    st.markdown(f"**Term:** {COURSE_INFO['term']}")
    st.divider()

    st.markdown("### 📚 Course Modules")
    module_names = list(MODULES.keys())
    selected_module = st.selectbox("Select a module to explore", module_names)
    mod = MODULES[selected_module]
    st.markdown(f"*{mod['description']}*")
    with st.expander("📋 View Sessions", expanded=True):
        for snum, scontent in mod["sessions"].items():
            st.markdown(f"**Session {snum}:** {scontent}")
    if "test_info" in mod:
        st.info(mod["test_info"])

    with st.expander("📖 Course Outcomes"):
        for co in COURSE_INFO["course_outcomes"]:
            st.markdown(f"- {co}")

    with st.expander("📚 Textbooks"):
        for b in COURSE_INFO["textbooks"]:
            st.markdown(f"- {b}")
        st.markdown("**Reference Books:**")
        for b in COURSE_INFO["reference_books"]:
            st.markdown(f"- {b}")

with C2:
    st.markdown("## 💬 ML Course Chatbot")
    st.markdown("*Ask questions about the Machine Learning course taught by Rampur Srinath*")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi! I'm your ML course assistant. Ask me about any topic from **BIS602 Machine Learning** taught by **Rampur Srinath**.\n\nI can help with:\n• 📖 Module topics & sessions\n• 🔍 Algorithm explanations\n• 📊 Evaluation metrics\n• 📝 Exam info & portions\n\n*I only answer questions within this course syllabus.*",
            }
        ]
        st.session_state.api_messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "assistant",
                "content": "Hi! I'm your NIE ML course assistant. Ask me about any topic from BIS602 Machine Learning taught by **Rampur Srinath**.",
            },
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask something about the ML course..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if not enforce_rate_limit():
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": "⏳ Please wait a moment before asking another question (rate limit: 5 requests/min).",
                }
            )
        else:
            st.session_state.api_messages.append({"role": "user", "content": prompt})

            with st.spinner("Thinking..."):
                answer = call_llm(st.session_state.api_messages)

            st.session_state.api_messages.append({"role": "assistant", "content": answer})
            st.session_state.messages.append({"role": "assistant", "content": answer})

        st.rerun()
