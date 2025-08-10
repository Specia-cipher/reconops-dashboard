from datetime import datetime
from flask_login import current_user
from reconops_dashboard import db
from reconops_dashboard.models import ScanResult, SystemLog

def save_scan_result(target, scan_output, user_id=None):
    if user_id is None:
        if current_user.is_authenticated:
            user_id = current_user.id
        else:
            raise ValueError("User must be authenticated to save scan results")
    
    scan_result = ScanResult(
        target=target,
        scan_output=scan_output,
        created_at=datetime.utcnow(),
        user_id=user_id
    )
    db.session.add(scan_result)
    db.session.commit()

def save_system_log(level, message, user_id=None):
    log_entry = SystemLog(
        level=level,
        message=message,
        user_id=user_id
    )
    db.session.add(log_entry)
    db.session.commit()
