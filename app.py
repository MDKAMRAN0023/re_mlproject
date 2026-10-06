from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Gemini
from src.chatbot import get_gemini_response

# Load .env
from dotenv import load_dotenv

load_dotenv()

application = Flask(__name__)

app = application


# =========================
# Home Page
# =========================
@app.route('/')
def index():
    return render_template('index.html')


# =========================
# Prediction Route
# =========================
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('home.html')

    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get(
                'parental_level_of_education'
            ),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get(
                'test_preparation_course'
            ),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        pred_df = data.get_data_as_data_frame()

        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()

        print("Mid Prediction")

        results = predict_pipeline.predict(pred_df)

        print("after Prediction")

        return render_template(
            'home.html',
            results=results[0]
        )


# =========================
# Gemini Chatbot
# =========================

@app.route('/chatbot')
def chatbot_page():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    if not user_message:
        return jsonify({
            "error": "Message is required"
        }), 400

    response = get_gemini_response(user_message)

    return jsonify({
        "response": response
    })


# =========================
# Run Flask
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0")