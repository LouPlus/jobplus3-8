# -*- coding: utf-8 -*-

from flask import (abort, Blueprint, request, current_app, flash,
        url_for, render_template, redirect)

from flask_login import login_required
from flask_login import current_user

from simplejob.models import User, Job, db
from simplejob.forms import CompanyProfileForm, JobForm


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


@company.route("/<int:company_id>/jobs")
def company_jobs(company_id):
    company = User.query.get_or_404(company_id)
    if not company.is_company:
        abort(404)
    return render_template('company/detail.html',
            company=company, active='',
            panel='job')


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
    return render_template('company/jobs_manage.html',
            pagination = pagination, company_id=company_id)


@company.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = CompanyProfileForm(obj=current_user)
    return render_template('company/profile.html', form = form)


@company.route('/<int:company_id>/admin/publish_job/', methods=['GET', 'POST'])
@login_required
def publish_job(company_id):
    if current_user.id != company_id:
        abort(404)
    form = JobForm()
    if form.validate_on_submit():
        form.create_job(current_user)
        flash("职位创建成功", "success")
        return redirect(url_for('company.job_manage',
            company_id=current_user.id))
    return render_template('company/publish_job.html',
            form=form, company_id=company_id)


@company.route('/<int:company_id>/admin/edit_job/<int:job_id>/', methods=['GET', 'POST'])
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
        return redirect(url_for('company.job_manage',
                company_id=current_user.id))
    return render_template('company/edit_job.html',
            form=form, company_id=company_id,
            job=job)


@company.route('/<int:company_id>/admin/jobs/<int:job_id>/delete')
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
    return redirect(url_for('company.job_manage',
            company_id=current_user.id))
