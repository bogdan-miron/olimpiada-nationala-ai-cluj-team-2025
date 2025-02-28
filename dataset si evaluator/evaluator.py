import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

from solutii.student.solution_code import mean_traffic


# Load predictions
df_sol = pd.read_csv("../solutii/student/dataset_solution.csv")
df_gt = pd.read_csv("./dataset_ground_truth.csv")
df_sol.set_index("id", inplace=True)
df_gt.set_index("id", inplace=True)


### Compute the score for P1 and P2
#################
mean_traffic_gt = df_gt["mean_traffic_level"].values[0]
std_traffic_gt = df_gt["std_traffic_level"].values[0]

mean_traffic_level = df_sol["mean_traffic_level"].values[0]
std_traffic_level = df_sol["std_traffic_level"].values[0]


p1 = (mean_traffic_gt == mean_traffic_level) * 20.0
p2 = (std_traffic_gt == std_traffic_level) * 20.0

# P3: Compute accuracy
# ==========
# Select only the common ids present in both DataFrames
common_ids = df_gt.index.intersection(df_sol.index)

# Compare the 'result' column from both DataFrames
# This comparison uses index alignment and compares only rows with the same id
comparison = df_gt.loc[common_ids, "on_time"] == df_sol.loc[common_ids, "on_time"]

# Calculate overall accuracy (percentage of matching rows)
accuracy = comparison.mean()
print(f"Overall Accuracy: {accuracy:.2f}")

# Score accuracy with 0 if accuracy is less than 0.8 and with 60 if accuracy is higher than 0.978
# linear interpolation
p3 = min(max(60.0 * (accuracy - 0.8) / 0.178, 0), 60)


# Compute the final score
score = p1 + p2 + p3
print(f"Score: {score:.2f} | P1: {p1}, P2:{p2}, P3: {p3}")

# Optionally, you can see the rows that do not match:
mismatches = df_gt.loc[common_ids][comparison == False]
print("Rows with mismatches:")
print(mismatches)
