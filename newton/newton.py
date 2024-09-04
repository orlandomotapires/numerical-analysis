import math
import pandas as pd

def f(x):
    return x * math.log(x) - 1

def derivada_f(x):
    return math.log(x) + 1

def newton(x0, tol):
    iter_count = 0
    x = x0
    prev_x = x
    
    # Lista para armazenar os resultados
    results = []

    #print(f"{'ITER.':<8}{'x':<8}{'f(x)':<14}{'f\'(x)':<14}{'|xn - xn-1|':<10}{'|xn - xn-1|/|xn|':<12}{'|F(xn)|':<12}")

    while True:
        prev_x = x
        fx = f(x)

        dfx = derivada_f(x)
        
        # Verifica se a derivada é zero para evitar divisão por zero
        if dfx == 0:
            print("Derivada é zero. O método não pode continuar.")
            return None
        
        x = x - fx / dfx
        
        # Calcula o erro
        erro_absoluto = abs(x - prev_x)
        erro_relativo = abs(erro_absoluto / x)
        erro_funcao = abs(f(x))

        # Exibe os resultados da iteração atual
        print(f"{iter_count:<8}{prev_x:<8.4f}{fx:<14.10f}{dfx:<14.10f}{erro_absoluto:<10.4f}{erro_relativo:<12.4f}{erro_funcao:<12.5f}")

        # Armazena os resultados em uma lista
        results.append({
            'Iteração': iter_count,
            'x': prev_x,
            'f(x)': fx,
            'f\'(x)': dfx,
            '|xn - xn-1|': erro_absoluto,
            '|xn - xn-1|/|xn|': erro_relativo,
            '|F(xn)|': erro_funcao
        })

        # Critério de parada
        if erro_absoluto < tol:
            break

        iter_count += 1

    # Última iteração
    fx = f(x)
    dfx = derivada_f(x)
    erro_absoluto = abs(x - prev_x)
    erro_relativo = abs(erro_absoluto / x)
    erro_funcao = abs(f(x))

    print(f"{iter_count:<8}{x:<8.4f}{fx:<14.10f}{dfx:<14.10f}{erro_absoluto:<10.4f}{erro_relativo:<12.4f}{erro_funcao:<12.5f}")

    results.append({
        'Iteração': iter_count,
        'x': x,
        'f(x)': fx,
        'f\'(x)': dfx,
        '|xn - xn-1|': erro_absoluto,
        '|xn - xn-1|/|xn|': erro_relativo,
        '|F(xn)|': erro_funcao
    })

    # Cria o DataFrame
    df = pd.DataFrame(results)
    return x, df

# Parâmetros iniciais
x0 = 2  # Chute inicial
tol = 0.001  # Tolerância

# Executa o método de Newton e salva os resultados em um DataFrame
raiz, df_resultados = newton(x0, tol)

if raiz is not None:
    print(f"\nRaiz aproximada: {raiz:.4f}")
    df_resultados.to_csv('./df_resultados_newton.csv')
