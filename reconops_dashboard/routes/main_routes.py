from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from reconops_dashboard.models import ScanResult, SystemLog
from reconops_dashboard.utils.scan_engine import run_scan
from reconops_dashboard.utils.db_helper import save_system_log
from reconops_dashboard.utils.forms import ScanForm

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def home():
    return render_template('home.html')

@main.route('/scan', methods=['GET', 'POST'])
@login_required
def scan():
    form = ScanForm()
    if form.validate_on_submit():
        target = form.target.data

        # run_scan runs the scan and already saves the scan result with user_id
        output = run_scan(target)

        # Save system log with user association
        save_system_log('INFO', f"Scan completed for target: {target}", user_id=current_user.id)

        flash('Scan completed and saved successfully!', 'success')
        return redirect(url_for('main.results'))
    elif form.is_submitted():
        flash('Please provide a valid target.', 'warning')
    return render_template('scan.html', form=form)

@main.route('/results')
@login_required
def results():
    scans = ScanResult.query.order_by(ScanResult.created_at.desc()).all()
    return render_template('results.html', scans=scans)

@main.route('/logs')
@login_required
def logs():
    logs = SystemLog.query.order_by(SystemLog.timestamp.desc()).all()
    return render_template('logs.html', logs=logs)
