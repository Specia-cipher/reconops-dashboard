# ReconOps Dashboard

![ReconOps Logo](https://user-images.githubusercontent.com/your-github-username/reconops-dashboard-logo.png)

_A modular network reconnaissance web app built with Flask, Flask-WTF, and Bootstrap 5._

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Planned Roadmap](#planned-roadmap)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [About the Author](#about-the-author)

---

## About

ReconOps Dashboard is a network reconnaissance utility that provides a user-friendly web interface for initiating and viewing Nmap scan results and system logs. Designed with modularity and security at its core, ReconOps aims to serve as a foundation for exploring modern back-end, security, and deployment workflows.

---

## Features

- **CSRF-Protected Flask-WTF Forms:**  
  Ensures every web form is secure against CSRF attacks.

- **Nmap Scan Integration:**  
  Quickly perform Nmap scans on domains/IPs and view the output directly in the dashboard.

- **Persistent Scan Records:**  
  All scan results are stored in a database with timestamps for audit purposes.

- **System Logging:**  
  Tracks user actions and scan events for basic auditing.

- **Responsive UI with Bootstrap 5:**  
  Clean interface for laptops and mobile devices.

---

## Planned Roadmap

We will focus on implementing the following key features in the next phases of development. This roadmap demonstrates an understanding of real-world workflows and highlights skills relevant to employers.

### Next Major Features (In Active Development)

| Feature                  | Why It Matters                                       | Timeline       |
|--------------------------|------------------------------------------------------|----------------|
| **User Authentication**  | Realistic access control & user management            | Next major     |
| **Scan History per User**| Data persistence and personalized audit trail         | In progress    |
| **Result Export (CSV/JSON)** | Provides practical server-side file handling and reporting | Near future    |
| **Dockerization**         | Modern deployment practices and environment consistency | Near future    |

### Near-Future & Optional Enhancements

| Feature                     | Value to Employers and Users                           | Timeline  |
|-----------------------------|--------------------------------------------------------|-----------|
| **Advanced Scan Options**   | UI and backend flexibility allowing customized scans  | Optional  |
| **Simple REST API Endpoints**| Backend extensibility, service-oriented architecture  | Optional  |
| **Enhanced Audit Logging**  | Improved monitoring, security, and operational insight | Stretch   |
| **Custom User Settings**     | User experience enhancement and application extensibility | Stretch   |

---

## Installation

### Prerequisites

- Python 3.8+ (recommended: venv)
- pip
- [Nmap](https://nmap.org/download.html) installed on your system
- Git

### Steps

git clone https://github.com/Specia-cipher/reconops-dashboard.git
cd reconops-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Configure your .env or environment variables if needed
flask db upgrade # Sets up the database
python app.py

text

Access the app at [http://localhost:5000](http://localhost:5000)

---

## Usage

- Enter a target IP or domain and click "Run Scan"
- View scan results and logs via navigation links
- All user actions and scan records are saved for traceability

*Note: After planned authentication is added, features will become user-dependent!*

---

## Project Structure

reconops-dashboard/
│
├── app.py
├── requirements.txt
├── reconops_dashboard/
│ ├── init.py
│ ├── models.py
│ ├── routes/
│ │ ├── main_routes.py
│ │ └── settings_routes.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── scan.html
│ │ ├── results.html
│ │ ├── logs.html
│ │ └── settings.html
│ ├── utils/
│ │ ├── scan_engine.py
│ │ ├── forms.py
│ │ ├── db_helper.py
│ │ ├── log_helper.py
│ │ └── settings_helper.py
│ └── static/
└── instance/
└── reconops.db

text

---

## Contributing

Pull requests and feedback are welcome!  
See [CONTRIBUTING.md](https://github.com/Specia-cipher/reconops-dashboard/blob/main/CONTRIBUTING.md) for details.

---

## License

This project is licensed under the MIT License.

---

## About the Author

**Specia-cipher (gen-cipher)**  
- GitHub: [Specia-cipher](https://github.com/Specia-cipher)  
- Email: [your.email@example.com]  
- Project assembled with a focus on robust back-end design, security, and real-world workflows.

