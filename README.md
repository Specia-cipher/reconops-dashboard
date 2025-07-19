# 📊 ReconOps-Dashboard

A web-based reconnaissance and situational awareness dashboard for ethical hackers and red teamers. Built with Flask for a clean, modular design – optimized for both desktop labs and mobile environments.  

Where **AttackOps-Lab** focuses on offensive tooling and **DefenseOps-Lab** on defensive hardening, **ReconOps-Dashboard** gives you a bird’s-eye view of reconnaissance data, helping you map and monitor targets in real time.  

---

## 📌 Features

✅ Live target recon data visualization (subdomains, open ports, services).  
✅ Modular architecture: plug in existing tools (Nmap, Sublist3r, etc).  
✅ API endpoints for mobile lab integration (Termux/Kali UserLAnd).  
✅ Dashboard built with Flask + Bootstrap for lightweight, responsive UI.  
✅ JSON export for integration with other pipelines.  

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Specia-cipher/reconops-dashboard.git
cd reconops-dashboard

# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the app
flask run --host=0.0.0.0 --port=5000
🔥 Modules
Module	Description
🌐 Subdomain Map	Visualize discovered subdomains in real time
📡 Port Scanner	Map open ports and services (Nmap backend)
📜 Log Viewer	Parse and monitor recon logs (JSON support)
📥 Data Export	Export all findings as JSON or CSV

🐳 Docker Support (Planned)
bash
Copy
Edit
docker build -t reconops-dashboard .
docker run -p 5000:5000 reconops-dashboard
👨‍💻 About the Author
Sanni Babatunde Idris | DevSecOps Engineer | Ethical Hacker
🔗 GitHub | LinkedIn

⚠️ Disclaimer
This tool is for educational and authorized security testing only. Do not use against systems you do not own or have explicit permission to test.
