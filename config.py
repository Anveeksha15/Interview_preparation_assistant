import os
from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
from langchain_groq import ChatGroq
llm=ChatGroq(model="gemma2-9b-it",temperature=0.7)