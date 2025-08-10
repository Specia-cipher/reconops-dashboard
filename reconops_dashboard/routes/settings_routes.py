# reconops_dashboard/routes/settings_routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from reconops_dashboard.forms import ChangePasswordForm, RegenerateApiKeyForm
from reconops_dashboard import db
import uuid

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    change_password_form = ChangePasswordForm()
    regenerate_api_key_form = RegenerateApiKeyForm()

    # Handle form submissions based on which button was clicked
    if change_password_form.submit_change_password.data and change_password_form.validate_on_submit():
        # This block will ONLY execute if the change password button was clicked and the form is valid
        current_user.set_password(change_password_form.new_password.data)
        db.session.commit()
        flash('Your password has been updated successfully.', 'success')
        return redirect(url_for('settings.settings'))
    
    if regenerate_api_key_form.submit_regenerate_api_key.data and regenerate_api_key_form.validate_on_submit():
        # This block will ONLY execute if the regenerate API key button was clicked
        current_user.api_key = str(uuid.uuid4())
        db.session.commit()
        flash('Your API key has been regenerated successfully.', 'success')
        return redirect(url_for('settings.settings'))
    
    # If the request method is GET or if the form is invalid on POST
    return render_template(
        'settings.html',
        change_password_form=change_password_form,
        regenerate_api_key_form=regenerate_api_key_form
    )
