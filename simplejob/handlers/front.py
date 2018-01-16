# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template


front = Blueprint("front", __name__)


@front.route("/")
def index():
    return render_template("index.html")
