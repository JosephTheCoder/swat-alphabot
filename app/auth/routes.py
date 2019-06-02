from app import logger
from flask import jsonify, Response, request, redirect, session, url_for, current_app, render_template
from . import bp
import json
import os
from flask_login import current_user, login_user, logout_user


@bp.route('/login', methods=['POST'])
def login_company():
    if current_user.is_authenticated:
        return redirect(url_for('video_stream.index'))

    username = request.form['username']
    password = request.form['password']

    sudo_user = 'admin'
    sudo_pass = 'rmsf2019'

    if username==sudo_user and password==sudo_pass:
        logger.error("Tried to login with invalid credentials!")
        return render_template('login.html', error="Invalid credentials!")

    return redirect(url_for('video_stream.index'))


@bp.route('/login', methods=['GET'])
def get_login_form():
    if current_user.is_authenticated:
        return redirect(url_for('video_stream.index'))
        
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('video_stream.index'))

# @bp.route('/company_registration', methods=['POST'])
# def register_compamny():
#     username = request.json.get('username')
#     password = request.json.get('password')

#     if username is None or password is None:
#         abort(400) # missing arguments to auth
#     if CompanyFinder.get_by_username(username) is not None:
#         abort(400) # company already exists
    
#     company = Company(username=username)
#     company.hash_password(password)
#     db.session.add(company)
#     db.session.commmit()

#     return redirect('/')