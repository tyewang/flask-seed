import os

from flask.ext.migrate import MigrateCommand
from invoke import task, Collection

os.environ["ENV"] = "DEVELOPMENT"
from app import app, db

@task(aliases=['run'])
def run_server():
    app.run(debug=True)

@task(aliases=['reset'])
def reset_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

@task
def migrate(command):
    MigrateCommand.app = app
    MigrateCommand.handle('', [command])

namespace = Collection('development')
for tasks in [run_server, reset_database, migrate]:
    namespace.add_task(tasks)
