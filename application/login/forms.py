from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo

from ..main.models import User


class LoginForm(FlaskForm):
    """Defines WTForms form to login based on username and password.

    Attributes
    ----------
    username : StringField
        Valid identifier for each user.
    password : PasswordField
    remember_me : BooleanField
        True if user wants the app to remember past session expiry.
    submit : SubmitField
        Self explanatory

    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    """Defines WTForms form to create user.

    Attributes
    ----------
    username : StringField
        Valid identifier for each user.
    password : PasswordField
        Valid password.
    password : PasswordField
        Valid password, but repeated.
    submit : SubmitField
        Self explanatory

    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Checks if user exists in database.

        Parameters
        ----------
        username : string
            Username to look for in database.

        Returns
        -------


        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
