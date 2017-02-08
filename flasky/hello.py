# coding=utf-8

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Do not tell you'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://qiao:123456@localhost/flasky'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class NameForm(FlaskForm):
    name = StringField(u'姓名', validators=[DataRequired(message=u'姓名不能为空')])
    submit = SubmitField(u'提交')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<role {0}>'.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username, role_id=2):
        self.username = username
        # self.age = age
        self.role_id = role_id

    def __repr__(self):
        return '<user {0}>'.format(self.name)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))


@app.route('/', methods=['GET', 'POST'])
def index(name='World'):
    name = session.get('name') if session.get('name') else name
    return render_template('index.html', name=name, current_time=datetime.utcnow())


@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name='World'):
    form = NameForm()
    if form.validate_on_submit():
        username = User.query.filter_by(username=form.name.data).first()
        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #    flash(u'姓名已经改变')
        if username is None:
            flash(u'不存在该用户')
            username = User(username=form.name.data)
            db.session.add(username)
            session['known'] = False
        else:
            session['known'] = True
        # form.name.data = ''
        session['name'] = form.name.data.capitalize()
        return redirect(url_for('user', name=session.get('name')))
    name = session.get('name') if session.get('name') else name
    return render_template('user.html', form=form, name=name, known=session.get('known', False))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_internal_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
