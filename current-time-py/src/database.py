import pymongo

from pymongo import MongoClient
from os import environ

def connect_to_database():
    # Connect to mongodb using pymongo
    CONNECTION_STRING = environ['MONGO_URL']

    TLS_FILE = environ['TLS_FILE_PATH']

    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING, tls=True, tlsCAFile=TLS_FILE)

    database = client[environ['MONGO_DB_NAME']]

    return database

# Get all registries from collection
def get_data():
    database = connect_to_database()

    # Select collection
    collection_name = environ['COLLECTION_NAME']
    collection = database[collection_name]

    # Get all docs
    res = collection.find({})
    
    # Close database connection
    database.client.close()

    # Returns first item
    return res[0]

# Insert a JSON object into the database
def insert_data(json_object):
    # Create DB Client
    database = connect_to_database()

    # Select collection
    collection_name = environ['COLLECTION_NAME']
    collection      = database[collection_name]

    # Insert new item
    insert_result = collection.insert_one(json_object)
        
    # Close database connection
    database.client.close()

    #return insert_result
    return insert_result.inserted_id != None 