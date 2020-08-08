from flask import Blueprint, render_template
from flask_login import login_required


main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')

@main_bp.route('/')
@login_required
def index():
    posts = [{
    }]

    return render_template("main.html", title = 'Home Page', posts=posts)

@main_bp.route('/about')
def about():
    return render_template("about.html", title = 'About')


@main_bp.app_errorhandler(404)
def not_found(e):
  return render_template('404.html'), 404
