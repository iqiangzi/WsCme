from flask import Blueprint, make_response, jsonify
import redis
from app_api.database import db_session
from flask import request, abort
from app_api.common.exception_custom import ArgumentException
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import inspect

bp_main = Blueprint("views", __name__)


@bp_main.route("/")
@bp_main.route("/index")
def index():
    redis_store = redis.StrictRedis(host='localhost', db=4)
    redis_store.set("token")
    return "hello world"


@bp_main.app_errorhandler(404)
def notfound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@bp_main.teardown_app_request
def shutdown_session(exception=None):
    db_session.remove()


def checkrequestjson(*arg, **kwargs):
    def _check(fun):
        def Wrapper():

            if not request.method:
                return
            if not request.json:
                abort(400)
            custom_dict = []
            checklist = []
            igon = arg[1:]
            if kwargs:
                custom_dict = kwargs.pop("need", [])

            if arg:
                if not isinstance(arg[0], DeclarativeMeta):
                    raise ArgumentException("check装饰器的第一个参数必须是sqlalchemy的模型类")
                else:
                    checklist = [c.name for c in inspect(arg[0]).columns if c.name not in igon]

            checklist = set(checklist) | set(custom_dict)
            requestlist = set(request.json.keys())
            if len(checklist & requestlist) != len(checklist):
                abort(400)
            return fun()

        return Wrapper

    return _check
