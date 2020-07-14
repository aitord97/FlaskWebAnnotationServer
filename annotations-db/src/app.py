from flask import Flask, jsonify
from annotation import annotations




app = Flask(__name__)




@app.route('/', methods = [ 'GET' ])
def hello ():
    return jsonify({'response': 'hello!!'})

@app.route('/annotations', methods = [ 'GET' ])
def annotationsHandler ():
    return jsonify(annotations)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4001, debug=True)
