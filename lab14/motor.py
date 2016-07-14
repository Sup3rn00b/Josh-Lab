import RPi.GPIO as GPIO
import time

class Motor:

    def __init__(self, forward, reverse, pwm, standby=3):
        GPIO.setmode(GPIO.BCM)

        self.forwardPin = forward
        self.reversePin = reverse
        self.pin_pwm = pwm
        self.pin_stdby = standby

        GPIO.setup(self.forwardPin, GPIO.OUT)
        GPIO.setup(self.reversePin, GPIO.OUT)
        GPIO.setup(self.pin_pwm, GPIO.OUT)
        GPIO.setup(self.pin_stdby, GPIO.OUT)

        GPIO.output(self.forwardPin, 0)
        GPIO.output(self.reversePin, 0)
        GPIO.output(self.pin_stdby, 1)

        self.p = GPIO.PWM(self.pin_pwm, 100)
        self.p.start(50)
        self.currentDutyCycle = 50

    def forward(self):
        GPIO.output(self.reversePin, 0)
        GPIO.output(self.forwardPin, 1)

    def reverse(self):
        GPIO.output(self.forwardPin, 0)
        GPIO.output(self.reversePin, 1)

    def stop(self):
        GPIO.output(self.forwardPin, 1)
        GPIO.output(self.reversePin, 1)
        time.sleep(.2)
        GPIO.output(self.forwardPin, 0)
        GPIO.output(self.reversePin, 0)

    def speed(self, amount):
        self.p.ChangeDutyCycle(float(amount))
        self.currentDutyCycle = float(amount)

    def enable(self,value):
        GPIO.output(self.pin_stdby, value)


if __name__ == "__main__":

    car = Motor(23,24, 18)

    print car

    cmd = raw_input("cmd>> ")
    go = True
    while (go):
        if (cmd == 'q'):
            go = False
        elif (cmd == 'f'):
            car.forward()
        elif (cmd == 'r'):
            car.reverse()
        elif (cmd == 's'):
            dc = saveDC = car.currentDutyCycle

            while (dc > 30):
	        car.speed(dc)
	        dc = dc - 2;
		time.sleep(.1)
            car.stop()
            car.speed(saveDC)
        elif (cmd == 'g'):
	    speed = raw_input("Gas: ")
	    car.speed(speed)
        else:
            car.stop()
        cmd = raw_input("cmd>> ")



