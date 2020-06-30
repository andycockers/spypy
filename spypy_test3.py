import time
import picamera
from datetime import datetime, timedelta

#timestr = time.strftime("%Y%m%d-%H%M%S")
#print(timestr)

import glob
import datetime
import subprocess
import os
from configparser import ConfigParser
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
GPIO.setmode (GPIO.BCM)

pirPin = 4
GPIO.setup(pirPin, GPIO.IN)
camera = PiCamera()
counter = 1

filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

while True:
  if GPIO.input(pirPin):
   try: 
    camera.start_preview()
    time.sleep(1)
    print("Movement Detected, capturing image")
    #camera.capture('image%s.jpg' % counter)
    camera.capture('%s.jpg' % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    files_path = os.path.join(folder, '*')
    files = sorted(
    glob.iglob(files_path), key=os.path.getctime, reverse=True) 
    print(files[0])
    #print('image%s.jpg' % counter)
    counter = counter + 1
    camera.stop_preview()
   except:
    camera.stop_preview()
    time.sleep(3)
