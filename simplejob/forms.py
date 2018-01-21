# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms import ValidationError

from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import DataRequired as Required

from simplejob.models import db
from simplejob.models import User


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
    phone_num = StringField("手机号",
            validators=[Required(message="请填写内容"), Length(11, 11,
                message="请确认您输入的手机号")])       
    job_years = StringField("工作年限",
            validators=[Required(message="请填写内容"), Length(1, 2,
                message="请确认您输入的工作年限")])       
    resume_url = StringField("简历",
            validators=[Required(message="请填写内容")])
    submit = SubmitField("提交")

    def update_profile(self, user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
