import math
import pandas as pd

def f(x):
    return x * math.log(x) - 1

def secante(a, b, tol):
    iter_count = 0
    
    # Lista para armazenar os resultados
    results = []

    # Iteração inicial
    fa = f(a)
    fb = f(b)
    
    print(f"{'ITER.':<8}{'a':<10}{'b':<10}{'f(a)':<14}{'f(b)':<14}{'ze':<12}{'f(ze)':<14}{'|XN - XN-1|':<10}{'|XN - XN-1|/|Xn|':<12}{'|F(ze)|':<12}")

    while abs(b - a) > tol:
        # Cálculo do novo ponto ze usando a fórmula da secante
        ze = b - fb * (b - a) / (fb - fa)
        fze = f(ze)
        
        # Calcula o erro
        erro_absoluto = abs(ze - b)
        erro_relativo = abs(erro_absoluto / ze)
        erro_funcao = abs(fze)

        # Exibe os resultados da iteração atual
        print(f"{iter_count:<8}{a:<10.6f}{b:<10.6f}{fa:<14.10f}{fb:<14.10f}{ze:<12.6f}{fze:<14.10f}{erro_absoluto:<10.4f}{erro_relativo:<12.4f}{erro_funcao:<12.5f}")

        # Armazena os resultados em uma lista
        results.append({
            'Iteração': iter_count,
            'a': a,
            'b': b,
            'f(a)': fa,
            'f(b)': fb,
            'ze': ze,
            'f(ze)': fze,
            '|XN - XN-1|': erro_absoluto,
            '|XN - XN-1|/|Xn|': erro_relativo,
            '|F(ze)|': erro_funcao
        })

        # Atualiza os valores para a próxima iteração
        a = b
        fa = fb
        b = ze
        fb = fze

        iter_count += 1

    # Última iteração
    print(f"{iter_count:<8}{a:<10.6f}{b:<10.6f}{fa:<14.10f}{fb:<14.10f}{ze:<12.6f}{fze:<14.10f}{erro_absoluto:<10.4f}{erro_relativo:<12.4f}{erro_funcao:<12.5f}")
    
    results.append({
        'Iteração': iter_count,
        'a': a,
        'b': b,
        'f(a)': fa,
        'f(b)': fb,
        'ze': ze,
        'f(ze)': fze,
        '|XN - XN-1|': erro_absoluto,
        '|XN - XN-1|/|Xn|': erro_relativo,
        '|F(ze)|': erro_funcao
    })

    # Cria o DataFrame
    df = pd.DataFrame(results)
    return ze, df

# Parâmetros iniciais
a = 1  # Valor inicial
b = 2  # Valor inicial
tol = 0.001  # Tolerância

# Executa o método da secante e salva os resultados em um DataFrame
raiz, df_resultados = secante(a, b, tol)

if raiz is not None:
    print(f"\nRaiz aproximada: {raiz:.6f}")
    df_resultados.to_csv('./df_resultados_secante.csv')
