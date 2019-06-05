from app import logger
from flask import render_template, Response, request, redirect, url_for
from . import bp, Robot, GPIO, RIGHT_INFRARED, LEFT_INFRARED
from flask_login import login_required

# The function below is executed when someone requests a URL with the pin number and action in it:
@login_required
@bp.route("/move/forward")
def forward():
   right_IR_status = GPIO.input(RIGHT_INFRARED)
   left_IR_status = GPIO.input(LEFT_INFRARED)

   if right_IR_status == 1 and left_IR_status == 1:
      Robot.forward()

   return ('', 204)


@login_required
@bp.route("/move/left")
def left():
   right_IR_status = GPIO.input(RIGHT_INFRARED)
   left_IR_status = GPIO.input(LEFT_INFRARED)

   if left_IR_status == 1:
      Robot.left()

   return ('', 204)


@login_required
@bp.route("/move/right")
def right():
   right_IR_status = GPIO.input(RIGHT_INFRARED)
   left_IR_status = GPIO.input(LEFT_INFRARED)

   if right_IR_status == 1:
      Robot.right()
   
   return ('', 204)


@login_required
@bp.route("/move/backward")
def backward():
   Robot.backward()

   return ('', 204)


@login_required
@bp.route("/move/stop")
def stop():
   Robot.stop()

   return ('', 204)