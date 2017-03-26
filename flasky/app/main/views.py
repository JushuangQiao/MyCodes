# coding=utf-8

from datetime import datetime
from flask import render_template, session, url_for, redirect, flash, abort
from flask_login import login_required, current_user
from setting import Config
from . import main
from .forms import NameForm, ProfileForm, EditAdminForm
from .. import db
from ..models.models import User, Role
from ..email import send_email
from ..decorators import admin_required


@main.route('/', methods=['GET', 'POST'])
def index(name='World'):
    name = session.get('name') if session.get('name') else name
    return render_template('main/index.html', name=name, current_time=datetime.utcnow())


@main.route('/user/<name>', methods=['GET', 'POST'])
def user(name='World'):
    form = NameForm()
    if form.validate_on_submit():
        username = User.query.filter_by(username=form.name.data).first()
        if username is None:
            flash(u'不存在该用户')
            username = User(username=form.name.data)
            db.session.add(username)
            session['known'] = False
            if Config.FLASKY_ADMIN:
                send_email(Config.FLASKY_ADMIN, 'New User', 'mail/new_user', user=username)
        else:
            session['known'] = True
        session['name'] = form.name.data.capitalize()
        return redirect(url_for('main.user', name=session.get('name')))
    name = session.get('name') if session.get('name') else name
    return render_template('main/user.html', form=form, name=name, known=session.get('known', False))


@main.route('/user/<username>/details')
def user_detail(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('main/user_detail.html', user=user)


@main.route('/user/<username>/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.real_name = form.real_name.data
        current_user.age = form.age.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        # flash(u'您的资料已更改')
        return redirect(url_for('main.user_detail', username=current_user.username))
    form.real_name = current_user.real_name
    form.age = current_user.age
    form.location = current_user.location
    form.about_me = current_user.about_me
    return render_template('main/edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        # user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.real_name = form.real_name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        # flash('The profile has been updated.')
        return redirect(url_for('main.user', name=user.username))
    form.email.data = user.email
    form.username.data = user.username
    # form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.real_name.data = user.real_name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('main/edit_profile.html', form=form, user=user)
