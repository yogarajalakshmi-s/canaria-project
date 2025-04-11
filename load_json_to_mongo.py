import json
import os
from infra.mongo_connector import MongoDBConnector

def load_jobs_from_json(data_dir="data"):
    connector = MongoDBConnector()

    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(data_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                jobs = data.get("jobs", [])
                print(f"Processing {len(jobs)} jobs from {filename}")

                inserted = 0
                for job in jobs:
                    if isinstance(job, str):
                        job = job.strip()
                        if not job:
                            continue
                        try:
                            job = json.loads(job)
                        except json.JSONDecodeError:
                            print(f"Skipping invalid job string: {job}")
                            continue

                    if not isinstance(job, dict):
                        print(f"Skipping job that's not a dict: {job}")
                        continue

                    if not connector.item_exists({"title": job.get("title")}):
                        connector.insert_item(job)
                        inserted += 1

                print(f"Inserted {inserted} new jobs from {filename}")

if __name__ == "__main__":
    load_jobs_from_json()
