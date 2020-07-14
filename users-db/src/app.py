from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/', methods = [ 'GET' ])
def hello ():
    return jsonify({'response': 'hello im users api!!'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4002, debug=True)
