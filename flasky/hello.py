# coding=utf-8

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Do not tell you'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField(u'姓名', validators=[DataRequired(message=u'姓名不能为空')])
    submit = SubmitField(u'提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = session.get('name')
    return render_template('index.html', name=name, current_time=datetime.utcnow())


@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name='World'):
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash(u'姓名已经改变')
        session['name'] = form.name.data.capitalize()
        return redirect(url_for('user', name=session.get('name')))
    name = session.get('name') if session.get('name') else name
    return render_template('user.html', form=form, name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_internal_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
