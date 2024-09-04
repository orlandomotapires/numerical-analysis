import numpy as np
import pandas as pd

# Definindo a matriz A e o vetor b
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 3]], dtype=float)
b = np.array([15, 10, 10], dtype=float)

# Inicializando os valores
x = np.zeros_like(b)
iterations = 9  # Definindo o número de iterações fornecido
results = []

# Método da Jacobi
for i in range(iterations):
    x_new = np.zeros_like(x)
    for j in range(len(A)):
        s1 = np.dot(A[j, :j], x[:j])
        s2 = np.dot(A[j, j+1:], x[j+1:])
        x_new[j] = (b[j] - s1 - s2) / A[j, j]
    
    abs_error = np.linalg.norm(x_new - x, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x_new, ord=np.inf)
    
    results.append({
        'Iteração': i,
        'x': x_new[0],
        'y': x_new[1],
        'z': x_new[2],
        'abs': abs_error,
        'rel': rel_error
    })
    
    x = x_new

# Criando DataFrame para resultados
df_jacobi = pd.DataFrame(results)
print(df_jacobi)
