from app import logger, config
from flask import request, redirect, session, url_for, render_template
from . import bp
import json
import os
from flask_login import UserMixin, login_user, logout_user, current_user, LoginManager

from app.auth.finders.user_finder import UserFinder

@bp.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('index.html')

@bp.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    
    username = request.form['username']
    password = request.form['password']

    user = UserFinder.get_from_username(username=username)

    if user is None or not user.check_password(password):
        logger.error("User tried to login with invalid credentials!")
        return render_template('login.html', error="Invalid credentials!")

    login_user(user)
    session['name'] = user.username
    return redirect(url_for('auth.index'))

@bp.route('/login', methods=['GET'])
def get_login_form():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
        
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user(current_user)
    session.pop('name')
    return redirect(url_for('auth.login'))