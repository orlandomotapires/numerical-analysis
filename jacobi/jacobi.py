import numpy as np
import pandas as pd

# Define the matrix A and the vector b
A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]], dtype=float)
b = np.array([7, -8, 6], dtype=float)

# Initialize the values
x = np.array([0.7, -1.6, 0.6], dtype=float)  # Initial values for x, y, z
tolerance = 0.05  # Define the tolerance
iterations = 100  # Maximum number of iterations
results = []

# Jacobi Method
for i in range(iterations):
    x_new = np.zeros_like(x)
    for j in range(len(A)):
        s1 = np.dot(A[j, :j], x[:j])
        s2 = np.dot(A[j, j+1:], x[j+1:])
        x_new[j] = (b[j] - s1 - s2) / A[j, j]
    
    abs_error = np.linalg.norm(x_new - x, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x_new, ord=np.inf)
    
    results.append({
        'Iteration': i,
        'x': x_new[0],
        'y': x_new[1],
        'z': x_new[2],
        'Absolute Error': abs_error,
        'Relative Error': rel_error
    })
    
    if abs_error < tolerance:
        print(f'Converged in {i} iterations.')
        break
    
    x = x_new

# Create DataFrame for results
df_jacobi = pd.DataFrame(results)
print(df_jacobi)
