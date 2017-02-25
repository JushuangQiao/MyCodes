# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(u'邮箱不能为空'), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired(u'密码不能为空')])
    remember_me = BooleanField(u'保存密码')
    submit = SubmitField(u'登录')
