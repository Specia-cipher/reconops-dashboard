# reconops_dashboard/routes/settings_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
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

@settings_bp.route('/account')
@login_required
def account():
    # Pass current_user to template for display
    return render_template('account.html', user=current_user)
