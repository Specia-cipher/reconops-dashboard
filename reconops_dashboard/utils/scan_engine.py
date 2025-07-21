# reconops_dashboard/utils/scan_engine.py

import subprocess
from reconops_dashboard import db
from reconops_dashboard.models import ScanResult, SystemLog

def run_scan(target, timeout=60, flags='-Pn -sV'):
    """
    Runs an nmap scan on the specified target and saves the result to the database.
    """
    try:
        # Build the nmap command
        cmd = ['nmap'] + flags.split() + [target]
        
        # Execute the nmap command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        scan_output = result.stdout
        
        # Save scan result
        scan_result = ScanResult(target=target, scan_output=scan_output)
        db.session.add(scan_result)
        db.session.commit()
        
        # Log the scan
        log_entry = SystemLog(level='INFO', message=f"Nmap scan completed for {target}")
        db.session.add(log_entry)
        db.session.commit()
        
        return scan_output

    except subprocess.TimeoutExpired:
        error_msg = f"Nmap scan timed out for target: {target}"
        log_error('WARNING', error_msg)
        return error_msg

    except Exception as e:
        error_msg = f"Error running nmap scan for {target}: {str(e)}"
        log_error('ERROR', error_msg)
        return error_msg

def log_error(level, message):
    """
    Helper to log errors to SystemLog.
    """
    error_log = SystemLog(level=level, message=message)
    db.session.add(error_log)
    db.session.commit()
