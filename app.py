import streamlit as st
import google.generativeai as genai



st.title("Welcome to Gemini Chat Bot")

genai.configure(api_key="AIzaSyDKp_qIiCPkasqqqywfhfCZyTWzEnwkzrU")

text=st.text_input("Enter Your Prompt:")

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
