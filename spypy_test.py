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

camera = PiCamera()
camera.resolution = (1024, 768)

sleep(2)
camera.capture('foo.jpg')