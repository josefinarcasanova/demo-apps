import pymongo

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from icos import create_cos_client, get_cos_file

from os import environ, listdir
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def connect_to_database():
    try:
        # Connect to mongodb using pymongo
        mongo_connect_str = environ['MONGO_URL']

        print("------------------------------------------------")

        print("Dir before", listdir("."))

        tls_file = retreive_certificate()
        tls_file_name = environ['TLS_FILE_NAME']

        print("Dir after", listdir("."))


        print("\nConnect str:", mongo_connect_str)
        print("\ntls_file", tls_file)
        print("\ntls_file_name", tls_file_name)
            

        # Create a connection using MongoClient
        client = MongoClient(
            mongo_connect_str,
            tls=True,
            tlsCAFile=tls_file_name
        )

        print("\nclient", client)
        print("")

        database = client[environ['MONGO_DB_NAME']]

        return database
    
    except ConnectionFailure as err:
        print(err)        

def retreive_certificate():
    return get_cos_file(
        cos_client=None,
        bucket_name=None,
        file_name=environ['TLS_FILE_NAME'],
        file_key=environ['TLS_FILE_NAME']
    )

# Get all registries from collection
def get_data(database):
    if database == None:
        database = connect_to_database()

    # Select collection
    collection_name = environ['MONGO_COLLECTION_NAME']
    collection = database[collection_name]

    # Get all docs
    res = collection.find({})
    
    # Close database connection
    database.client.close()

    # Returns first item
    return res[0]

# Insert a JSON object into the database
def insert_data(database, json_object):
    # Create DB Client
    if database == None:
        database = connect_to_database()

    # Select collection
    collection_name = environ['MONGO_COLLECTION_NAME']
    collection      = database[collection_name]

    # Get collection size, pre insertion
    pre_count = collection.count_documents({})

    # Insert new item
    insert_result = collection.insert_one(json_object)

    # Get collection size, post insertion
    post_count = collection.count_documents({})
        
    # Close database connection
    database.client.close()

    #return insert_result
    return (pre_count + 1) == (post_count)