os.environ["ENV"] = "DEVELOPMENT"

from app import flask_app

if __name__ == '__main__':
    flask_app.run(debug=True)
