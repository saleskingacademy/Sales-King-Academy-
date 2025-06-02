
from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    if payload:
        print("GitHub push received. Triggering build sequence.")
        return jsonify({"status": "Webhook triggered, command bridge activated"}), 200
    return jsonify({"error": "No payload received"}), 400

@app.route('/frontend', methods=['GET'])
def frontend():
    return "Sales King Academy front-end interface ready."

@app.route('/command', methods=['POST'])
def command_bridge():
    data = request.json
    if data and 'command' in data:
        cmd = data['command']
        print(f"AI Command Received: {cmd}")
        return jsonify({"executed": cmd}), 200
    return jsonify({"error": "No command provided"}), 400

@app.route('/backend', methods=['POST'])
def backend():
    data = request.json
    print(f"Backend data received: {data}")
    return jsonify({"status": "Backend triggered"}), 200

@app.route('/', methods=['GET'])
def index():
    return "Sales King Academy AI Command System Active."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
