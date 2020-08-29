from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from wtforms.widgets import TextArea

from ..main.models import User


class MetadataForm(FlaskForm):

    keywords = StringField('Keywords', widget=TextArea())
    submit = SubmitField('Save')
