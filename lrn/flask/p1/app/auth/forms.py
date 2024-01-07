from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo, Regexp

from ..models import User


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('log in')


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                         'usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('password',
                             validators=[DataRequired(), EqualTo('password2', message='passwords must match')])
    password2 = PasswordField('confirm password', validators=[DataRequired()])
    submit = SubmitField('register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username already in use')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('old password', validators=[DataRequired()])
    password = PasswordField('new password',
                             validators=[DataRequired(), EqualTo('password2', message='passwords must match')])
    password2 = PasswordField('confirm new password', validators=[DataRequired()])
    submit = SubmitField('update')
