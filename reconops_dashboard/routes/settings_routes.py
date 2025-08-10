# reconops_dashboard/routes/settings_routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from reconops_dashboard.forms import SettingsForm, RegenerateApiKeyForm # Import new form
from reconops_dashboard.utils.settings_helper import get_settings, update_settings
from reconops_dashboard import db

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm()
    
    if form.validate_on_submit():
        update_settings(current_user, form.scan_timeout.data, form.scan_flags.data)
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('settings.settings'))
    
    # Pre-fill form with current user's settings
    form.scan_timeout.data = current_user.scan_timeout
    form.scan_flags.data = current_user.scan_flags
    
    return render_template('settings.html', form=form)

@settings_bp.route('/account', methods=['GET'])
@login_required
def account():
    # Pass the new form to the template
    regen_form = RegenerateApiKeyForm()
    return render_template('account.html', user=current_user, regen_form=regen_form)

@settings_bp.route('/account/regenerate_api_key', methods=['POST'])
@login_required
def regenerate_api_key():
    # Create the form here to validate the CSRF token
    regen_form = RegenerateApiKeyForm()
    if regen_form.validate_on_submit():
        current_user.regenerate_api_key()
        db.session.commit()
        flash('New API key has been generated successfully!', 'success')
    else:
        flash('Failed to regenerate API key. Please try again.', 'error')
    
    return redirect(url_for('settings.account'))
