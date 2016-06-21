import flask
import json
import Servo
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

app = flask.Flask(__name__)
panServo = Servo.Servo(14)
tiltServo = Servo.Servo(15)

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
    return json.dumps({'cmd':'motor', 'value':speed})

@app.route('/motor/forward')
def motorForward():
    return json.dumps({'cmd':'motorForward'});

@app.route('/motor/reverse')
def motorReverse():
    return json.dumps({'cmd':'motorReverse'});

@app.route('/motor/stop')
def motorStop():
    return json.dumps({'cmd':'motorStop'});

app.run(host="10.0.0.30", debug=True)
# app.run(debug=True)
