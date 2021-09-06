import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from app.core.config import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = os.getenv('ADMIN_SECRET_KEY', 'secret')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = settings.DEBUG

db = SQLAlchemy(app)

admin = Admin(app, template_mode='bootstrap4')

# Register models for admin
from app.models.user import User  # noqa
from app.models.blog import Blog  # noqa
from app.admin import views  # noqa
admin.add_view(views.UserView(User, db.session))
admin.add_view(views.BlogView(Blog, db.session))
