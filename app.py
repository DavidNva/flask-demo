# app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Base de datos simulada
tasks = [
    {"id": 1, "title": "Tarea 1", "completed": False},
    {"id": 2, "title": "Tarea 2", "completed": True}
]

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "message": "API is running"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/task', methods=['POST'])
def add_task():
    if not request.json or 'title' not in request.json:
        return jsonify({"error": "Title is required"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json['title'],
        "completed": False
    }
    tasks.append(new_task)
    return jsonify({"task": new_task}), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)