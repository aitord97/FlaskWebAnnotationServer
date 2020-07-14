
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

conn, dbCursor = dbCursor()

dbCursor.execute("CREATE TABLE users( id SERIAL PRIMARY KEY, name VARCHAR(30))")
dbCursor.execute("INSERT INTO users(name) VALUES ('aitor')")
conn.commit()

dbCursor.close()
conn.close()