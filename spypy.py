import time
import datetime
import subprocess
import os
from configparser import ConfigParser
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIR = 4
GPIO.setup(PIR, GPIO.IN)

#  Directory Path
Base_Dir = os.path.dirname(os.path.realpath(__file__)) + '/'

def get_file_name():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def photo():
    capturename = get_file_name()
    print('Motion detected! Taking snapshot')
    cmd = "raspistill -w 640 -h 480 -n -t 10 -q 10 -e jpg -th none -o {}capture/{}.jpg".format(Base_Dir, capturename)
    camerapid = subprocess.call(cmd, shell=True)

class spiboxMessenger:
  def getFileList(self):
       self.filelist = []
       i = 0
       for file in os.listdir(Base_Dir + "capture"):
          if file.endswith('.jpg') or file.endswith('.mp4'):
             self.filelist.extend([None])
             self.filelist[i] = file
             i = i+1

  def moveFiles(self):
        for filename in self.filelist:
            print('moving ' + filename + ' to archive')
            pid = subprocess.call(['sudo','mv', Base_Dir + 'capture/' + filename, Base_Dir + 'capture/archive/'])

  
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)
    messenger = spiboxMessenger()
    messenger.init()
    try:
        print("Turning on motion sensor...")
 
        # Loop until PIR indicates nothing is happening
        while GPIO.input(PIR)==1:
            Current_State  = 0
 
        print("  Sensor ready")
 
        while True:
            print('Waiting for movement')
            GPIO.wait_for_edge(PIR,GPIO.RISING)
            
            if messenger.recordtype == 'IMG':
                photo()
            elif messenger.recordtype == 'VID':
                video(RecordTime = messenger.recordtime * 1000)
                
            messenger.getFileList()
            messenger.emailFiles()
            messenger.moveFiles()

    except KeyboardInterrupt:
      print("  Bye for now")
      # Reset GPIO
      GPIO.cleanup()
#try:
#               print("PIR Module Test (CTRL+C to exit)")
#               time.sleep(2)
#               print("Ready")
#               while True:
#                             if GPIO.input(PIR_PIN):
#                                             print("Motion Detected")
#               time.sleep(1)
#except KeyboardInterrupt:
#               print("Quit")
#               GPIO.cleanup()