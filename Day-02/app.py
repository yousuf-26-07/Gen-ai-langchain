
import os
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn

from dotenv import load_dotenv
load_dotenv()
OutputParser = StrOutputParser()

app = FastAPI(
    title="Langchain with Google Gemini API",
    description="An example FastAPI application using Langchain with Google Gemini API",
    version="1.0.0"
)

model1 = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
model2 = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

prompt1 = ChatPromptTemplate.from_template(
    "give me a essay on the topic {topic} for 350 word"
)

prompt2 = ChatPromptTemplate.from_template(
    "give me a story from history on the topic {topic} for 350 word"
)
add_routes(
    app,
    prompt1 | model1 | OutputParser,
    path = "/essay"
)

add_routes(
    app,
    prompt2 | model2 |OutputParser,
    path = "/story"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=3000)

