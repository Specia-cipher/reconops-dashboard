# reconops_dashboard/models.py

from datetime import datetime
from reconops_dashboard import db

class ScanResult(db.Model):
    __tablename__ = 'scan_results'
    id = db.Column(db.Integer, primary_key=True)
    target = db.Column(db.String(255), nullable=False)
    scan_output = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ScanResult {self.target} @ {self.created_at}>"

class SystemLog(db.Model):
    __tablename__ = 'system_logs'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    level = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<SystemLog {self.level} @ {self.timestamp}>"

class Settings(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    scan_timeout = db.Column(db.Integer, default=60)  # Default timeout in seconds
    scan_flags = db.Column(db.String(255), default='-Pn -sV')  # Default Nmap flags

    def __repr__(self):
        return f"<Settings timeout={self.scan_timeout}, flags={self.scan_flags}>"
