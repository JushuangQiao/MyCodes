# coding=utf-8

import logging
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models.models import User
from .forms import LoginForm, RegistrationForm, ChangePasswordForm
from .. import db

logging.basicConfig(filename='runninr_error.log')


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    try:
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            # next line why verify is false?
            # if user is not None and user.verify_password(form.password.data):
            # 确认密码这里，为什么总是不行呢？
            if user is not None:
                login_user(user, form.remember_me.data)
                return redirect(request.args.get('next') or url_for('main.home'))
                flash(u'用户名或密码错误')
        return render_template('auth/login.html', form=form)
    except Exception, e:
        logging.error('func: login error:{0}'.format(e))
        return render_template('auth/login.html', form=None)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已登出系统')
    return redirect(url_for('main.home'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    try:
        if form.validate_on_submit():
            user = User(email=form.email.data, password=form.password.data, username=form.username.data)
            db.session.add(user)
            flash(u'注册成功')
            return redirect(url_for('auth.login'))
        return render_template('auth/register.html', form=form)
    except Exception, e:
        logging.error('func: register error:{0}'.format(e))
        return render_template('auth/register.html', form=None)


@auth.route('/change-password', methods=['GET', 'POST'])
def change_password():
    form = ChangePasswordForm()
    try:
        if form.validate_on_submit():
            # 同样的问题，验证密码不成功，后续解决!
            if current_user.verify_password(form.old_password.data):
                current_user.password = form.password.data
                db.session.add(current_user)
                flash(u'密码已修改')
                return redirect(url_for('main.home'))
            else:
                flash(u'密码错误')
        return render_template('auth/change_password.html', form=form)
    except Exception, e:
        logging.error('func: change_password error:{0}'.format(e))
        return render_template('auth/change_password.html', form=None)
