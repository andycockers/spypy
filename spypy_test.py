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
               time.sleep(2)
               print("Ready")
               while True:
                             if GPIO.input(PIR):
                                             print("Motion detected, capturing image")
                                             camera.capture(filename)
                             time.sleep(2)
except KeyboardInterrupt:
               print(" Quit")
               GPIO.cleanup()
#sleep(2)
#camera.capture(filename)