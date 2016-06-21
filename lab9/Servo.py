import RPi.GPIO as GPIO

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



