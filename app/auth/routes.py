from app import logger, config
from flask import request, redirect, session, url_for, render_template
from . import bp
import json
import os
from flask_login import UserMixin, login_user, logout_user, current_user, LoginManager
from appserver import app

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


users = {os.environ['ADMIN_USER']: {'password': os.environ['ADMIN_PASS']}}

class User(UserMixin):
    pass


@login_manager.user_loader
def get_user(username):
    if username not in users:
        return None

    user = User()
    return 


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in users:
        return

    user = User()
    user.id = username

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[username]['password']

    return user


@bp.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('index.html')

@bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if password == users[username]['password']:
        user = User()
        user.id = username
        login_user(user)
        return redirect(url_for('auth.index'))

    logger.error("Tried to login with invalid credentials!")
    return render_template('login.html', error="Invalid credentials!")


@bp.route('/login', methods=['GET'])
def get_login_form():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
        
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.index'))