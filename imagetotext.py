import requests
import streamlit as st
import base64

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("bg.png")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Welcome to the Image-to-Text Bot")

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

# Function to make API request
def query(image_data):
    response = requests.post(API_URL, headers=headers, data=image_data)
    return response.json()

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    if st.button("Convert"):
        # Read the uploaded image file
        image_bytes = uploaded_file.read()

        # Call the query function to get the response
        result = query(image_bytes)

        # Display the result
        if "error" in result:
            st.error("Error: " + result["error"])
        else:
            caption = result[0]["generated_text"]
            st.success(f"Caption: {caption}")

# output=(query)

# output = query("/content/image.jpeg")