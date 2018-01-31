# -*- coding: utf-8 -*-

from flask import (abort, Blueprint, request, current_app, flash,
        url_for, render_template, redirect, render_template)

from flask_login import login_required
from flask_login import current_user

from simplejob.models import User, Job
from simplejob.forms import CompanyProfileForm


company = Blueprint("company", __name__, url_prefix="/company")

@company.route("/")
def index():
    page = request.args.get('page', default = 1, type = int)
    pagination = User.query.filter(
            User.role == User.ROLE_COMPANY
            ).order_by(User.created_at.desc()
                ).paginate(
                    page = page,
                    per_page = current_app.config['INDEX_PER_PAGE'],
                    error_out = False
                    )
    return render_template('company/index.html', pagination = pagination,
            active = 'company')

@company.route("/detail/<int:company_id>", methods=['GET', 'POST'])
def detail(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    form = CompanyProfileForm(obj=current_user)
    return render_template("company/detail.html",
            company=company, active="", panel="about", form=form)

@company.route('/job_manage/<int:company_id>', methods=['GET', 'POST'])
@login_required
def job_manage(company_id):
    page = request.args.get('page', default = 1, type = int)
    pagination = Job.query.filter_by(
            company_id = company_id
            ).order_by(Job.created_at.desc()).paginate(
                    page = page,
                    per_page = current_app.config['INDEX_PER_PAGE'],
                    error_out = False
                    )
    return render_template('company/jobs_manage.html', pagination = pagination)



@company.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = CompanyProfileForm(obj=current_user)
    return render_template('company/profile.html', form = form)

'''
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


@company.route("/<int:company_id>")
def detail(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    return render_template("company/detail.html",
            company=company, active="", panel="about")
'''
