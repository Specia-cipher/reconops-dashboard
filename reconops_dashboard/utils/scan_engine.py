# reconops_dashboard/utils/scan_engine.py
import subprocess
import re
from flask import current_app
from flask_login import current_user
from reconops_dashboard import db
from reconops_dashboard.models import ScanResult, SystemLog

# Constants
ALLOWED_NMAP_FLAGS = {'-Pn', '-sV', '-T4', '-p', '-O'} # Whitelist safe flags
MAX_TIMEOUT = 3600 # 1 hour maximum

def validate_target(target):
    """Validate target IP/domain format."""
    ip_regex = r'^(\d{1,3}\.){3}\d{1,3}$'
    domain_regex = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(ip_regex, target) or re.match(domain_regex, target)

def sanitize_flags(flags_str):
    """Convert flags string to safe list of arguments."""
    if not flags_str:
        return ['-Pn', '-sV'] # Default safe flags
    
    flags = []
    for flag in flags_str.split():
        if flag in ALLOWED_NMAP_FLAGS or flag.lstrip('-').isdigit():
            flags.append(flag)
    return flags or ['-Pn', '-sV'] # Fallback to defaults

def run_scan(target, timeout=180):
    """
    Securely runs nmap scan with current user's settings.
    Requires an authenticated user.
    """
    try:
        if not current_user.is_authenticated:
            raise ValueError("Authentication required for scanning")

        # Validate target
        if not validate_target(target):
            raise ValueError(f"Invalid target format: {target}")

        # Get user-specific settings
        flags = sanitize_flags(getattr(current_user, 'scan_flags', None))
        timeout = min(getattr(current_user, 'scan_timeout', timeout), MAX_TIMEOUT)

        # Build and execute command
        cmd = ['nmap', *flags, target]
        current_app.logger.info(f"Executing: {' '.join(cmd)}")
        
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            shell=False
        )

        # --- DEBUG: Print stdout and stderr to the terminal ---
        print("--- NMAP STDOUT ---")
        print(result.stdout)
        print("--- NMAP STDERR ---")
        print(result.stderr)
        
        # If the scan produced no stdout, check stderr for errors or provide a generic message.
        if not result.stdout:
            if result.stderr:
                output = f"Nmap scan completed with errors:\n{result.stderr}"
            else:
                output = "Nmap scan completed, but no output was returned."
        else:
            output = result.stdout

        # Save results with user association
        scan = ScanResult(
            target=target,
            scan_output=output,
            user_id=current_user.id
        )
        db.session.add(scan)
        
        # Log the scan
        log_entry = SystemLog(
            level='INFO',
            message=f"Scan completed for {target}",
            user_id=current_user.id
        )
        db.session.add(log_entry)
        
        db.session.commit()
        return output

    except subprocess.TimeoutExpired:
        error_msg = f"Scan timed out for {target}"
        log_error('WARNING', error_msg)
        return error_msg
        
    except Exception as e:
        error_msg = f"Scan failed: {str(e)}"
        log_error('ERROR', error_msg)
        db.session.rollback()
        return error_msg

def log_error(level, message):
    """Centralized error logging with user context."""
    try:
        error_log = SystemLog(
            level=level,
            message=message,
            user_id=current_user.id if current_user.is_authenticated else None
        )
        db.session.add(error_log)
        db.session.commit()
    except Exception:
        db.session.rollback()
        current_app.logger.error(f"Failed to log error: {message}")
