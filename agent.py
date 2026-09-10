from groq_ai import ask_groq, ask_groq_json


# ---------- Analyze Student Task ----------
def analyze_task(question):

    prompt = f"""
Analyze this student's request.

Student request:
{question}

Return a simple plan with:

1. subject
2. topic
3. main_task
4. actions

Possible actions:
EXPLAIN
PRACTICE
QUIZ
SOLVE

Important:
- Identify the actual subject and topic.
- Do not invent a subject if it can be understood from the request.
- actions should contain only actions actually requested.
"""

    result = ask_groq_json(prompt)

    return result


# ---------- Practice Generator ----------
def generate_practice(subject, topic, count=5):

    prompt = f"""
Create {count} practice questions.

Subject: {subject}
Topic: {topic}

Rules:
- Questions only.
- Do NOT provide answers.
- Do NOT solve them.
- Questions should be student-friendly.
- Start easier and gradually become harder.

Return JSON exactly like this:

{{
    "questions": [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4",
        "Question 5"
    ]
}}
"""

    return ask_groq_json(prompt)


# ---------- Quiz Generator ----------
def generate_quiz(subject, topic, count=5):

    prompt = f"""
Create exactly {count} multiple-choice quiz questions.

Subject: {subject}
Topic: {topic}

Each question must have:
- question
- four options
- correct answer

IMPORTANT:
The correct answers are for the application to use internally.
They must NOT be displayed to the student before submission.

Return JSON exactly in this structure:

{{
    "questions": [
        {{
            "question": "Question text",
            "options": {{
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
            }},
            "answer": "A"
        }}
    ]
}}
"""

    return ask_groq_json(prompt)