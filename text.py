from dotenv import load_dotenv
load_dotenv()  ## Loading all the enviornment variables
import streamlit as st 
import google.generativeai as genai 
import os


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## function to load GEmini Pro model

model=genai.GenerativeModel("gemini-pro")
def get_response(question):
    response= model.generate_content(question)
    return response.text

## initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input= st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

## When submit is clicked

if submit:
    response=get_response(input)
    st.subheader("The Response is :")
    st.write(response)

