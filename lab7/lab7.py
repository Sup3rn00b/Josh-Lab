from flask import Flask
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([14,15],GPIO.OUT)
GPIO.output([14,15],0)



app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World again</h1>"
#stuart
@app.route('/start')
def startmotor():
    GPIO.output(14,1)
    GPIO.output(15,0)
    return "OK! I started!";
#rev
@app.route('/rev')
def revmotor():
    GPIO.output(14,0)
    GPIO.output(15,1)
    return "Look Mom! I'm going in reverse";
#stop    
@app.route('/stop')
def stopmotor():
    GPIO.output(14,0)
    GPIO.output(15,0)
    return "I'm tired. stopping now.";


if __name__ == '__main__' :
    app.run(debug=True,host='10.0.0.30')
