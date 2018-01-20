# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import ValidationError

from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import DataRequired as Required

from simplejob.models import User


class LoginForm(FlaskForm):
    email = StringField("邮箱",
            validators=[Required(message="请填写内容"),
                Email(message="请输入合法的email地址")])
    password = PasswordField("密码",
            validators=[Required(message="请填写内容"), Length(6, 24,
                message="请确认您输入的密码")])
    submit = SubmitField("提交")

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱未注册")

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError("密码错误")
