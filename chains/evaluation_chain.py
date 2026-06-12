from langchain_core.prompts import PromptTemplate
from config import llm

def get_evaluation_chain(qtype):
    criteria = (
        "Structure, Clarity, Relevance, Impact"
        if qtype == "behavioral"
        else "Correctness, Clarity, Depth, Use of Examples"
    )
    template = open("prompts/evaluation_prompt.txt").read()
    prompt = PromptTemplate(template=template, input_variables=["question", "answer", "criteria", "history"])
    return prompt | llm, criteria