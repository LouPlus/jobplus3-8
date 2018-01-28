# -*- coding: utf-8 -*-

import re

from flask_wtf import FlaskForm

from wtforms import IntegerField
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms import ValidationError
from wtforms import SelectField

from wtforms.validators import URL
from wtforms.validators import Length
from wtforms.validators import EqualTo
from wtforms.validators import Regexp
from wtforms.validators import Email
from wtforms.validators import DataRequired as Required

from simplejob.models import db
from simplejob.models import User
from simplejob.models import Company

class RegisterForm(FlaskForm):
    username = StringField("用户名",
            validators=[Required(message="请填写内容"), Length(3, 24,
                message="密码长度要在3～24个字符之间")])
    email = StringField("邮箱",
            validators=[Required(message="请填写内容"),
                Email(message="请输入合法的email地址")])
    password = PasswordField("密码",
            validators=[Required(message="请填写内容"), Length(6, 24,
                message="密码长度要在6～24个字符之间")])
    repeat_password = PasswordField("重复密码",
            validators=[Required(message="请填写内容"), EqualTo("password",
                message="密码不一致")])
    submit = SubmitField("提交")

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if not field.data.isalnum():
            raise ValidationError("用户名必须由数字和字母组成")
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("用户名已经存在")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱已经存在")


class LoginForm(FlaskForm):
    email = StringField("邮箱",
            validators=[Required(message="请填写内容"),
                Email(message="请输入合法的email地址")])
    password = PasswordField("密码",
            validators=[Required(message="请填写内容"), Length(6, 24,
                message="请确认您输入的密码")])
    remember_me = BooleanField("记住我")
    submit = SubmitField("提交")

    def validate_email(self, field):
        if field.data and not (User.query.filter_by(email=field.data).first() or Company.query.filter_by(email=field.data).first()):
            raise ValidationError("邮箱未注册")

    def validate_password(self, field):
        if User.query.filter_by(email=self.email.data).first():
            user = User.query.filter_by(email=self.email.data).first()
        elif Company.query.filter_by(email=self.email.data).first():
            user = Company.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError("密码错误")


class UserProfileForm(FlaskForm):
    username = StringField("姓名",
            validators=[Required(message="请填写内容"), Length(3, 24,
                message="密码长度要在3～24个字符之间")])
    email = StringField("邮箱",
            validators=[Required(message="请填写内容"),
                Email(message="请输入合法的email地址")])
    password = PasswordField("密码",
            validators=[Required(message="请填写内容"), Length(6, 24,
                message="密码长度要在6～24个字符之间")])
    phone = StringField("手机号",
            validators=[Required(message="请填写内容"), Length(11, 11,
                message="请确认您输入的手机号"),
                Regexp("1[3458]\\d{9}", flags=re.I, message="请输入正确的手机号")])
    resume_url = StringField("简历",
             validators=[Required(message="请填写内容")])
    submit = SubmitField("提交")

    def update_profile(self, user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()


class CompanyProfileForm(FlaskForm):
    name = StringField("企业名称",
            validators=[Required(message="请填写内容"), Length(3, 24)])
    email = StringField("企业邮箱",
            validators=[Required(message="请填写内容"),
                Email(message="请输入合法的email地址")])
    password = PasswordField("密码",
            validators=[Length(6, 24,
                message="密码长度要在6～24个字符之间")])
    address = StringField("办公地址",
            validators=[Required(message="请填写内容"), Length(6, 128,
                message="工作地址长度要在6～128个字符之间")])
    logo = StringField("公司Logo",
            validators=[Required(message="请填写内容"), Length(1, 128,
                message="请确认您输入的Logo")])
    website = StringField("公司网址",
            validators=[Required(message="请填写内容"),
                URL(message="请确认您输入的网址")])
    description = StringField("公司简介",
            validators=[Required(message="请填写内容"), Length(1, 128,
                message="请确认您输入的内容")])
    company_info = TextAreaField("公司详情",
            validators=[Required(message="请填写内容"), Length(1, 1024,
                message="请确认您输入的内容")])
    finance_stage = SelectField("融资阶段",
            choices=[
                ("未融资", "未融资"),
                ("天使轮", "天使轮"),
                ("A轮", "A轮"),
                ("B轮", "B轮"),
                ("C轮", "C轮"),
                ("D轮及以上", "D轮及以上"),
                ("上市公司", "上市公司"),
                ("不需要融资", "不需要融资"),
                ]
            )
    field = SelectField("行业领域",
            choices=[
                ("移动互联网", "移动互联网"),
                ("电子商务", "电子商务"),
                ("金融", "金融"),
                ("企业服务", "企业服务"),
                ("教育", "教育"),
                ("文化娱乐", "文化娱乐"),
                ("游戏", "游戏"),
                ("O2O", "O2O"),
                ("硬件", "硬件"),
                ]
            )
    submit = SubmitField("提交")

    def update_profile(self, user):
        if user.company_detail:
            company_detail = user.company_detail
        else:
            company_detail = Company()
            company_detail.user_id = user.id

        self.populate_obj(company_detail)
        db.session.add(user)
        db.session.add(company_detail)
        db.session.commit()


class JobForm(FlaskForm):
    name = StringField("职位名称")
    salary_low = IntegerField("最低薪水")
    salary_high = IntegerField("最高薪水")
    location = StringField("工作地点")
    tags = StringField("职位标签(用逗号区隔)")
    exp = SelectField("工作年限",
                choices=[
                    ("应届毕业生", "应届毕业生"),
                    ("3年及以下", "3年及以下"),
                    ("3-5年", "3-5年"),
                    ("5-10年", "5-10年"),
                    ("10年以上", "10年以上"),
                    ("不限", "不限"),
                    ]
                )
    degree = SelectField("学历要求",
                choices=[
                    ("不限", "不限"),
                    ("大专", "大专"),
                    ("本科", "本科"),
                    ("硕士", "硕士"),
                    ("博士", "博士"),
                    ]
                )
    description = TextAreaField("职位描述", validators=[Length(0, 1500)])
    submit = SubmitField("发布")

    def create_job(self, company):
        job = Job()
        self.populate_obj(job)
        job.company_id = company.id
        db.session.add(job)
        db.session.commit()
        return job

    def updata_job(self, job):
        self.populate_obj(job)
        db.session.add(job)
        db.session.commit()
        return job
