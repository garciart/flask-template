"""Administration forms manager.
"""
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from sqlalchemy import select
from app import db
from app.models import User, Role


class AddUserForm(FlaskForm):
    """Parameters for the Add User form template.
    """
    username = StringField('Username', validators=[DataRequired()])
    user_email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    is_admin = BooleanField('This user an administrator')
    submit = SubmitField('Add User')

    def validate_username(self, username):
        # type: (StringField) -> None
        """Check if a username already exists in the database.

        :param StringField username: The username to check
        :return: None
        :raises ValidationError: If the submitted username already exists
        """
        _user = db.session.scalar(select(User).where(
            User.username == username.data))
        if _user is not None:
            raise ValidationError('User already exists.')

    def validate_email(self, user_email):
        # type: (StringField) -> None
        """Check if an email address already exists in the database.

        :param StringField user_email: The email address to check
        :return: None
        :raises ValidationError: If the submitted email address already exists
        """
        _user = db.session.scalar(select(User).where(
            User.user_email == user_email.data))
        if _user is not None:
            raise ValidationError('Email address already exists.')


class EditUserForm(FlaskForm):
    """Parameters for the Edit Role form template.
    """
    username = StringField('Username', validators=[DataRequired()])
    user_email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password')
    password2 = PasswordField(
        'Repeat Password', validators=[EqualTo('password')])
    is_admin = BooleanField('This user an administrator')
    submit = SubmitField('Update User')

    def __init__(self, original_username, *args, **kwargs):
        # type: (str, any, any) -> None
        """Get the username of the user being edited.

        :params str original_username: The edited user's username
        :return: None
        """
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        # type: (StringField) -> None
        """Check if a username already exists in the database.

        :param StringField username: The username to check
        :return: None
        :raises ValidationError: If the submitted username already exists
        """
        if username.data != self.original_username:
            _user = db.session.scalar(select(User).where(
                User.username == self.username.data))
            if _user is not None:
                raise ValidationError('Username already exists.')


class DeleteUserForm(FlaskForm):
    """Parameters for the Delete User form template.
    """
    submit = SubmitField('Delete User')
    cancel = SubmitField('Cancel')


class AddRoleForm(FlaskForm):
    """Parameters for the Add Role form template.
    """
    role_name = StringField('Role', validators=[DataRequired()])
    submit = SubmitField('Add Role')

    def validate_role_name(self, role_name):
        # type: (StringField) -> None
        """Check if a role already exists in the database.

        :param StringField role_name: The role to check
        :return: None
        :raises ValidationError: If the submitted role already exists
        """
        _role = db.session.scalar(select(Role).where(
            Role.role_name == role_name.data))
        if _role is not None:
            raise ValidationError('Role already exists.')


class EditRoleForm(FlaskForm):
    """Parameters for the Edit Role form template.
    """
    role_name = StringField('Role name', validators=[DataRequired()])
    submit = SubmitField('Update Role')

    def __init__(self, original_role_name, *args, **kwargs):
        # type: (str, any, any) -> None
        """Get the name of the role being edited.

        :params str original_role_name: The edited role's name
        :return: None
        """
        super().__init__(*args, **kwargs)
        self.original_role_name = original_role_name

    def validate_role_name(self, role_name):
        # type: (StringField) -> None
        """Check if a role already exists in the database.

        :param StringField role_name: The role to check
        :return: None
        :raises ValidationError: If the submitted role already exists
        """
        if role_name.data != self.original_role_name:
            _role = db.session.scalar(select(Role).where(
                Role.role_name == self.role_name.data))
            if _role is not None:
                raise ValidationError('Role already exists.')


class DeleteRoleForm(FlaskForm):
    """Parameters for the Delete Role form template.
    """
    submit = SubmitField('Delete Role')
    cancel = SubmitField('Cancel')
