from langchain_core.prompts import PromptTemplate
from config import llm

def get_question_chain():
    template = open("prompts/question_prompt.txt").read()
    prompt = PromptTemplate(template=template, input_variables=["role", "qtype"])
    return prompt | llm