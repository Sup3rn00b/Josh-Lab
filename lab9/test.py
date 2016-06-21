import Servo
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

tilt=Servo.Servo(14)
pan=Servo.Servo(15)
tiltPos = raw_input("...Now, What Tilt do you wish?")
panPos = raw_input("...and the Pan?")


while tiltPos != "exit":
    print("Understood...")

    tilt.moveTo(int(tiltPos))
    pan.moveTo(int(panPos))

    tiltPos = raw_input("...Now, What Tilt do you wish?")
    panPos = raw_input("...and the Pan?")

GPIO.cleanup()
