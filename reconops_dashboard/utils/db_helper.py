from reconops_dashboard import db
from reconops_dashboard.models import ScanResult, SystemLog

def save_scan_result(target, scan_output):
    """
    Save scan results to the database.
    """
    scan_result = ScanResult(target=target, scan_output=scan_output)
    db.session.add(scan_result)
    db.session.commit()

def save_system_log(level, message):
    """
    Save a system log entry to the database.
    """
    log_entry = SystemLog(level=level, message=message)
    db.session.add(log_entry)
    db.session.commit()
