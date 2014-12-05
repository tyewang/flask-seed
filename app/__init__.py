from flask import Flask
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

import controllers
