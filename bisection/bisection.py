import math
import pandas as pd

def f(x):
    return x * math.log(x) - 1

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("f(a) * f(b) >= 0: The root existence condition is not satisfied.")
        return None

    iter_count = 0
    c = a
    prev_c = c
    
    # List to store results
    results = []

    print(f"{'ITER.':<8}{'a':<8}{'f(a)':<14}{'b':<8}{'f(b)':<14}{'c':<8}{'f(c)':<14}{'f(a)*f(c)':<10}{'f(c)*f(b)':<10}{'|xn - xn-1|':<10}{'|xn - xn-1|/|xn|':<12}{'|F(xn)|':<12}")
    
    while (b - a) / 2.0 > tol:
        prev_c = c
        c = (a + b) / 2.0
        fc = f(c)

        # Calculate errors
        absolute_error = abs(c - prev_c)
        relative_error = abs(absolute_error / c)
        function_error = abs(fc)

        # Display current iteration results
        print(f"{iter_count:<8}{a:<8.4f}{f(a):<14.10f}{b:<8.4f}{f(b):<14.10f}{c:<8.4f}{fc:<14.10f}{f(a)*fc:<10.6f}{fc*f(b):<10.6f}{absolute_error:<10.4f}{relative_error:<12.4f}{function_error:<12.5f}")

        # Store results in a list
        results.append({
            'Iteration': iter_count,
            'a': a,
            'f(a)': f(a),
            'b': b,
            'f(b)': f(b),
            'c': c,
            'f(c)': fc,
            'f(a)*f(c)': f(a) * fc,
            'f(c)*f(b)': fc * f(b),
            '|xn - xn-1|': absolute_error,
            '|xn - xn-1|/|xn|': relative_error,
            '|F(xn)|': function_error
        })

        # Check the product of signs to determine the new interval
        if f(a) * fc < 0:
            b = c
        else:
            a = c

        iter_count += 1

    # Last error calculation
    absolute_error = abs(c - prev_c)
    relative_error = abs(absolute_error / c)
    function_error = abs(fc)
    
    # Display last iteration
    print(f"{iter_count:<8}{a:<8.4f}{f(a):<14.10f}{b:<8.4f}{f(b):<14.10f}{c:<8.4f}{fc:<14.10f}{f(a)*fc:<10.6f}{fc*f(b):<10.6f}{absolute_error:<10.4f}{relative_error:<12.4f}{function_error:<12.5f}")

    # Store last iteration
    results.append({
        'Iteration': iter_count,
        'a': a,
        'f(a)': f(a),
        'b': b,
        'f(b)': f(b),
        'c': c,
        'f(c)': fc,
        'f(a)*f(c)': f(a) * fc,
        'f(c)*f(b)': fc * f(b),
        '|xn - xn-1|': absolute_error,
        '|xn - xn-1|/|xn|': relative_error,
        '|F(xn)|': function_error
    })

    # Create DataFrame
    df = pd.DataFrame(results)
    return c, df

# Initial parameters
a = 1
b = 2
tol = 0.001

# Execute the bisection method and save results in a DataFrame
root, df_results = bisection(a, b, tol)

if root is not None:
    print(f"\nApproximated root: {root:.4f}")
    df_results.to_csv('./df_results_bisection.csv', index=False)
