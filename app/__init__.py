from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

from config import Config

bootstrap = Bootstrap()
csrf = CsrfProtect()
db = SQLAlchemy()
view = Blueprint('view', __name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap.init_app(app)
    csrf.init_app(app)
    db.init_app(app)

    from app import views
    app.register_blueprint(view)

    return app
