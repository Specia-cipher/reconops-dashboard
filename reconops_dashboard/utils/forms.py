from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ScanForm(FlaskForm):
    target = StringField('Target', validators=[DataRequired()])
    submit = SubmitField('Scan')
