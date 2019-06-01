from app import logger
from flask import render_template
from . import bp, Robot, GPIO, RIGHT_INFRARED, LEFT_INFRARED

# The function below is executed when someone requests a URL with the pin number and action in it:
@bp.route("/<action>")
def action(action):
   right_IR_status = GPIO.input(RIGHT_INFRARED)
   left_IR_status = GPIO.input(LEFT_INFRARED)

   if action == "forward":
      if right_IR_status == 1 and left_IR_status == 1:
         Robot.forward()
   
   if action == "backward":
         Robot.backward()

   if action == "left":
      if left_IR_status == 1:
         Robot.left()

   if action == "right":
      if right_IR_status == 1:
         Robot.right()