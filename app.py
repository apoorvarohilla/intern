from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        age INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

init_db()

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the User API!"})

# Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name, email, age = data.get("name"), data.get("email"), data.get("age")
    if not name or not email or not age:
        return jsonify({"error": "All fields (name, email, age) are required"}), 400
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return jsonify({"message": "User created successfully", "user_id": user_id}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 400

# Retrieve all users
@app.route("/users", methods=["GET"])
def get_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = [{"id": row[0], "name": row[1], "email": row[2], "age": row[3]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(users)

# Retrieve a single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify({"id": row[0], "name": row[1], "email": row[2], "age": row[3]})
    return jsonify({"error": "User not found"}), 404

# Update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    name, email, age = data.get("name"), data.get("email"), data.get("age")
    if not name or not email or not age:
        return jsonify({"error": "All fields (name, email, age) are required"}), 400
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?", (name, email, age, user_id))
    conn.commit()
    conn.close()
    if cursor.rowcount:
        return jsonify({"message": "User updated successfully"})
    return jsonify({"error": "User not found"}), 404

# Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    if cursor.rowcount:
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
