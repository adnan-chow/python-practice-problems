import numpy as np

def matrix_multiply(a, b):
    return np.dot(a, b).tolist()

# Test the function
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print(matrix_multiply(a, b))