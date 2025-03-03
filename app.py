import os
import subprocess
import pickle
import sqlite3
import requests
from xml.etree.ElementTree import parse

# Hardcoded Credentials (CWE-798)
USERNAME = "admin"
PASSWORD = "password123"

# SQL Injection (CWE-89)
def get_user_info(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Vulnerable to SQL Injection
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Command Injection (CWE-78)
def run_command(user_input):
    return subprocess.run(f"echo {user_input}", shell=True)  # Unsafe usage of shell=True

# Insecure Deserialization (CWE-502)
def load_user_data(serialized_data):
    return pickle.loads(serialized_data)  # Unsafe deserialization of untrusted data

# Path Traversal (CWE-22)
def read_file(filename):
    with open(f"/etc/{filename}", "r") as f:  # Allows traversal like '../../passwd'
        return f.read()

# XXE (XML External Entity) Attack (CWE-611)
def parse_xml(xml_file):
    tree = parse(xml_file)  # No protection against external entity injection
    return tree.getroot()

# Insecure HTTP Request (CWE-829)
def fetch_data():
    response = requests.get("http://example.com/api/data")  # Uses HTTP instead of HTTPS
    return response.text

# Main function to test vulnerabilities
if __name__ == "__main__":
    print("Fetching user info (SQL Injection)...", get_user_info("1 OR 1=1"))
    print("Executing command (Command Injection)...", run_command("; rm -rf /"))
    
    # Example of insecure deserialization
    malicious_data = pickle.dumps({"username": "attacker", "role": "admin"})
    print("Loading user data (Insecure Deserialization)...", load_user_data(malicious_data))
    
    # Path Traversal Example
    print("Reading file (Path Traversal)...", read_file("../../etc/passwd"))
    
    # XML Parsing (XXE)
    print("Parsing XML (XXE)...", parse_xml("data.xml"))
    
    # Fetching data over HTTP
    print("Fetching data (Insecure HTTP Request)...", fetch_data())
