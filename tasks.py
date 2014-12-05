import os

from flask.ext.migrate import MigrateCommand
from invoke import task, run, Collection

from app import flask_app, db

@task(default=True)
def run_tests():
    os.environ["ENV"] = "TEST"
    run('nosetests tests/')

@task()
def clear_pyc():
    run('find . -name "*.pyc" -delete')

@task
def reset_database():
    db.drop_all()
    db.create_all()

@task
def migrate(command):
    MigrateCommand.app = flask_app
    MigrateCommand.handle('', [command])

namespace = Collection()
for root_tasks in [run_tests, clear_pyc]:
    namespace.add_task(root_tasks)

db_tasks = Collection('db')
for db_task in [reset_database, migrate]:
    db_tasks.add_task(db_task)

namespace.add_collection(db_tasks)
