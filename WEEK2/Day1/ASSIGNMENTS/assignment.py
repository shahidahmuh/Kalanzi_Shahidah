"""
Error-Proof Calculator
A calculator that never crashes, explained the easy way.
"""


# STEP 1: A custom error type
# This is just a label we made up. It works exactly like Python's
# built-in errors (ValueError, TypeError, etc.) but we get to name it
# whatever we want, so the error message is clearer.

class InvalidInputError(Exception):
    pass


# STEP 2: A decorator that checks the inputs are numbers
# A decorator is just a function that wraps another function.
# Think of it like a security guard standing in front of a door:
# before letting you through to the real function, it checks your ID.

def validate_inputs(func):
    def wrapper(a, b):
        # Check both inputs. If either one is NOT a number, stop here.
        for value in (a, b):
            if not isinstance(value, (int, float)):
                return f"Error: '{value}' is not a number."
        # Both inputs are fine -> let the real function run.
        return func(a, b)
    wrapper.__name__ = func.__name__  # keep the original name for logging
    return wrapper


# STEP 3: A decorator that catches division by zero
# try/except is just "attempt this, and if it breaks in this
# specific way, do something safe instead of crashing."

def safe_divide(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Infinity"
    wrapper.__name__ = func.__name__  # keep the original name for logging
    return wrapper


# STEP 4: A decorator that writes every call to log.txt

def log_call(func):
    name = func.__name__  # grab the real name BEFORE we wrap it
    def wrapper(a, b):
        result = func(a, b)
        with open("log.txt", "a") as f:
            f.write(f"{name}({a}, {b}) = {result}\n")
        return result
    return wrapper


# STEP 5: The actual math functions
# Decorators stack like layers. Reading top to bottom, each one
# wraps the one below it. So for divide:
#   log_call wraps validate_inputs wraps safe_divide wraps the real division.

@log_call
@validate_inputs
def add(a, b):
    return a + b

@log_call
@validate_inputs
def subtract(a, b):
    return a - b

@log_call
@validate_inputs
def multiply(a, b):
    return a * b

@log_call
@validate_inputs
@safe_divide
def divide(a, b):
    return a / b


# STEP 6: Test it - try to break it on purpose


if __name__ == "__main__":
    print(add(2, 3))            # 5
    print(subtract(10, 4))      # 6
    print(multiply(3, 7))       # 21
    print(divide(9, 3))         # 3.0
    print(divide(5, 0))         # Infinity  (would normally crash!)
    print(add("hello", 3))      # Error message (would normally crash!)
    print(multiply(None, 2))    # Error message (would normally crash!)

    print("\nNothing crashed. Check log.txt for the full history.")