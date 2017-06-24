from flask import Blueprint
from app_api.service.trainingstitution import TrainingstitutionService
from app_api.common.db import add
from app_api.entity.examination import TrainingInstitution
from . import checkrequestjson

bp_traininginstitution = Blueprint("traininginstitution",__name__,url_prefix="/traininginstitution")

@bp_traininginstitution.route("/",methods=["POST"])
@checkrequestjson(TrainingInstitution,"Id","Desc")
def post():

    pass