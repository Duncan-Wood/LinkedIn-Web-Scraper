import json

def add_indices_to_jobs(file_path):
    with open(file_path, 'r') as file:
        jobs_data = json.load(file)
    
    for index, job in enumerate(jobs_data):
        job["index"] = index

    with open(file_path, 'w') as file:
        json.dump(jobs_data, file, indent=2)

if __name__ == '__main__':
    jobs_json_file = '../basic_scrapy_spider/jobs.json'  # Update with the correct path
    add_indices_to_jobs(jobs_json_file)
