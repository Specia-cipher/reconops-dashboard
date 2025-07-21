# reconops_dashboard/utils/settings_helper.py
from reconops_dashboard import db
from reconops_dashboard.models import Settings

def get_settings():
    settings = Settings.query.first()
    if not settings:
        settings = Settings()
        db.session.add(settings)
        db.session.commit()
    return settings

def update_settings(scan_timeout, scan_flags):
    settings = get_settings()
    settings.scan_timeout = scan_timeout
    settings.scan_flags = scan_flags
    db.session.commit()
