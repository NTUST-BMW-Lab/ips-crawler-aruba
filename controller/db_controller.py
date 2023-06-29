import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
mongo_db = os.getenv('MONGO_DB')
mongo_port = os.getenv('MONGO_PORT')
mongo_client = os.getenv('MONGO_CLIENT')

client = MongoClient(mongo_client, int(mongo_port))
db = client[mongo_db]

def put_json_to_db(json_data, collection_name):
    '''
    put_json_to_db: Puts JSON Data to Mongo Database
        Parameters:
            - json_data: JSON Data
            - collection_name: Database Collection in which the data will be stored
    '''
    collection = db[collection_name]

    collection.insert_many(json_data)
