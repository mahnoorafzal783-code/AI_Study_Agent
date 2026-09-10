import streamlit as st

from groq_ai import ask_groq, ask_groq_image
from agent import analyze_task, generate_practice, generate_quiz


st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🎓",
    layout="wide"
)


# ---------- Soft Pink Theme ----------
st.markdown("""
<style>

.stApp {
    background: #FFF5F8;
}

.block-container {
    max-width: 1100px;
    padding-top: 30px;
}

.hero {
    background: linear-gradient(135deg, #FCE4EC, #F3E5F5);
    padding: 35px;
    border-radius: 28px;
    text-align: center;
    border: 1px solid #F8DCE8;
    margin-bottom: 25px;
}

.hero h1 {
    color: #8E5A70;
    font-size: 44px;
}

.hero p {
    color: #7A6870;
    font-size: 17px;
}

.card {
    background: white;
    padding: 24px;
    border-radius: 22px;
    border: 1px solid #F1DDE5;
    box-shadow: 0 8px 25px rgba(142, 90, 112, 0.08);
    margin-bottom: 22px;
}

.card-title {
    color: #8E5A70;
    font-size: 21px;
    font-weight: 700;
}

div.stButton > button {
    width: 100%;
    border-radius: 15px;
    border: none;
    background: #D99AAF;
    color: white;
    font-size: 16px;
    font-weight: 700;
    padding: 11px;
}

div.stButton > button:hover {
    background: #C9829A;
    color: white;
}

section[data-testid="stSidebar"] {
    background: #FBEAF0;
}

</style>
""", unsafe_allow_html=True)


# ---------- Sidebar ----------
with st.sidebar:

    st.markdown("## 🎓 StudyMate AI")
    st.caption("Your Personal AI Study Agent")

    st.divider()

    st.markdown("### 📚 Subjects")

    st.write("📐 Mathematics")
    st.write("⚛️ Physics")
    st.write("🧪 Chemistry")
    st.write("🧬 Biology")
    st.write("📖 English")
    st.write("💻 Computer Science")

    st.divider()

    st.caption("🌸 Learn • Practice • Quiz")


# ---------- Hero ----------
st.markdown("""
<div class="hero">

<h1>🎓 StudyMate AI</h1>

<p>
Your intelligent personal study agent
</p>

</div>
""", unsafe_allow_html=True)


# ---------- Welcome ----------
st.markdown("""
<div class="card">

<div class="card-title">
👋 Hello, Student!
</div>

<p>
Tell StudyMate what you need. The agent will analyze your
request and perform only the learning actions that are relevant.
</p>

</div>
""", unsafe_allow_html=True)


# ---------- Image Upload ----------
st.markdown("""
<div class="card">

<div class="card-title">
📷 Upload a Study Question
</div>

<p>
Upload a textbook question, handwritten question, diagram,
or other study image.
</p>

</div>
""", unsafe_allow_html=True)


uploaded_image = st.file_uploader(
    "Upload image",
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed"
)


image_question = st.text_input(
    "What should StudyMate do with this image?",
    placeholder="Example: Explain this question step-by-step."
)


if uploaded_image:

    st.image(
        uploaded_image,
        caption="Uploaded study image",
        use_container_width=True
    )

    if st.button("🔍 Analyze Image"):

        image_bytes = uploaded_image.getvalue()

        with st.spinner("👁️ StudyMate AI is analyzing the image..."):

            image_answer = ask_groq_image(
                image_bytes,
                image_question
                if image_question.strip()
                else
                "Analyze this educational image and explain it clearly."
            )

        st.markdown("""
        <div class="card">

        <div class="card-title">
        🧠 Image Analysis
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown(image_answer)


# ---------- Question ----------
st.markdown("""
<div class="card">

<div class="card-title">
💬 What would you like to do today?
</div>

</div>
""", unsafe_allow_html=True)


question = st.text_area(
    "Question",
    placeholder=(
        "Example: Explain Newton's Second Law and give me "
        "5 practice questions."
    ),
    height=140,
    label_visibility="collapsed"
)


# =========================================================
# MAIN AGENT
# =========================================================

if st.button("✨ Ask StudyMate AI"):

    if not question.strip():

        st.warning("Please enter a question first.")

    else:

        # IMPORTANT:
        # Clear old quiz before processing a new request.
        st.session_state.pop("quiz_questions", None)
        st.session_state.pop("quiz_submitted", None)
        st.session_state.pop("quiz_results", None)

        # ---------- Analyze ----------
        with st.spinner("🧠 Agent is analyzing your request..."):

            plan = analyze_task(question)

        subject = plan.get(
            "subject",
            "General"
        )

        topic = plan.get(
            "topic",
            question
        )

        main_task = plan.get(
            "main_task",
            "Learn"
        )

        actions = plan.get(
            "actions",
            ["EXPLAIN"]
        )


        # Make sure actions is a list
        if isinstance(actions, str):

            actions = [actions]


        # Convert actions to uppercase
        actions = [
            str(action).upper().strip()
            for action in actions
        ]


        # ---------- Agent Decision ----------
        st.markdown("""
        <div class="card">

        <div class="card-title">
        🧠 Agent Decision
        </div>

        </div>
        """, unsafe_allow_html=True)


        st.write(f"*Subject:* {subject}")
        st.write(f"*Topic:* {topic}")
        st.write(f"*Main Task:* {main_task}")

        st.write(
            "*Actions:* "
            + " → ".join(actions)
        )


        # =================================================
        # EXPLANATION
        # =================================================

        if "EXPLAIN" in actions:

            st.markdown("""
            <div class="card">

            <div class="card-title">
            ✨ AI Explanation
            </div>

            </div>
            """, unsafe_allow_html=True)


            with st.spinner("✨ Preparing explanation..."):

                answer = ask_groq(
                    f"""
Explain the following topic clearly.

Subject: {subject}

Topic: {topic}

Student request:
{question}

Give only the explanation requested by the student.

Do not automatically add practice questions.

Do not automatically add a quiz.

Do not provide unrelated study material.
"""
                )


            st.markdown(answer)


        # =================================================
        # PRACTICE QUESTIONS
        # =================================================

        if "PRACTICE" in actions:

            st.markdown("""
            <div class="card">

            <div class="card-title">
            📝 Practice Questions
            </div>

            <p>
            Try these yourself first.
            Answers will not be shown unless you ask StudyMate
            to solve them.
            </p>

            </div>
            """, unsafe_allow_html=True)


            with st.spinner(
                "📝 Creating practice questions..."
            ):

                practice_data = generate_practice(
                    subject,
                    topic,
                    5
                )


            practice_questions = practice_data.get(
                "questions",
                []
            )


            if practice_questions:

                for i, q in enumerate(
                    practice_questions,
                    1
                ):

                    st.markdown(
                        f"*{i}. {q}*"
                    )


            else:

                st.warning(
                    "Practice questions could not be generated."
                )


        # =================================================
        # QUIZ
        # =================================================

        if "QUIZ" in actions:

            st.markdown("""
            <div class="card">

            <div class="card-title">
            🎯 Quick Quiz
            </div>

            <p>
            Choose your answers yourself.
            Correct answers stay hidden until you submit.
            </p>

            </div>
            """, unsafe_allow_html=True)


            with st.spinner(
                "🎯 Creating your quiz..."
            ):

                quiz_data = generate_quiz(
                    subject,
                    topic,
                    5
                )


            quiz_questions = quiz_data.get(
                "questions",
                []
            )


            if quiz_questions:

                # Save only the NEW quiz
                st.session_state["quiz_questions"] = (
                    quiz_questions
                )

                st.session_state["quiz_submitted"] = False

            else:

                st.warning(
                    "Quiz could not be generated."
                )


# =========================================================
# INTERACTIVE QUIZ
# =========================================================

if "quiz_questions" in st.session_state:

    quiz_questions = st.session_state[
        "quiz_questions"
    ]


    st.markdown("### 🎯 Answer the Quiz")


    user_answers = {}


    for i, item in enumerate(
        quiz_questions
    ):

        st.markdown(
            f"*Q{i + 1}. {item['question']}*"
        )


        options = item["options"]


        user_answers[i] = st.radio(
            f"Choose your answer for Question {i + 1}",
            list(options.keys()),

            format_func=lambda x, opts=options:
                f"{x}. {opts[x]}",

            key=f"quiz_answer_{i}"
        )


    if st.button("✅ Submit Quiz"):

        score = 0
        results = []


        for i, item in enumerate(
            quiz_questions
        ):

            correct = item["answer"]

            selected = user_answers[i]


            if selected == correct:

                score += 1

                results.append(
                    f"Q{i + 1}: ✅ Correct"
                )

            else:

                results.append(
                    f"Q{i + 1}: ❌ "
                    f"Your answer: {selected} | "
                    f"Correct answer: {correct}"
                )


        st.session_state["quiz_submitted"] = True

        st.session_state["quiz_results"] = results


        st.markdown("""
        <div class="card">

        <div class="card-title">
        🏆 Quiz Result
        </div>

        </div>
        """, unsafe_allow_html=True)


        st.success(
            f"Your Score: {score} / "
            f"{len(quiz_questions)}"
        )


        for result in results:

            st.write(result)


# ---------- Footer ----------
st.divider()

st.caption(
    "🎓 StudyMate AI • Analyze • Explain • Practice • Quiz • Learn"
)