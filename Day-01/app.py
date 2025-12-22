from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os



##Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that translant english to french"),
        ("user", "Translate the following text to french: {text}"),
    ]
)

##Streamlit App
st.title("English to French Translator")
input_text = st.text_input("Enter text in English:")
##llm 
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=os.getenv("GOOGLE_API")
    )

OutputParser=StrOutputParser()
chain= prompt | llm | OutputParser

if input_text:
    st.write(chain.invoke({"text": input_text}))