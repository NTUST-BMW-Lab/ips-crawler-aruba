import os
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.uri = 'mongodb://140.118.123.112:27017/'
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
        ap_documents = []
        for ap in documents:
            ap_document = {
                'curr-rssi': ap['curr-rssi'],
                'essid': ap['essid'],
                'bssid': ap['bssid'],
                'ap-type': ap['ap-type'],
                'ap-name': ap['ap_name']
            }
            ap_documents.append(ap_document)

        collection = self.get_collection(collection_name)
        collection.insert_many(ap_documents)
        print("Documents inserted successfully!")

    def close(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db = None
            print("Connection to the MongoDB database closed.")
