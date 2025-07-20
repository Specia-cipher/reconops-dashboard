from flask import Blueprint, render_template, request, flash
from reconops_dashboard.utils.scan_engine import run_nmap_scan

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/scan', methods=['GET', 'POST'])
def scan():
    scan_result = None
    if request.method == 'POST':
        target = request.form.get('target')
        if target:
            scan_result = run_nmap_scan(target)
        else:
            flash("Please provide a target to scan.", "warning")
    return render_template('scan.html', scan_result=scan_result)

@main.route('/results')
def results():
    return render_template('results.html')

@main.route('/logs')
def logs():
    return render_template('logs.html')

@main.route('/settings')
def settings():
    return render_template('settings.html')
