import math
import pandas as pd

def f(x):
    return x * math.log(x) - 1

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("f(a) * f(b) >= 0: A condição de existência de raiz não é satisfeita.")
        return None

    iter_count = 0
    c = a
    prev_c = c
    
    # Lista para armazenar os resultados
    results = []

    print(f"{'ITER.':<8}{'a':<8}{'f(a)':<14}{'b':<8}{'f(b)':<14}{'c':<8}{'f(c)':<14}{'f(a)*f(c)':<10}{'f(c)*f(b)':<10}{'|xn - xn-1|':<10}{'|xn - xn-1|/|xn|':<12}{'|F(xn)|':<12}")
    
    while (b - a) / 2.0 > tol:
        prev_c = c
        c = (a + b) / 2.0
        fc = f(c)

        # Calcula o erro
        erro_absoluto = abs(c - prev_c)
        erro_relativo = abs(erro_absoluto / c)
        erro_funcao = abs(fc)

        # Exibe os resultados da iteração atual
        print(f"{iter_count:<8}{a:<8.4f}{f(a):<14.10f}{b:<8.4f}{f(b):<14.10f}{c:<8.4f}{fc:<14.10f}{f(a)*fc:<10.6f}{fc*f(b):<10.6f}{erro_absoluto:<10.4f}{erro_relativo:<12.4f}{erro_funcao:<12.5f}")

        # Armazena os resultados em uma lista
        results.append({
            'Iteração': iter_count,
            'a': a,
            'f(a)': f(a),
            'b': b,
            'f(b)': f(b),
            'c': c,
            'f(c)': fc,
            'f(a)*f(c)': f(a) * fc,
            'f(c)*f(b)': fc * f(b),
            '|xn - xn-1|': erro_absoluto,
            '|xn - xn-1|/|xn|': erro_relativo,
            '|F(xn)|': erro_funcao
        })

        # Verifica o produto dos sinais para determinar o novo intervalo
        if f(a) * fc < 0:
            b = c
        else:
            a = c

        iter_count += 1

    # Último cálculo de erro
    erro_absoluto = abs(c - prev_c)
    erro_relativo = abs(erro_absoluto / c)
    erro_funcao = abs(fc)
    
    # Exibe a última iteração
    print(f"{iter_count:<8}{a:<8.4f}{f(a):<14.10f}{b:<8.4f}{f(b):<14.10f}{c:<8.4f}{fc:<14.10f}{f(a)*fc:<10.6f}{fc*f(b):<10.6f}{erro_absoluto:<10.4f}{erro_relativo:<12.4f}{erro_funcao:<12.5f}")

    # Armazena a última iteração
    results.append({
        'Iteração': iter_count,
        'a': a,
        'f(a)': f(a),
        'b': b,
        'f(b)': f(b),
        'c': c,
        'f(c)': fc,
        'f(a)*f(c)': f(a) * fc,
        'f(c)*f(b)': fc * f(b),
        '|xn - xn-1|': erro_absoluto,
        '|xn - xn-1|/|xn|': erro_relativo,
        '|F(xn)|': erro_funcao
    })

    # Cria o DataFrame
    df = pd.DataFrame(results)
    return c, df

# Parâmetros iniciais
a = 1
b = 2
tol = 0.001

# Executa o método da bissecção e salva os resultados em um DataFrame
raiz, df_resultados = bisection(a, b, tol)

if raiz is not None:
    print(f"\nRaiz aproximada: {raiz:.4f}")
    df_resultados.to_csv('./df_resultados_bisseccao.csv')


