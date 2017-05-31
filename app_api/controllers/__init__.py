from flask import Blueprint
import redis

bp_main = Blueprint("views",__name__)

@bp_main.route("/")
@bp_main.route("/index")
def index():
    redis_store = redis.StrictRedis(host='localhost', db=4)
    redis_store.set("token")
    return "hello world"