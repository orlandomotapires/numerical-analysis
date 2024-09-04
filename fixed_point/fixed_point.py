import math
import pandas as pd

def f(x):
    return x * math.log(x) - 1

def B(x):
    return math.exp(1 / x)

def fixed_point(x0, tol):
    iter_count = 0
    x = x0
    
    # List to store results
    results = []

    print(f"{'ITER.':<8}{'x':<10}{'f(x)':<14}{'|f(x)|':<10}{'|xn - xn-1|':<12}{'|xn - xn-1|/|xn|':<14}{'x':<10}{'B(x)':<10}")

    while True:
        fx = f(x)
        bx = B(x)
        
        # Calculate errors
        absolute_error = abs(fx)
        relative_error = abs(absolute_error / x)
        iterative_error = abs(x - bx)

        # Display results of the current iteration
        print(f"{iter_count:<8}{x:<10.4f}{fx:<14.10f}{absolute_error:<10.4f}{iterative_error:<12.4f}{relative_error:<14.4f}{bx:<10.4f}{B(bx):<10.4f}")

        # Store results in a list
        results.append({
            'Iteration': iter_count,
            'x': x,
            'f(x)': fx,
            '|f(x)|': absolute_error,
            '|xn - xn-1|': iterative_error,
            '|xn - xn-1|/|xn|': relative_error,
            'x': x,
            'B(x)': bx
        })

        # Convergence criterion
        if abs(x - bx) < tol:
            break

        # Update value of x
        x = bx
        iter_count += 1

    # Final iteration
    fx = f(x)
    bx = B(x)
    absolute_error = abs(fx)
    relative_error = abs(absolute_error / x)
    iterative_error = abs(x - bx)
    
    print(f"{iter_count:<8}{x:<10.4f}{fx:<14.10f}{absolute_error:<10.4f}{iterative_error:<12.4f}{relative_error:<14.4f}{bx:<10.4f}{B(bx):<10.4f}")
    
    results.append({
        'Iteration': iter_count,
        'x': x,
        'f(x)': fx,
        '|f(x)|': absolute_error,
        '|xn - xn-1|': iterative_error,
        '|xn - xn-1|/|xn|': relative_error,
        'x': x,
        'B(x)': bx
    })

    # Create DataFrame
    df = pd.DataFrame(results)
    return x, df

# Initial parameters
x0 = 2  # Initial value
tol = 0.0001  # Tolerance

# Execute the fixed point method and save the results in a DataFrame
root, df_results = fixed_point(x0, tol)

if root is not None:
    print(f"\nApproximate root: {root:.4f}")
    df_results.to_csv('./df_results_fixed_point.csv')
