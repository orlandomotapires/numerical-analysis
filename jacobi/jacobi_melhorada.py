import pandas as pd

def jacobi_melhorado(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    results = []

    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum1) / A[i][i]
        
        # Cálculo dos erros
        abs_err = [abs(x[i] - x_old[i]) for i in range(n)]
        rel_err = [abs_err[i] / abs(x[i]) if x[i] != 0 else 0 for i in range(n)]
        
        # Armazena os resultados
        results.append({
            'Iteração': k,
            'x': x[0],
            'y': x[1],
            'z': x[2],
            'abs': max(abs_err),
            'rel': max(rel_err)
        })

        if max(abs_err) < tol:
            break
    
    df = pd.DataFrame(results)
    return df

# Matriz dos coeficientes
A = [[2, -1, 0.5], [1, 3, -1], [0.5, -1, 1]]
b = [0.5, 1, 1.5]
x0 = [0, 0, 0]  # Chute inicial
tol = 0.0001
max_iter = 20

# Executa o método de Jacobi Melhorado
df_jacobi_melhorado = jacobi_melhorado(A, b, x0, tol, max_iter)
df_jacobi_melhorado.to_csv('jacobi_melhorado_results.csv', index=False)
print(df_jacobi_melhorado)
