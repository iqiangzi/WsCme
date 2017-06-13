from flask import Flask
from config.config import config
from .database import init_db
from flask_restful import Api


def create_app(config_name):
    app = Flask(__name__)

    configobj = config["default"]
    app.config.from_object(configobj)
    configobj.init_app(app)
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

    # db.init_app(app)

    api = Api(app)

    from .controllers import bp_main
    from .controllers.login import bp_login

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_login)

    from .controllers.restful import RestFul
    api.add_resource(RestFul, '/users')

    return app
