from app import logger, config
from flask import jsonify, Response, request, redirect, session, url_for, current_app, render_template
from . import bp
import json
import os
from flask_login import login_manager, current_user, login_user, logout_user, UserMixin

class User(UserMixin):

    def __init__(self, username):
        self.name = username

    @property
    def id(self):
        return self.name

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

    if username != config['ADMIN_USER'] or password != config['ADMIN_PASS']:
        logger.error("Tried to login with invalid credentials!")
        return render_template('login.html', error="Invalid credentials!")

    user = User('admin')
    login_user(user)
    return redirect(url_for('auth.index'))


@bp.route('/login', methods=['GET'])
def get_login_form():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
        
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.index'))