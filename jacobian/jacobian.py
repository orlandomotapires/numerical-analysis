import numpy as np
import pandas as pd

# Define the Jacobian matrix and function f
def jacobian(x, K):
    return np.array([[-150 * np.sin(x[0]) - 2 * K, K], 
                     [K, -50 * np.sin(x[1]) - K]])

def f(x, K):
    return np.array([150 * np.cos(x[0]) + K * (x[1] - x[0]) - K * x[0], 
                     50 * np.cos(x[1]) - K * (x[1] - x[0])])

# Initialize values
x = np.array([0.5, 0.5])
K = 10  # Define the value of K here
tolerance = 1e-3  # Define the desired tolerance
max_iterations = 100  # Define the maximum number of iterations
results = []

# Newton-Raphson method using the Jacobian matrix
for i in range(max_iterations):
    J = jacobian(x, K)
    F = f(x, K)
    J_inv = np.linalg.inv(J)
    delta_x = np.dot(J_inv, -F)
    x_new = x + delta_x
    
    abs_error = np.linalg.norm(x_new - x, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x, ord=np.inf)
    
    results.append({
        'Iteration': i,
        'x1': x_new[0],
        'x2': x_new[1],
        'Absolute Error': abs_error,
        'Relative Error': rel_error
    })
    
    if abs_error < tolerance:
        print(f'Convergence reached at iteration {i}')
        break
    
    x = x_new

# Creating DataFrame for results
df_jacobian = pd.DataFrame(results)
print(df_jacobian)
