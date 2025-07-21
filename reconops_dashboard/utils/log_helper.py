from reconops_dashboard import db
from reconops_dashboard.models import SystemLog

def log_event(level, message):
    log = SystemLog(level=level, message=message)
    db.session.add(log)
    db.session.commit()
