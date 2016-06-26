import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class StepMotor:

    def __init__(self,a,b,c,d,e):
        self.apin=a
        self.bpin=b
        self.cpin=c
        self.dpin=d
        self.enablePin=e

        GPIO.setup(a,GPIO.OUT)
        GPIO.setup(b,GPIO.OUT)
        GPIO.setup(c,GPIO.OUT)
        GPIO.setup(d,GPIO.OUT)
        GPIO.setup(e,GPIO.OUT)

        self.enable(True)

    def setPins(self,a,b,c,d):
        GPIO.output(self.apin,a)
        GPIO.output(self.bpin,b)
        GPIO.output(self.cpin,c)
        GPIO.output(self.dpin,d)

    def step(self):
        self.setPins(1,0,1,0)
        self.setPins(0,1,1,0)
        self.setPins(0,1,0,1)
        self.setPins(1,0,0,1)

    def stepBack(self):
        self.setPins(1,0,0,1)
        self.setPins(0,1,0,1)
        self.setPins(0,1,1,0)
        self.setPins(1,0,1,0)

    def enable(self,setEnable):
        if setEnable==True:
            GPIO.output(self.enablePin,1)
        else:
            GPIO.output(self.enablePin,0)
            print("hi")

    def forward(self,steps):
        for x in range(steps):
            self.step()

    def backwards(self,steps):
        for x in range(steps):
            self.stepBack()

if __name__ == "__main__":
    stepMotor = StepMotor(14,15,18,23,24)
    choice=raw_input("Steps? >>>")
    while choice!="exit":
        stepMotor.forward(int(choice))
        choice=raw_input("Steps? >>>")
