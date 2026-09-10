import os
import base64
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)


# ---------- Normal Text AI ----------
def ask_groq(question):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are StudyMate AI, a friendly personal study agent. "
                    "Help students with any academic subject. "
                    "Explain concepts clearly and simply. "
                    "Do not automatically solve practice questions or quizzes "
                    "unless the student explicitly asks for the solution."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.3,
        max_completion_tokens=1000
    )

    return response.choices[0].message.content


# ---------- JSON AI ----------
def ask_groq_json(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are StudyMate AI. "
                    "Return only valid JSON. "
                    "Follow the requested JSON structure exactly."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_completion_tokens=1500,
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)


# ---------- Image AI ----------
def ask_groq_image(image_bytes, question):
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are StudyMate AI, a friendly study agent. "
                    "Analyze educational images, diagrams, handwritten questions "
                    "and textbook questions carefully. "
                    "Explain the answer clearly for a student."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": question
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        temperature=0.2,
        max_completion_tokens=1200
    )

    return response.choices[0].message.content