# from dotenv import load_dotenv
# load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image


import google.generativeai as genai

st.set_page_config(page_title="Geminipro", page_icon="🔮")
gemini_api_key = st.sidebar.text_input('Enter Gemini API Key', type='password')
st.sidebar.markdown("Create your Gemini API Key [here](https://aistudio.google.com/app/apikey)")
genai.configure(api_key=gemini_api_key)

# Function to load OpenAI model and get respones
def get_gemini_response(input,image):
    if not gemini_api_key.startswith('AI'):
        st.warning('Please enter a valid Gemini API key')
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

#initialize our streamlit app
st.title("Gemini Pro Vision")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Upload an image..", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
