Fictional Character Battle Outcome Prediction
🔍 Overview
This script analyzes battle outcomes based on fictional character attributes using multiple machine learning models. It cleans data, extracts features, and compares models to find the best predictor.

⚡ How It Works
Loads & cleans the dataset (handles missing values).
Encodes categorical variables for machine learning.
Splits data into training and testing sets.
Applies feature scaling to improve model performance.
Trains and evaluates multiple models, including:
Logistic Regression
Decision Tree
Random Forest
Naive Bayes
Support Vector Machine (SVM)
XGBoost (with Hyperparameter Tuning)
Uses SMOTE to handle imbalanced data.
Generates performance reports for all models.

🔧 Requirements
Install the required libraries:

pip install pandas numpy seaborn matplotlib scikit-learn xgboost imbalanced-learn

🚀 How to Run
Upload the dataset to the script (if using Google Colab).

Run the script in Python:
python script_name.py
The script will process the data and compare multiple models.
📌 Features
✅ Cleans and preprocesses data
✅ Handles missing values and encodes categorical data
✅ Compares multiple machine learning models
✅ Uses SMOTE to balance the dataset
✅ Hyperparameter tuning for XGBoost
✅ Generates accuracy, confusion matrix, and classification reports

📂 Output
Best model accuracy & performance report
Confusion matrices for each model
Feature importance plots for decision-based models