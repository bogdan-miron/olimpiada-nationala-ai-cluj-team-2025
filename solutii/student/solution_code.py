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
# The id should to be used for standardization or training
# because it is a unique identifier and does not provide useful information
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print model performance
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


#### Now respond
df_predict = pd.read_csv("dataset_predict.csv")
X_inp = df_predict[['id', 'distance_km', 'package_weight_kg', 'traffic_level']]

# Get the mean and standard deviation of the traffic_level in the X_inp, using 2 decimal places
mean_traffic = round(X_inp['traffic_level'].mean(), 2)
std_traffic = round(X_inp['traffic_level'].std(), 2)

# Store ids and apply standardization
ids = X_inp['id']
X_inp = X_inp.drop(columns=['id'])
X_inp = scaler.transform(X_inp)
y_out = model.predict(X_inp)

# Create a dataframe with: id, mean_traffic_level, std_traffic_level, on_time
df_predictions = pd.DataFrame({
    "id": ids,
    # Must have the same number: the mean of traffic_level column in X_inp
    "mean_traffic_level": mean_traffic,
    "std_traffic_level": std_traffic,
    "on_time": y_out
})

df_predictions.to_csv("dataset_solution.csv", index=False)




