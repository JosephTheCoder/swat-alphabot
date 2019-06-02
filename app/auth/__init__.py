from flask import Blueprint, current_app
import os

bp = Blueprint('auth', __name__)

from app.auth import routes