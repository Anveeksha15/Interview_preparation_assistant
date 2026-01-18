import streamlit as st
from langchain.memory import ConversationBufferMemory
from chains.question_chain import get_question_chain
from chains.evaluation_chain import get_evaluation_chain
from chains.better_answer_chain import get_better_answer_chain

st.set_page_config(page_title="Interview Prep AI", layout="centered")
st.title("Interview Preparation Assistant")

with st.sidebar:
    st.header("Interview Settings")
    role = st.text_input("Job Role", value="ML Intern")
    qtype = st.selectbox("Question Type", ["technical", "behavioral"])
    start_interview = st.button("Start Interview")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()
    st.session_state.question_num = 1
    st.session_state.history = []
    st.session_state.asked = False
    st.session_state.continue_interview = False

question_chain = get_question_chain()
evaluation_chain, criteria = get_evaluation_chain(qtype, st.session_state.memory)
better_chain = get_better_answer_chain(st.session_state.memory)

if start_interview or st.session_state.asked or st.session_state.continue_interview:
    if not st.session_state.asked:
        question = question_chain.invoke({"role": role, "qtype": qtype})
        st.session_state.question_text = question.content if hasattr(question, "content") else str(question)
        st.session_state.asked = True
        st.session_state.continue_interview = False 

    st.subheader(f"Question {st.session_state.question_num}")
    st.markdown(f"> **Q:** {st.session_state.question_text}")


    answer_key = f"answer_input_{st.session_state.question_num}"
    answer = st.text_area("Your Answer", key=answer_key)

    col1, col2 = st.columns([1, 1])
    with col1:
        submit = st.button("Submit Answer")
    with col2:
        next_question = st.button("Next Question")

    if submit and answer:
       
        st.session_state.memory.save_context(
            {"input": st.session_state.question_text},
            {"output": answer}
        )

    
        evaluation = evaluation_chain.invoke({
            "question": st.session_state.question_text,
            "answer": answer,
            "criteria": criteria
        })
        evaluation_text = evaluation.content if hasattr(evaluation, "content") else str(evaluation)

        better = better_chain.invoke({"question": st.session_state.question_text})
        better_text = better.content if hasattr(better, "content") else str(better)

        
        st.subheader("Evaluation")
        st.write(evaluation_text)

        st.subheader("Suggested Better Answer")
        st.write(better_text)

   
    if (submit and answer) or next_question:
        st.session_state.question_num += 1
        st.session_state.asked = False
        st.session_state.continue_interview = True  
