Iris Dataset Clustering Analysis

This repository contains Python code for performing clustering analysis on the famous Iris dataset. The code demonstrates the application of K-means and DBSCAN clustering algorithms, visualized using PCA (Principal Component Analysis) and t-SNE (t-Distributed Stochastic Neighbor Embedding) techniques.

Description
The Iris dataset is a classic dataset from the field of machine learning and statistics. It consists of 150 samples from three species of Iris (Iris setosa, Iris virginica, and Iris versicolor). Each sample has four features: the lengths and the widths of the sepals and petals.

In this project, we:

Standardize the dataset to have a mean of zero and variance of one.
Apply K-means clustering to categorize the data into three clusters.
Visualize the clusters using PCA and t-SNE.
Apply DBSCAN clustering to identify densely packed areas and outliers.
Visualize the results of DBSCAN clustering using PCA and t-SNE.

Libraries Used
numpy
matplotlib
seaborn
scikit-learn
Visualization

Two types of visualizations are provided:

PCA Visualization: Helps in visualizing the data in two principal components derived from the original four dimensions.
t-SNE Visualization: Provides a more nuanced visualization, emphasizing the local structure of the data.
How to Run
To run this analysis, make sure you have Python installed along with the necessary libraries. Clone this repository, navigate to the directory containing the file, and run the script:

python iris_clustering.py
Results
You can expect to see plots showing the clusters formed by each algorithm using both PCA and t-SNE for dimensionality reduction.

