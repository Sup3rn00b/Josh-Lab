import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)

P=GPIO.PWM(15,100)
P.start(0)
com= raw_input("Hey nerd gime a numba: : ")

while not (com=="q"):
    P.ChangeDutyCycle(int(com))
    print "."
    com= raw_input("Hey nerd gime a numba: : ")

GPIO.cleanup()
