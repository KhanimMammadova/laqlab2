import numpy as np

def compute_z(x, a, b):
    if a == b:
        return 9 * x**2 + b
    elif a > b:
        return 8 * x - a
    else:  
        return 7 * a**2 + b
b_values = np.arange(1, 2.1, 0.1)
x = 2  
a = 1.5
for b in b_values:
    z = compute_z(x, a, b)
    print(f"b = {b:.1f}, z = {z}")
