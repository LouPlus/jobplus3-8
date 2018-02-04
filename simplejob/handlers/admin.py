# -*- coding: utf-8 -*-

from flask import (Blueprint, current_app, flash, request, \
        redirect, render_template, url_for)

from flask_login import login_user

from simplejob.models import (db, Job, User)

from simplejob.forms import (CompanyProfileForm, LoginForm, \
        RegisterForm, UserProfileForm)

from simplejob.decorators import admin_required


admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/")
@admin_required
def index():
    return render_template("admin/admin_base.html")


@admin.route("/users")
@admin_required
def users():
    page = request.args.get("page", default=1, type=int)
    pagination = User.query.paginate(
        page=page,
        per_page=current_app.config["ADMIN_PER_PAGE"],
        error_out=False
    )
    return render_template("admin/users.html", pagination=pagination)


@admin.route("/users/adduser", methods=["GET", "POST"])
@admin_required
def adduser():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash("用户创建成功", "success")
        return redirect(url_for("admin.users"))
    return render_template("admin/create_user.html", form=form)


@admin.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.role == user.ROLE_COMPANY:
        form = CompanyProfileForm(obj=user)
    elif user.role == user.ROLE_JOBHUNTER:
        form = UserProfileForm(obj=user)
    if form.validate_on_submit():
        form.update_profile(user)
        flash("信息更新成功", "success")
        return redirect(url_for("admin.users"))
    return render_template("admin/edit_user.html", form=form, user=user)


@admin.route("/users/<int:user_id>/disable", methods=["GET", "POST"])
@admin_required
def disable_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_enable:
       user.is_enable = False
       flash("已禁用", "success")
    else:
       user.is_enable = True
       flash("已启用", "success")
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("admin.users"))


@admin.route("/users/addcompany", methods=["GET", "POST"])
@admin_required
def addcompany():
    form = RegisterForm()
    form.username.label = u"企业名称"
    if form.validate_on_submit():
        if not form.username.data.isalnum():
            flash("企业名称必须由数字和字母组成", "error")
            return redirect(url_for("admin.users"))
        company = form.create_user()
        company.role = User.ROLE_COMPANY
        db.session.add(company)
        db.session.commit()
        flash("企业创建成功", "success")
        return redirect(url_for("admin.users"))
    return render_template("admin/create_company.html", form=form)


@admin.route("/jobs")
@admin_required
def jobs():
    page = request.args.get("page", default=1, type=int)
    pagination = Job.query.paginate(
        page=page,
        per_page=current_app.config["ADMIN_PER_PAGE"],
        error_out=False
    )
    return render_template("admin/jobs.html", pagination=pagination)
