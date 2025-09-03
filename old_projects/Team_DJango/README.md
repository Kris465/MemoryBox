# TEAM_DJANGO-1 Project

This project is a full-fledged Django application with two sub-applications: a blog and a shop. It includes a CAPTCHA entry point for bot verification and a transition page.

## Structure:
- `myproject/`: Main Django project configuration (settings, URLs).
- `blog/`: Django application for the blog with models, views, templates, and static files.
- `shop/`: Django application for the shop with models, views, templates, and static files.
- `templates/`: Project-level templates (base, index, firstpage).
- `static/`: Project-level static files (firts.css, firts.js, fonts).
- `media/`: Directory for user-uploaded media files (e.g., blog post images).

## Getting Started:

### 1. **Setup Python Environment (RECOMMENDED: Python 3.11):**

**Reason for Python 3.11:** You are currently encountering a `ValueError: Unable to configure formatter 'django.server'` and `AttributeError: module 'string' has no attribute 'formatter_parser'` errors. These are known incompatibilities between Django's logging system and changes introduced in Python 3.12. Using Python 3.11 will resolve these issues.

**How to Install Python 3.11 (if not already installed):**
* **Windows:** Download the installer from the official Python website: [https://www.python.org/downloads/release/python-3118/](https://www.python.org/downloads/release/python-3118/). Make sure to check "Add Python 3.11 to PATH" during installation.
* **macOS (using Homebrew):**
    ```bash
    brew install python@3.11
    ```
* **Linux (using `deadsnakes` PPA for Ubuntu/Debian):
    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.11 python3.11-venv
    ```

**Create and Activate Virtual Environment with Python 3.11:**
After installing Python 3.11, create a new virtual environment explicitly using `python3.11`:
```bash
# Delete the old project directory to start fresh
rmdir /s /q TEAM_DJANGO-1  # On Windows
# rm -rf TEAM_DJANGO-1    # On macOS/Linux

# Re-run the setup_project.py script (you just did this, so it will recreate the directory)
python C:\4chan\.GITHUB\Team_DJango\setup_project.py

# Navigate into the newly created project directory
cd TEAM_DJANGO-1

# Create a virtual environment using Python 3.11
python3.11 -m venv venv
# If 'python3.11' is not found, try 'py -3.11 -m venv venv' on Windows,
# or specify the full path like 'C:\Python311\python.exe -m venv venv'

# Activate the virtual environment
# On Windows:
.venv/Scripts/activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. **Install Django and other dependencies within the Python 3.11 venv:**
Once your Python 3.11 virtual environment is activated (you'll see `(venv)` at the beginning of your prompt), install Django:
```bash
pip install Django
```

### 3. **Apply Database Migrations:**
This creates the necessary database tables for your Django models (Posts, Products, Users).
```bash
python manage.py makemigrations blog
python manage.py makemigrations shop
python manage.py migrate
```

### 4. **Create a Superuser (for Admin Panel access):**
You'll need this to access the Django administration panel and add blog posts/products.
```bash
python manage.py createsuperuser
```
Follow the prompts to create a username, email, and password.

### 5. **Run the Django Development Server:**
```bash
python manage.py runserver
```

### 6. **Access the Application:**
- **CAPTCHA Page:** Open `http://127.0.0.1:8000/` in your browser.
- **Django Admin Panel:** Open `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you just created. From here, you can add `Posts` for the blog and `Products` for the shop.

## Bot Verification (CAPTCHA):
The CAPTCHA is now handled on the server-side by Django. The code for the CAPTCHA is dynamically generated and validated on the backend, making it impossible to bypass simply by manipulating client-side JavaScript. Each failed attempt generates a new CAPTCHA.

## Admin Panel Features:
- **Blog Posts:** Add, edit, and delete blog posts directly through the Django admin interface.
- **Shop Products:** Add, edit, and delete products for the shop.
- **User Management:** Django's built-in user management allows you to create, edit, and manage users and their permissions.

Enjoy your full-featured Django project!
