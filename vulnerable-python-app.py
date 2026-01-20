#!/usr/bin/env python3

import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# VULNERABILITY 1: Command Injection via os.system()
@app.route('/ping', methods=['POST'])
def ping_host():
    data = request.get_json()
    host = data.get('host', 'localhost')
    
    # Direct command injection vulnerability
    command = f"ping -c 4 {host}"
    result = os.system(command)
    
    return jsonify({"status": "completed", "exit_code": result})

# VULNERABILITY 2: Command Injection via subprocess with shell=True
@app.route('/nslookup', methods=['POST'])
def dns_lookup():
    data = request.get_json()
    domain = data.get('domain')
    
    # Command injection through subprocess with shell=True
    cmd = f"nslookup {domain}"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Command timed out"})

# VULNERABILITY 3: Code Injection via eval()
@app.route('/calculator', methods=['POST'])
def calculator():
    data = request.get_json()
    expression = data.get('expression')
    
    try:
        # eval() vulnerability - arbitrary code execution
        result = eval(expression)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)