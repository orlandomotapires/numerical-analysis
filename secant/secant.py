import math
import pandas as pd

def f(x):
    return x * math.log(x) - 1

def secant(a, b, tol):
    iter_count = 0
    
    # List to store results
    results = []

    # Initial iteration
    fa = f(a)
    fb = f(b)
    
    print(f"{'ITER.':<8}{'a':<10}{'b':<10}{'f(a)':<14}{'f(b)':<14}{'ze':<12}{'f(ze)':<14}{'|XN - XN-1|':<10}{'|XN - XN-1|/|Xn|':<12}{'|F(ze)|':<12}")

    while abs(b - a) > tol:
        # Calculate the new point ze using the secant formula
        ze = b - fb * (b - a) / (fb - fa)
        fze = f(ze)
        
        # Calculate errors
        absolute_error = abs(ze - b)
        relative_error = abs(absolute_error / ze)
        function_error = abs(fze)

        # Display results of the current iteration
        print(f"{iter_count:<8}{a:<10.6f}{b:<10.6f}{fa:<14.10f}{fb:<14.10f}{ze:<12.6f}{fze:<14.10f}{absolute_error:<10.4f}{relative_error:<12.4f}{function_error:<12.5f}")

        # Store results in a list
        results.append({
            'Iteration': iter_count,
            'a': a,
            'b': b,
            'f(a)': fa,
            'f(b)': fb,
            'ze': ze,
            'f(ze)': fze,
            '|XN - XN-1|': absolute_error,
            '|XN - XN-1|/|Xn|': relative_error,
            '|F(ze)|': function_error
        })

        # Update values for the next iteration
        a = b
        fa = fb
        b = ze
        fb = fze

        iter_count += 1

    # Final iteration
    print(f"{iter_count:<8}{a:<10.6f}{b:<10.6f}{fa:<14.10f}{fb:<14.10f}{ze:<12.6f}{fze:<14.10f}{absolute_error:<10.4f}{relative_error:<12.4f}{function_error:<12.5f}")
    
    results.append({
        'Iteration': iter_count,
        'a': a,
        'b': b,
        'f(a)': fa,
        'f(b)': fb,
        'ze': ze,
        'f(ze)': fze,
        '|XN - XN-1|': absolute_error,
        '|XN - XN-1|/|Xn|': relative_error,
        '|F(ze)|': function_error
    })

    # Create DataFrame
    df = pd.DataFrame(results)
    return ze, df

# Initial parameters
a = 1  # Initial value
b = 2  # Initial value
tol = 0.001  # Tolerance

# Execute the secant method and save the results in a DataFrame
root, df_results = secant(a, b, tol)

if root is not None:
    print(f"\nApproximate root: {root:.6f}")
    df_results.to_csv('./df_results_secant.csv')
