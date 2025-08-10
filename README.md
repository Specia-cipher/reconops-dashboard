ReconOps Dashboard
A secure, modular network reconnaissance dashboard built with Flask and Tailwind CSS.

About the Project
The ReconOps Dashboard is a modern web application designed to streamline network reconnaissance. It provides a user-friendly interface for launching Nmap scans and reviewing results. This project demonstrates skills in:

Back-End Development: Secure user authentication, database management with Flask-SQLAlchemy, and external tool integration.

Front-End Design: A sleek, responsive user interface built with Tailwind CSS.

Security Best Practices: Implementation of CSRF protection, secure password hashing, and user-specific access controls.

API Development: Foundations for a private REST API.

Key Features
Secure Authentication: Complete user registration, login, and logout flows with secure password hashing.

Nmap Scan Engine: Perform Nmap scans on any domain or IP address.

Customizable Scan Settings: Modify Nmap scan flags and timeouts from the settings page.

Dynamic Dashboard & Logging: Tracks all user actions and scan events.

API Key Management: Each user gets a unique, private API key for endpoint authentication.

Polished UI: A modern, responsive design using Tailwind CSS.

Planned Roadmap
We are currently working on the following features:

User Password Change: A secure workflow for users to update their passwords.

Dashboard Analytics: Real-time statistics and visualizations on the main dashboard.

Private REST API: Secure API endpoints for programmatic access to scan results.

Installation & Setup
Prerequisites
Python 3.8+

Nmap installed on your system.

Git

Instructions
Clone the repository:
git clone https://github.com/Specia-cipher/reconops-dashboard.git
cd reconops-dashboard

Set up a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Initialize the database:
flask db upgrade

Run the application:
python app.py

The app will be accessible at http://localhost:5000.

About the Author
Specia-cipher (Sanni Idris)

GitHub: Specia-cipher

LinkedIn: Sanni Idris

Email: sannifreelancer6779@gmail.com

This project was built to showcase a passion for full-stack development, network security, and creating elegant, user-focused applications.
