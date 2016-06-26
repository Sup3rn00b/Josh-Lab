import RPi.GPIO as GPIO

class Motor:

    def __init__(self, pin, pin2, pinpwm):
        self.pin = pin
        self.pin2 = pin2
        self.pinpwm = pinpwm
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pinpwm, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)

	GPIO.output(self.pin, 0)
	GPIO.output(self.pin2, 0)
        GPIO.output(3,1)

        self.pwm = GPIO.PWM(self.pinpwm, 100)
        self.pwm.start(50)

    def setSpeed(self, speed):
        self.pwm.ChangeDutyCycle(float(speed))

    def forward(self):
        GPIO.output(self.pin,1)
        GPIO.output(self.pin2,0)

    def reverse(self):
        GPIO.output(self.pin,0)
        GPIO.output(self.pin2,1)

    def stop(self):
        #self.pwm.stop()
        GPIO.output(self.pin,0)
        GPIO.output(self.pin2,0)


