# Importing libraries
import streamlit as st
from prompt_engine import run_prompt

#creating streamlit page
st.set_page_config(page_title="Prompt Engineering APP", layout="centered")
st.title("Prompt Engineering App")

# prompt types Dropdown
prompt_types = [
    "Zero-Shot",
    "Few-shot",
    "Instruction - Based",
    "Chain-of-Thought",
    "Role-based"
]

selected_prompt = st.selectbox("Select Prompt Type", prompt_types)
user_input = st.text_area("Enter your input here", height=150)

if st.button("Generate Response"):
    with st.spinner("Generating content......."):
        output = run_prompt(selected_prompt, user_input)   
        st.markdown("Response:")
        st.code(output)