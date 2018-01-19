from flask import Flask, render_template
from simplejob.config import configs
from flask_migrate import Migrate
from simplejob.models import db, User, Company, Job

def register_blueprints(app):
    from .handlers import front
    # , job, company, admin, user, tests
    app.register_blueprint(front)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    Migrate(app, db)
    register_blueprints(app)
    return app
