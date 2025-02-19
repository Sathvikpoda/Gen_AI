import numpy as np

def calc_eigenvectors(matrix):
    return np.linalg.eig(matrix)

# Example matrix
matrix = np.array([[1, 2], [3, 4]])

print("Matrix:")
print(matrix)

eigenvalues, eigenvectors = calc_eigenvectors(matrix)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)