import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

from solutii.student.solution_code import mean_traffic

# Load dataset_stats.csv
df_stats = pd.read_csv("dataset_stats.csv", dtype=float)
mean_traffic_level = df_stats["mean_traffic_level"].values[0]
std_traffic_level = df_stats["std_traffic_level"].values[0]

gt_stats = pd.read_csv("dataset_stats_ground_truth.csv", dtype=float)
mean_traffic_gt = gt_stats["mean_traffic_level"].values[0]
std_traffic_gt = gt_stats["std_traffic_level"].values[0]

p1_0 = (mean_traffic_gt == mean_traffic_level) * 20.0
p1_1 = (std_traffic_gt == std_traffic_level) * 20.0

p1_total = p1_0 + p1_1
# Check if the mean_traffic_level is correct

# Load predictions
df_sol = pd.read_csv("../solutii/student/dataset_solution.csv")
df_gt = pd.read_csv("./dataset_ground_truth.csv")

# Compute accuracy
accuracy = accuracy_score(df_sol["on_time"], df_gt["on_time"])
print(f"Model Accuracy: {accuracy:.3f}")

# Score accuracy with 0 if accuracy is less than 0.8 and with 60 if accuracy is higher than 0.978
# linear interpolation
p2 = min(max(60.0 * (accuracy - 0.8) / 0.178, 0), 60)


# Compute the final score
score = p1_total + p2
print(f"Score: {score:.2f} | P1: {p1_total:.2f}, P1_1:{p1_0}, P1_2: {p1_1} | P2: {p2:.2f}")