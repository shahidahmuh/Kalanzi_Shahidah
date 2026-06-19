# calculator.py

# Custom Error + Input Checker

class InvalidInputError(Exception):
    pass

def check_inputs(a, b):
    if not isinstance(a, (int, float)):
        raise InvalidInputError(f"'{a}' is not a number!")
    if not isinstance(b, (int, float)):
        raise InvalidInputError(f"'{b}' is not a number!")


# Safe Divide + Logging

def safe_divide(a, b):
    if b == 0:
        return "Infinity"
    return a / b

def log_to_file(operation, a, b, result):
    file = open("log.txt", "a")
    file.write(f"{operation}({a}, {b}) = {result}\n")
    file.close()


# Add and Subtract

def add(a, b):
    check_inputs(a, b)
    result = a + b
    log_to_file("add", a, b, result)
    return result

def subtract(a, b):
    check_inputs(a, b)
    result = a - b
    log_to_file("subtract", a, b, result)
    return result


# Multiply and Divide

def multiply(a, b):
    check_inputs(a, b)
    result = a * b
    log_to_file("multiply", a, b, result)
    return result

def divide(a, b):
    check_inputs(a, b)
    result = safe_divide(a, b)
    log_to_file("divide", a, b, result)
    return result


# Main Program

print("Welcome to the Error-Proof Calculator!")
print("Type 1. 'quit' to 2. stop.\n")

while True:

    print("Choose: add / subtract / multiply / divide")
    operation = input("Your choice: ")

    if operation == "1":
        print("Goodbye!")
        break

    a = input("Enter first number: ")
    b = input("Enter second number: ")

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Please type actual numbers!\n")
        continue

    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            print("Unknown operation!\n")
            continue

        print(f"Answer: {result}\n")

    except InvalidInputError as e:
        print(f"Input Error: {e}\n")