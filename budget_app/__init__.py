from flask import Flask
from home.views import home_blueprint
from database import db


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')


app.register_blueprint(home_blueprint)
db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)