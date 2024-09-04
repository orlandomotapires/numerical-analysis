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

# Improved Jacobi Method (Gauss-Seidel)
for i in range(iterations):
    x_old = x.copy()  # Keep old values for error calculation
    for j in range(len(A)):
        s1 = np.dot(A[j, :j], x[:j])  # Use the most recent values
        s2 = np.dot(A[j, j+1:], x_old[j+1:])  # Use old values for positions that are not yet updated
        x[j] = (b[j] - s1 - s2) / A[j, j]
    
    abs_error = np.linalg.norm(x - x_old, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x, ord=np.inf)
    
    results.append({
        'Iteration': i,
        'x': x[0],
        'y': x[1],
        'z': x[2],
        'Absolute Error': abs_error,
        'Relative Error': rel_error
    })
    
    if abs_error < tolerance:
        print(f'Converged in {i} iterations.')
        break

# Create DataFrame for results
df_gauss_seidel = pd.DataFrame(results)
print(df_gauss_seidel)
