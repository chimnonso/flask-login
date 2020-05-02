from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import ValidationError
from myproject.models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Password must match!!!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Join Us')

    def check_mail(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Mail already exist')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first:
            raise ValidationError('Username already exist!!!')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')