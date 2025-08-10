# reconops_dashboard/models.py
from datetime import datetime
from reconops_dashboard import db, login_manager
from flask_login import UserMixin
import bcrypt  # Stronger than werkzeug for passwords
import secrets

class ScanResult(db.Model):
    __tablename__ = 'scan_results'
    id = db.Column(db.Integer, primary_key=True)
    target = db.Column(db.String(255), nullable=False)
    scan_output = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    # Critical user link ▼
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='scans')

    def __repr__(self):
        return f"<ScanResult {self.target} by User {self.user_id}>"

class SystemLog(db.Model):
    __tablename__ = 'system_logs'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    level = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    # Critical user link ▼
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  # Allow null for system logs
    user = db.relationship('User', backref='logs')

    def __repr__(self):
        return f"<SystemLog {self.level} @ {self.timestamp}>"

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')
    api_key = db.Column(db.String(64), unique=True, default=lambda: secrets.token_hex(32))  # For future API auth
    # User-specific scan settings ▼
    scan_timeout = db.Column(db.Integer, default=180)
    scan_flags = db.Column(db.String(255), default='-Pn -sV')

    def set_password(self, password):
        """Bcrypt password hashing (Nigeria-approved strong encryption)."""
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, password):
        """Verify bcrypt password."""
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())
    
    def regenerate_api_key(self):
        """Generates a new API key for the user."""
        self.api_key = secrets.token_hex(32)

    def __repr__(self):
        return f"<User {self.username} ({self.role})>"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
