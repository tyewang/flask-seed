import os

from flask.ext.migrate import MigrateCommand, Migrate
from invoke import task, Collection

@task
def migrate_upgrade():
    os.environ["ENV"] = os.environ.get("ENV", "PRODUCTION")
    from app import app, db
    Migrate(app, db)
    MigrateCommand.app = app
    MigrateCommand.handle('', ['upgrade'])

namespace = Collection('production')
for tasks in [migrate_upgrade]:
    namespace.add_task(tasks)
