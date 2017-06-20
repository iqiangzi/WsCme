from flask import Blueprint, json, request, abort, jsonify
from app_api.common.db import get_rows, get_lists
from app_api.entity.examination.training_institution import TrainingInstitutionCategory
from . import checkrequestjson

bp_trainingstitutioncategory = Blueprint("trainingstitutioncategory", __name__, url_prefix="/trainingstitutioncategory")


@bp_trainingstitutioncategory.route("/", methods=["GET"])
def get():
    items = get_lists(TrainingInstitutionCategory, TrainingInstitutionCategory.Id != "")

    return jsonify(success=True, data=[
        {
            "id": l.Id,
            "name": l.Name
        }
        for l in items])


@bp_trainingstitutioncategory.route("/", methods=["POST"])
@checkrequestjson(need=["name","dd"])
def post():

    s = request.get_json()
    print(s)
    # if not request.json:
    #     abort(400)
    # checklist = [c for c in TrainingInstitutionCategory.__dict__ if not c.startswith("_") and c !="metadata" and c != "_sa_class_manager"]
    # requestlist = [c for c in request.json.keys()]
    # intersection = set(checklist) & set(requestlist)
    # # print(intersection)
    # print(requestlist)
    # if len(intersection) != len(checklist):
    #     abort(400)

    return jsonify({"success": True})
