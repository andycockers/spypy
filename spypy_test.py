import time
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

counter = 0
filename = "capture{}.jpg"
while os.path.isfile(filename.format(counter)):
    counter += 1
filename = filename.format(counter)

camera = PiCamera()
camera.resolution = (1024, 768)

try:
               print("Monitoring")
               time.sleep(1)
               print("Ready")
               while True:
                             if GPIO.input(PIR):
                                            for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
                                             print('Captured %s' % filename)
                             time.sleep(1)
except KeyboardInterrupt:
               print(" Quit")
               GPIO.cleanup()
#sleep(2)
#camera.capture(filename)
