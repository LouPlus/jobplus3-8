# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash
from flask import render_template

from flask_login import login_user

from simplejob.models import Company
from simplejob.forms import LoginForm
from simplejob.decorators import company_required


company = Blueprint("company", __name__, url_prefix="/company")

