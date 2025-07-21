# reconops_dashboard/routes/settings_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from reconops_dashboard.utils.settings_helper import get_settings, update_settings

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/', methods=['GET', 'POST'])
def settings():
    settings = get_settings()
    if request.method == 'POST':
        timeout = int(request.form.get('scan_timeout', 60))
        flags = request.form.get('scan_flags', '-Pn -sV')
        update_settings(timeout, flags)
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('settings.settings'))
    return render_template('settings.html', settings=settings)
