import math
import pandas as pd

def f(x):
    return x * math.log(x) - 1

def derivative_f(x):
    return math.log(x) + 1

def newton(x0, tol):
    iter_count = 0
    x = x0
    prev_x = x
    
    # List to store results
    results = []

    # Newton-Raphson loop
    while True:
        prev_x = x
        fx = f(x)
        dfx = derivative_f(x)
        
        # Check if the derivative is zero to avoid division by zero
        if dfx == 0:
            print("Derivative is zero. The method cannot continue.")
            return None
        
        # Update the value of x
        x = x - fx / dfx
        
        # Calculate errors
        absolute_error = abs(x - prev_x)
        relative_error = abs(absolute_error / x)
        function_error = abs(f(x))

        # Store results
        results.append({
            'Iteration': iter_count,
            'x': prev_x,
            'f(x)': fx,
            'f\'(x)': dfx,
            '|xn - xn-1|': absolute_error,
            '|xn - xn-1|/|xn|': relative_error,
            '|F(xn)|': function_error
        })

        # Stopping criterion
        if absolute_error < tol:
            break

        iter_count += 1

    # Last iteration
    fx = f(x)
    dfx = derivative_f(x)
    absolute_error = abs(x - prev_x)
    relative_error = abs(absolute_error / x)
    function_error = abs(f(x))

    results.append({
        'Iteration': iter_count,
        'x': x,
        'f(x)': fx,
        'f\'(x)': dfx,
        '|xn - xn-1|': absolute_error,
        '|xn - xn-1|/|xn|': relative_error,
        '|F(xn)|': function_error
    })

    # Create DataFrame
    df = pd.DataFrame(results)
    return x, df

# Initial parameters
x0 = 2  # Initial guess
tol = 0.001  # Tolerance

# Run the Newton method and save results in a DataFrame
root, df_results = newton(x0, tol)

if root is not None:
    print(f"\nApproximated root: {root:.4f}")
    df_results.to_csv('./df_results_newton.csv', index=False)
