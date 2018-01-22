# -*- coding: utf-8 -*-

from flask import (flash, Blueprint, url_for,
        redirect, render_template, request, current_app)

from flask_login import (login_user, logout_user,
        login_required)

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
        login_user(user, form.remember_me.data)
        next = ".index"
        if user.is_admin:
            next = "admin.manage"
        elif user.is_company:
            next = "company.profile"
        elif user.is_jobhunter:
            next = "user.profile"
        return redirect(url_for(next))
    return render_template("login.html", form=form)


@front.route("/")
def index():
    # 获取参数中传过来的页数
    page = request.args.get('page', default = 1, type = int)
    # 生成分页对象
    pagination = Job.query.paginate(
            page = page,
            per_page = current_app.config['INDEX_PER_PAGE'],
            error_out = False
            )
    return render_template('index.html', pagination = pagination)

@front.route("/logout")
@login_required
def logout():
    logout_user()
    flash("您已经退出登录", "success")
    return redirect(url_for(".index"))
