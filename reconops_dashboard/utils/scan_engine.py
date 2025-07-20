import subprocess
from reconops_dashboard import db
from reconops_dashboard.models import ScanResult

def run_nmap_scan(target):
    """
    Run an nmap scan on the specified target and save the result to the database.
    """
    try:
        # Run nmap scan
        result = subprocess.run(
            ['nmap', '-Pn', '-sV', target],
            capture_output=True,
            text=True,
            timeout=60
        )
        scan_output = result.stdout

        # Save to database
        scan_result = ScanResult(target=target, scan_output=scan_output)
        db.session.add(scan_result)
        db.session.commit()

        return scan_output

    except subprocess.TimeoutExpired:
        return "Nmap scan timed out."
    except Exception as e:
        return f"Error during scan: {str(e)}"
