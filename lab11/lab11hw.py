import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class ViewFinder:
    def __init__(self,trig,echo):
        self.trigger=trig
        self.echo=echo
        GPIO.setup(trig,GPIO.OUT)
        GPIO.setup(echo,GPIO.IN)
        time.sleep(1)

    def sendSignal(self):

	print("1")

        GPIO.output(self.trigger,False)
        time.sleep(0.5)

        GPIO.output(self.trigger,True)
        time.sleep(0.00001)
        GPIO.output(self.trigger,False)

	print("2")

        while GPIO.input(self.echo)==0:
            pulse_start=time.time()

        while GPIO.input(self.echo)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance,2)

	print("3")

        return distance

if __name__ == "__main__":

    print("4")

    eyes = ViewFinder(14,15)

    print (eyes.sendSignal(),"centimeters")
    time.sleep(1)
    print (eyes.sendSignal(),"centimeters")
    time.sleep(1)
    print (eyes.sendSignal(),"centimeters")
    time.sleep(1)
    print (eyes.sendSignal(),"centimeters")
    time.sleep(1)
    print ("Done.")
