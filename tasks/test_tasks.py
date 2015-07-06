import os
from functools import wraps

from invoke import task, run, Collection

def _setup_environment(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        os.environ["ENV"] = os.environ.get("ENV", "TEST")
        return func(*args, **kwargs)
    return decorator

@task(default=True, aliases=['run'])
@_setup_environment
def run_tests():
    run('nosetests tests/', pty=True)

@task(aliases=['reset'])
@_setup_environment
def reset_database():
    from app import app, db
    with app.app_context():
        db.drop_all()
        db.create_all()

namespace = Collection('test')
for tasks in [run_tests, reset_database]:
    namespace.add_task(tasks)
