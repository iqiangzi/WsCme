from flask_restful import Resource,fields,marshal_with,reqparse
# from app_api.entity.examination.training_institution import TrainingInstitution, Category
from app_api.entity.examination import *
import json
from app_api.database import db
from datetime import datetime

# resource_fields={
#     "Created":fields.String
# }

parser = reqparse.RequestParser()
parser.add_argument('rate',type=int,help="rate is int")
# args = parser.parse_args()


class RestFul(Resource):
    def post(self):
        args = parser.parse_args(strict=True)

        return args["rate"]
    # @marshal_with(resource_fields,envelope='')
    def get(self):

        category = db.session.query(Category).first()
        value = category.Id
        traininginstitution = db.session.query(TrainingInstitution).first()
        traininginstitution.Category.append(Category(Id=value))
        # db.session.commit()

        # traininginstitution.Category.remove(category)
        db.session.commit()

        return category.to_dict()

