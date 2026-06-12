from langchain_core.prompts import PromptTemplate
from config import llm

def get_better_answer_chain():
    template = open("prompts/better_answer_prompt.txt").read()
    prompt = PromptTemplate(template=template, input_variables=["question", "history"])
    return prompt | llm