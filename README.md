# Student Performance AI

An end-to-end Machine Learning project that predicts a student's mathematics performance based on demographic, academic, and preparation-related features.

The project also includes an **AI-powered Gemini chatbot**, a **Flask web application**, **Docker containerization**, and **Docker Compose** support.

---

## 🚀 Project Overview

The **Student Performance AI** application predicts a student's mathematics score using Machine Learning.

The prediction is based on:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The project follows an end-to-end Machine Learning workflow:

**Data → Preprocessing → Model Training → Model Evaluation → Prediction → Flask API/Web App → Docker → AI Chatbot**

---

## 🤖 Machine Learning

Multiple regression algorithms were evaluated:

- Random Forest Regressor
- Decision Tree Regressor
- Gradient Boosting Regressor
- Linear Regression
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

The best-performing model is saved in:

```text
artifacts/model.pkl
```

The preprocessing pipeline is saved in:

```text
artifacts/preprocessor.pkl
```

### Model Performance

Current R² Score:

```text
0.8794
```

---

## 🧠 AI Chatbot

The project includes a Gemini-powered chatbot that can answer questions about the Student Performance AI project.

### Chatbot Features

- Gemini API integration
- Project-aware responses
- Flask `/chat` API endpoint
- Dedicated chatbot web interface
- Markdown response rendering
- Typing indicator
- Enter-key support
- Error handling

The Gemini API key is loaded securely from the `.env` file.

---

## 🌐 Web Application

The application provides:

### Prediction Page

Users can enter student information and receive a predicted mathematics score.

### AI Assistant

Users can ask questions about:

- Machine Learning
- The project architecture
- Dataset features
- Models
- Prediction process
- Flask
- Docker
- Project implementation

---

## 🛠️ Technology Stack

### Programming

- Python 3.8

### Machine Learning

- Scikit-learn
- XGBoost
- CatBoost
- Pandas
- NumPy

### Backend

- Flask

### Generative AI

- Google Gemini API
- Python Requests

### Frontend

- HTML
- CSS
- JavaScript

### Deployment & DevOps

- Docker
- Docker Compose
- Git
- GitHub

---

## 📁 Project Structure

```text
re__mlproject/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   └── test.csv
│
├── data/
│   └── stud.csv
│
├── notebook/
│   └── *.ipynb
│
├── src/
│   ├── components/
│   ├── pipeline/
│   └── chatbot.py
│
├── templates/
│   ├── index.html
│   ├── home.html
│   └── chatbot.html
│
├── logs/
│
├── app.py
├── requirements.txt
├── setup.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/MDKAMRAN0023/re_mlproject.git
```

### 2. Navigate to the project

```bash
cd re_mlproject
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

**Never commit your `.env` file or API key to GitHub.**

The project already includes `.env` in `.gitignore`.

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

### Prediction Page

```text
http://localhost:5000/predictdata
```

### AI Chatbot

```text
http://localhost:5000/chatbot
```

---

## 🐳 Run with Docker

Build and start the application:

```bash
docker compose up -d --build
```

Check running containers:

```bash
docker compose ps
```

Open:

```text
http://localhost:5000
```

Stop the application:

```bash
docker compose down
```

---

## 🔌 API Endpoint

### Chatbot API

**POST**

```text
/chat
```

Example request:

```json
{
  "message": "What is machine learning?"
}
```

Example response:

```json
{
  "response": "Machine learning is a method of teaching computers to learn patterns from data..."
}
```

---

## 📊 Machine Learning Pipeline

```text
Dataset
   ↓
Data Ingestion
   ↓
Data Transformation
   ↓
Feature Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
model.pkl
   ↓
Flask Prediction Application
```

---

## 🤖 AI Chatbot Architecture

```text
User
 ↓
Chatbot UI
 ↓
Flask /chat Endpoint
 ↓
Gemini API
 ↓
Project Context + User Question
 ↓
AI Response
 ↓
Chatbot UI
```

---

## 🐳 Docker Architecture

```text
User
 ↓
Browser
 ↓
Docker Container
 ↓
Flask Application
 ├── ML Prediction Pipeline
 └── Gemini Chatbot
```

---

## 🔒 Security

Sensitive configuration is stored using environment variables.

The following files are excluded from Git:

```text
.env
venv/
__pycache__/
logs/
catboost_info/
.vscode/
```

---

## 📌 Future Improvements

- Deploy the application to a cloud platform
- Add CI/CD pipeline
- Add automated testing
- Add model monitoring
- Add experiment tracking
- Improve chatbot memory
- Add authentication
- Add prediction history
- Add model performance dashboard

---

## 👨‍💻 Author

**MD Kamran Ahmad**

GitHub:

https://github.com/MDKAMRAN0023

---

## ⭐ Project Highlights

- End-to-end Machine Learning pipeline
- Multiple regression algorithms
- Model selection and hyperparameter tuning
- Flask web application
- Gemini AI chatbot
- Dockerized application
- Docker Compose support
- Git/GitHub version control
- Environment-based API key management