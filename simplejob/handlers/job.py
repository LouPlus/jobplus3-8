# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import flash
from flask import render_template

from flask_login import login_user

from simplejob.models import Job
from simplejob.forms import LoginForm
from simplejob.decorators import jobhuter_required


job = Blueprint("job", __name__, url_prefix="/job")


@job.route("/login")
@jobhuter_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        login_user(email)
        return redirect(url_for("front.index"))
    flash("邮箱或密码错误，请重试！", "error")
    return render_template("job/login.html", form=form)


@job.route('/<int:job_id>')
def detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job/detail.html', job = job)
