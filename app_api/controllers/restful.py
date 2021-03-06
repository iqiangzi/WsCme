# -*- coding:utf-8 -*-
from flask_restful import Resource,fields,marshal_with,reqparse
from app_api.entity.examination.training_institution import TrainingInstitution, TrainingInstitutionCategory
from app_api.entity.examination import *
import json
from app_api.database import db_session
from datetime import datetime
from app_api.common.db import get_lists
from app_api.common.resouce_fields import resource_fields



parser = reqparse.RequestParser()
parser.add_argument('rate',type=int,help="rate is int")
# args = parser.parse_args()

resource_fields.update(Desc = fields.Integer)

class RestFul(Resource):
    def insert(self):
        return "aa"
    def post(self):
        args = parser.parse_args(strict=True)

        return args["rate"]
    @marshal_with(resource_fields,envelope='')
    def get(self):

        # category = db.session.query(Category).first()
        # value = category.Id
        # traininginstitution = db.session.query(TrainingInstitution).first()
        # traininginstitution.Category.append(Category(Id=value))
        # db.session.commit()

        # traininginstitution.Category.remove(category)
        result = get_lists(TrainingInstitutionCategory,TrainingInstitutionCategory.Name != "")

        # result.to_dict()
        # return {c for c in t.__dict__}
        re = {
            "success":True,
            "data":json.dumps(result)
        }

        return re
