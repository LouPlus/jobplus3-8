# -*- coding: utf-8 -*-

from flask import abort
from flask import Blueprint
from flask import request
from flask import url_for
from flask import flash
from flask import current_app
from flask import redirect
from flask import render_template

from flask_login import current_user
from flask_login import login_user
from flask_login import login_required

from simplejob.models import db
from simplejob.models import Job


job = Blueprint("job", __name__, url_prefix="/job")


@job.route("/")
def index():
    page = request.args.get('page', default = 1, type = int)
    pagination = Job.query.order_by(
            db.desc(Job.created_at)
            ).paginate(
            page = page,
            per_page = current_app.config['INDEX_PER_PAGE'],
            error_out = False
            )
    return render_template('job/index.html', pagination = pagination,
            active = 'job')



@job.route('/<int:job_id>')
def detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job/detail.html', job = job)


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
        return redirect(url_for("company.profile"))


@job.route("<int:job_id>/enable")
@login_required
def enable_job(job_id):
    job = Job.query.get_or_404(job_id)
    if not current_user.is_admin and current_user.id != job.company.id:
        abort(404)
    if job.is_enable:
        flash("职位已上线", "warnning")
    else:
        job.is_enable = True
        db.session.add(job)
        db.session.commit()
        flash("职位上线成功", "success")
    if current_user.is_admin:
        return redirect(url_for("admin.jobs"))
    else:
        return redirect(url_for("company.profile"))
