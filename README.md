🛡️ ReconOps Dashboard
A secure, modular network reconnaissance dashboard built with Flask and Tailwind CSS.
🎯 About the Project
The ReconOps Dashboard is a modern web application designed to streamline network reconnaissance. Built with a focus on security, extensibility, and clean architecture, it provides a user-friendly interface for launching Nmap scans and reviewing results. This project serves as a comprehensive demonstration of full-stack development skills, including:

Robust Back-End Development: Secure user authentication, database management with Flask-SQLAlchemy, and integration of external command-line tools.

Modern Front-End Design: A sleek, responsive user interface built with Tailwind CSS, ensuring a professional and consistent experience on any device.

Security Best Practices: Implementation of CSRF protection, secure password hashing, and user-specific access controls.

API Development: Foundations for a private REST API, demonstrating an understanding of service-oriented architecture.

✨ Key Features
🔒 Secure Authentication & Authorization:

Complete user registration, login, and logout flows.

Secure password storage using Bcrypt.

Session management with Flask-Login and robust CSRF protection with Flask-WTF.

🕵️ Nmap Scan Engine:

Perform Nmap scans on any domain or IP address directly from the dashboard.

All scan results are stored persistently for historical review and auditing.

⚙️ Customizable Scan Settings:

Allows users to modify Nmap scan flags and timeouts from the settings page.

This feature demonstrates an extensible backend design and provides granular control for the user.

📊 Dynamic Dashboard & Logging:

Centralized system logs track all user actions and scan events.

A clean, intuitive dashboard provides a snapshot of recent activity.

🔑 API Key Management:

Each user is assigned a unique, private API key for future endpoint authentication.

Securely view, copy, and regenerate API keys from the account settings.

🎨 Polished UI:

A modern, responsive design using Tailwind CSS for a premium look and feel.

User-specific UI elements and seamless navigation for a great user experience.

🚀 Planned Roadmap
This project is in active development with a clear roadmap to enhance its functionality and production readiness.

Next Major Features (In Progress)
User Password Change: Implement a secure workflow for users to update their passwords.

Dashboard Analytics: Add real-time statistics and visualizations to the main dashboard.

Private REST API: Develop secure API endpoints for programmatic access to scan results.

Long-Term Enhancements
Result Export: Add functionality to export scan results to common formats like CSV or JSON.

Dockerization: Containerize the application for easy, consistent deployment across environments.

🛠️ Installation & Setup
Prerequisites
Python 3.8+

Nmap installed and available in your system's PATH.

Git

Instructions
Clone the repository:

Bash

git clone https://github.com/Specia-cipher/reconops-dashboard.git
cd reconops-dashboard
Set up a virtual environment:

Bash

python3 -m venv venv
source venv/bin/activate
Install dependencies:

Bash

pip install -r requirements.txt
Initialize the database:

Bash

flask db upgrade
Run the application:

Bash

python app.py
The application will be accessible at http://localhost:5000.

📂 Project Structure
reconops-dashboard/
│
├── app.py                      # Main application entry point
├── requirements.txt            # Project dependencies
│
├── reconops_dashboard/
│   ├── __init__.py             # Application factory and configuration
│   ├── models.py               # Database models (User, ScanResult)
│   ├── routes/                 # Flask blueprints for different route groups
│   ├── templates/              # HTML templates (Jinja2)
│   ├── static/                 # CSS, images, and JavaScript files
│   └── utils/                  # Helper modules for scanning, logging, etc.
│
└── instance/
    └── reconops.db             # SQLite database file
🤝 Contributing
Contributions, issues, and feature requests are welcome!

📜 License
This project is licensed under the MIT License.

👤 About the Author
Specia-cipher (Sanni Idris)

GitHub: Specia-cipher

LinkedIn: Sanni Idris

Email: sannifreelancer6779@gmail.com

This project was built to showcase a passion for full-stack development, network security, and creating elegant, user-focused applications.

