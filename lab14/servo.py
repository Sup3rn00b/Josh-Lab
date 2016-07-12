import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Servo:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 100)
        self.pwm.start(10);

    def DegreesToNum(self, deg):
        val = int(num)
        return (.18)*deg + 5

    def numToDegrees(self, num):
        val = int(num)
        return (val*.1) + 5

    def moveTo(self, num):
        deg = self.numToDegrees(num)
        print "PWM Setting: ", deg
        self.pwm.ChangeDutyCycle(deg)

    def stop(self):
        self.pwm.stop()

if __name__ == "__main__":
    gearbox=Servo(18)

    cmd = raw_input(">> ")
    while (cmd != "q"):
        gearbox.moveTo(int(cmd))
        cmd = raw_input(">> ")

    GPIO.cleanup()
