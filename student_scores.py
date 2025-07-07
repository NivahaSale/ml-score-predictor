import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np  
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Sample data
data = {
    'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2],
    'Scores': [21, 47, 27, 75, 30, 20, 88]
}
# Create a DataFrame
df = pd.DataFrame(data)

# Step 3: Split into inputs (X) and outputs (y)
X = df[['Hours']]   # Features (2D)
y = df['Scores']    # Labels (1D)

# Step 4: Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

#  Save the model to a file
joblib.dump(model, "student_score_model.pkl")
print("Model saved as student_score_model.pkl")


# Step 6: Predict
predictions = model.predict(X_test)

# Step 7: Show results
print("Test Input (Hours):")
print(X_test)
print("\nActual Scores:", y_test.tolist())
print("Predicted Scores:", predictions.tolist())



print("Slope (m):", model.coef_)
print("Intercept (b):", model.intercept_)


#  Custom prediction point
custom_hours = [[10]]
predicted_score = model.predict(custom_hours)


# Plotting
plt.scatter(X, y, color='blue', label='Actual Scores')
regression_line = model.predict(X)
plt.plot(X, regression_line, color='red', label='Prediction Line')
plt.scatter(custom_hours, predicted_score, color='green', s=100, label=f'Prediction for {custom_hours[0][0]} hrs')

plt.title('Hours Studied vs Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.legend()
plt.show()

print(f"\n If a student studies for {custom_hours[0][0]} hours, they might score: {predicted_score[0]:.2f} marks")

# Accuracy Metrics
print("\nModel Formula:")
print(f"Slope (m): {model.coef_[0]:.2f}")
print(f"Intercept (b): {model.intercept_:.2f}")

print("\n📊 Model Accuracy Report:")
print("Mean Absolute Error (MAE):", mean_absolute_error(y_test, predictions))
print("Mean Squared Error (MSE):", mean_squared_error(y_test, predictions))


rmse = np.sqrt(mean_squared_error(y_test, predictions))
print("Root Mean Squared Error (RMSE):", rmse)

print("R² Score:", r2_score(y_test, predictions))
