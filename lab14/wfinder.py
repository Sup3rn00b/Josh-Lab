import RPi.GPIO as GPIO
import time
import servo
import seeker
GPIO.setmode(GPIO.BCM)

class WallFinder:

    def __init__(self,pan,tilt,seek):

        self.eyes=seek
        self.neck=pan

    def findWall(self):
        least=5000
        leastFar=0
        leastFar2=0

        self.eyes.units("cm")
        self.neck.moveTo(90)
        time.sleep(1)

        for x in range(18):
            self.neck.moveTo(x*10)
            time.sleep(0.01)
            ph = self.eyes.distance()
            print(ph)
            time.sleep(0.2)
            if ph<least:
                least=ph
                leastFar=x

        self.neck.moveTo(leastFar)
        time.sleep(1)
        self.neck.moveTo(leastFar-15)
        print("...Second Round Let's Go!...")

        for x in range(30):
            self.neck.moveTo(leastFar+x)
            time.sleep(0.01)
            ph = self.eyes.distance()
            print(ph)
            time.sleep(0.01)
            if ph<least:
                least=ph
                leastFar2=x
        self.neck.moveTo(leastFar2)
        print ("Here.")
