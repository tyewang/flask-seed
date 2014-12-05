import os

from invoke import task, run

from app import db

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
