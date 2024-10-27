import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(temperature=0, api_key=GROQ_API_KEY, model_name="Llama3-70b-8192")
