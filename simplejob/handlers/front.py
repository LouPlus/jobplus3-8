# -*- coding: utf-8 -*-

from flask import flash
from flask import Blueprint
from flask import url_for
from flask import redirect
from flask import render_template

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from simplejob.models import db
from simplejob.models import User
from simplejob.models import Job
from simplejob.forms import LoginForm
from simplejob.forms import RegisterForm


front = Blueprint("front", __name__)


@front.route("/userregister", methods=["GET", "POST"])
def userregister():
    form = RegisterForm()
    if form.validate_on_submit():
        if not form.username.data.isalnum():
            flash("用户名必须由数字和字母组成", "error")
            return redirect(url_for(".userregister"))
        form.create_user()
        flash("注册成功，请登录！", "success")
        return redirect(url_for(".login"))
    return render_template("user/register.html", form=form)


@front.route("/companyregister", methods=["GET", "POST"])
def companyregister():
    form = RegisterForm()
    form.username.label = u"企业名称"
    if form.validate_on_submit():
        if not form.username.data.isalnum():
            flash("企业名称必须由数字和字母组成", "error")
            return redirect(url_for(".companyregister"))
        company = form.create_user()
        company.role = User.ROLE_COMPANY
        db.session.add(company)
        db.session.commit()
        flash("注册成功，请登录！", "success")
        return redirect(url_for(".login"))
    return render_template("company/register.html", form=form)


@front.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user.is_enable)
        if not user.is_enable:
            flash("该用户已被管理员禁用", "error")
            return redirect(url_for(".login"))
        else:
            login_user(user, form.remember_me.data)
            next = ".index"
            if user.is_admin:
                next = "admin.users"
            elif user.is_company:
                next = "company.profile"
            elif user.is_jobhunter:
                next = "user.profile"
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
