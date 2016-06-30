import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class ViewFinder:
    def __init__(self,a,b):
        self.trigger=a
        self.echo=b
        GPIO.setup(a,GPIO.OUT)
        GPIO.setup(b,GPIO.OUT)

    def sendSignal(self):
        while GPIO.input(self.echo)==0:
            pulse_start=time.time()

        while GPIO.input(self.echo)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance,2)

        return distance

