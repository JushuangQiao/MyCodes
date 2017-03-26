# coding=utf-8

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from . import *
from .. import login_manager


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTILES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(db.String(64), unique=True)
    default = Column(Boolean, default=False, index=True)
    permissions = Column(Integer)
    users = relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.COMMENT | Permission.FOLLOW | Permission.WRITE_ARTILES, True),
            'Moderator': (Permission.COMMENT | Permission.FOLLOW | Permission.WRITE_ARTILES |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }
        for role in roles:
            r = Role.query.filter_by(name=role).first()
            if r is None:
                r = Role(name=role)
            r.permissions = roles[role][0]
            r.default = roles[role][1]
            session.add(r)
        session.commit()

    def __repr__(self):
        return '<role {0}>'.format(self.name)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True)
    password_hash = Column(String(64))
    email = Column(String(64), unique=True, index=True)
    age = Column(Integer, nullable=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    real_name = Column(String(64))
    location = Column(String(64))
    about_me = Column(Text())
    member_since = Column(DateTime(), default=datetime.utcnow)
    last_seen = Column(DateTime(), default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, ps):
        return check_password_hash(self.password_hash, ps)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.age = kwargs.get('age')
        self.password_hash = (generate_password_hash(kwargs.get('password')) if kwargs.get('password') else
                              generate_password_hash('123456'))
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def ping(self):
        self.last_seen = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return '<user {0}>'.format(self.username)


class AnonymousUser(AnonymousUserMixin):
    '''
    匿名用户
    '''
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
