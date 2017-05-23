# coding=utf-8

import logging
from flask import render_template, redirect, url_for, request, flash
from flask_login import logout_user, login_required, current_user
from . import auth
from ..models.manager import UserManager
from .forms import LoginForm, RegistrationForm, ChangePasswordForm
from .. import db


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        UserManager.ping(current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    try:
        if form.validate_on_submit():
            user = UserManager.verify_password(form)
            if user:
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
            UserManager.add_user(form)
            flash(u'注册成功')
            return redirect(url_for('auth.login'))
        return render_template('auth/register.html', form=form)
    except Exception, e:
        logging.error('func: register error:{0}'.format(e))
        return render_template('auth/register.html', form=form)


@auth.route('/change-password', methods=['GET', 'POST'])
def change_password():
    form = ChangePasswordForm()
    try:
        if form.validate_on_submit():
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
