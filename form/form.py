from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", 
                                     validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    phone = TelField("Phone Number", validators=[Optional(), Length(min=7, max=15)])
    submit = SubmitField("Register")
