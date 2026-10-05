# NotesManagement---Django
A simple and user-friendly **Notes Management System** built using **Django**.  
This application allows students to create, view, edit, and delete study notes based on different subjects and topics.

The project is designed to help students organize their preparation material in one place.

---

## ✨ Features

- 🏠 Attractive Home Page
- ➕ Add new notes
- 📖 View all notes
- 👁️ View complete question and answer
- ✏️ Edit existing notes
- 🗑️ Delete notes
- 🔍 Organize notes by language/subject
- 📝 Store questions and answers
- 💬 Success and error messages
- 🎨 Clean and professional UI
- 📱 Simple and easy-to-use interface

---

## 📚 Subjects Covered

The application can be used to prepare notes for different subjects such as:

- 🐍 Python
- 📊 Data Analytics
- ⚡ JavaScript
- 🌐 HTML
- 🎨 CSS

More subjects can easily be added later.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Django | Web Framework |
| HTML | Page Structure |
| CSS | Styling |
| SQLite | Database |
| Git | Version Control |
| GitHub | Source Code Management |

---

## 🏗️ Project Structure

```text
NotesManagement/
│
├── manage.py
│
├── myapp/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── practice/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── home.html
│   ├── notes.html
│   ├── addnote.html
│   ├── editnote.html
│   └── viewnote.html
│
├── static/
│   └── ...
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Suprajabayya/NotesManagement---Django.git
```

### 2. Open the Project

```bash
cd NotesManagement---Django
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

---

## 📦 Install Django

```bash
pip install django
```

---

## 🗄️ Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 👤 Create Superuser

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Enter your:

```text
Username
Email
Password
```

---

## ▶️ Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 🔄 Application Workflow

```text
             🏠 Home
                │
                ▼
          📖 My Notes
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
    👁 View   ✏️ Edit   🗑 Delete
       │
       ▼
  Question + Answer


             🏠 Home
                │
                ▼
           ➕ Add Note
                │
                ▼
        Select Subject
                │
                ▼
          Enter Topic
                │
                ▼
        Enter Question
                │
                ▼
         Enter Answer
                │
                ▼
           💾 Save Note
                │
                ▼
          📖 My Notes
```

---

## 📝 Note Structure

Each note contains:

```text
Language
    ↓
Topic
    ↓
Question
    ↓
Answer
```

### Example

```text
Language: Python

Topic: Lists

Question:
What is a list in Python?

Answer:
A list is an ordered and mutable collection
that can store multiple values.
```

---

## 🔧 CRUD Operations

The application implements the basic **CRUD operations**:

### Create

Students can create a new note by entering:

- Language
- Topic
- Question
- Answer

### Read

Students can:

- View all notes
- View a complete individual note

### Update

Students can edit existing:

- Language
- Topic
- Question
- Answer

### Delete

Students can delete unwanted notes.

---

## 🧩 Django Concepts Used

This project demonstrates important Django concepts:

- Django Project
- Django Application
- MVT Architecture
- URL Routing
- Views
- Templates
- Template Tags
- Models
- ORM
- CRUD Operations
- Forms
- GET and POST requests
- `render()`
- `redirect()`
- Django Messages
- CSRF Token
- Static Files
- Django Admin
- Migrations
- Superuser

---

## 🏛️ MVT Architecture

```text
User
 │
 ▼
URL
 │
 ▼
View
 │
 ├──────────────► Model
 │                  │
 │                  ▼
 │               Database
 │
 ▼
Template
 │
 ▼
HTML Response
 │
 ▼
User
```

### Model

Handles database-related operations.

### View

Contains the application logic and communicates between the model and template.

### Template

Displays the information to the user using HTML and Django Template Language.

---

## 🔐 Admin Panel

The Django admin panel can be accessed using:

```text
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials created with:

```bash
python manage.py createsuperuser
```

---

## 🚀 Future Enhancements

The project can be extended with:

- 🔎 Search notes
- 🏷️ Filter notes by subject
- 📌 Favorite notes
- 📊 Dashboard with note statistics
- 👤 User registration and login
- 🔐 User-specific notes
- 📄 Export notes as PDF
- 🌙 Dark mode
- 📱 Improved mobile responsiveness
- 🤖 AI-based question generation
- 🧠 AI-based answer suggestions

---

## 🎯 Project Objective

The main objective of this project is to provide students with a simple platform to **create, organize, revise, and manage technical study notes**.

It also demonstrates practical implementation of **Django MVT architecture and CRUD operations**.

---

## 👩‍💻 Author

**Supraja Bayya**

Computer Science and Engineering Graduate

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📌 GitHub Repository

[Notes Management – Django](https://github.com/Suprajabayya/NotesManagement---Django)
