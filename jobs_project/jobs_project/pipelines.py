# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../infra'))

from infra.mongo_connector import MongoDBConnector
from infra.redis_connector import RedisConnector
import scrapy

class JobsProjectPipeline:
    def __init__(self):
        self.mongo = MongoDBConnector('mongodb://localhost:27017/', 'jobs_db', 'raw_table')
        self.collection = self.mongo.collection

    def process_item(self, item, spider):
        if not self.collection.find_one({"job_id": item.get("job_id")}):
            self.collection.insert_one(dict(item))
        return item


class RedisPipeline:
    def __init__(self):
        self.redis = RedisConnector()

    def process_item(self, item, spider):
        unique_key = item.get("job_id")

        if not unique_key:
            raise scrapy.exceptions.DropItem(f"Missing or invalid 'job_id' in item: {item}")

        if self.redis.is_duplicate(unique_key):
            raise scrapy.exceptions.DropItem(f"Duplicate item found: {unique_key}")
        else:
            self.redis.mark_as_scraped(unique_key)
            return item

