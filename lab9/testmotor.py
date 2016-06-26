import Motor
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

motor=Motor.Motor(14,15,18)

GPIO.setup(3, GPIO.OUT)
GPIO.output(3, 1)

speed = raw_input("...Speed?")
counter=1

while speed != "exit":
    if counter==1:
        motor.setSpeed(float(speed))
        motor.forward()
        print("Done.")
        counter=2
        speed = raw_input("...Speed?")
    if counter==2:
        motor.setSpeed(float(speed))
        motor.reverse()
        print("Done.")
        counter=1
        speed = raw_input("...Speed?")

motor.stop()
GPIO.cleanup()
print("All Finished.")
