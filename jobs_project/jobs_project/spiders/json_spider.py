import os
import json
import scrapy
import csv

class JSONSpider(scrapy.Spider):
    name = 'json_spider'

    def __init__(self, *args, **kwargs):
        super(JSONSpider, self).__init__(*args, **kwargs)
        self.data_dir = '/app/jobs_project/data'

    def start_requests(self):
        for file_name in os.listdir(self.data_dir):
            if file_name.endswith(".json"):
                file_path = os.path.join(self.data_dir, file_name)
                yield scrapy.Request(
                    url=f'file://{file_path}',
                    callback=self.parse_json,
                    meta={'file_path': file_path}
                )

    def parse_json(self, response):
        try:
            data = json.loads(response.text)
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse JSON from {response.meta['file_path']}: {e}")
            return

        all_items = []

        if isinstance(data, dict):
            all_items = [data]
        elif isinstance(data, list):
            all_items = [item for item in data if isinstance(item, dict)]

        if not all_items:
            return

        # Get dynamic fieldnames from all keys
        all_keys = set()
        for item in all_items:
            all_keys.update(item.keys())
        fieldnames = sorted(all_keys)

        file_exists = os.path.exists('final_jobs.csv')

        with open('final_jobs.csv', mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists or os.path.getsize('final_jobs.csv') == 0:
                writer.writeheader()

            for item in all_items:
                writer.writerow(item)

        for item in all_items:
            yield item

