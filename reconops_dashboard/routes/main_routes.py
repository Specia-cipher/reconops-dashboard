from flask import Blueprint, render_template, request, redirect, url_for, flash
from reconops_dashboard.utils.scan_engine import run_nmap_scan
from reconops_dashboard.models import ScanResult
from reconops_dashboard import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        target = request.form.get('target')
        if target:
            # Run the scan
            output = run_nmap_scan(target)

            # Save to database
            new_scan = ScanResult(target=target, scan_output=output)
            db.session.add(new_scan)
            db.session.commit()

            flash('Scan completed and saved successfully!', 'success')
            return redirect(url_for('main.results'))
        else:
            flash('Please enter a valid target (IP or domain).', 'warning')

    return render_template('scan.html')

@main.route('/results')
def results():
    scans = ScanResult.query.order_by(ScanResult.created_at.desc()).all()
    return render_template('results.html', scans=scans)

@main.route('/logs')
def logs():
    return render_template('logs.html')

@main.route('/settings')
def settings():
    return render_template('settings.html')
