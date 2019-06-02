from app import logger
from flask import render_template, Response, request
from . import bp, Robot, GPIO, RIGHT_INFRARED, LEFT_INFRARED
from app.auth.wrappers import require_api_token

# The function below is executed when someone requests a URL with the pin number and action in it:
@require_api_token
@bp.route("/move")
def action():
   right_IR_status = GPIO.input(RIGHT_INFRARED)
   left_IR_status = GPIO.input(LEFT_INFRARED)

   action = request.args.get('action')
   logger.info(action)

   if action == "forward":
      if right_IR_status == 1 and left_IR_status == 1:
         Robot.forward()
         return Response(status=200) 
   
   if action == "backward":
         Robot.backward()
         return Response(status=200) 

   if action == "left":
      if left_IR_status == 1:
         Robot.left()
         return Response(status=200) 

   if action == "right":
      if right_IR_status == 1:
         Robot.right()
         return Response(status=200) 

   return Response(status=400) 