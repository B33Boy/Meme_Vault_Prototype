from flask import Blueprint, render_template
from flask_login import login_required

from . import config as cfg

general_bp = Blueprint('general_bp', __name__, template_folder='templates', static_folder='static')

@general_bp.route('/')
@login_required
def index():
    posts = [{
    'author': {'username': 'John'},
    'body': 'Beautiful day in Portland!'
    },
    {
    'author': {'username': 'Susan'},
    'body': 'The Avengers movie was so cool!'
    }]

    return render_template("general.html", title = 'Home Page', posts=posts)
