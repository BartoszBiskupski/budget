from flask import Flask
from database import db
from config_deployment import DB
from flask_bootstrap import Bootstrap
from sqlalchemy.orm.mapper import configure_mappers
import sqlalchemy as sa
from sqlalchemy_searchable import make_searchable
from home.views import home_blueprint
from account.views import account_blueprint
from os import path

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DB.SQLALCHEMY_TRACK_MODIFICATIONS
app.static_path = path.join(path.abspath(__file__), 'static')
app.config['SECRET_KEY'] = DB.SECRET_KEY

Bootstrap(app)

db.init_app(app)
make_searchable(db.metadata)


# with app.test_request_context():
#     if not database_exists(DB.SQLALCHEMY_DATABASE_URI):
#         create_database(DB.SQLALCHEMY_DATABASE_URI)
#     from auth.models import User, WorkingTimeRecord, LeaveApplication
#     from invoices.models import Products, Customers, Invoices, Basket, Quantities, Suppliers, Orders
#     sa.orm.configure_mappers()
#     db.create_all()
#     db.session.commit()
#     if not User.query.filter_by(username='admin').first():
#         init_admin()

app.register_blueprint(home_blueprint)
app.register_blueprint(account_blueprint)


if __name__ == '__main__':
   app.run(debug=True)