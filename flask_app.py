from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

@app.route("/add", methods=["GET"])
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"sum": a + b})

@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    return jsonify({"product": data["a"] * data["b"]})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)


# Run command: python flask_app.py