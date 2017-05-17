# coding=utf-8

import os
from app import create_app, db
from app.models.models import User, Role, Post, Permission, Follow, Comment
from app.models.manager import UserManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell, Server


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
server = Server(host='0.0.0.0', port=8888)


def make_shell_context():
    ret = dict()
    ret['app'] = app
    ret['db'] = db
    ret['User'] = User
    ret['Role'] = Role
    ret['Post'] = Post
    ret['Follow'] = Follow
    ret['Permission'] = Permission
    ret['Comment'] = Comment
    ret['UserManager'] = UserManager
    return ret
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('server', server)


@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
