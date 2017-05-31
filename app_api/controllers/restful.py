from flask_restful import  Resource

class RestFul(Resource):
    def get(self):
        return {"a":"b"}