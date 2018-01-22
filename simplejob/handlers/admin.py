# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash
from flask import url_for
from flask import request
from flask import current_app
from flask import redirect
from flask import render_template

from flask_login import login_user

from simplejob.models import db
from simplejob.models import User
from simplejob.forms import RegisterForm
from simplejob.forms import LoginForm
from simplejob.forms import UserProfileForm
from simplejob.forms import CompanyProfileForm
from simplejob.decorators import admin_required


admin = Blueprint("admin", __name__, url_prefix="/admin")


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
       user.is_enable = True
       flash("已启用", "success")
    else:
       user.is_enable = False
       flash("已禁用", "success")
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("admin.users"))

@admin.route("/users/addcompany", methods=["GET", "POST"])
@admin_required
def addcompany():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash("企业创建成功", "success")
        return redirect(url_for("admin.users"))
    return render_template("admin/create_company.html", form=form)
