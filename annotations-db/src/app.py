import mongoManager
from flask import Flask, jsonify, request
from annotation import annotations






app = Flask(__name__)



@app.route('/', methods = [ 'GET' ])
def hello ():
    return jsonify({'response': 'hello!!'})

@app.route('/annotations', methods = [ 'GET' ])
def annotationsHandler():
    conn = mongoManager.mongoConnection()
    return jsonify(mongoManager.mongoFind(conn,'annotaions', request.form['group'], request.form))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4001, debug=True)
