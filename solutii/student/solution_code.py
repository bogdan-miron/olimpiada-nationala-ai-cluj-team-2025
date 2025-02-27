import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("dataset_train.csv")

# Define features and target variable
X = df[['distance_km', 'package_weight_kg', 'traffic_level']]
y = df['on_time']

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features for better model performance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Save predictions
results = pd.DataFrame(X_test, columns=['distance_km', 'package_weight_kg', 'traffic_level'])
results['actual'] = y_test.values
results['predicted'] = y_pred
#results.to_csv("dataset_train_solution.csv", index=False)

# Print model performance
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


#### Now respond
df_predict = pd.read_csv("dataset_predict.csv")
X_inp = df_predict[['distance_km', 'package_weight_kg', 'traffic_level']]
X_inp = scaler.transform(X_inp)

y_out = model.predict(X_inp)

df_predictions = pd.DataFrame(y_out, columns=["on_time"])
df_predictions.to_csv("dataset_solution.csv", index=False)


