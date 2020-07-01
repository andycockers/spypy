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
    list_of_files = glob.glob('*.jpg') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getmtime)
    print (latest_file)
    print(files[0])
    counter = counter + 1
    camera.stop_preview()
   except:
    KeyboardInterrupt:
               print(" Quit")
               camera.stop_preview()
               GPIO.cleanup()
               time.sleep(3)
