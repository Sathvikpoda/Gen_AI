Wholesale Customers Data Clustering
This repository contains Python code for performing clustering analysis on the "Wholesale customers" dataset sourced from the UCI Machine Learning Repository. The code demonstrates the application of K-means clustering algorithm combined with PCA (Principal Component Analysis) for data visualization and cluster evaluation using silhouette scores.

Description
The "Wholesale customers" dataset includes data about customers of a wholesale distributor. It involves several product categories like Fresh, Milk, Grocery, etc. The aim of this project is to segment these customers based on their annual spending on various product categories.

Key steps implemented in the project:

Standardization of the dataset to ensure each feature contributes equally.
Dimensionality reduction using PCA to reduce the features to two principal components for easy visualization.
Application of K-means clustering to segment customers.
Evaluation of cluster quality using silhouette scores.
Visualization of the clusters using a 2D scatter plot.

Libraries Used
pandas
matplotlib
seaborn
numpy
scikit-learn

How to Run
To execute this analysis, ensure Python is installed along with the required libraries. Clone this repository, navigate to the directory containing the script, and run the following:
python wholesale_customers_clustering.py
Results
Expect to see a 2D scatter plot showing the segmentation of customers into distinct clusters. The silhouette score provided will give insight into the separation distance between the resulting clusters, indicating the effectiveness of the clustering.