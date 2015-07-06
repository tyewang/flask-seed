import os
from functools import wraps

from flask.ext.migrate import MigrateCommand, Migrate
from invoke import run, task, Collection

from data.populate_development_data import populate

def _setup_environment(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        os.environ["ENV"] = os.environ.get("ENV", "DEVELOPMENT")
        return func(*args, **kwargs)
    return decorator

@task(aliases=['console'])
@_setup_environment
def start_console():
    run('ipython', pty=True)

@task(aliases=['run'])
@_setup_environment
def run_server():
    from app import app
    app.run(debug=True)

@task(aliases=['reset'])
@_setup_environment
def reset_database():
    from app import app, db
    with app.app_context():
        db.drop_all()
        db.create_all()
        populate(db)

@task
# no _setup_environment because decorators break invoke argument passing
def migrate(command):
    os.environ["ENV"] = os.environ.get("ENV", "DEVELOPMENT")
    from app import app, db
    Migrate(app, db)
    MigrateCommand.app = app
    MigrateCommand.handle('', [command])

namespace = Collection('development')
for tasks in [start_console, run_server, reset_database, migrate]:
    namespace.add_task(tasks)
