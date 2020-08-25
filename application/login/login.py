from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from .forms import LoginForm, RegistrationForm
from ..main.models import User
from app import db

login_bp = Blueprint('login_bp', __name__,
                     template_folder='templates')


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login blueprint, incorporates WTForms and Flask-Login.

    Returns
    -------
    function
        rendered template of login.html
    """
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index', username=current_user.username))

    form = LoginForm()

    # If validated, redirect to main page
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', category='danger')
            return redirect(url_for('login_bp.login'))

        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main_bp.index', username=current_user.username)

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@login_bp.route('/logout')
def logout():
    """Logout blueprint, incorporates Flask-Login

    Returns
    -------
    function
        redirects to login page

    """
    logout_user()

    return redirect(url_for('login_bp.login'))


@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Register user blueprint, incorporates WTForms and Flask-Login, and database.

    Returns
    -------
    function
        rendered template of register.html

    """
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.index', username=current_user.username))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login_bp.login'))

    return render_template('register.html', title='Register', form=form)
