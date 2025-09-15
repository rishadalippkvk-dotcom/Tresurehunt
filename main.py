import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Treasure Hunt", layout="centered")

# --- Initialize session state ---
if "level" not in st.session_state:
    st.session_state.level = 1

# --- Define questions, answers, and hints ---
levels = {
    1: {"q": "🌍 What is the capital of France?", "a": "paris", "hint": "City of love, Eiffel Tower."},
    2: {"q": "🔢 What is 12 × 8?", "a": "96", "hint": "Think multiplication table of 12."},
    3: {"q": "🐍 Which programming language is named after a snake?", "a": "python", "hint": "It’s also a comedy group from the UK."},
    4: {"q": "🪐 Which planet is known as the Red Planet?", "a": "mars", "hint": "Fourth planet from the Sun."},
    5: {"q": "🎬 Who directed the movie 'Inception'?", "a": "nolan", "hint": "Same director as 'The Dark Knight'."},
    6: {"q": "📘 What does 'HTML' stand for?", "a": "hypertext markup language", "hint": "It’s the standard language for building web pages."},
    7: {"q": "💻 What is 2 to the power of 5?", "a": "32", "hint": "2 × 2 × 2 × 2 × 2."},
    8: {"q": "🔑 Final Riddle: I speak without a mouth and hear without ears. What am I?", "a": "echo", "hint": "You can hear me in caves and mountains."}
}

# --- UI Styling + Background ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
    background-size: cover;
    background-position: center;
}
.stTextInput > div > div > input {
    border: 2px solid #4CAF50;
    border-radius: 10px;
    padding: 8px;
}
.card {
    background-color: rgba(0, 0, 0, 0.65);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.5);
    margin-bottom: 20px;
    color: white;
}
h1, h2, h3, h4, h5, h6, p {
    color: white !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Title ---
st.title("🏆 Treasure Hunt Challenge")
st.write("Solve the puzzles below to unlock each level 🔑")

# --- Levels ---
for level in range(1, 9):
    if st.session_state.level >= level:
        with st.container():
            st.markdown(f"<div class='card'>", unsafe_allow_html=True)
            st.subheader(f"Level {level}")

            st.write(levels[level]["q"])

            # --- Hint Expander ---
            with st.expander("💡 Need a hint?"):
                st.info(levels[level]["hint"])

            key_input = st.text_input(f"Your Answer for Level {level}", type="default", key=f"input_{level}")

            if key_input:
                if key_input.strip().lower() == levels[level]["a"]:
                    if st.session_state.level == level and st.session_state.level < 8:
                        st.success(f"✅ Correct! Level {level} unlocked.")
                        st.session_state.level += 1
                else:
                    st.error("❌ Wrong answer. Try again!")

            st.markdown("</div>", unsafe_allow_html=True)

# --- Final message ---
if st.session_state.level > 8:
    st.balloons()
    st.success("🎉 Congratulations! You have completed all 8 levels of the Treasure Hunt!")
