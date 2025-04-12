# 🧮 Django Calculator

This is a **simple calculator web app** built using **Django** that mimics the look and functionality of a real calculator. The interface includes number buttons, basic arithmetic operators, and a display area — all styled with CSS to resemble a physical calculator.

---

## 💡 Features

- Responsive calculator UI (HTML + CSS)
- Supports basic operations:
  - ➕ Addition
  - ➖ Subtraction
  - ✖️ Multiplication
  - ➗ Division
- Input via clickable buttons (0-9, ., =, C)
- Calculation handled on the backend using Django

---

## 🛠️ Technologies Used

- **Python 3**
- **Django**
- **HTML/CSS**
- **JavaScript (optional for dynamic input handling)**

---

## 🚀 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/django-calculator.git
   ```

2. **Navigate into the project folder**
   ```bash
   cd django-calculator
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Django**
   ```bash
   pip install django
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

---


## 📁 Project Structure

```
django-calculator/
├── calculator/         # Django app
│   ├── templates/
│   │   └── calculator.html
│   └── views.py
├── static/
│   └── style.css
├── manage.py
├── db.sqlite3
└── README.md
```

---

## 📬 Feedback & Contributions

Pull requests are welcome!  
For suggestions or improvements, feel free to [open an issue](https://github.com/your-username/django-calculator/issues).

---

### Made with ❤️ using Django
