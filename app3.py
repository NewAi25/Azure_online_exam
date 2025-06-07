
import streamlit as st
import json
import random
import time

# Constants
TOTAL_QUESTIONS = 40
EXAM_DURATION_MINUTES = 120

@st.cache_data
def load_questions():
    with open("questions.json", "r") as f:
        data = json.load(f)
    available = len(data)
    num_to_sample = min(TOTAL_QUESTIONS, available)
    return random.sample(data, num_to_sample)

def init_session():
    if "questions" not in st.session_state:
        st.session_state.questions = load_questions()
        st.session_state.answers = [None] * len(st.session_state.questions)
        st.session_state.start_time = time.time()
        st.session_state.auto_submit = False

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
    selected_option = st.radio(
        label="Select one:",
        options=q["options"],
        key=f"q_{idx}"
    )
    st.markdown("---")

def calculate_score():
    score = 0
    for i, ans_idx in enumerate(st.session_state.answers):
        correct = st.session_state.questions[i]["answer"]
        chosen = st.session_state.questions[i]["options"][ans_idx] if ans_idx is not None else None
        if chosen == correct:
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
        if submitted or st.session_state.auto_submit:
            for i in range(len(st.session_state.questions)):
                selected = st.session_state.get(f"q_{i}")
                if selected in st.session_state.questions[i]["options"]:
                    st.session_state.answers[i] = st.session_state.questions[i]["options"].index(selected)

            score = calculate_score()
            st.success(f"✅ You scored {score} out of {len(st.session_state.questions)}")
            with st.expander("📘 Review Your Answers"):
                for i, q in enumerate(st.session_state.questions):
                    your_ans = q["options"][st.session_state.answers[i]] if st.session_state.answers[i] is not None else "Not Answered"
                    st.markdown(f"**Q{i+1}: {q['question']}**")
                    st.markdown(f"- ✅ Correct: **{q['answer']}**")
                    st.markdown(f"- 🧾 Your Answer: {your_ans}")
                    st.markdown("---")

if __name__ == "__main__":
    main()
