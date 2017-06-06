from flask import Blueprint,json

bp_login = Blueprint("login", __name__)


@bp_login.route("/login")
def login():
    json1 = {"name":"登陆方法","id":1}

    return json.dumps(json1)

