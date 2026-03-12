from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Congratulations! You Have Successfully Deployed Your Flask App."

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/tasks")
def tasks():
    data = [
        {"id":1,"task":"Learn Docker"},
        {"id":2,"task":"Learn Jenkins"},
        {"id":3,"task":"Learn Kubernetes"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
