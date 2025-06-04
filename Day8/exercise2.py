import numpy as np


matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Original Matrix:")
print(matrix)

transpose = matrix.T
print("\nTranspose:")
print(transpose)

determinant = np.linalg.det(matrix)
print("\nDeterminant:", determinant)

if determinant != 0:
    inverse = np.linalg.inv(matrix)
    print("\nInverse:")
    print(inverse)
else:
    print("\nInverse: The matrix is singular and does not have an inverse.")
