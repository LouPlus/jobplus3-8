# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash
from flask import render_template

from flask_login import login_user

from simplejob.models import Company
from simplejob.forms import LoginForm
from simplejob.decorators import company_required


company = Blueprint("company", __name__, url_prefix="/company")


@company.route("/login")
@company_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        login_user(email)
        return redirect(url_for("front.index"))
    flash("邮箱或密码错误，请重试！", "error")
    return render_template("company/login.html", form=form)
