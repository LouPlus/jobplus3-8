# -*- coding: utf-8 -*-

from flask import flash
from flask import Blueprint
from flask import url_for
from flask import redirect
from flask import render_template

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from simplejob.models import User
from simplejob.models import Job
from simplejob.forms import LoginForm


front = Blueprint("front", __name__)


@front.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        next = ".index"
        if user.is_admin:
            next = "admin.manage"
        elif user.is_company:
            next = "company.info"
        elif user.is_jobhunter:
            next = "job.info"
        return redirect(url_for(next))
    return render_template("login.html", form=form)


@front.route("/")
def index():
    jobs = Job.query.all()
    return render_template("index.html", jobs = jobs)


@front.route("/logout")
@login_required
def logout():
    logout_user()
    flash("您已经退出登录", "success")
    return redirect(url_for(".index"))
