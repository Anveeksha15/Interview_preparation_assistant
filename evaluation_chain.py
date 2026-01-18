from langchain.prompts import PromptTemplate
from config import llm

def get_evaluation_chain(qtype, memory):
    criteria = (
        "Structure, Clarity, Relevance, Impact"
        if qtype == "behavioral"
        else "Correctness, Clarity, Depth, Use of Examples"
    )
    prompt = PromptTemplate.from_file("prompts/evaluation_prompt.txt", input_variables=["question", "answer", "criteria"])
    return prompt | llm, criteria