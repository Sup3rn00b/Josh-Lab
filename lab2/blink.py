import RPi.GPIO as GPIO
import time
gplist = [14,15]
GPIO.setmode(GPIO.BCM)
GPIO.setup(gplist,GPIO.OUT)

while True:
    GPIO.output(14,0)
    GPIO.output(15,1)
    time.sleep(1)
    GPIO.output(14,1)
    GPIO.output(15,0)
    time.sleep(1)

