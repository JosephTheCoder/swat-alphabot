from flask import Blueprint
from app import GPIO
from AlphaBot import AlphaBot

bp = Blueprint('robot_control', __name__)

# Create Alphabot Instance -----------------------------------
Robot = AlphaBot()

RIGHT_INFRARED = 16
LEFT_INFRARED = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RIGHT_INFRARED,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(LEFT_INFRARED,GPIO.IN,GPIO.PUD_UP)

from app.robot_control import routes
