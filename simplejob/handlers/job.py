# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash
from flask import current_app
from flask import render_template

from flask_login import login_user

from simplejob.models import Job
from simplejob.decorators import jobhuter_required


job = Blueprint("job", __name__, url_prefix="/job")


@job.route("/")
def index():
    page = request.args.get('page', default = 1, type = int)
    pagination = Job.query.paginate(
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
