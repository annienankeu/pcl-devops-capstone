# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Congratulations! You Have Successfully Deployed Your Flask App."

# @app.route("/health")
# def health():
#     return {"status": "healthy"}

# @app.route("/tasks")
# def tasks():
#     data = [
#         {"id":1,"task":"Learn Docker"},
#         {"id":2,"task":"Learn Jenkins"},
#         {"id":3,"task":"Learn Kubernetes"}
#     ]
#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# =========================
# DATABASE CONNECTION
# =========================
def get_db_connection():
    return mysql.connector.connect(
        host="db",              # Docker service name from docker-compose
        user="user",
        password="password",
        database="capstone"
    )

# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    return "Congratulations! You Have Successfully Deployed Your Flask App with Docker + MySQL."

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/tasks")
def tasks():
    data = [
        {"id": 1, "task": "Learn Docker"},
        {"id": 2, "task": "Learn Jenkins"},
        {"id": 3, "task": "Learn Kubernetes"}
    ]
    return jsonify(data)

# =========================
# MYSQL TEST ROUTE
# =========================
@app.route("/db-test")
def db_test():
    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT 'MySQL Connected Successfully'")
        result = cursor.fetchone()

        cursor.close()
        db.close()

        return {"message": result[0]}

    except Exception as e:
        return {"error": str(e)}

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)