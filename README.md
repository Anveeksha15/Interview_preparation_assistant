# 🎯 Interview Preparation AI

An interactive AI assistant built with **Streamlit** and **LangChain** to help users prepare for technical or behavioral job interviews. The app generates tailored questions, evaluates user responses, and suggests improved answers using advanced LLM-based chains.

## 🚀 Features

- 📌 Choose a job role and question type (technical or behavioral)
- 🤖 AI-generated interview questions based on your role
- 📝 Input your answers directly in the app
- ✅ Get real-time evaluation of your answers
- 💡 Receive AI-suggested better answers for continuous learning
- 🔁 Continue the interview with multiple rounds

## 🛠️ Tech Stack

- **Streamlit** – for building the interactive web UI
- **LangChain** – for chaining LLM-based question generation, evaluation, and answer improvement
- **LLMs** – used through LangChain chains for generating questions, evaluating responses, and suggesting improvements

## 📁 Project Structure

```
.
├── app.py                         # Main Streamlit app
├── chains/
│   ├── question_chain.py         # Question generation chain
│   ├── evaluation_chain.py       # Answer evaluation chain
│   └── better_answer_chain.py    # Improved answer suggestion chain
└── README.md                     # This file
```

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/interview-prep-ai.git
   cd interview-prep-ai
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## 🧠 Chains Overview

- **`get_question_chain()`** – Generates a role-specific interview question.
- **`get_evaluation_chain()`** – Evaluates the user's answer based on pre-defined criteria.
- **`get_better_answer_chain()`** – Suggests an improved version of the user's answer.

## 📌 Example Use Case

1. Enter "ML Intern" as the job role.
2. Select **Technical** questions.
3. Click **Start Interview**.
4. Respond to the AI-generated question.
5. View the evaluation and suggested better answer.
6. Proceed to the next question to continue your practice session.

## 🙌 Contributions

Feel free to submit issues or pull requests! Suggestions for new question types, evaluation criteria, or improvements to the chains are welcome.

## 📜 License

MIT License

