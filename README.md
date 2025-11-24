📘 Student Performance Prediction using Machine Learning
📌 Overview

This project uses Machine Learning to predict whether a student will pass or fail based on factors such as hours studied, attendance, assignments completed, and class participation.
A Decision Tree Classifier is used to train the model on a synthetic dataset of 200 students.

🚀 Features

Synthetic dataset generation

Exploratory data analysis (EDA)

Visualization of student performance patterns

Machine Learning model training using Decision Tree

Model evaluation (Accuracy, Confusion Matrix, Cla📂 Dataset Description

The dataset contains 200 records with the following features:

Feature	Description
hours_studied	Number of hours studied per week
attendance	Attendance percentage (50–100%)
assignments_completed	Number of assignments completed
class_participation	Participation level (1–10)
pass	Target variable: 1 = Pass, 0 = Fail

The pass/fail label is generated using:

(hours_studied + assignments_completed + class_participation > 22) 
AND attendance > 65ssification Report)

🧪 Technologies Used

Python

Pandas

NumPy

Matplotlib

Scikit-learn

🛠️ How to Run the Project
1. Install dependencies
pip install pandas numpy matplotlib scikit-learn

2. Run the Python script
python student_performance_prediction.py

📊 Visualizations

The project includes scatter plots that show relationships between:

Hours studied vs attendance

Pass/fail distribution

These graphs help understand how different factors affect student outcomes.


🤖 Machine Learning Model

The model used is:

Decision Tree Classifier

Easy to interpret

Works well with rule-based synthetic data

Evaluation metrics displayed:

Accuracy

Confusion Matrix

Precision, Recall, F1-score

📈 Sample Output

Summary statistics of dataset

Scatter plot visualization

Model accuracy score

Classification report
