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

pirPin = 4
GPIO.setup(pirPin, GPIO.IN)
camera = PiCamera()
counter = 1 

while True:
  if GPIO.input(pirPin):
   try: 
    camera.start_preview()
    time.sleep(1)
    print("Movement Detected, capturing image")
    camera.capture('img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg')
    counter = counter + 1
    camera.stop_preview()
   except:
    camera.stop_preview()
    time.sleep(3)
