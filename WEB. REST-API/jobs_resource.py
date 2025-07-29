from flask_restful import Resource, reqparse
from models import Job

class JobsResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('description', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('user_id', type=int, required=True, help="This field cannot be left blank!")

    def get(self, job_id):
        job = Job.find_by_id(job_id)
        if job:
            return job.json()
        return {'message': 'Job not found'}, 404

    def delete(self, job_id):
        job = Job.find_by_id(job_id)
        if job:
            job.delete_from_db()
            return {'message': 'Job deleted.'}
        return {'message': 'Job not found'}, 404

    def put(self, job_id):
        data = JobsResource.parser.parse_args()
        job = Job.find_by_id(job_id)
        if job:
            job.title = data['title']
            job.description = data['description']
            job.user_id = data['user_id']
            job.save_to_db()
            return job.json()
        return {'message': 'Job not found'}, 404

class JobsListResource(Resource):
    def get(self):
        return {'jobs': [job.json() for job in Job.query.all()]}

    def post(self):
        data = JobsResource.parser.parse_args()
        job = Job(**data)
        job.save_to_db()
        return job.json(), 201
