from pymongo import MongoClient
import logging
import os

class MongoDBConnector:
    def __init__(self, uri=None, db_name="job_data", collection_name="jobs"):
        self.uri = uri or os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.client = MongoClient(self.uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        logging.debug(f"Connected to MongoDB at {uri}")

    def find_all(self):
        return list(self.collection.find())

    def insert_item(self, item):
        try:
            return self.collection.insert_one(item)
        except Exception as e:
            print(f"Error inserting item: {e}")
            return None

    def item_exists(self, query):
        return self.collection.find_one(query) is not None
