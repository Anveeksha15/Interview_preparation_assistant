from langchain.prompts import PromptTemplate
from config import llm

def get_better_answer_chain(memory):
    prompt = PromptTemplate.from_file("prompts/better_answer_prompt.txt", input_variables=["question"])
    return prompt | llm