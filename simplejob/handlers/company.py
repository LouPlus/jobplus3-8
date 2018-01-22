# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash
from flask import url_for
from flask import render_template
from flask import redirect

from flask_login import login_required
from flask_login import current_user

from simplejob.forms import CompanyProfileForm


company = Blueprint("company", __name__, url_prefix="/company")


@company.route("/admin/profile", methods=["GET", "POST"])
@login_required
def profile():
    if not current_user.is_company:
        flash("您没有权限访问", "warning")
        return redirect(url_for("front.index"))
    form = CompanyProfileForm(obj=current_user.company_detail)
    if form.validate_on_submit():
        if form.password.data != current_user._password:
            form.update_profile(current_user)
            flash("企业信息更新成功，请重新登录", "success")
            return redirect(url_for("front.logout"))
        else:
            form.update_profile(current_user)
            flash("企业信息更新成功", "success")
            return redirect(url_for(".profile"))
    return render_template("company/profile.html", form=form)
