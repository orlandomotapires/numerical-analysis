import math
import pandas as pd

def f(x):
    return x * math.log(x) - 1

def B(x):
    return math.exp(1 / x)

def ponto_fixo(x0, tol):
    iter_count = 0
    x = x0
    
    # Lista para armazenar os resultados
    results = []

    print(f"{'ITER.':<8}{'x':<10}{'f(x)':<14}{'|f(x)|':<10}{'|xn - xn-1|':<12}{'|xn - xn-1|/|xn|':<14}{'x':<10}{'B(x)':<10}")

    while True:
        fx = f(x)
        bx = B(x)
        
        # Calcula o erro
        erro_absoluto = abs(fx)
        erro_relativo = abs(erro_absoluto / x)
        erro_iterativo = abs(x - bx)

        # Exibe os resultados da iteração atual
        print(f"{iter_count:<8}{x:<10.4f}{fx:<14.10f}{erro_absoluto:<10.4f}{erro_iterativo:<12.4f}{erro_relativo:<14.4f}{bx:<10.4f}{B(bx):<10.4f}")

        # Armazena os resultados em uma lista
        results.append({
            'Iteração': iter_count,
            'x': x,
            'f(x)': fx,
            '|f(x)|': erro_absoluto,
            '|xn - xn-1|': erro_iterativo,
            '|xn - xn-1|/|xn|': erro_relativo,
            'x': x,
            'B(x)': bx
        })

        # Critério de parada
        if abs(x - bx) < tol:
            break

        # Atualiza o valor de x
        x = bx
        iter_count += 1

    # Última iteração
    fx = f(x)
    bx = B(x)
    erro_absoluto = abs(fx)
    erro_relativo = abs(erro_absoluto / x)
    erro_iterativo = abs(x - bx)
    
    print(f"{iter_count:<8}{x:<10.4f}{fx:<14.10f}{erro_absoluto:<10.4f}{erro_iterativo:<12.4f}{erro_relativo:<14.4f}{bx:<10.4f}{B(bx):<10.4f}")
    
    results.append({
        'Iteração': iter_count,
        'x': x,
        'f(x)': fx,
        '|f(x)|': erro_absoluto,
        '|xn - xn-1|': erro_iterativo,
        '|xn - xn-1|/|xn|': erro_relativo,
        'x': x,
        'B(x)': bx
    })

    # Cria o DataFrame
    df = pd.DataFrame(results)
    return x, df

# Parâmetros iniciais
x0 = 2  # Valor inicial
tol = 0.0001  # Tolerância

# Executa o método do ponto fixo e salva os resultados em um DataFrame
raiz, df_resultados = ponto_fixo(x0, tol)

if raiz is not None:
    print(f"\nRaiz aproximada: {raiz:.4f}")
    df_resultados.to_csv('./df_resultados_ponto_fixo.csv')
