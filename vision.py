from dotenv import load_dotenv
load_dotenv()  ## Loading all the enviornment variables
import streamlit as st 
import google.generativeai as genai 
import os
from PIL import Image



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## function to load GEmini Pro model

model=genai.GenerativeModel("gemini-pro-vision")

def get_response(prompt,image):
    if prompt!="":
        response=model.generate_content([prompt,image])
    else:
        response= model.generate_content(image)
    return response.text

st.title("Image Upload Example")

st.header("Gemini Application")
prompt=st.text_input("Input Prompt: ",key="prompt")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Classifying...")


submit=st.button("Generate Response")

if submit:
    response=get_response(prompt,image)
    st.subheader("The Response is :")
    st.write(response)

