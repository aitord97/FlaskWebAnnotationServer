from flask import Flask, jsonify, request
import psycopg2
def dbCursor () :
    
    try:
        connection = psycopg2.connect(
            user = "postgres",
            password = "admin",
            host = "0.0.0.0",
            port = "5432",
            database = "annotations-db")
        return connection, connection.cursor()
    except :
        print("error")

app = Flask(__name__)
conn, dbCursor = dbCursor()
@app.route('/', methods = [ 'GET' ])
def hello ():
    return jsonify({'response': 'hello im users api!!'})

@app.route('/users', methods = [ 'GET' ])
def getUsers ():
    dbCursor.execute("SELECT * FROM users")
    response = jsonify(dbCursor.fetchall())
    return response
@app.route('/user', methods = [ 'POST' ])
def setUser():
    dbCursor.execute("INSERT INTO users(name) VALUES ('"+request.form['name']+"')")
    conn.commit()
    return "OK", 200



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4002, debug=True)
