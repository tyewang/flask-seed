from invoke import task, run, Collection

from tasks import development_tasks, test_tasks

@task
def clear_pyc():
    run('find . -name "*.pyc" -delete')

namespace = Collection()
namespace.add_task(clear_pyc)
namespace.add_collection(development_tasks.namespace)
namespace.add_collection(test_tasks.namespace)
