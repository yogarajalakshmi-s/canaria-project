import csv
from infra.mongo_connector import MongoDBConnector

def export_jobs_to_csv(filename="final_jobs.csv"):
    connector = MongoDBConnector()
    jobs = connector.find_all()

    if not jobs:
        print("No jobs found in the database.")
        return

    for job in jobs:
        job.pop('_id', None)

    fieldnames = jobs[0].keys()

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs)

    print(f"Exported {len(jobs)} jobs to {filename}.")

if __name__ == "__main__":
    export_jobs_to_csv()
