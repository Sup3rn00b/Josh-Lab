import Servo
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)



tilt=Servo.Servo(14)
pan=Servo.Servo(15)
t = raw_input("...Now, What Tilt do you wish?")
p = raw_input("...and the Pan?")

#MOTOR


#TILT AND PAN
while t != "exit":
    print("Understood...")

    tilt.moveTo(int(t))
    pan.moveTo(int(p))

    c=raw_input("...Now, What Tilt do you wish?")
    p = raw_input("...and the Pan?")

GPIO.cleanup()
