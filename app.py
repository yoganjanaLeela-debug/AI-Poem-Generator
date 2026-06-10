import streamlit as st
import ollama

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Poem Generator",
    page_icon="🪶",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🪶 AI Poem Generator")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "💡 Inspiration",
        "ℹ️ About"
    ]
)

# =========================
# HOME PAGE
# =========================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="main-title">
            🪶 AI Poem Generator
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
            Turn your thoughts into beautiful words ✨
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        topic = st.text_input(
            "Topic",
            placeholder="Friendship"
        )

    with col2:
        mood = st.selectbox(
            "Mood",
            [
                "Happy",
                "Sad",
                "Romantic",
                "Inspirational"
            ]
        )

    with col3:
        style = st.selectbox(
            "Style",
            [
                "Haiku",
                "Sonnet",
                "Free Verse",
                "Rhyming"
            ]
        )

    if style == "Haiku":
        lines = 3
        st.info("Haiku poems use 3 lines.")
    else:
        lines = st.slider(
            "Number of Lines",
            min_value=4,
            max_value=20,
            value=8
        )

    if st.button("✨ Generate Poem"):

        if topic.strip() == "":
            st.warning("Please enter a topic.")

        else:

            with st.spinner("Generating poem..."):

                prompt = f"""
Write a {style} poem about {topic}.

Mood: {mood}

STRICT RULES:
- Write EXACTLY {lines} lines.
- Each line must be on a separate line.
- Do not write a title.
- Do not write explanations.
- Output ONLY the poem.
"""

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                poem = response["message"]["content"].strip()

                poem_lines = [
                    line.strip()
                    for line in poem.split("\n")
                    if line.strip()
                ]

                if len(poem_lines) > lines:
                    poem_lines = poem_lines[:lines]

                poem = "\n".join(poem_lines)
                st.session_state["poem"] = poem

            # Show title

            st.markdown(
                 """
                   <div class="poem-title">
                       💜 Your Poem
                  </div>
                """,
                unsafe_allow_html=True
            )

# Show poem

            st.markdown(
                  f"""
                  <div class="poem-card">
                  {poem.replace(chr(10), '<br>')}
                  </div>
                  """,
                  unsafe_allow_html=True
            )

# Buttons

            col1, col2, col3 = st.columns(3)

            with col1:
                st.download_button(
                     "⬇ Download Poem",
                     poem,
                     file_name="poem.txt",
                     mime="text/plain"
            )

            with col2:
                if st.button("🔄 Regenerate"):
                    st.rerun()
           
# =========================
# INSPIRATION PAGE
# =========================

elif page == "💡 Inspiration":

    st.markdown(
        """
        <div class="main-title">
            💡 Poetry Inspiration
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
## 💡 Try These Topics

🌿 Nature

❤️ Love

🤝 Friendship

🌙 Dreams

🔥 Courage

🚀 Adventure

👨‍👩‍👧 Family

🏆 Success

⭐ Hope

💻 Technology

🎵 Music

🌧 Rain

🌅 Sunrise

🌌 Universe

🦋 Freedom
""")

# =========================
# ABOUT PAGE
# =========================

elif page == "ℹ️ About":

    st.markdown(
        """
        <div class="main-title">
            ℹ️ About
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
## 🚀 Tech Stack

- Streamlit
- Ollama
- Llama 3.2
- Python

## ✨ Features

- AI Poem Generation
- Multiple Poem Styles
- Mood Selection
- Download Poems
- Beautiful UI

## 🔮 Future Enhancements

- PDF Export
- Poem Sharing
- Poem History
""")