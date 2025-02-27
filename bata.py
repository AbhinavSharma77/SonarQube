import os
import json
import hashlib
import subprocess

# Bug 1: Division by zero
def divide_numbers(a, b):
    return a / b  # Bug: Potential division by zero

# Bug 2: Referencing an undefined variable
def undefined_variable():
    return x + 5  # Bug: x is not defined

# Bug 3: Infinite loop
def infinite_loop():
    while True:  # Bug: Loop never terminates
        print("Looping...")

# Vulnerability 1: Hardcoded credentials
USERNAME = "admin"
PASSWORD = "supersecretpassword"  # Hardcoded password

def authenticate(user, pwd):
    if user == USERNAME and pwd == PASSWORD:  # Vulnerability
        return "Access Granted"
    else:
        return "Access Denied"

# Vulnerability 2: Command Injection
def execute_system_command(cmd):
    os.system(cmd)  # Vulnerability: Direct command execution

# Security Hotspot 1: Insecure Hashing Algorithm
def insecure_hashing(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 is weak and should not be used

# Security Hotspot 2: Dangerous eval() usage
def dangerous_eval(user_input):
    return eval(user_input)  # Security issue: Eval can be exploited

# Code Smell 1: Unused variable
def unused_variable_example():
    unused = "I am never used"  # This variable is never used
    return 42

# Code Smell 2: Function does too many things
def complex_function(data):
    try:
        json_data = json.loads(data)
        result = json_data.get("key", "default")
        print("Processing data:", result)
        os.system("echo Done")  # Mixed responsibilities (Bad practice)
        return result
    except Exception as e:
        print("Error:", e)

# Duplications: Identical code blocks
def duplicate_function1(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def duplicate_function2(numbers):
    total = 0
    for num in numbers:
        total += num
    return total  # Exact duplicate of duplicate_function1()

# Low Coverage Potential: No tests written
def risky_math_operation(a, b):
    if a > 10:
        return a * b
    elif b == 0:
        print("Warning: Division by zero")  # No exception raised
    else:
        return a / b  # Potential bug not handled

# Bug: Function missing a return value
def missing_return():
    x = 5  # No return statement

# Run test cases
if __name__ == "__main__":
    print(divide_numbers(10, 0))  # Bug: Division by zero
    print(undefined_variable())   # Bug: Undefined variable
    # infinite_loop()  # Uncomment to see infinite loop in action (bug)

    print(authenticate("admin", "wrongpassword"))  # Hardcoded credentials issue
    execute_system_command("ls")  # Command injection vulnerability
    print(insecure_hashing("password123"))  # Security issue: MD5 hashing
    print(dangerous_eval("2 + 2"))  # Security issue: Eval execution

    print(unused_variable_example())  # Unused variable
    print(complex_function('{"key": "value"}'))  # Code Smell

    print(duplicate_function1([10, 20, 30]))
    print(duplicate_function2([10, 20, 30]))  # Duplicate function

    print(risky_math_operation(20, 0))  # Low test coverage
    print(missing_return())  # Bug: No return value
