# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash

from flask_login import login_user

from simplejob.forms import LoginForm
from simplejob.decorators import admin_required


admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/login")
@admin_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        login_user(email)
        return redirect(url_for("front.index"))
    flash("邮箱或密码错误，请重试！", "error")
    return render_template("admin/login.html", form=form)
