# Nonlinear and linear System Solver Methods

## Overview

This project provides implementations of various numerical methods for solving nonlinear and linear systems of equations. The methods included are:

1. **Bisection Method**
2. **Jacobi Method**
3. **Enhanced Jacobi Method**
4. **Newton's Method**
5. **Jacobian Matrix Method**
6. **Fixed Point Iteration**
7. **Secant Method**

## Methods

### 1. Bisection Method

The Bisection Method is a root-finding algorithm that repeatedly divides an interval in half and then selects a subinterval in which a root must lie. It is simple but guarantees convergence if the function changes sign over the interval.

**Usage Example:**
```python
def bisection(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("The function must change sign over the interval [a, b]")
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return (a + b) / 2
```

### 2. Jacobi Method

The Jacobi Method is an iterative algorithm used to solve linear systems of equations. It is particularly effective for large systems where direct methods are computationally expensive.

**Usage Example:**
```python
import numpy as np
import pandas as pd

# Defining matrix A and vector b
A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]], dtype=float)
b = np.array([7, -8, 6], dtype=float)

# Initializing values
x = np.zeros_like(b)
iterations = 9
results = []

# Jacobi Method
for i in range(iterations):
    x_new = np.zeros_like(x)
    for j in range(len(A)):
        s1 = np.dot(A[j, :j], x[:j])
        s2 = np.dot(A[j, j+1:], x[j+1:])
        x_new[j] = (b[j] - s1 - s2) / A[j, j]
    
    abs_error = np.linalg.norm(x_new - x, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x_new, ord=np.inf)
    
    results.append({
        'Iteration': i,
        'x': x_new[0],
        'y': x_new[1],
        'z': x_new[2],
        'abs': abs_error,
        'rel': rel_error
    })
    
    x = x_new

# Creating DataFrame for results
df_jacobi = pd.DataFrame(results)
print(df_jacobi)
```

### 3. Enhanced Jacobi Method

The Enhanced Jacobi Method extends the traditional Jacobi Method by incorporating a stopping criterion based on tolerance and potentially allowing for more complex matrix operations.

**Usage Example:**
```python
import numpy as np
import pandas as pd

# Defining matrix A and vector b
A = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]], dtype=float)
b = np.array([7, -8, 6], dtype=float)

# Initializing values
x = np.zeros_like(b)
tolerance = 1e-3
max_iterations = 100
results = []

# Enhanced Jacobi Method
for i in range(max_iterations):
    x_new = np.zeros_like(x)
    for j in range(len(A)):
        s1 = np.dot(A[j, :j], x[:j])
        s2 = np.dot(A[j, j+1:], x[j+1:])
        x_new[j] = (b[j] - s1 - s2) / A[j, j]
    
    abs_error = np.linalg.norm(x_new - x, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x_new, ord=np.inf)
    
    results.append({
        'Iteration': i,
        'x': x_new[0],
        'y': x_new[1],
        'z': x_new[2],
        'abs': abs_error,
        'rel': rel_error
    })
    
    if abs_error < tolerance:
        print(f'Convergence reached at iteration {i}')
        break
    
    x = x_new

# Creating DataFrame for results
df_jacobi_enhanced = pd.DataFrame(results)
print(df_jacobi_enhanced)
```

### 4. Newton's Method

Newton's Method is an iterative technique for finding successively better approximations to the roots (or zeroes) of a real-valued function. It requires the Jacobian matrix and is known for its rapid convergence near the root.

**Usage Example:**
```python
import numpy as np

def newton_method(f, J, x0, tol=1e-5, max_iter=100):
    x = x0
    for _ in range(max_iter):
        F = f(x)
        J_inv = np.linalg.inv(J(x))
        delta_x = -np.dot(J_inv, F)
        x_new = x + delta_x
        
        if np.linalg.norm(delta_x, ord=np.inf) < tol:
            return x_new
        
        x = x_new
    return x
```

### 5. Jacobian Matrix Method

This method involves solving nonlinear systems by iterating using the Jacobian matrix. It allows for the implementation of custom functions on the diagonal of the Jacobian matrix.

**Usage Example:**
```python
import numpy as np
import pandas as pd

def jacobian(x, K):
    return np.array([[-150 * np.sin(x[0]) - 2 * K, K], 
                     [K, -50 * np.sin(x[1]) - K]])

def f(x, K):
    return np.array([150 * np.cos(x[0]) + K * (x[1] - x[0]) - K * x[0], 
                     50 * np.cos(x[1]) - K * (x[1] - x[0])])

# Initializing values
x = np.array([0.5, 0.5])
K = 10
tolerance = 1e-3
max_iterations = 100
results = []

# Jacobian Method
for i in range(max_iterations):
    J = jacobian(x, K)
    F = f(x, K)
    J_inv = np.linalg.inv(J)
    delta_x = np.dot(J_inv, -F)
    x_new = x + delta_x
    
    abs_error = np.linalg.norm(x_new - x, ord=np.inf)
    rel_error = abs_error / np.linalg.norm(x, ord=np.inf)
    
    results.append({
        'Iteration': i,
        'x1': x_new[0],
        'x2': x_new[1],
        'abs': abs_error,
        'rel': rel_error
    })
    
    if abs_error < tolerance:
        print(f'Convergence reached at iteration {i}')
        break
    
    x = x_new

# Creating DataFrame for results
df_jacobian = pd.DataFrame(results)
print(df_jacobian)
```

### 6. Fixed Point Iteration

Fixed Point Iteration is used to find points that satisfy a given function, `g(x) = x`. This method requires an initial guess and iterates until convergence.

**Usage Example:**
```python
import numpy as np

def fixed_point(g, x0, tol=1e-5, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if np.abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x
```

### 7. Secant Method

The Secant Method is a root-finding algorithm that uses a sequence of roots of secant lines to approximate the root of a function. It does not require the calculation of derivatives.

**Usage Example:**

```python
import numpy as np

def secant_method(f, x0, x1, tol=1e-5, max_iter=100):
    for _ in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 == f_x0:
            raise ValueError("Division by zero in secant method")
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        if np.abs(x_new - x1) < tol:
            return x_new
        
        x0, x1 = x1, x_new
    return x_new
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.