# -*- coding: utf-8 -*-

from flask import (Blueprint, flash, \
        redirect, render_template, url_for)

from flask_login import (current_user, login_required)

from simplejob.forms import UserProfileForm


user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.update_profile(current_user)
        flash("个人信息更新成功", "success")
        return redirect(url_for("front.index"))
    return render_template("user/profile.html", form=form)
