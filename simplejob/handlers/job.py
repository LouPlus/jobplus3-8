# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash
from flask import render_template

from flask_login import login_user

from simplejob.models import Job
from simplejob.decorators import jobhuter_required


job = Blueprint("job", __name__, url_prefix="/job")


@job.route("/info")
def info():
    return render_template("index.html")


@job.route('/<int:job_id>')
def detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job/detail.html', job = job)
