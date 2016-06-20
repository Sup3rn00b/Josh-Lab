import flask
import json

app = flask.Flask(__name__)

@app.route("/home/<path>")
def index(path):
    return flask.send_from_directory("", path)

@app.route("/home/lib/<path>")
def lib(path):
    return flask.send_from_directory("lib", path)

@app.route("/forward")
def goForward():
    return json.dumps({'value':'going forward'})

@app.route('/stop')
def stopNow():
    return json.dumps({'value':'stoping'})

app.run(host="10.0.0.30", debug=True)
