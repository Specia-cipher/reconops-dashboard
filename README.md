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

User Password Change: A secure workflow for users to update their passwords.

Nmap Scan Engine: Perform Nmap scans on any domain or IP address.

Customizable Scan Settings: Modify Nmap scan flags and timeouts from the settings page.

Dynamic Dashboard & Logging: Tracks all user actions and scan events.

API Key Management: Each user gets a unique, private API key for endpoint authentication.

Polished UI: A modern, responsive design using Tailwind CSS.

Planned Roadmap
We are currently working on the following features, with a special focus on scalability and advanced functionality:

Private REST API: Secure API endpoints for programmatic access to scan results and initiating new scans.

Dashboard Analytics: Implement real-time statistics and visualizations on the main dashboard to provide deeper insights into scan data.

Scan History and Archiving: A dedicated section to review all past scans, with the ability to filter, search, and archive results.

Scheduled Scans: Functionality to schedule Nmap scans to run automatically at specified times or intervals.

Containerization and Deployment: Complete the Docker containerization process and develop deployment guides for various environments.

Multi-User Collaboration: Enable multiple users to collaborate on projects and share scan data securely.

Installation & Setup
Prerequisites
Python 3.8+

Nmap installed on your system.

Git

Docker (for containerized deployment)

Instructions
1. Clone the repository:

git clone https://github.com/Specia-cipher/reconops-dashboard.git
cd reconops-dashboard

2. Set up a virtual environment (if not using Docker):

python3 -m venv venv
source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Initialize the database:

flask db upgrade

5. Run the application locally (if not using Docker):

python app.py

The app will be accessible at http://localhost:5000.

6. Containerization with Docker (Recommended):
Alternatively, you can build and run the application in a Docker container for a consistent, isolated environment.

Build the Docker image:

docker build -t reconops-dashboard .

Run the Docker container:

docker run -p 5000:5000 reconops-dashboard

The app will be accessible at http://localhost:5000 from your host machine.

About the Author
Specia-cipher (Sanni Idris)

GitHub: Specia-cipher

LinkedIn: Sanni Idris

Email: sannifreelancer6779@gmail.com

This project was built to showcase a passion for full-stack development, network security, and creating elegant, user-focused applications.
