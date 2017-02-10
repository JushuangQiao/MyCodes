# coding=utf-8

from .. import db


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
