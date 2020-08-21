# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_type):

    flask_app = Flask(__name__)

    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    flask_app.config.from_pyfile(configuration)

    db.init_app(flask_app)
    bootstrap.init_app(flask_app)

    from app.catalog import main

    flask_app.register_blueprint(main)

    return flask_app
