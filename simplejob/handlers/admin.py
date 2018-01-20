# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash

from flask_login import login_user

from simplejob.forms import LoginForm
from simplejob.decorators import admin_required


admin = Blueprint("admin", __name__, url_prefix="/admin")
