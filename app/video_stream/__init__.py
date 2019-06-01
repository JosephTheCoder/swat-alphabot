from flask import Blueprint
bp = Blueprint('video_stream', __name__)

from app.video_stream import routes
