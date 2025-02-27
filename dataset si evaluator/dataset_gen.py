import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Total number of samples
num_samples = 150
num_samples_train = 100
num_samples_test = num_samples - num_samples_train

# 70% on_time = 1, 30% on_time = 0
num_on_time = int(num_samples * 0.5)   # 105 samples with on_time = 1
num_delayed = num_samples - num_on_time # 45 samples with on_time = 0

# Generate features for on_time deliveries (more favorable conditions)
# Favorable conditions: shorter distances, lighter packages, and lower traffic levels
distance_km_on_time = np.random.uniform(1, 500, num_on_time)          # Shorter distances
package_weight_kg_on_time = np.random.uniform(0.5, 100, num_on_time)     # Lighter packages
traffic_level_on_time = np.random.randint(1, 10, num_on_time)           # Traffic level 1 or 2

# Generate features for delayed deliveries (less favorable conditions)
# Less favorable conditions: longer distances, heavier packages, and higher traffic levels
distance_km_delayed = np.random.uniform(500, 700, num_delayed)           # Longer distances
package_weight_kg_delayed = np.random.uniform(100, 150, num_delayed)      # Heavier packages
traffic_level_delayed = np.random.randint(9, 15, num_delayed)             # Traffic level 2 or 3

# Create DataFrame for on_time deliveries
df_on_time = pd.DataFrame({
    "distance_km": np.round(distance_km_on_time, 2),
    "package_weight_kg": np.round(package_weight_kg_on_time, 2),
    "traffic_level": traffic_level_on_time,
    "on_time": np.ones(num_on_time, dtype=int)  # on_time = 1
})

# Create DataFrame for delayed deliveries
df_delayed = pd.DataFrame({
    "distance_km": np.round(distance_km_delayed, 2),
    "package_weight_kg": np.round(package_weight_kg_delayed, 2),
    "traffic_level": traffic_level_delayed,
    "on_time": np.zeros(num_delayed, dtype=int)  # on_time = 0
})

# Combine both DataFrames
df_total = pd.concat([df_on_time, df_delayed], ignore_index=True)

# Shuffle the dataset to mix on_time and delayed cases
df_total = df_total.sample(frac=1, random_state=42).reset_index(drop=True)

# Split the dataset: first 100 samples for training, the remaining 50 for ground truth
df_train = df_total.iloc[:num_samples_train]
df_ground_truth = df_total.iloc[num_samples_train:]

# Save the datasets to CSV files
df_train.to_csv("dataset_train.csv", index=False)
df_ground_truth.to_csv("dataset_ground_truth.csv", index=False)

# Create dataset_predict.csv by removing the on_time column from the ground truth set
df_predict = df_ground_truth.drop(columns=["on_time"])
df_predict.to_csv("dataset_predict.csv", index=False)

print("Dataset generation complete:")
print("Training set shape:", df_train.shape)
print("Ground truth set shape:", df_ground_truth.shape)
print("Prediction set shape:", df_predict.shape)
