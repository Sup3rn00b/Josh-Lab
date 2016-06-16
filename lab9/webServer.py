import flask
import json

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.send_from_directory("static", "index.html")

@app.route("/forward")
def goForward():
    return json.dumps({'value':'going forward'})

@app.route('/stop')
def stopNow():
    return json.dumps({'value':'stoping'})

app.run(debug=True)
