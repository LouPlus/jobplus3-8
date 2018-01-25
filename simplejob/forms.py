# -*- coding: utf-8 -*-

import re

from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms import ValidationError

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
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱未注册")

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
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
    job_years = StringField("工作年限",
            validators=[Required(message="请填写内容"), Length(1, 2,
                message="请确认您输入的工作年限")])       
    # resume_url = StringField("简历",
    #         validators=[Required(message="请填写内容")])
    submit = SubmitField("提交")

    def update_profile(self, user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()


class CompanyProfileForm(FlaskForm):
    name = StringField("企业名称",
            validators=[Required(message="请填写内容"), Length(3, 24, 
                message="密码长度要在3～24个字符之间")])
    email = StringField("企业邮箱",
            validators=[Required(message="请填写内容"),
                Email(message="请输入合法的email地址")])
    password = PasswordField("密码",
            validators=[Length(6, 24, 
                message="密码长度要在6～24个字符之间")])
    address = StringField("办公地址",
            validators=[Required(message="请填写内容"), Length(6, 128,
                message="密码长度要在6～128个字符之间")])       
    logo = StringField("公司Logo",
            validators=[Required(message="请填写内容"), Length(1, 128,
                message="请确认您输入的Logo")])       
    website = StringField("公司网址",
            validators=[Required(message="请填写内容"), Length(12, 128,
                message="请确认您输入的网址")])
    summary = StringField("公司简介",
            validators=[Required(message="请填写内容"), Length(12, 128,
                message="请确认您输入的内容")])
    company_info = TextAreaField("公司详情",
            validators=[Required(message="请填写内容"), Length(12, 1024,
                message="请确认您输入的内容")])
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
