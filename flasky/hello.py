# coding:utf-8

import flask
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[Required()])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = flask.session.get('name')
        if old_name is not None and old_name != form.name.data:
            flask.flash('Looks like you have changed your name!')
        flask.session['name'] = form.name.data
        return flask.redirect(flask.url_for('index'))
    return flask.render_template('index.html', form=form, name=flask.session.get('name'))


@app.route('/user/<name>')
def user(name):
    return flask.render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return flask.render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()

