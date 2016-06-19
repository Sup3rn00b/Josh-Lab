import RPi.GPIO as GPIO

class Servo:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 100)
        self.pwm.start(10);

    def moveTo(self, degrees):
        self.pwm.ChangeDutyCycle(degrees)

    def stop(self):
        self.pwm.stop()



