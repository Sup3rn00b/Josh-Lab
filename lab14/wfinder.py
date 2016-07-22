import RPi.GPIO as GPIO
import time
import servo
import seeker
import arraylabs
GPIO.setmode(GPIO.BCM)

class WallFinder:

    def __init__(self,pan,tilt,seek):

        self.neck=pan
        self.tilt=tilt
        self.eyes=seek
        self.eyes.units("in")
        self.tilt.moveTo(75)
        self.DECREASE=0
        self.INCREASE=1
        self.UNSET=2

    def scanWall(self):
        distanceArray=[]

        self.neck.moveTo(90)
        time.sleep(1)

        for x in range(18):
            self.neck.moveTo(x*10)
            time.sleep(0.2)
            ph = self.eyes.distance()
            time.sleep(0.2)
            distanceArray.append(ph)
            print "Scan: ", x*10, " => ", ph
        return distanceArray

    def cornerDetect(self,dists):
        prev=self.UNSET
        switchCount=0

        dataSize=dists.__len__()
        for x in range(dataSize-1):
            difference=dists[x]-dists[x+1]
            if difference>= 0:
                print("Decrease")
                if prev==self.INCREASE:
                    switchCount=switchCount+1
                prev=self.DECREASE

            elif difference<= 0:
                print("Increase")
                if prev==self.DECREASE:
                    switchCount=switchCount+1
                prev=self.INCREASE
            else:
                print("None")

        print (switchCount)
        if switchCount ==3:
            return True
        else:
            return False

    def findWall(self):
        ar=self.scanWall()
        mindex=ar.index(min(ar))
        leastAngle=mindex*10
        self.neck.moveTo(leastAngle)
        time.sleep(2);
        print "Here:", leastAngle, " => ",  ar[mindex]

seeker=seeker.Range(10,9)
panner=servo.Servo(7)
tilter=servo.Servo(8)

looker=WallFinder(panner,tilter,seeker)

#looker.findWall()
looker.cornerDetect(looker.scanWall())