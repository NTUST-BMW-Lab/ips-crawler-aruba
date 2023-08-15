import json
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId

load_dotenv()


class Database:
    def __init__(self):
        self.uri = os.getenv('DB_URI')
        self.db_name = 'wifi_crawl'
        self.client = None
        self.db = None

    def connect(self):
        try:
            if self.uri and self.db_name:
                self.client = MongoClient(self.uri)
                self.db = self.client[self.db_name]
                print("Connected to the MongoDB database successfully!")
            else:
                raise ValueError("Missing MongoDB environment variables.")
        except Exception as e:
            print("An error occurred while connecting to the database:", e)

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def insert_documents(self, collection_name, documents):
        collection = self.get_collection(collection_name)

        formatted_documents = []
        for essid, values in documents.items():
            document = {
                '_id': ObjectId(),
                'essid': essid,
                'count': values['count']
            }
            for ap_name, rssi in values.items():
                if ap_name not in ['count']:
                    document[ap_name] = rssi
            formatted_documents.append(document)

        if formatted_documents:
            collection.insert_many(formatted_documents)
            print("Documents inserted successfully!")
        else:
            print("No documents to insert.")

    def insert_raw_documents(self, collection_name, documents):
        formatted_documents = []

        if 'Monitored AP Table' in documents and isinstance(documents['Monitored AP Table'], list):
            monitored_ap_table = documents['Monitored AP Table']
            print(documents)

            # Iterate through each entry in the 'Monitored AP Table' and add 'ap_name' to each document
            for entry in monitored_ap_table:
                # Create a new formatted document with 'ap_name' and 'new_column' included
                entry['ap_name'] = documents['ap_name']
                entry['count'] = documents['count']
                entry['timestamp'] = documents['timestamp']
                entry['Radio0_EIRP'] = documents['Radio0_EIRP']
                entry['Radio1_EIRP'] = documents['Radio1_EIRP']

                # Add the formatted document to the list
                formatted_documents.append(entry)

        print(formatted_documents)
        collection = self.get_collection(collection_name)
        collection.insert_many(formatted_documents)

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None
            print("Connection to the MongoDB database closed.")
