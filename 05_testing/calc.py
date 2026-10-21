"""
Calculator utility module demonstrating typed operations and error boundaries.
"""

def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Subtract y from x."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y

# Backward compatibility alias
multipy = multiply

def divide(x: float, y: float) -> float:
    """Divide x by y. Raises ValueError on division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def power(base: float, exponent: float) -> float:
    """Raise base to exponent."""
    return base ** exponent
