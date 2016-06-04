import RPi.GPIO as GPIO
import time
gplist = [14,15,18]
GPIO.setmode(GPIO.BCM)
GPIO.setup(gplist,GPIO.OUT)
P=GPIO.PWM(18,100)
choice=50
P.start(choice)
while (choice<=100):
    
    GPIO.output(14,0)
    GPIO.output(15,1)
    P.ChangeDutyCycle(choice)
    time.sleep(2)

    P.stop()
    time.sleep(2)
    P.start(choice)
    
    GPIO.output(14,1)
    GPIO.output(15,0)
    P.ChangeDutyCycle(choice)
    time.sleep(2)
    
    choice = int(raw_input("number"))

P.stop()
GPIO.cleanup()
