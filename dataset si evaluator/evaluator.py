import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# Load predictions
df_sol = pd.read_csv("../solutii/student/dataset_solution.csv")
df_gt = pd.read_csv("./dataset_ground_truth.csv")

# Compute accuracy
accuracy = accuracy_score(df_sol["on_time"], df_gt["on_time"])
print(f"Model Accuracy: {accuracy:.3f}")

# Print detailed classification report
print("Classification Report:\n", classification_report(df_sol["on_time"], df_gt["on_time"]))

# Evaluation Criteria
if accuracy > 0.8:
    print("Great model! The predictions are highly accurate.")
elif accuracy > 0.6:
    print("Decent model, but could be improved with more data.")
else:
    print("Poor model. Consider adding more features or tuning hyperparameters.")