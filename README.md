# 🎓 AI-Powered Student Performance Prediction Dashboard

An end-to-end Machine Learning project that predicts student academic performance using study habits, attendance, failures, and behavioral factors.  
Built with Python, Scikit-learn, Streamlit, Plotly, and ML Pipelines.

---

# 🚀 Live Features

✅ Student Performance Prediction  
✅ Interactive AI Dashboard  
✅ Machine Learning Pipeline  
✅ Real-time Predictions  
✅ Data Preprocessing Pipeline  
✅ Automated Model Selection  
✅ Risk Analysis System  
✅ AI Recommendation Engine  
✅ Interactive Charts & Analytics  
✅ Production-Style Modular Architecture  

---

# 📸 Project Preview

## Dashboard Overview

(Add your dashboard screenshot here)

```bash
assets/dashboard.png
```

---

# 🧠 Problem Statement

Educational institutions often struggle to identify students who are academically at risk.

This project uses Machine Learning algorithms to analyze:
- Study time
- Attendance
- Past failures
- Internet access
- Student behavior patterns

and predicts the final academic grade of a student.

The system also provides:
- Performance analysis
- Academic risk detection
- AI-generated recommendations

---

# 🛠️ Tech Stack

## Programming Language
- Python

## Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Pickle

## Machine Learning
- Random Forest Regressor
- Gradient Boosting Regressor
- Decision Tree Regressor
- Linear Regression

## Data Visualization
- Plotly
- Streamlit Charts

---

# 📂 Project Structure

```bash
student-performance-predictor/
│
├── app/
│   └── app.py
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── config/
│   └── config.yaml
│
├── data/
│   └── student-mat.csv
│
├── notebooks/
│   └── student_prediction.ipynb
│
├── src/
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   └── utils/
│       ├── helpers.py
│       ├── logger.py
│       └── exception.py
│
├── logs/
├── setup.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset Information

Dataset Used:
- UCI Student Performance Dataset

Features Used:
- Age
- Study Time
- Past Failures
- Absences
- Gender
- Internet Access

Target Variable:
- Final Grade (G3)

---

# ⚙️ Machine Learning Workflow

## 1️⃣ Data Ingestion
- Load dataset
- Split into train/test data

## 2️⃣ Data Transformation
- Feature selection
- Scaling numerical features
- Encoding categorical features

## 3️⃣ Model Training
Multiple models trained:
- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting

## 4️⃣ Model Evaluation
Evaluation Metrics:
- R² Score
- MAE
- MSE
- RMSE

## 5️⃣ Prediction Pipeline
- Loads saved model
- Transforms input data
- Predicts student performance

## 6️⃣ Streamlit Dashboard
Interactive dashboard for:
- Student input
- Predictions
- Analytics
- Recommendations

---

# 📈 Dashboard Features

## 🎯 Prediction System
Predicts final student grade in real time.

## 📊 Analytics Dashboard
Interactive charts and academic analytics.

## ⚠️ Risk Detection
Detects students at academic risk.

## 💡 AI Recommendations
Provides personalized study recommendations.

## 📉 Performance Contribution Analysis
Visualizes impact of:
- Study Time
- Absences
- Failures

---

# 🖥️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/hitheesha10/student-performance-predictor.git
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate Virtual Environment

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Training Pipeline

```bash
python src/pipeline/training_pipeline.py
```

---

# ▶️ Run Streamlit App

```bash
streamlit run app/app.py
```

---

# 📊 Model Performance

| Model | Performance |
|------|------|
| Linear Regression | Good |
| Decision Tree | Better |
| Random Forest | Best |
| Gradient Boosting | Competitive |

---

# 🔥 Resume Highlights

This project demonstrates:

✅ End-to-End Machine Learning Workflow  
✅ Production-Level Project Structure  
✅ Machine Learning Pipelines  
✅ Feature Engineering  
✅ Data Preprocessing  
✅ Interactive Dashboard Development  
✅ Real-time Prediction Systems  
✅ Data Visualization Skills  
✅ Software Engineering Practices  
✅ Deployment-Ready Architecture  

---

# 🚀 Future Improvements

- User Authentication
- Cloud Deployment
- Student Report PDF Export
- Database Integration
- Historical Prediction Tracking
- Deep Learning Integration
- Mobile Responsive Dashboard
- Multi-student Analytics

---
