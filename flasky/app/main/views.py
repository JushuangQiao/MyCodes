# coding=utf-8

from datetime import datetime
from flask import render_template, session, url_for, redirect, flash
from setting.config import Config
from . import main
from .forms import NameForm
from .. import db
from ..models.models import User
from ..email import send_email


@main.route('/', methods=['GET', 'POST'])
def index(name='World'):
    name = session.get('name') if session.get('name') else name
    return render_template('index.html', name=name, current_time=datetime.utcnow())


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
    return render_template('user.html', form=form, name=name, known=session.get('known', False))
