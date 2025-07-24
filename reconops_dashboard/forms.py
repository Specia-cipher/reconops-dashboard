# reconops_dashboard/forms.py
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class SettingsForm(FlaskForm):
    scan_timeout = IntegerField('Scan Timeout (seconds)', validators=[DataRequired(), NumberRange(min=1, max=3600)])
    scan_flags = StringField('Scan Flags', validators=[DataRequired()])
    submit = SubmitField('Save Settings')

