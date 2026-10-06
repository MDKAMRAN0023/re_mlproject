import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/"
    "v1beta/models/gemini-3.5-flash-lite:generateContent"
)


# =========================
# Project Context
# =========================

PROJECT_CONTEXT = """
You are the AI assistant for a Student Performance Prediction project.

Project name:
Student Performance AI

Project purpose:
This project predicts a student's exam performance using machine learning.

Dataset features:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Reading Score
- Writing Score

Target:
The model predicts the student's mathematics/exam performance score.

Machine Learning:
The project compares multiple regression algorithms, including:
- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

The best-performing model is saved as:
artifacts/model.pkl

The preprocessing pipeline is saved as:
artifacts/preprocessor.pkl

Current model performance:
R2 score is approximately 0.8794.

Backend:
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy

Deployment / engineering:
- Docker
- Docker Compose

AI Chatbot:
- Gemini API
- Flask /chat endpoint
- HTML/CSS/JavaScript frontend

The user is asking questions about this specific project.
Answer based on this project context whenever relevant.

If the user asks something unrelated to the project, you can still answer normally.

Keep explanations simple and beginner-friendly.
"""


def get_gemini_response(prompt):

    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY not found in .env file"
        )

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }

    full_prompt = PROJECT_CONTEXT + "\n\nUser question:\n" + prompt

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": full_prompt
                    }
                ]
            }
        ]
    }

    for attempt in range(3):

        response = requests.post(
            GEMINI_URL,
            headers=headers,
            json=data,
            timeout=30
        )

        if response.status_code == 200:

            result = response.json()

            return result["candidates"][0]["content"]["parts"][0]["text"]

        if response.status_code == 503:

            print(
                f"Gemini busy. Retry {attempt + 1}/3..."
            )

            if attempt < 2:
                time.sleep(2)

            continue

        print(
            "Gemini API Error:",
            response.status_code
        )

        print(response.text)

        return "Gemini API error occurred."

    return "Gemini is currently busy. Please try again later."

