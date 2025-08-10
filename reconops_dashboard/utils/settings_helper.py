# reconops_dashboard/utils/settings_helper.py
from reconops_dashboard import db
from reconops_dashboard.models import User

def get_settings(user):
    """Get the current user's settings (now stored in User model)"""
    return user

def update_settings(user, timeout, flags):
    """Update scan settings for a user"""
    user.scan_timeout = timeout
    user.scan_flags = flags
    db.session.commit()
