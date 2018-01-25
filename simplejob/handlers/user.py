# -*- coding: utf-8 -*-
import os

from flask import flash
from flask import url_for
from flask import Blueprint
from flask import request
from flask import redirect
from flask import render_template
from flask import current_app

from flask_login import login_required
from flask_login import current_user

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


@user.route("/", methods=["POST", "GET"])
@login_required
def upload():
    if request.method == "POST":
        resume = request.files.get("file")
        resume.save(os.path.join(current_app.config["UPLOADED_PATH"], resume.filename))
    return redirect(url_for(".profile"))
