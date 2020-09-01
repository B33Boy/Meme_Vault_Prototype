from flask import Blueprint, render_template, current_app, request, url_for, redirect, send_from_directory, flash, jsonify, session
from flask_login import login_required, current_user
import os

from ..main.models import User, Post, get_posts_by_user, add_post_for_user, delete_post_for_user


main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates')


@main_bp.route('/')
def home():
    return redirect(url_for('login_bp.login'))


@main_bp.route('/<username>')
@login_required
def index(username):

    user = User.query.filter_by(username=username).first_or_404()

    # posts = Post.query.filter_by(username=username).all_or_404()

    posts = get_posts_by_user(user.username)

    # Send image names to html for rendering
    target = os.path.join(current_app.config['BASEDIR'], 'images/{}'.format(current_user.username)).replace("\\","/") 
    print("TARGET: ", target)
    
    # Make sure the listdirectory is created
    if not os.path.isdir(target):
        os.mkdir(target)
    
    image_names = os.listdir(target)

    return render_template("main.html", user=user, title='Home Page', posts=posts, image_names=image_names)


@main_bp.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images/{}".format(current_user.username), filename)


@main_bp.route('/<username>/<filename>', methods=['GET', 'POST'])
def add_metadata(username, filename, inps=[]):
    user = current_user.username

    prev = ['Blue', 'Sokka', 'Grumpy']

    if request.method == 'POST':
        prev = []

        f = request.form        
        for key in f.keys():
            for value in f.getlist(key):
                value = value.strip()
                print("FORM VALUE: ", value)
                if value == '' or value == None:
                    flash('Empty value in field', category='danger')
                else:
                    prev.append(value)


    # if request.method == 'POST':
    # prev = session.pop('inputs', None)

    return render_template("complete.html", user=user, filename=filename, prev=prev, inps=inps)

@main_bp.route('/<username>/<filename>/delete', methods=['POST'])
def delete_post(username, filename):

    # Get filepath
    target = os.path.join(current_app.config['BASEDIR'], 'images/{}'.format(current_user.username)).replace("\\","/")
    filepath = '/'.join([target, filename])
    
    # Delete from database
    delete_post_for_user(username=username, filepath=filepath)
    
    # delete the file
    os.remove(filepath)
    flash('Deleted File {}'.format(filename), category='danger')
    
    return redirect(url_for('main_bp.index', username=username))


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
    target = os.path.join(current_app.config['BASEDIR'], 'images/{}'.format(current_user.username)).replace("\\","/")
    print('target:',target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist('file'):

        filename = file.filename
        ext = os.path.splitext(filename)[1].lower()

        if ext in current_app.config['EXT']:
            print("File supported moving on...")
            dest = '/'.join([target, filename])
            file.save(dest)

            add_post_for_user(current_user.username, dest)


        else:
            # request.files.clear()
            flash('Invalid file format', category='danger')

    return redirect(url_for('main_bp.index', username=current_user.username))


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
