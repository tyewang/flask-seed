import os

from invoke import task, run, Collection

os.environ["ENV"] = "TEST"

@task(default=True, aliases=['run'])
def run_tests():
    run('nosetests tests/')

namespace = Collection('test')
for tasks in [run_tests]:
    namespace.add_task(tasks)
