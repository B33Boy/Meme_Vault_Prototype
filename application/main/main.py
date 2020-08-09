from flask import Blueprint, render_template, current_app, request
from flask_login import login_required
import os

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates', static_folder='static')


@main_bp.route('/')
@login_required
def index():
    """Index page blueprint

    Returns
    -------
    function
        rendered template of main.html

    """

    posts = [{
    }]

    return render_template("main.html", title='Home Page', posts=posts)


@main_bp.route('/about')
def about():
    """About page blueprint.

    Returns
    -------
    function
        rendered template of about.html

    """
    return render_template("about.html", title='About')


@main_bp.route('/upload', methods=['POST'])
def upload():
    """


    """
    target = os.path.join(current_app.config['BASEDIR'], 'images/').replace("\\","/")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):
        filename = file.filename
        dest = '/'.join([target, filename])
        file.save(dest)

    return render_template('complete.html')



@main_bp.app_errorhandler(404)
def not_found(e):
    """Error 404 page blueprint

    Parameters
    ----------
    e : exception object
        denotes type of exception

    Returns
    -------
    function
        rendered template of 404.html

    """
    return render_template('404.html'), 404
