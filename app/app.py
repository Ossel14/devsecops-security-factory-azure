import os
from flask import Flask, jsonify, request

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY", "dev-only-placeholder-key")


def require_api_key(f):
    def wrapper(*args, **kwargs):
        key = request.headers.get("X-API-Key")
        if key != API_KEY:
            return jsonify({"error": "unauthorized"}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/secure-data")
@require_api_key
def secure_data():
    return jsonify({"message": "this is protected content"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host -- required for container networking, low risk pre-deployment