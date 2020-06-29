import RPi.GPIO as GPIO 
import time
from picamera import PiCamera
GPIO.setmode (GPIO.BCM)

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
