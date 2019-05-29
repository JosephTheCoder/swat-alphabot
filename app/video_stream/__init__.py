from flask import Blueprint
bp = Blueprint('video_stream', __name__)

# Setup Video -----------------------------------
import cv2
video_camera = cv2.VideoCapture(0) 


from app.video_stream import routes
