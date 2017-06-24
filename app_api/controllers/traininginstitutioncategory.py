from flask import Blueprint, json, request, abort, jsonify
from app_api.common.db import get_rows, get_lists, add, get_row_by_id, edit, delete
from app_api.entity.examination.training_institution import TrainingInstitutionCategory
from . import checkrequestjson

bp_trainingstitutioncategory = Blueprint("trainingstitutioncategory", __name__, url_prefix="/trainingstitutioncategory")


@bp_trainingstitutioncategory.route("/", methods=["GET"])
def get():
    items = get_lists(TrainingInstitutionCategory, TrainingInstitutionCategory.Id != "")

    return jsonify(success=True, data=[
        {
            "id": l.Id,
            "name": l.Name,
            "created": l.Created.isoformat(),
            "desc": l.Desc
        }
        for l in items])


@bp_trainingstitutioncategory.route("/<string:id>", methods=["GET"])
def get_by_id(id):
    row = get_row_by_id(TrainingInstitutionCategory, id)
    return jsonify(success=True, date={
        "id": row.Id,
        "name": row.Name,
        "created": row.Created.isoformat(),
        "desc": row.Desc
    })


@bp_trainingstitutioncategory.route("/", methods=["POST"])
@checkrequestjson(need=["name"])
def post():
    category_info = {"Name": request.json["name"]}
    addkey_category = add(TrainingInstitutionCategory, category_info)
    if len(addkey_category) == 32:
        return jsonify({"success": True, "date": addkey_category})
    else:
        return jsonify({"success": False, "date": None})


@bp_trainingstitutioncategory.route("/", methods=["PUT"])
@checkrequestjson(need=["id"])
def put():
    category_info = {}
    if "name" in request.json:
        category_info.update(Name=request.json["name"])
    if "desc" in request.json:
        category_info.update(Desc=request.json["desc"])
    result = edit(TrainingInstitutionCategory, request.json["id"], category_info)
    if result > 0:
        return jsonify({"success": True})


@bp_trainingstitutioncategory.route("/<string:id>", methods=["DELETE"])
def delete_by_id(id):
    delete(TrainingInstitutionCategory, id)
    return jsonify({"success":True})
    pass
