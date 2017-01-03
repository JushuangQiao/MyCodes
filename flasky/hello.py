from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello():
    return '<h1>Hello World</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {name}</h1>'.format(name=name)


if __name__ == '__main__':
    manager.run()
