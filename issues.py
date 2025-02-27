import os
import json

# Bug: Division by zero
def divide_numbers(a, b):
    return a / b  # Potential division by zero error

# Vulnerability: Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"

def authenticate(user, pwd):
    if user == USERNAME and pwd == PASSWORD:  # Security issue: Hardcoded credentials
        return "Access Granted"
    else:
        return "Access Denied"

# Security Hotspot: Use of eval()
def execute_command(command):
    return eval(command)  # Dangerous use of eval, can lead to code injection

# Code Smell: Unused variable
def calculate_sum(numbers):
    total = 0
    unused_variable = "I am not used"  # This variable is never used
    for num in numbers:
        total += num
    return total

# Low Test Coverage Potential: Complex function with no tests
def process_data(data):
    try:
        json_data = json.loads(data)  # Code Smell: No error handling
        return json_data["value"]
    except Exception as e:
        print("Error processing data:", e)

# Duplications: Duplicate Code
def duplicate_function1(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def duplicate_function2(numbers):
    total = 0
    for num in numbers:
        total += num
    return total  # Duplicate of duplicate_function1()

# Bug: Missing return statement
def missing_return():
    x = 5  # Function does not return anything, can cause issues

# Run test cases
if __name__ == "__main__":
    print(divide_numbers(10, 0))  # This will cause a division by zero error
    print(authenticate("admin", "wrongpassword"))
    print(execute_command("2 + 2"))  # Dangerous eval execution
    print(calculate_sum([1, 2, 3, 4, 5]))
    print(process_data('{"value": 42}'))
    print(duplicate_function1([10, 20, 30]))
    print(duplicate_function2([10, 20, 30]))
