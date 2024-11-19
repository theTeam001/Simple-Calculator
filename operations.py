# Operations.py

import math

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract the second number from the first."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide the first number by the second."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def modulus(x, y):
    """Return the remainder of the division of x by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x % y

def power(x, y):
    """Raise x to the power of y."""
    return x ** y

def sqrt(x):
    """Return the square root of x."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number!")
    return math.sqrt(x)

def log(x, base=10):
    """Return the logarithm of x to the given base (default is base 10)."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values!")
    if base <= 1:
        raise ValueError("Logarithm base must be greater than 1.")
    return math.log(x, base)

def power_of_10(x):
    """Return 10 raised to the power of x."""
    return 10 ** x
