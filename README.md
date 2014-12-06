Flask Seed
============

Where every Flask project should start.

## How to grow your seed:

```
git clone git@github.com:tyewang/flask-seed.git
mv flask-seed your-new-project-name
cd your-new-project-name
git remote set-url origin your-new-project-git-url
```

Don't forget to set up a virtual environment (I suggest using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)) and `pip install -r requirements.txt`

## What's in the seed:
- A basic directory structure, including folders for controllers, tests, etc.
- Invoke tasks for common operations.
- Migrations.

## Interesting Requirements:
- [invoke](http://www.pyinvoke.org/)
- [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate)
- ipdb
- [nose-run-line-number](https://github.com/pitluga/nose-run-line-number) - I use this in conjunction with [vimux-nose-test](https://github.com/pitluga/vimux-nose-test) which is awesome.
- [factory_boy](http://factoryboy.readthedocs.org/en/latest/)
