import numpy as np
import pandas as pd

# Definindo a matriz A e o vetor b
A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]], dtype=float)
b = np.array([7, -8, 6], dtype=float)

# Inicializando os valores
x = np.array([0.7, -1.6, 0.6], dtype=float)  # Valores iniciais para x, y, z
tolerance = 0.05  # Definindo a tolerância
iterations = 100  # Número máximo de iterações
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
    
    if abs_error < tolerance:
        print(f'Convergiu em {i} iterações.')
        break
    
    x = x_new

# Criando DataFrame para resultados
df_jacobi = pd.DataFrame(results)
print(df_jacobi)
