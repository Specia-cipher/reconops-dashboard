# reconops_dashboard/routes/settings_routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from reconops_dashboard.forms import SettingsForm
from reconops_dashboard.utils.settings_helper import get_settings, update_settings

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/', methods=['GET', 'POST'])
@login_required
def settings():
    settings = get_settings()
    form = SettingsForm()

    if form.validate_on_submit():
        timeout = form.scan_timeout.data
        flags = form.scan_flags.data
        update_settings(timeout, flags)
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('settings.settings'))
    else:
        # Pre-fill form fields on GET or if validation fails
        form.scan_timeout.data = settings.scan_timeout
        form.scan_flags.data = settings.scan_flags

    return render_template('settings.html', form=form)

@settings_bp.route('/account')
@login_required
def account():
    # Pass current_user to template for display
    return render_template('account.html', user=current_user)
