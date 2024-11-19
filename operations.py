# Operations.py

import math
import random

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

def sin(x):
    """Return the sine of x (x in radians)."""
    return math.sin(x)

def cos(x):
    """Return the cosine of x (x in radians)."""
    return math.cos(x)

def tan(x):
    """Return the tangent of x (x in radians)."""
    return math.tan(x)

def asin(x):
    """Return the arcsine of x (x is in the range [-1, 1])."""
    if x < -1 or x > 1:
        raise ValueError("Arcsine is undefined for values outside the range [-1, 1].")
    return math.asin(x)

def acos(x):
    """Return the arccosine of x (x is in the range [-1, 1])."""
    if x < -1 or x > 1:
        raise ValueError("Arccosine is undefined for values outside the range [-1, 1].")
    return math.acos(x)

def atan(x):
    """Return the arctangent of x."""
    return math.atan(x)

def exp(x):
    """Return e raised to the power of x."""
    return math.exp(x)

def factorial(x):
    """Return the factorial of x."""
    if x < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    return math.factorial(x)

def combinations(n, r):
    """Return the number of combinations (n choose r)."""
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative integers.")
    if r > n:
        raise ValueError("r cannot be greater than n.")
    return math.comb(n, r)

def permutations(n, r):
    """Return the number of permutations (n permute r)."""
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative integers.")
    if r > n:
        raise ValueError("r cannot be greater than n.")
    return math.perm(n, r)

def round_to(x, digits=0):
    """Return x rounded to the specified number of decimal places (default is 0)."""
    return round(x, digits)

def abs_value(x):
    """Return the absolute value of x."""
    return abs(x)

def rand_int(low, high):
    """Return a random integer between low and high (inclusive)."""
    if low > high:
        raise ValueError("Low must be less than or equal to high.")
    return random.randint(low, high)

def rand_float(low, high):
    """Return a random floating-point number between low and high."""
    if low > high:
        raise ValueError("Low must be less than or equal to high.")
    return random.uniform(low, high)

def rand_choice(sequence):
    """Return a random element from a non-empty sequence."""
    if not sequence:
        raise ValueError("Sequence must not be empty.")
    return random.choice(sequence)

def deg_to_rad(degrees):
    """Convert degrees to radians."""
    return math.radians(degrees)

def rad_to_deg(radians):
    """Convert radians to degrees."""
    return math.degrees(radians)
