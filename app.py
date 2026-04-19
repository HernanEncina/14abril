from flask import Flask, request, jsonify, send_from_directory
import datetime
import os

app = Flask(__name__)

LOG_FILE = "backup.log"

def log_action(action):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {action}\n")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/calc", methods=["POST"])
def calc():
    data = request.json
    a = int(data["a"])
    b = int(data["b"])
    op = data["op"]

    result = None

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b

    log_action(f"Arithmetic: {a} {op} {b} = {result}")
    return jsonify(result=result)

@app.route("/binary", methods=["POST"])
def binary():
    data = request.json
    num = int(data["num"])
    result = bin(num)

    log_action(f"Binary: {num} -> {result}")
    return jsonify(result=result)

@app.route("/logic", methods=["POST"])
def logic():
    data = request.json
    a = int(data["a"])
    b = int(data["b"])
    op = data["op"]

    if op == "AND":
        result = a & b
    elif op == "OR":
        result = a | b
    elif op == "XOR":
        result = a ^ b

    log_action(f"Logic: {a} {op} {b} = {result}")
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6767)