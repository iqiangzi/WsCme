# -*- coding:utf-8 -*-
from flask_restful import Resource,fields,marshal_with,reqparse
from app_api.entity.examination.training_institution import TrainingInstitution, TrainingInstitutionCategory
from app_api.entity.examination import *
import json
from app_api.database import db_session
from datetime import datetime

resource_fields={
    "Name":fields.String
}

parser = reqparse.RequestParser()
parser.add_argument('rate',type=int,help="rate is int")
# args = parser.parse_args()


class RestFul(Resource):
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
        t = TrainingInstitutionCategory()
        t.Name = "公共科目"
        t.Desc = 0
        db_session.add(t)
        db_session.commit()

        # return {c for c in t.__dict__}

        return t.to_dict()
