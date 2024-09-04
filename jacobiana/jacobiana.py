import numpy as np
import pandas as pd

# Definindo a matriz Jacobiana e a função f
def jacobian(x):
    return np.array([[-150*np.sin(x[0]) - 2*x[1], -2*x[0]], [x[1] - x[0], -50*np.sin(x[1]) - x[0]]])

def f(x):
    return np.array([150*np.cos(x[0]) + x[1] - x[0] - x[0], 50*np.cos(x[1]) - x[1] - x[0]])

# Inicializando os valores
x = np.array([0.5, 0.5])
iterations = 10
results = []

# Método da Jacobiana
for i in range(iterations):
    J = jacobian(x)
    F = f(x)
    J_inv = np.linalg.inv(J)
    delta_x = np.dot(J_inv, -F)
    x_new = x + delta_x
    
    abs_error = np.linalg.norm(x_new - x, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x, ord=np.inf)
    
    results.append({
        'Iteração': i,
        'x': x_new[0],
        'y': x_new[1],
        'abs': abs_error,
        'rel': rel_error
    })
    
    x = x_new

# Criando DataFrame para resultados
df_jacobiana = pd.DataFrame(results)
print(df_jacobiana)
