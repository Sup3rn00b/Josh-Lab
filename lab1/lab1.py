import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.output(14,1)
while True:
    GPIO.output(14,1)
    time.sleep(0.02)
    GPIO.output(14,0)
    time.sleep(0.02)
    
