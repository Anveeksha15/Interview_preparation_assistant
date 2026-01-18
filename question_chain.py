from langchain.prompts import PromptTemplate
from config import llm

def get_question_chain():
    prompt = PromptTemplate.from_file("prompts/question_prompt.txt", input_variables=["role", "qtype"])
    return prompt | llm
