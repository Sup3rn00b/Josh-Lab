import Servo
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

tilt=Servo.Servo(14)
c = raw_input("...Now, What Tilt do you wish?")
#todo that check for int

while c != "exit":
    print("Understood...")
    # TODO: Test For Time Spacing
    tilt.moveTo(int(c))
    c=raw_input("...Now, What Tilt do you wish?")

GPIO.cleanup()
