from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from appserver import app
from app.database import db
import os, os.path

manager = Manager(app)

current_path = os.path.dirname(os.path.realpath(__file__))

migrations_dir = os.path.join(current_path, 'app', 'database', 'migrations')
migrate = Migrate(app, db, directory=migrations_dir)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()