import RPi.GPIO as GPIO
import time
import servo
import seeker
GPIO.setmode(GPIO.BCM)

class WallFinder:

    eyes=seeker.Range(24,23)
    neck=servo.Servo(18)

    def findWall(self,eyes,neck):
        least=5000
        leastFar=0
        leastFar2=0

        eyes.units("cm")
        neck.moveTo(90)
        time.sleep(1)

        for x in range(18):
            neck.moveTo(x*10)
            time.sleep(0.01)
            ph = eyes.distance()
            print(ph)
            time.sleep(0.2)
            if ph<least:
                least=ph
                leastFar=x

        neck.moveTo(leastFar)
        time.sleep(1)
        neck.moveTo(leastFar-15)
        print("...Second Round Let's Go!...")

        for x in range(30):
            neck.moveTo(leastFar+x)
            time.sleep(0.01)
            ph = eyes.distance()
            print(ph)
            time.sleep(0.01)
            if ph<least:
                least=ph
                leastFar2=x
        neck.moveTo(leastFar2)
        print ("Here.")
