from main import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# This will be a command for the 'db' command, example: python manager.py db migrate
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()