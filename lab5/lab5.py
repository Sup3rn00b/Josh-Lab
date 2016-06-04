import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trig=14
echo=15
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
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
    print "Distance:",distance(),"cm."
    
