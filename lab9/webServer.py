import flask
import json

app = flask.Flask(__name__)

@app.route("/home/<path>")
def index(path):
    return flask.send_from_directory("", path)

@app.route("/home/lib/<path>")
def lib(path):
    return flask.send_from_directory("lib", path)

@app.route("/pan/<pan>")
def setPan(pan):
    return json.dumps({'cmd':'pan', 'value':pan})

@app.route('/tilt/<tilt>')
def setTilt(tilt):
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

# app.run(host="10.0.0.30", debug=True)
app.run(debug=True)