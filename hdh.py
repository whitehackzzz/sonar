# Example of SQL Injection in Python
import sqlite3

def sql_injection_example():
    user_input = "' OR 1=1 --"
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    # Vulnerable SQL query with user input directly concatenated
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    for row in results:
        print(f"User: {row[0]}")
    
    connection.close()

# Example of Cross-Site Scripting (XSS) in Python (Flask Web App)
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET'])
def xss_example():
    user_input = request.args.get('user_input')
    # Vulnerable to XSS, as user input is reflected without sanitization
    return f"<h1>User Input: {user_input}</h1>"

# Example of Insecure File Handling
import os

def insecure_file_handling_example():
    file_path = "/etc/passwd"  # Sensitive system file
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            print(file.read())

# Example of Hardcoded Credentials
def hardcoded_credentials_example():
    username = "admin"  # Hardcoded username
    password = "password123"  # Hardcoded password

    if username == "admin" and password == "password123":
        print("Access granted")
    else:
        print("Access denied")

# Running examples
if __name__ == '__main__':
    sql_injection_example()
    app.run(debug=True)  # Run Flask app for XSS
    insecure_file_handling_example()
    hardcoded_credentials_example()
