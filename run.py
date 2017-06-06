import os
from app_api import create_app
from app_api.database import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

app = create_app("default")

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(use_debugger=True))

if __name__ == "__main__":
    manager.run()
    # app.run()
