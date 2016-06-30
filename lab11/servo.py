import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Servo:


    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 100)
        self.pwm.start(10);

    def numToDegrees(self, num):
        val = int(num)
        return (val*.1) + 5

    def moveTo(self, num):
        deg = self.numToDegrees(num)
        self.pwm.ChangeDutyCycle(deg)

    def stop(self):
        self.pwm.stop()

if __name__ == "__main__":

    gearbox=Servo(18)

    gearbox.moveTo(90)
    time.sleep(0.5)
    gearbox.moveTo(45)