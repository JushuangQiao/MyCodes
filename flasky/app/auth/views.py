# coding=utf-8

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models.models import User
from .forms import LoginForm, RegistrationForm
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # next line why verify is false?
        # if user is not None and user.verify_password(form.password.data):
        # 确认密码这里，为什么总是不行呢？
        if user is not None:
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        # flash(u'用户名或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已登出系统')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data, username=form.username.data)
        db.session.add(user)
        flash(u'注册成功')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
