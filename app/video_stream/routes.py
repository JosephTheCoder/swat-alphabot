from app import logger
from . import bp, video_camera
from flask import flash, render_template, request, Response

import cv2

@bp.route('/') 
def index(): 
   """Video streaming .""" 
   return render_template('index.html') 

@bp.route('/video_feed') 
def video_feed(): 
   """Video streaming route. Put this in the src attribute of an img tag.""" 
   return Response(generate_video(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame') 

def generate_video(): 
   """Video streaming generator function.""" 
   while True: 
       rval, frame = video_camera.read() 
       cv2.imwrite('pic.jpg', frame) 
       yield (b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + open('pic.jpg', 'rb').read() + b'\r\n') 