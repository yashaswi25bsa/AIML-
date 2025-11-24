# Student Performance Prediction using Machine Learning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Create Dataset (Synthetic Example)
np.random.seed(42)
num_students = 200
data = {
    "hours_studied": np.random.randint(1, 20, num_students),
    "attendance": np.random.randint(50, 101, num_students),
    "assignments_completed": np.random.randint(0, 10, num_students),
    "class_participation": np.random.randint(1, 10, num_students)
}

df = pd.DataFrame(data)
# Define passing: If hours_studied + assignments_completed + participation > threshold and attendance > 65
df['pass'] = ((df['hours_studied'] + df['assignments_completed'] + df['class_participation'] > 22) & (df['attendance'] > 65)).astype(int)

# 2. Data Analysis
print("First 5 entries:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

# Plot relationships
plt.figure(figsize=(8,5))
plt.scatter(df['hours_studied'], df['attendance'], c=df['pass'], cmap='bwr', alpha=0.7)
plt.xlabel("Hours Studied")
plt.ylabel("Attendance")
plt.title("Hours Studied vs")
plt.show()
