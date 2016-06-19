import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)

pwm = GPIO.PWM(14, 100)

pwm.start(50)

cmd = raw_input(">> ")
while (cmd != "exit"):
    pwm.ChangeDutyCycle(int(cmd))
    cmd = raw_input(">> ")

GPIO.cleanup()