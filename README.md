# ML Score Predictor

This is one of my very first machine learning projects.

This simple app predicts a student’s score based on how many hours they studied — built using Linear Regression as part of my ML learning journey. It’s a small but meaningful step toward understanding how machine learning works in real life.

---

## Topics Covered

This project helped me learn and apply the following concepts:

- Linear Regression (Supervised Learning)
- Model training and testing
- Data preprocessing using pandas
- Train-test split using `train_test_split()`
- Visualizing data with Matplotlib
- Calculating evaluation metrics:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R² Score
- Saving and loading models with `joblib`
- Making predictions with custom input
- Building a basic web interface using Flask and HTML

---

## What This Project Does

- Takes input like: “I studied for 7.3 hours”
- Predicts a score based on that input
- Shows how even a small dataset can teach us a lot about model training
- Visualizes the prediction with a clean graph

Built using:
- Python
- scikit-learn
- Flask (for the web version)
- Matplotlib

---

## Why I Built This

I wanted to learn:
- How ML models work from scratch
- How to train, test, and save a model
- How to connect ML with a simple web app
- And mostly, to build something fun and functional while learning

---

## Dataset Used

A tiny dataset (just 7 samples) of study hours and their corresponding scores:

```python
Hours:  [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2]
Scores: [21, 47, 27, 75, 30, 20, 88]


## How to Run Locally

### 1. Clone the Repository

git clone https://github.com/your-username/ml-score-predictor.git
cd ml-score-predictor

### 2.Create a Virtual Environment

python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On Mac/Linux

### 3.Install Dependencies:
pip install -r requirements.txt
### 4.Run the ML Script:
python student_scores.py
### 5.Run the Web App
python app.py


# Project Structure
ml-score-predictor/
├── student_scores.py          # Main ML script
├── student_score_model.pkl    # Saved trained model
├── app.py                     # Flask app to interact via browser
├── templates/
│   └── index.html             # Simple frontend form
├── requirements.txt           # List of required libraries
└── README.md


