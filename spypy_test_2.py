import time
import picamera
from datetime import datetime, timedelta

import datetime
import subprocess
import os
from configparser import ConfigParser
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

GPIO.setmode(GPIO.BCM)
PIR = 4
GPIO.setup(PIR, GPIO.IN)

camera = PiCamera()
camera.resolution = (1024, 768)

def wait():
    GPIO.input(PIR)
try:
 if GPIO.input(PIR):
        for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
            print('Captured %s' % filename)
            
except KeyboardInterrupt:
               print(" Quit")
               GPIO.cleanup()