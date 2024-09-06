import requests
import streamlit as st
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/sdxl-turbo"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input("Enter your prompt here:"),
})


image = Image.open(io.BytesIO(image_bytes))

if st.button('Generate'):
	st.image(image)