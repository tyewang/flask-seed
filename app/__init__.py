from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
db = SQLAlchemy(flask_app)

import controllers
