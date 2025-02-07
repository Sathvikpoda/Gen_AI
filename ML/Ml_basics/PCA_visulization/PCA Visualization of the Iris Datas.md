PCA Visualization of the Iris Dataset
This repository contains Python code that demonstrates the use of Principal Component Analysis (PCA) to visualize the Iris dataset. The project compares scatter plots of the original features with plots of the principal components to show how PCA simplifies the data while maintaining essential patterns.

Description
The Iris dataset consists of measurements of 150 iris flowers from three different species. Each flower is described by four features: sepal length, sepal width, petal length, and petal width. This project visualizes these features and applies PCA to reduce dimensionality for a clearer visualization of species clusters.

Key Steps Implemented:
Data Visualization: Plot original features (petal length vs. petal width) to see how species are distributed based on these dimensions.
Feature Standardization: Standardize the dataset to prepare it for PCA, ensuring each feature contributes equally.
PCA Application: Reduce the feature set to two principal components and visualize the results.
Comparative Visualization: Compare scatter plots before and after PCA to observe the effect of this dimensionality reduction technique.
Libraries Used
pandas
matplotlib
seaborn
scikit-learn

How to Run
Ensure you have Python installed along with the necessary libraries. Update the file path in the script to where you've saved your dataset. Run the script to see the visualizations:
python iris_pca_visualization.py

Results
The output will be two plots displayed in one figure:

Without PCA: A scatter plot showing petal length versus petal width, colored by species.
With PCA: A scatter plot of the first two principal components, also colored by species.
These plots help in understanding how PCA transforms the data into a new coordinate system that better highlights differences between species.