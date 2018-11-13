# coding: utf-8
import logging

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.models import db
from app.main import create_app

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


@manager.command
def dropdb():
    """drop all database
    """
    db.drop_all()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s# %(message)s",
                        datefmt="%Y/%m/%d-%H:%M:%S")
    print(app.url_map)
    manager.run()
