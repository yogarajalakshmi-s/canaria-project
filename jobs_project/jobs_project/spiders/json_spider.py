import os
import json
import scrapy
from pymongo import MongoClient

class JSONSpider(scrapy.Spider):
    name = 'JSONSpider'

    def start_requests(self):
        mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
        self.client = MongoClient(mongo_uri)
        self.db = self.client["job_data"]
        self.collection = self.db["jobs"]

        data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        data_dir = os.path.abspath(data_dir)

        for file_name in os.listdir(data_dir):
            if file_name.endswith(".json"):
                file_path = os.path.join(data_dir, file_name)
                yield scrapy.Request(
                    url=f'file://{file_path}',
                    callback=self.parse_json,
                    meta={'file_path': file_path}
                )

    def parse_json(self, response):
        file_path = response.meta['file_path']
        with open(file_path, 'r', encoding='utf-8') as f:
            jobs = json.load(f)

        for job in jobs:
            self.collection.insert_one(job)
            yield job
