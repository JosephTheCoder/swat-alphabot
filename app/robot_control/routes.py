from app import logger
from flask import render_template, Response, request, redirect, url_for
from . import bp, Robot, GPIO, RIGHT_INFRARED, LEFT_INFRARED
from flask_login import login_required

# The function below is executed when someone requests a URL with the pin number and action in it:
@login_required
@bp.route("/move")
def action():
   right_IR_status = GPIO.input(RIGHT_INFRARED)
   left_IR_status = GPIO.input(LEFT_INFRARED)

   action = request.args.get('action')
   logger.info(action)

   if action == "forward":
      #if right_IR_status == 1 and left_IR_status == 1:
      Robot.forward()

   if action == "backward":
      Robot.backward()

   if action == "left":
      #if left_IR_status == 1:
      Robot.left()

   if action == "right":
      #if right_IR_status == 1:
      Robot.right()

   if action == "stop":
         Robot.stop()

   return 200