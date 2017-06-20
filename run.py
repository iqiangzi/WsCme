from app_api import create_app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app_api.database import db_session,init_db
from flask import make_response,jsonify

app = create_app("default")

manager = Manager(app)

migrate = Migrate(app, db_session)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(use_debugger=True))



if __name__ == "__main__":
    manager.run()
    # app.run()