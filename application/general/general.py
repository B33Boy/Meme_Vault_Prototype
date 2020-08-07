from flask import Blueprint, render_template
from . import config as cfg

general_bp = Blueprint('general_bp', __name__, template_folder='templates', static_folder='static')

@general_bp.route('/')
def index():
    return render_template("general.html")
