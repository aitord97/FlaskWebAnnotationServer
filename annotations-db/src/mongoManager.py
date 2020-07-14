from pymongo import MongoClient, errors

def mongoConnection():
    try:
        client = MongoClient(
            host = [ 'mongodb' ],
            serverSelectionTimeoutMS = 3000, # 3 second timeout
            username = "root",
            password = "operator",
        )
        return client
    except errors.ServerSelectionTimeoutError as err:
        print(err)

def mongoFind(connection, database, collection, query):
    return list(connection[database][collection].find(query))