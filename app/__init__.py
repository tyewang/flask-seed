from flask import Flask
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import controllers
