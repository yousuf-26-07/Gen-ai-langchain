from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translates English to French"),
        ("user", "Translate the following text to French: {text}"),
    ]
)

st.title("English to French Translator")
input_text = st.text_input("Enter text in English:")

@st.cache_resource
def load_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

llm = load_llm()
parser = StrOutputParser()
chain = prompt | llm | parser

if input_text:
    st.write(chain.invoke({"text": input_text}))
