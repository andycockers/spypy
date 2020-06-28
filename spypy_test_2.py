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

def wait():
    GPIO.input(PIR)

with picamera.PiCamera() as camera:
    camera.start_preview()
    wait()
    for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
        print('Captured %s' % filename)
        wait()