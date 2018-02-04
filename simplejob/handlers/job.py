# -*- coding: utf-8 -*-

from flask import (abort, Blueprint, current_app, flash, \
        redirect, request, url_for, render_template)

from flask_login import (current_user, login_user, login_required)

from simplejob.models import (db, Delivery, Job)


job = Blueprint("job", __name__, url_prefix="/job")


@job.route("/")
def index():
    page = request.args.get("page", default=1, type=int)
    pagination = Job.query.filter(Job.is_enable.is_(True)).order_by(
            Job.created_at.desc()).paginate(
                page=page,
                per_page=current_app.config["INDEX_PER_PAGE"],
                error_out=False
            )
    jpagination = ["应届毕业生", "3年及以下", "3-5年", "5-10年", "10年以上", "不限"]
    return render_template("job/index.html", pagination=pagination,
            jpagination=jpagination, active="job")

@job.route("/filter")
def jfilter():
    status = request.args.get("status", "all")
    page = request.args.get("page", default=1, type=int)
    job_filter = Job.query.filter(Job.exp==status)
    pagination = job_filter.order_by(Job.created_at.desc()).paginate(
                page=page,
                per_page=3,
                error_out=False
            )
    jpagination = ["应届毕业生", "3年及以下", "3-5年", "5-10年", "10年以上", "不限"]
    return render_template("job/filter.html",
            pagination=pagination, jpagination=jpagination)


@job.route("/<int:job_id>")
def detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template("job/detail.html", job=job)


@job.route("<int:job_id>/disable")
@login_required
def disable_job(job_id):
    job = Job.query.get_or_404(job_id)
    if not current_user.is_admin and current_user.id != job.company.id:
        abort(404)
    if not job.is_enable:
        flash("职位已下线", "warnning")
    else:
        job.is_enable = False
        db.session.add(job)
        db.session.commit()
        flash("职位下线成功", "success")
    if current_user.is_admin:
        return redirect(url_for("admin.jobs"))
    else:
        return redirect(url_for("company.job_manage",
            company_id=job.company.id))


@job.route("<int:job_id>/enable")
@login_required
def enable_job(job_id):
    job = Job.query.get_or_404(job_id)
    if not current_user.is_admin and current_user.id != job.company.id:
        abort(404)
    if job.is_enable:
        flash("职位已上线", "warning")
    else:
        job.is_enable = True
        db.session.add(job)
        db.session.commit()
        flash("职位上线成功", "success")
    if current_user.is_admin:
        return redirect(url_for("admin.jobs"))
    else:
        return redirect(url_for("company.job_manage",
            company_id=job.company.id))


@job.route("/<int:job_id>/apply")
@login_required
def job_apply(job_id):
    job = Job.query.get_or_404(job_id)
    if current_user.resume_url is None:
        flash("请先上传简历", "warning")
    elif job.current_user_is_applied:
        flash("该职位已上传简历", "warning")
    else:
        delivery = Delivery(
                    job_id=job.id,
                    user_id=current_user.id,
                    company_id=job.company.id
                )
        db.session.add(delivery)
        db.session.commit()
        flash("简历投递成功", "success")
    return redirect(url_for(".detail", job_id=job.id))
