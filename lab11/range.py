import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Range:
    def __init__(self,trig,echo):
        self.trigger=trig
        self.echo=echo
        GPIO.setup(trig,GPIO.OUT)
        GPIO.setup(echo,GPIO.IN)
        time.sleep(1)
        self.toCentimeters = 17150
	self.toInches = 6752
	self.convert = self.toCentimeters
	self.unitStr = "cm"


    def units(self, unitstr):
	self.unitStr = unitstr;
        if unitstr == "cm":
	    self.convert = self.toCentimeters
	    self.unitStr = "cm"
        else:
	    self.convert = self.toInches
	    self.unitStr = "in"

    def distance(self):

        GPIO.output(self.trigger,False)
        time.sleep(0.5)

        GPIO.output(self.trigger,True)
        time.sleep(0.00001)
        GPIO.output(self.trigger,False)

        while GPIO.input(self.echo)==0:
            pulse_start=time.time()

        while GPIO.input(self.echo)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * self.convert
        distance = round(distance,2)

        return distance

if __name__ == "__main__":

    eyes = Range(24, 23)
    eyes.units("in")

    print eyes.distance(), eyes.unitStr
    time.sleep(1)
    print eyes.distance(), eyes.unitStr
    time.sleep(1)
    print eyes.distance(), eyes.unitStr
    time.sleep(1)
    print eyes.distance(), eyes.unitStr
    time.sleep(1)
    print ("Done.")

