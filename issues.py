import os
import json
import subprocess  
import jwt  
import hashlib

# Hardcoded credentials (Security Vulnerability)
USERNAME = "admin"
PASSWORD = "password123"

# Unused import (Code Smell)
import math  

# Function with potential SQL injection vulnerability
def authenticate_user(user, password):
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{password}'"  # SQL Injection risk
    print("Executing query:", query)  
    return True if user == USERNAME and password == PASSWORD else False

# Function with division by zero (Bug)
def divide_numbers(a, b):
    return a / b  # This will cause a ZeroDivisionError if b=0

# Function with command injection vulnerability
def run_system_command(cmd):
    subprocess.call(cmd, shell=True)  # Dangerous! Allows arbitrary command execution

# Function with Insecure Hashing Algorithm
def store_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 is insecure

# Function using JWT without verification (Security Issue)
def decode_jwt(token):
    return jwt.decode(token, options={"verify_signature": False})  # Unverified JWT decoding

# Function with unused variable (Code Smell)
def process_data(data):
    unused_var = "I am never used"  # Code Smell: Unused variable
    return json.dumps(data)

# Function with an infinite loop (Bug)
def infinite_loop():
    while True:
        print("This loop never ends!")  # Code Smell

# Calling functions with intentional issues
authenticate_user("admin", "password123")
divide_numbers(10, 0)  # Will cause ZeroDivisionError
run_system_command("rm -rf /")  # Extreme danger (DO NOT RUN THIS)
store_password("mypassword")
decode_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30=")  # Insecure JWT usage
