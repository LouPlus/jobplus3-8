# -*- coding: utf-8 -*-

from flask import (abort, Blueprint, current_app, flash, \
        render_template, redirect, request, url_for)

from flask_login import (current_user, login_required)

from simplejob.models import (Company, db, Delivery, Job, User)
from simplejob.forms import (CompanyProfileForm, JobForm)


company = Blueprint("company", __name__, url_prefix="/company")


@company.route("/")
def index():
    status = request.args.get("cfilter", "all")
    page = request.args.get("page", default=1, type=int)
    pagination = User.query.filter(
            User.role == User.ROLE_COMPANY
            ).order_by(User.created_at.desc()
                ).paginate(
                    page=page,
                    per_page=current_app.config["INDEX_PER_PAGE"],
                    error_out=False
                    )
    cpagination = ["移动互联网", "电子商务", "金融", 
            "企业服务", "教育", "文化娱乐", "游戏", "O2O", "硬件"]
    return render_template("company/index.html",
            pagination=pagination, cpagination=cpagination)


@company.route("/filter")
def cfilter():
    status = request.args.get("status", "all")
    page = request.args.get("page", default=1, type=int)
    job_filter = Company.query.filter(Company.field==status)
    pagination = job_filter.order_by(Company.created_at.desc()).paginate(
                page=page,
                per_page=current_app.config["INDEX_PER_PAGE"],
                error_out=False
            )
    cpagination = ["移动互联网", "电子商务", "金融", 
            "企业服务", "教育", "文化娱乐", "游戏", "O2O", "硬件"]
    return render_template("company/filter.html",
            pagination=pagination, cpagination=cpagination)


@company.route("/detail/<int:company_id>")
def detail(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    return render_template("company/detail.html",
            company=company, active="", panel="about")


@company.route("/<int:company_id>/jobs")
def company_jobs(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    return render_template("company/detail.html",
            company=company, active="", panel="job")


@company.route("/<int:company_id>/admin")
@login_required
def job_manage(company_id):
    if not current_user.is_admin and not current_user.id == company_id:
        abort(404)
    page = request.args.get("page", default=1, type=int)
    pagination = Job.query.filter_by(
            company_id=company_id
            ).order_by(Job.created_at.desc()).paginate(
                    page=page,
                    per_page=current_app.config["INDEX_PER_PAGE"],
                    error_out=False
                    )
    return render_template("company/jobs_manage.html",
            pagination=pagination, company_id=company_id)


@company.route("/profile/", methods=["GET", "POST"])
@login_required
def profile():
    if not current_user.is_company:
        flash("您不是企业用户", "warning")
        return redirect(url_for("front.index"))
    form = CompanyProfileForm(obj=current_user.company_detail)
    form.name.data = current_user.username
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.update_profile(current_user)
        flash("企业用户信息更新成功", "success")
        return redirect(url_for("front.index"))
    return render_template("company/profile.html", form=form)


@company.route("/<int:company_id>/admin/publish_job/", methods=["GET", "POST"])
@login_required
def publish_job(company_id):
    if current_user.id != company_id:
        abort(404)
    form = JobForm()
    if form.validate_on_submit():
        form.create_job(current_user)
        flash("职位创建成功", "success")
        return redirect(url_for("company.job_manage",
            company_id=current_user.id))
    return render_template("company/publish_job.html",
            form=form, company_id=company_id)


@company.route("/<int:company_id>/admin/edit_job/<int:job_id>/", methods=["GET", "POST"])
@login_required
def edit_job(company_id, job_id):
    if current_user.id != company_id:
        abort(404)
    job = Job.query.get_or_404(job_id)
    if job.company_id != current_user.id:
        abort(404)
    form = JobForm(obj=job)
    if form.validate_on_submit():
        form.update_job(job)
        flash("职位更新成功", "success")
        return redirect(url_for("company.job_manage",
                company_id=current_user.id))
    return render_template("company/edit_job.html",
            form=form, company_id=company_id, job=job)


@company.route("/<int:company_id>/admin/jobs/<int:job_id>/delete")
@login_required
def delete_job(company_id, job_id):
    if current_user.id != company_id:
        abort(404)
    job = Job.query.get_or_404(job_id)
    if job.company_id != current_user.id:
        abort(404)
    db.session.delete(job)
    db.session.commit()
    flash("职位删除成功", "success")
    return redirect(url_for("company.job_manage",
            company_id=current_user.id))


@company.route("/<int:company_id>/admin/apply")
@login_required
def company_job_apply(company_id):
    if not current_user.is_admin and not current_user.id == company_id:
        abort(404)
    status = request.args.get("status", "all")
    page = request.args.get("page", default=1, type=int)
    job_filter = Delivery.query.filter_by(company_id=company_id)
    if status == "waiting":
        job_filter = job_filter.filter(Delivery.status==Delivery.STATUS_WAITTING)
    elif status == "accept":
        job_filter = job_filter.filter(Delivery.status==Delivery.STATUS_ACCEPT)
    elif status == "reject":
        job_filter = job_filter.filter(Delivery.status==Delivery.STATUS_REJECT)  
    pagination = job_filter.order_by(Delivery.created_at.desc()).paginate(
                page=page,
                per_page=current_app.config["ADMIN_PER_PAGE"],
                error_out=False
            )
    return render_template("company/company_apply.html", pagination=pagination,
            company_id=company_id)


@company.route("/<int:company_id>/admin/apply/<int:delivery_id>/accept/")
@login_required
def company_job_apply_accept(company_id, delivery_id):
    delivery = Delivery.query.get_or_404(delivery_id)
    if current_user.id != company_id:
        abort(404)
    delivery.status = Delivery.STATUS_ACCEPT
    flash("已接受该简历，可以开始安排面试", "success")
    db.session.add(delivery)
    db.session.commit()
    return redirect(url_for(".company_job_apply", company_id=company_id))


@company.route("/<int:company_id>/admin/apply/<int:delivery_id>/reject/")
@login_required
def company_job_apply_reject(company_id, delivery_id):
    delivery = Delivery.query.get_or_404(delivery_id)
    if current_user.id != company_id:
        abort(404)
    delivery.status = Delivery.STATUS_REJECT
    flash("已拒绝该简历", "success")
    db.session.add(delivery)
    db.session.commit()
    return redirect(url_for(".company_job_apply", company_id=company_id))
