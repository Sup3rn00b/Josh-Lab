import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trig=14
echo=15
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

#Motor
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
P=GPIO.PWM(18,100)
P.start(50)
GPIO.output(17,0)
GPIO.output(27,1)


GPIO.output(trig, False)
print "Waiting..."
time.sleep(2)
def distance():
    #GPIO.output(trig, False)
    #print "Waiting..."
    #time.sleep(2)

    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)

    while GPIO.input(echo)==0:
        pulse_start=time.time()

    while GPIO.input(echo)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance,2)

    return distance

inp="..."
while not (inp=="quit"):
    dist=distance()
    print "Distance:",dist,"cm."
    if dist<=50:
        speed=((50-dist)*2)
        print (speed)
        P.ChangeDutyCycle(speed)
        
        
