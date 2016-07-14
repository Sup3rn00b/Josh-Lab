import RPi.GPIO as GPIO
import time
import servo
import seeker
GPIO.setmode(GPIO.BCM)

class WallFinder:

    def __init__(self,pan,tilt,seek):

        self.neck=pan
        self.tilt=tilt
        self.eyes=seek
        self.eyes.units("cm")
        self.tilt.moveTo(80)

    def findWall(self):
        least=5000
        leastFar=0
        leastFar2=0


        self.neck.moveTo(90)
        time.sleep(1)

        for x in range(18):
            self.neck.moveTo(x*10)
            print("Angle:",x*10)
            time.sleep(0.01)
            ph = self.eyes.distance()
            print("Distance:",ph)
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
            print("Angle:",leastFar+x)
            time.sleep(0.01)
            ph = self.eyes.distance()
            print("Distance:",ph)
            time.sleep(0.01)
            if ph<least:
                least=ph
                leastFar2=x
        self.neck.moveTo(leastFar2)
        print ("Here.")

seeker=seeker.Range(24,23)
panner=servo.Servo(18)
tilter=servo.Servo(15)

looker=WallFinder(panner,tilter,seeker)

looker.findWall()