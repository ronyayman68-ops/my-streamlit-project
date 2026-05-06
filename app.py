import streamlit as st

# Sets a clean title in the browser tab
st.set_page_config(page_title="Rawan Streamlit", layout="centered")

st.title("Rawan's Streamlit App")

# A simple, clean input box
user_input = st.text_input("Enter your text below:", placeholder="Type here...")

if user_input:
    # Use columns to keep the output small and side-by-side
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Words", len(user_input.split()))
    
    with col2:
        st.metric("Characters", len(user_input))
        
    # Displays the final result in a subtle box
    st.info(f"**Processed Output:** {user_input}") 