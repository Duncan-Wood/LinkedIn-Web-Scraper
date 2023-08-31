""" This is the main file of the Jobs API. It contains the routes and the logic of the API. """
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def load_jobs_from_file(file_path):
    """ Load jobs from a JSON file. """
    with open(file_path, 'r', encoding="utf8") as file:
        jobs_data = json.load(file)
    return jobs_data

# Load jobs from the JSON file
jobs = load_jobs_from_file('../basic_scrapy_spider/jobs.json')

@app.route('/', methods=['GET'])
def home():
    """ Home route."""
    routes = {
        "routes": {
            "home": "/",
            "get_jobs": "/jobs",
            "get_job_by_index": "/jobs/<int:index>",
            "create_job": "/jobs",
            "update_job": "/jobs/<int:index>",
            "delete_job": "/jobs/<int:index>"
        }
    }
    return jsonify(routes)

@app.route('/jobs', methods=['GET'])
def get_all_jobs():
    """ Get all jobs."""
    return jsonify(jobs)

@app.route('/jobs/<int:index>', methods=['GET'])
def get_job_by_index(index):
    """ Get a job by its index."""
    if 0 <= index < len(jobs):
        return jsonify(jobs[index])
    return jsonify({"message": "Job not found"}), 404

@app.route('/jobs', methods=['POST'])
def create_job():
    """ Create a new job."""
    new_job = request.json
    jobs.append(new_job)
    return jsonify({"message": "Job created successfully", "job": new_job}), 201

@app.route('/jobs/<int:index>', methods=['PUT'])
def update_job(index):
    """ Update a job by its index."""
    if 0 <= index < len(jobs):
        updated_job = request.json
        jobs[index].update(updated_job)
        return jsonify({"message": "Job updated successfully", "job": jobs[index]})
    return jsonify({"message": "Job not found"}), 404

@app.route('/jobs/<int:index>', methods=['DELETE'])
def delete_job(index):
    """ Delete a job by its index."""
    if 0 <= index < len(jobs):
        deleted_job = jobs.pop(index)
        return jsonify({"message": "Job deleted successfully", "job": deleted_job})
    return jsonify({"message": "Job not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
