# ☕ Flask Cafés API

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST_API-000000?logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)
![API](https://img.shields.io/badge/API-RESTful-01D277)

### RESTful API built with Flask and SQLAlchemy providing full CRUD operations and structured data management.

---

## 🚀 Features

- Get a random café

- Retrieve all cafés

- Search cafés by location

- Add new cafés

- Update coffee prices

- Delete cafés with API key protection

- JSON-based responses

- SQLite database with SQLAlchemy ORM

---

## 🧠 Tech Stack

- Python

- Flask

- SQLAlchemy

- SQLite

- REST API design

---
## ⚙️ How It Works

- Flask serves REST-style endpoints
- SQLAlchemy handles database operations
- Query parameters and form data are used for filtering and updates
- Responses are returned in JSON format
- Protected delete requests require a valid API key
---
## 📂 Project Structure

    flask-cafes-api/
    ├── main.py
    ├── .env.example
    ├── .gitignore
    ├── LICENSE
    ├── requirements.txt
    ├── README.md
    ├── instance/
    │   └── cafes.db
    └── templates/
        └── index.html

---

## ⚙️ Installation

    git clone https://github.com/fernandogrh/flask-cafes-api.git
    cd flask-cafes-api
    pip install -r requirements.txt

---

## 🔑 Environment Variables

Copy `.env.example` and rename it to `.env`, then add:

    API_KEY=your_secret_api_key
--- 
## ▶️ Run the App

    python main.py

---

## 📡 API Endpoints

### 🔹 Get Random Café
    GET /random


### 🔹 Get All Cafés
    GET /all


### 🔹 Search by Location
    GET /search?loc=London


### 🔹 Add New Café
    POST /add

Form Data Example:

    name=Cafe Nero
    map_url=https://maps.google.com
    img_url=https://image.jpg
    location=London
    seats=50
    wifi=True
    toilet=True
    sockets=True
    calls=False
    coffee_price=£2.50

### 🔹 Update Coffee Price
    PATCH /update-price/<cafe_id>

Form Data:

    new_price=£3.00


### 🔹 Delete Café (Protected)
    DELETE /delete/<cafe_id>?api-key=YOUR_API_KEY

---

## 📄 Example Response

    {
        "cafe": {
            "name": "Cafe Nero",
            "location": "London",
            "has_wifi": true,
            "coffee_price": "£2.50"
        }
    }
---


## 🧩 Key Concepts Demonstrated
- RESTful API design

- CRUD operations

- Database integration with SQLAlchemy

- Environment variable handling

- Data serialization

- HTTP status codes
---

## 📌 Notes
- This project was built for learning and portfolio purposes.
- A sample SQLite database is included for demonstration.
---

## 🧠 What I Learned

- Designing RESTful APIs with multiple HTTP methods (GET, POST, PATCH, DELETE)
- Structuring Flask applications for clean route handling
- Using SQLAlchemy ORM for database modeling and queries
- Validating user input and handling edge cases
- Implementing API key protection for sensitive endpoints
- Converting database models into JSON responses
- Improving API reliability with proper error handling and status codes
---
## 👨‍💻 Author

Built by **Fernando Ramirez**

[GitHub](https://github.com/fernandogrh)