import joblib

# 🧠 Load the trained model
model = joblib.load("student_score_model.pkl")

# 🤔 Take custom input
hours = float(input("Enter study hours: "))
predicted_score = model.predict([[hours]])

print(f"📘 Predicted Score for {hours} hours: {predicted_score[0]:.2f}")
