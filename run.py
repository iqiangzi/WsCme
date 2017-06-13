from app_api import create_app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app_api.database import db_session,init_db

app = create_app("default")

manager = Manager(app)

migrate = Migrate(app, db_session)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(use_debugger=True))



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    init_db()
    manager.run()
    # app.run()