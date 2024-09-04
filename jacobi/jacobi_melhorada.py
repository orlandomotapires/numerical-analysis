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

# Método de Jacobi Melhorada (Gauss-Seidel)
for i in range(iterations):
    x_old = x.copy()  # Mantém os valores antigos para cálculo do erro
    for j in range(len(A)):
        s1 = np.dot(A[j, :j], x[:j])  # Usando os valores mais recentes
        s2 = np.dot(A[j, j+1:], x_old[j+1:])  # Usando os valores anteriores para as posições que ainda não foram atualizadas
        x[j] = (b[j] - s1 - s2) / A[j, j]
    
    abs_error = np.linalg.norm(x - x_old, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x, ord=np.inf)
    
    results.append({
        'Iteração': i,
        'x': x[0],
        'y': x[1],
        'z': x[2],
        'abs': abs_error,
        'rel': rel_error
    })
    
    if abs_error < tolerance:
        print(f'Convergiu em {i} iterações.')
        break

# Criando DataFrame para resultados
df_gauss_seidel = pd.DataFrame(results)
print(df_gauss_seidel)
