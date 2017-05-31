import os
from app_api import create_app
from app_api.database import db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

app = create_app("default")
manager = Manager(app)

# with app.test_request_context():
from app_api.entity import roles,user
migrate = Migrate(app,db)
    # db.create_all()
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()
