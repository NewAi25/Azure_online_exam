
# 🧠 Azure AZ-104 Mock Test App

This is a **Streamlit-based mock test platform** that simulates the real CBT (Computer-Based Test) experience for the **Microsoft Certified: Azure Administrator Associate (AZ-104)** exam.

---

## 🚀 Features

- ⏳ Real-time countdown timer (120 minutes)
- ✅ 40 randomly selected multiple-choice questions
- 📘 Review your answers with correct explanations after submission
- 🧠 Clean and user-friendly exam interface
- 💾 Caches question data for performance using `@st.cache_data`

---

## 📁 Project Structure

```
📦 Azure_online_exam/
├── app3.py                # Main Streamlit application
├── questions.json        # Question bank (editable)
└── README.md             # This file
```

---

## 🛠️ How to Run

1. **Clone the repository or download the files**

2. **Install required packages**

```bash
pip install streamlit
```

3. **Run the application**

```bash
streamlit run app.py
```

---

## 🧪 Sample Question Format (JSON)

Each question object in `questions.json` looks like this:

```json
{
  "question": "What does Azure service 25 provide?",
  "options": [
    "Option A - Resource provisioning",
    "Option B - Billing analysis",
    "Option C - Cost optimization",
    "Option D - Monitoring and alerting"
  ],
  "answer": "Option A - Resource provisioning"
}
```

---

## 📌 Customization Ideas

- Add difficulty levels or topic tags (e.g., Networking, Identity)
- Save user scores with timestamps
- Add user login for personalized history
- Add explanations for correct answers

---

## 📄 License

MIT License. Feel free to modify and use!

---

## ✍️ Author

Made with 💙 using Streamlit by [Manisha]
