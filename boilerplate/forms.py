from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired

class Contact(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    emailid = StringField('emailid', validators=[DataRequired(), Email()])
    mobileno = IntegerField('mobileno', validators=[DataRequired()])
