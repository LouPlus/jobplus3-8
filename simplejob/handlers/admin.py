# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash
from flask import render_template

from flask_login import login_user

from simplejob.forms import LoginForm
from simplejob.decorators import admin_required


admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/manage")
def manage():
    return render_template("index.html")
