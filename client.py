import requests
import streamlit as st

def get_response_gemini1(inputtext):
    response = requests.post(
        "http://localhost:3000/essay/invoke",
        json={"input": {"topic": inputtext}}
    )
    return response.json()

def get_response_gemini2(inputtext):
    response = requests.post(
        "http://localhost:3000/story/invoke",
        json={"input": {"topic": inputtext}}
    )
    return response.json()

st.title("Gemini Essay and Story Generator")

input_text = st.text_input("Enter a topic for essay")
input_text1 = st.text_input("Enter a topic for story")

if input_text:
    st.subheader("Essay Output")
    st.write(get_response_gemini1(input_text))

if input_text1:
    st.subheader("Story Output")
    st.write(get_response_gemini2(input_text1))
