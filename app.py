import streamlit as st

# Page configuration
st.set_page_config(page_title="Rawan's Text Lab", layout="centered")

st.title("Simple Text Analyzer")

# User Input
user_input = st.text_input(
    "Enter a sentence:", placeholder="How are you feeling today?"
)

if user_input:
    # 1. Basic Stats (Your original features)
    words = len(user_input.split())
    chars = len(user_input)
    positive_words = ["good", "happy", "great", "amazing", "love", "best"]
    negative_words = [
        "bad",
        "sad",
        "angry",
        "hate",
        "worst",
        "fail",
        "not Happy",
        "not good",
        "not great",
        "not amazing",
        "not love",
        "not best",
        "not bad",
        "not sad",
        "not angry",
        "not hate",
        "not worst",
        "not fail",
        "terrible",
        "awful",
        "horrible",
        "disappointing",
        "miserable",
        "depressing",
    ]

    mood = "Neutral"
    if any(word in user_input.lower() for word in positive_words):
        mood = "Positive"
    elif any(word in user_input.lower() for word in negative_words):
        mood = "Negative"

    col1, col2, col3 = st.columns(3)
    col1.metric("Words", words)
    col2.metric("Characters", chars)
    col3.metric("Mood", mood)

    st.write("---")
    st.subheader("Your Text Mirror")
    st.info(user_input[::-1])
    st.caption("Above is your text written backwards!")
