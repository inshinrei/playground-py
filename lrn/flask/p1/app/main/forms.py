from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError

from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('')


class EditProfileForm(FlaskForm):
    name = StringField('name', validators=[Length(0, 64)])
    location = StringField('location', validators=[Length(0, 64)])
    about_me = TextAreaField('about me')
    submit = SubmitField('submit')


class EditProfileAdminForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                         'usernames must have only letters, numbers, dots or underscores')])
    confirmed = BooleanField('confirmed')
    role = SelectField('role', coerce=int)
    name = StringField('name', validators=[Length(0, 64)])
    location = StringField('location', validators=[Length(0, 64)])
    about_me = TextAreaField('about')
    submit = SubmitField('submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('email already registered')

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('username already is use')


class PostForm(FlaskForm):
    body = PageDownField("what's on your mind?", validators=[DataRequired()])
    submit = SubmitField('submit')


class CommentForm(FlaskForm):
    body = StringField('enter your comment', validators=[DataRequired()])
    submit = SubmitField('submit')
