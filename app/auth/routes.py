from app import logger
from flask import jsonify, Response, request, redirect, session, url_for, current_app, render_template
from . import bp
import json
import os
from flask_login import current_user, login_user, logout_user

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

    sudo_user = 'admin'
    sudo_pass = 'rmsf2019'

    if username != sudo_user or password != sudo_pass:
        logger.error("Tried to login with invalid credentials!")
        return render_template('login.html', error="Invalid credentials!")

    current_user.is_authenticated = True
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