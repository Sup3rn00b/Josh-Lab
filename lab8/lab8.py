import flask
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
GPIO.setup (14,GPIO.OUT)

app=flask.Flask(__name__)

@app.route("/")
def hello():
    return flask.send_from_directory("static", "index.html")

@app.route('/readData')
def readData():
    return flask.jsonify({'data':42})

@app.route('/lightOn')
def lightMeUp():
    GPIO.output (14,1)
    return flask.jsonify({'pin':"Yeah ok I did it"})


@app.route('/lightOff')
def shutMeDown():
    GPIO.output (14,0)
    return flask.jsonify({'pin':"Yeah ok I stopped it"})

app.run(host='10.0.0.30', port=5000, debug=True)

