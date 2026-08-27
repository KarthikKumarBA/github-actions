from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "local")

    return jsonify({
        "message": "GitHub Actions Demo Application",
        "environment": environment
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)