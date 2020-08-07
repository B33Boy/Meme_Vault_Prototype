from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import LoginForm


login_bp = Blueprint('login_bp', __name__, template_folder='templates', static_folder='static')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # If validated, redirect to main page
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data), category='success')
        return redirect(url_for('general_bp.index'))
    else:
        flash('Login failed', category='danger')

    return render_template('login.html', title='Sign In', form=form)
