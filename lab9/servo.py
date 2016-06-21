import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)

pwm = GPIO.PWM(14, 100)

pwm.start(50)

def scale(val):
    ival = int(val)
    return ival*(.1) + 5.

cmd = raw_input(">> ")
while (cmd != "exit"):
    pwm.ChangeDutyCycle(scale(cmd))
    cmd = raw_input(">> ")

GPIO.cleanup()
