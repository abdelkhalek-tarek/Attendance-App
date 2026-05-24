from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root123",
        database="attendance"
    )

@app.route("/")
def home():
    return jsonify({"message": "Attendance System is running"})

@app.route("/users")
def users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")
    cursor.execute("INSERT INTO users (name) VALUES ('Ahmed')")
    db.commit()

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
