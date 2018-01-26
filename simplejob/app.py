import flask_whooshalchemyplus as whoosh

from flask import Flask, render_template

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment

from simplejob.config import configs
from simplejob.models import db, User, Company, Job


def register_blueprints(app):
    from .handlers import front, job, company, admin, user #, tests
    app.register_blueprint(front)
    app.register_blueprint(job)
    app.register_blueprint(company)
    app.register_blueprint(admin)
    app.register_blueprint(user)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_blueprints(app)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    
    moment = Moment(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        if User.query.get(id):
            user = User.query.get(id)
        elif Company.query.get(id):
            user = Company.query.get(id)
        return user

    login_manager.login_view = "front.login"
    login_manager.login_message = "请登录而后访问网页"
