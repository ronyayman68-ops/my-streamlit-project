import streamlit as st
st.set_page_config(page_title="Rawan's Text Lab", layout="centered")

st.title("✨ Simple Text Analyzer")

# User Input
user_input = st.text_input(
    "Enter a sentence:", placeholder="How are you feeling today?"
)

if user_input:
    # 1. Logic
    words = len(user_input.split())
    chars = len(user_input)
    
    positive_words = ["good", "happy", "great", "amazing", "love", "best"]
    negative_words = ["bad", "sad", "angry", "hate", "worst", "fail", "terrible", "awful"]

    # Sentiment Logic
    if any(word in user_input.lower() for word in positive_words):
        mood = "Positive 😊"
        st_mood = st.success
    elif any(word in user_input.lower() for word in negative_words):
        mood = "Negative 😔"
        st_mood = st.error
    else:
        mood = "Neutral 😐"
        st_mood = st.info

    # 2. Metrics Dashboard
    col1, col2, col3 = st.columns(3)
    col1.metric("Words", words)
    col2.metric("Characters", chars)
    col3.metric("Mood", mood)

    # 3. New Feature: Search and Replace
    st.write("---")
    st.subheader("🔍 Search & Replace")
    search_word = st.text_input("Find what word?")
    replace_word = st.text_input("Replace with?")
    
    if search_word and replace_word:
        new_text = user_input.replace(search_word, replace_word)
        st.write("**Updated Text:**")
        st.code(new_text)

    # 4. The Mirror
    st.write("---")
    st.subheader("🔁 Your Text Mirror")
    st_mood(user_input[::-1])
    st.caption("Above is your text written backwards!")