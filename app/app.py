from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})
#adding this comment to check if the protection rule is working
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host -- required for container networking, app has no auth yet so low risk pre-deployment