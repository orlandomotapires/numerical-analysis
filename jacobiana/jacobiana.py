import numpy as np
import pandas as pd

# Definindo a matriz Jacobiana e a função f
def jacobian(x, K):
    return np.array([[-150 * np.sin(x[0]) - 2 * K, K], 
                     [K, -50 * np.sin(x[1]) - K]])

def f(x, K):
    return np.array([150 * np.cos(x[0]) + K * (x[1] - x[0]) - K * x[0], 
                     50 * np.cos(x[1]) - K * (x[1] - x[0])])

# Inicializando os valores
x = np.array([0.5, 0.5])
K = 10  # Defina o valor de K aqui
tolerance = 1e-3  # Defina a tolerância desejada
max_iterations = 100  # Defina o número máximo de iterações
results = []

# Método da Jacobiana
for i in range(max_iterations):
    J = jacobian(x, K)
    F = f(x, K)
    J_inv = np.linalg.inv(J)
    delta_x = np.dot(J_inv, -F)
    x_new = x + delta_x
    
    abs_error = np.linalg.norm(x_new - x, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x, ord=np.inf)
    
    results.append({
        'Iteração': i,
        'x1': x_new[0],
        'x2': x_new[1],
        'abs': abs_error,
        'rel': rel_error
    })
    
    if abs_error < tolerance:
        print(f'Convergence reached at iteration {i}')
        break
    
    x = x_new

# Criando DataFrame para resultados
df_jacobiana = pd.DataFrame(results)
print(df_jacobiana)
