import flask
import json
import RPi.GPIO as GPIO

import Servo
import Motor

GPIO.setmode(GPIO.BCM)

app = flask.Flask(__name__)
panServo = Servo.Servo(24)
tiltServo = Servo.Servo(25)
motor = Motor.Motor(14,15,18)

motor.forward()
motor.setSpeed(0)

@app.route("/home/<path>")
def index(path):
    return flask.send_from_directory("", path)

@app.route("/home/lib/<path>")
def lib(path):
    return flask.send_from_directory("lib", path)

@app.route("/pan/<pan>")
def setPan(pan):
    panServo.moveTo(pan)
    return json.dumps({'cmd':'pan', 'value':pan})

@app.route('/tilt/<tilt>')
def setTilt(tilt):
    tiltServo.moveTo(tilt)
    return json.dumps({'cmd':'tilt', 'value':tilt})

@app.route('/motor/speed/<speed>')
def stopNow(speed):
    motor.setSpeed(int(speed))
    return json.dumps({'cmd':'motor', 'value':speed})

@app.route('/motor/forward')
def motorForward():
    motor.forward()
    return json.dumps({'cmd':'motorForward'});

@app.route('/motor/reverse')
def motorReverse():
    motor.reverse()
    return json.dumps({'cmd':'motorReverse'});

@app.route('/motor/stop')
def motorStop():
    motor.stop()
    return json.dumps({'cmd':'motorStop'});

app.run(host="10.0.0.30", debug=True)
# app.run(debug=True)
