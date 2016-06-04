import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)
P=GPIO.PWM(15,100)
P.start(50)
time.sleep(3)
P.ChangeDutyCycle(100)
time.sleep(3)

cmd = raw_input(">> ")
while (cmd != "q"):
    P.ChangeDutyCycle(int(cmd))
    
    cmd = raw_input(">> ")
    
