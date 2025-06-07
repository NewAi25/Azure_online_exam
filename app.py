import streamlit as st
import json
import random
import time

# Constants
TOTAL_QUESTIONS = 40
EXAM_DURATION_MINUTES = 120

# Load questions
@st.cache_data
def load_questions():
    with open("questions.json", "r") as f:
        data = json.load(f)
    return random.sample(data, TOTAL_QUESTIONS)

def init_session():
    if "questions" not in st.session_state:
        st.session_state.questions = load_questions()
        st.session_state.answers = [None] * TOTAL_QUESTIONS
        st.session_state.start_time = time.time()

def get_remaining_time():
    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, EXAM_DURATION_MINUTES * 60 - elapsed)
    return remaining

def show_timer():
    remaining = get_remaining_time()
    minutes = int(remaining // 60)
    seconds = int(remaining % 60)
    st.info(f"⏳ Time Remaining: {minutes:02d}:{seconds:02d}")

    if remaining <= 0:
        st.warning("⏰ Time's up! Submitting your test...")
        st.session_state.auto_submit = True

def display_question(q, idx):
    st.markdown(f"**Q{idx+1}. {q['question']}**")
    st.radio(
        "Select one:",
        q["options"],
        index=st.session_state.answers[idx] if st.session_state.answers[idx] is not None else -1,
        key=f"q_{idx}",
        on_change=lambda i=idx: update_answer(i)
    )
    st.markdown("---")

def update_answer(idx):
    selected = st.session_state.get(f"q_{idx}")
    question = st.session_state.questions[idx]
    if selected in question["options"]:
        st.session_state.answers[idx] = question["options"].index(selected)

def calculate_score():
    score = 0
    for i, ans_idx in enumerate(st.session_state.answers):
        if ans_idx is not None and st.session_state.questions[i]["options"][ans_idx] == st.session_state.questions[i]["answer"]:
            score += 1
    return score

def main():
    st.set_page_config("Azure AZ-104 Mock Test", layout="wide")
    st.title("🧠 Azure AZ-104 Mock Test")
    st.caption("Simulates the real CBT experience for AZ-104 (Microsoft Certified: Azure Administrator Associate)")

    init_session()
    show_timer()

    with st.form("mock_exam"):
        for idx, question in enumerate(st.session_state.questions):
            display_question(question, idx)

        submitted = st.form_submit_button("Submit Exam")
        if submitted or st.session_state.get("auto_submit"):
            score = calculate_score()
            st.success(f"✅ You scored {score} out of {TOTAL_QUESTIONS}")
            with st.expander("Review Your Answers"):
                for i, q in enumerate(st.session_state.questions):
                    your_ans = q["options"][st.session_state.answers[i]] if st.session_state.answers[i] is not None else "Not Answered"
                    st.markdown(f"**Q{i+1}: {q['question']}**")
                    st.markdown(f"- ✅ Correct: **{q['answer']}**")
                    st.markdown(f"- 🧾 Your Answer: {your_ans}")
                    st.markdown("---")

if __name__ == "__main__":
    main()
