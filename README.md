# Valientsketchooze Marketplace

## Project Description

This project is the development repository for the Valientsketchooze digital artwork marketplace. The goal is to build a dedicated platform for showcasing and selling digital art directly to customers, starting with a Minimum Viable Product (MVP) focused on core e-commerce functionality using UPI payments.

This project follows an Agile development methodology.

## Tech Stack (MVP)

* **Backend:** Python 3.x, Django
* **Database:** PostgreSQL
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (via Django Templates)
* **Payments:** UPI (via Gateway API - TBD)
* **Environment Management:** Python `venv`
* **Dependency Management:** `pip`, `requirements.txt`
* **Secrets Management:** `python-dotenv`, `.env` file
* **Version Control:** Git

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your system:

* Python (3.8 or newer recommended) & Pip
* Git
* PostgreSQL (Database server running)

### Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/iamvarunkumar/valientsketchooze_marketplace
    cd valientsketchooze-marketplace
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    # Create the virtual environment (named 'venv')
    python -m venv venv

    # Activate the virtual environment
    # Windows:
    .\venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    ```
    *(Remember to activate the `venv` each time you work on the project in a new terminal session.)*

3.  **Install Dependencies:**
    Install all required packages listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Setup PostgreSQL Database:**
    * Ensure your PostgreSQL server is running.
    * Create a dedicated database user and database for the project. Using `psql` or a tool like pgAdmin:
        ```sql
        -- Example using psql:
        CREATE USER valientsketchooze_user WITH PASSWORD 'your_strong_password';
        CREATE DATABASE valientsketchooze_db OWNER valientsketchooze_user;
        -- Optional timezone setting (adjust as needed):
        ALTER ROLE valientsketchooze_user SET timezone TO 'Asia/Kolkata';
        ```
    * Note down the database name, username, and password.

5.  **Configure Environment Variables:**
    * Create a `.env` file in the project root directory by copying the example file:
        ```bash
        cp .env.example .env
        ```
    * **Edit the `.env` file** and replace the placeholder values with your actual database credentials and generate a new Django `SECRET_KEY`. See the **Environment Variables** section below for details.
        * **Important:** The `.env` file is listed in `.gitignore` and should **never** be committed to version control as it contains sensitive information.

6.  **Apply Database Migrations:**
    Run the initial Django migrations to set up the database schema:
    ```bash
    python manage.py migrate
    ```

7.  **Run the Development Server:**
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```
    The application should now be running at `http://127.0.0.1:8000/`.

## Environment Variables

The application requires certain environment variables to be set. These are managed using a `.env` file in the project root. Create this file based on `.env.example`.

* `SECRET_KEY`: A long, random, unique string used by Django for cryptographic signing. **Keep this secret!** You can generate one using the Python interpreter:
    ```python
    import secrets; print(secrets.token_urlsafe(50))
    ```
* `DEBUG`: Set to `True` for development (provides detailed error pages). Set to `False` in production.
* `DATABASE_URL`: The connection string for your PostgreSQL database in the format:
    `postgres://<DB_USER>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>`
    Example for local setup: `postgres://valientsketchooze_user:your_strong_password@127.0.0.1:5432/valientsketchooze_db`

*(Other variables for email, payment gateways, etc., will be added here as needed.)*

## Project Structure (Initial)
valientsketchooze-marketplace/
├── config/             # Django project settings and main URLconf
├── marketplace/        # Core application for marketplace features
├── media/              # User-uploaded files (during local development)
├── templates/          # Project-level HTML templates (to be created)
├── venv/               # Python virtual environment (ignored by Git)
├── .env                # Local environment variables (ignored by Git)
├── .env.example        # Example environment variables file (committed to Git)
├── .gitignore          # Specifies intentionally untracked files Git should ignore
├── manage.py           # Django's command-line utility
├── README.md           # This file
└── requirements.txt    # Project dependencies

## Next Steps

This README covers the initial setup. Development will proceed in sprints, focusing on implementing the features outlined in the project plan (User Auth, Artwork Management, Frontend Display, UPI Payments, etc.).
