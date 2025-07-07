from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("student_score_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        hours = float(request.form["hours"])
        predicted = model.predict([[hours]])[0]
        prediction = max(0, min(100, predicted))
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
