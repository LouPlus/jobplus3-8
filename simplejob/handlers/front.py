# -*- coding: utf-8 -*-

from datetime import datetime

from flask import (Blueprint, current_app, flash, \
        redirect, render_template, request, url_for)

from flask_login import (login_user, logout_user, \
        login_required)

from simplejob.models import (Company, db, User, Job)

from simplejob.forms import (RegisterForm, LoginForm)


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
    return render_template("user/register.html", form=form,
            active="userregister")


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
    return render_template("company/register.html", form=form,
            active="companyregister")


@front.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            user = User.query.filter_by(email=form.email.data).first()
        elif Company.query.filter_by(email=form.email.data).first():
            user = Company.query.filter_by(email=form.email.data).first()
        if not user.is_enable:
            flash("该用户已被管理员禁用", "error")
            return redirect(url_for(".login"))
        else:
            login_user(user, form.remember_me.data)
            next = ".index"
            if user.is_admin:
                next = "admin.users"
            elif user.is_company:
                return redirect(url_for("company.job_manage",
                        company_id=user.id))
            elif user.is_jobhunter:
                next = "user.profile"
            return redirect(url_for(next))
    return render_template("login.html", form=form,
            active="login")


@front.route("/")
def index():
    newest_jobs = Job.query.filter(Job.is_enable.is_(True)
            ).order_by(Job.created_at.desc()).limit(9)
    newest_companies = User.query.filter(
        User.role==User.ROLE_COMPANY,
    ).order_by(User.created_at.desc()).limit(8)
    return render_template("index.html", 
        active="index",
        newest_jobs=newest_jobs,
        newest_companies=newest_companies
    )


@front.route("/logout")
@login_required
def logout():
    logout_user()
    flash("您已经退出登录", "success")
    return redirect(url_for(".index"))
