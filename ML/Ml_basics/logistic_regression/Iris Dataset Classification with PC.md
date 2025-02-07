Iris Dataset Classification with PCA and Logistic Regression

This repository contains Python code for classifying species in the Iris dataset using logistic regression after reducing dimensionality with PCA (Principal Component Analysis). The project demonstrates the effectiveness of combining PCA with logistic regression for better visualization and classification accuracy.

Description
The Iris dataset is a well-known dataset in machine learning, consisting of 150 samples of iris flowers from three different species. Each sample has four features: sepal length, sepal width, petal length, and petal width. The goal of this project is to classify these samples into their respective species using logistic regression after reducing the feature dimensions using PCA.

Key Steps Implemented:
Data Standardization: Standardize the feature set to ensure each feature contributes equally to the analysis.
Dimensionality Reduction using PCA: Reduce the features to two principal components for easy visualization and to potentially improve model performance.
Logistic Regression Model: Implement logistic regression to classify iris species.
Model Evaluation: Use cross-validation to evaluate the model performance on the training data and a separate test set to evaluate generalization.

Libraries Used
pandas
matplotlib
seaborn
numpy
scikit-learn

How to Run
Ensure Python is installed along with the required libraries. Clone this repository, navigate to the directory containing the script, and run it using:
python iris_pca_logistic_regression.py

Results
You will see the PCA-transformed scatter plot for the training set, showing how samples from different species are distributed in the reduced feature space. Additionally, the script outputs include cross-validated accuracy scores, mean accuracy, training accuracy, and test accuracy, providing a comprehensive overview of the model's performance.