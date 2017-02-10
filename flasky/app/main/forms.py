# coding=utf-8


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField(u'姓名', validators=[DataRequired(message=u'姓名不能为空')])
    submit = SubmitField(u'提交')
