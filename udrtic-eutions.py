import numpy as np

def find_quartic_roots(a, b, c, d, e):
    # Define the coefficients
    coefficients = [a, b, c, d, e]
    
    # Find roots using numpy
    roots = np.roots(coefficients)
    
    return roots

# Example usage:
a, b, c, d, e = 1, -4, 6, -4, 1  # (x - 1)^4 = 0
roots = find_quartic_roots(a, b, c, d, e)

print("Roots of the quartic equation:")
for root in roots:
    print(root)
