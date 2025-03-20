# 💻 Flask CRUD API with SQLite

This is a simple REST API built using **Flask** and **SQLite** for basic CRUD (Create, Read, Update, Delete) operations on user data.

## 🔍 Features
- Create a User
- Retrieve All Users
- Retrieve a User by ID
- Update a User
- Delete a User
- Proper Error Handling
- JSON Responses

## 🚀 Getting Started

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/flask-crud-api.git
cd flask-crud-api
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the Application
```sh
python app.py
```
The API will be available at: **http://127.0.0.1:5000**

---

## 📌 API Endpoints

### 🟢 Create a User  
**Endpoint:** `POST /users`  
**Request Body (JSON):**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 25
}
```
**Response (201 Created):**
```json
{
  "message": "User created successfully",
  "user_id": 1
}
```

---

### 🔵 Get All Users  
**Endpoint:** `GET /users`  
**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 25
  }
]
```

---

### 🟡 Get User by ID  
**Endpoint:** `GET /users/{user_id}`  
**Example Request:** `GET /users/1`  
**Response (200 OK):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "age": 25
}
```
**Error (404 Not Found):**
```json
{
  "error": "User not found"
}
```

---

### 🛠️ Update a User  
**Endpoint:** `PUT /users/{user_id}`  
**Example Request:** `PUT /users/1`  
**Request Body (JSON):**
```json
{
  "name": "John Updated",
  "email": "john.updated@example.com",
  "age": 26
}
```
**Response (200 OK):**
```json
{
  "message": "User updated successfully"
}
```
**Error (404 Not Found):**
```json
{
  "error": "User not found"
}
```

---

### 🟥 Delete a User  
**Endpoint:** `DELETE /users/{user_id}`  
**Example Request:** `DELETE /users/1`  
**Response (200 OK):**
```json
{
  "message": "User deleted successfully"
}
```
**Error (404 Not Found):**
```json
{
  "error": "User not found"
}
```

---

## 🛠️ Technologies Used
- **Python 3**
- **Flask**
- **SQLite**
- **Postman** (For testing API)

## 📓 Notes
- This API is meant for educational/demo purposes.
- The database is stored locally (`users.db`).
- Ensure that the Flask app is running before making API requests.

---

## 🏆 Contribution
Feel free to submit issues or create pull requests to improve this project.  

### 📩 Contact  
If you have any questions, feel free to reach out!

---

### 🔠 Happy Coding! 🚀

